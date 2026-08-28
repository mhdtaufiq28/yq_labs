package data

import "github.com/mhdtaufiq28/portofolio-backend/internal/models"

// AboutInfo — disamakan dengan frontend/components/sections/About.tsx
var AboutInfo = []models.ContactInfo{
	{Label: "Lokasi", Value: "Batam, Kepulauan Riau"},
	{Label: "Email", Value: "mhdtaufiq.work@gmail.com"},
	{Label: "LinkedIn", Value: "linkedin.com/in/mhdtaufiq28"},
	{Label: "Status", Value: "Open to work"},
}

// Skills — disamakan dengan frontend/components/sections/Skills.tsx
var Skills = []models.SkillGroup{
	{
		Title: "Programming",
		Items: []string{"Python", "Golang", "TypeScript", "SQL", "HTML/CSS"},
	},
	{
		Title: "Data & AI",
		Items: []string{"Text Mining", "Machine Learning", "Naive Bayes", "TF-IDF", "Data Analysis"},
	},
	{
		Title: "Tools & Systems",
		Items: []string{"IT Support", "PostgreSQL", "Git", "Next.js", "FastAPI"},
	},
}

// Projects — disamakan dengan frontend/components/sections/Projects.tsx
var Projects = []models.Project{
	{
		Title: "Analisis Sentimen Rempang",
		Desc:  "Sistem klasifikasi sentimen opini publik terhadap relokasi penduduk Rempang menggunakan Naive Bayes Classifier dan Text Mining. Akurasi 81%.",
		Tags:  []string{"Python", "Machine Learning", "NLP", "TF-IDF"},
		Type:  "Skripsi / Research",
	},
	{
		Title: "Web Portofolio",
		Desc:  "Web portofolio pribadi dibangun dengan Next.js, Golang, dan Python. Full-stack modern dengan REST API dan layanan analisis data.",
		Tags:  []string{"Next.js", "Golang", "Python", "PostgreSQL"},
		Type:  "Web Development",
	},
}
