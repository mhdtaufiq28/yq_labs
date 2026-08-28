package models

// Project merepresentasikan satu item portofolio, field-nya disamakan
// dengan interface Project di frontend/types/index.ts
type Project struct {
	Title string   `json:"title"`
	Desc  string   `json:"desc"`
	Tags  []string `json:"tags"`
	Type  string   `json:"type"`
}

// SkillGroup merepresentasikan satu kelompok skill (Programming, Data & AI, dst)
type SkillGroup struct {
	Title string   `json:"title"`
	Items []string `json:"items"`
}

// ContactInfo merepresentasikan satu baris info di section About
type ContactInfo struct {
	Label string `json:"label"`
	Value string `json:"value"`
}

// ContactMessage merepresentasikan payload dari form kontak
type ContactMessage struct {
	Name    string `json:"name" binding:"required"`
	Email   string `json:"email" binding:"required,email"`
	Message string `json:"message" binding:"required"`
}

// SentimentRequest adalah payload untuk endpoint analisis sentimen
// yang diteruskan ke Python service (model skripsi)
type SentimentRequest struct {
	Text string `json:"text" binding:"required"`
}

// SentimentResponse adalah bentuk hasil yang dikembalikan Python service
type SentimentResponse struct {
	Label      string  `json:"label"`      // "positif" | "negatif" | "netral"
	Confidence float64 `json:"confidence"` // 0.0 - 1.0
}
