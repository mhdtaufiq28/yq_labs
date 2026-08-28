package handlers

import (
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/mhdtaufiq28/portofolio-backend/internal/models"
)

// PostContact menerima pesan dari form kontak di frontend.
// Saat ini pesan hanya di-log; nanti bisa disambungkan ke email/DB.
func PostContact(c *gin.Context) {
	var msg models.ContactMessage
	if err := c.ShouldBindJSON(&msg); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	log.Printf("Pesan baru dari %s <%s>: %s\n", msg.Name, msg.Email, msg.Message)

	c.JSON(http.StatusCreated, gin.H{
		"status":  "ok",
		"message": "Pesan berhasil dikirim, terima kasih!",
	})
}
