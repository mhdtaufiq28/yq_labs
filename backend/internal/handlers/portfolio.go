package handlers

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"github.com/mhdtaufiq28/portofolio-backend/internal/data"
)

// GetAbout mengembalikan info about (lokasi, email, linkedin, status)
func GetAbout(c *gin.Context) {
	c.JSON(http.StatusOK, data.AboutInfo)
}

// GetSkills mengembalikan daftar kelompok skill
func GetSkills(c *gin.Context) {
	c.JSON(http.StatusOK, data.Skills)
}

// GetProjects mengembalikan daftar project
func GetProjects(c *gin.Context) {
	c.JSON(http.StatusOK, data.Projects)
}
