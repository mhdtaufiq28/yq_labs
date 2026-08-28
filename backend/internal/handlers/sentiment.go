package handlers

import (
	"bytes"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"os"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/mhdtaufiq28/portofolio-backend/internal/models"
)

func pythonServiceURL() string {
	url := os.Getenv("PY_SERVICE_URL")
	if url == "" {
		url = "http://localhost:8000"
	}
	return url
}

var httpClient = &http.Client{Timeout: 10 * time.Second}

// PostAnalyzeSentiment meneruskan teks ke Python service yang menjalankan
// model Naive Bayes hasil skripsi, lalu meneruskan hasilnya ke frontend.
// Ini adalah demo interaktif dari model skripsi langsung di halaman portofolio.
func PostAnalyzeSentiment(c *gin.Context) {
	var req models.SentimentRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	payload, err := json.Marshal(req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "gagal encode request"})
		return
	}

	resp, err := httpClient.Post(
		pythonServiceURL()+"/analyze",
		"application/json",
		bytes.NewReader(payload),
	)
	if err != nil {
		log.Printf("gagal menghubungi python service: %v\n", err)
		c.JSON(http.StatusBadGateway, gin.H{"error": "layanan analisis sedang tidak tersedia"})
		return
	}
	defer resp.Body.Close()

	c.Status(resp.StatusCode)
	c.Header("Content-Type", "application/json")
	io.Copy(c.Writer, resp.Body)
}
