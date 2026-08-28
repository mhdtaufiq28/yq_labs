# Backend — Go (Gin)

REST API untuk portofolio, dipakai oleh frontend Next.js.

## Menjalankan

```bash
cd backend
go mod tidy   # sinkronkan ulang dependency di mesin kamu
go run ./cmd/server
```

Server jalan di `http://localhost:8080` secara default. Endpoint `/health`
bisa dipakai untuk cek server hidup.

## Environment variables

Salin `.env.example` ke `.env` (atau set langsung di shell/hosting):

| Variable          | Default                 | Keterangan                                   |
|--------------------|--------------------------|-----------------------------------------------|
| `PORT`             | `8080`                  | Port server Go                                |
| `FRONTEND_ORIGIN`  | `http://localhost:3000` | Origin yang diizinkan CORS                    |
| `PY_SERVICE_URL`   | `http://localhost:8000` | Alamat Python service (analisis sentimen)     |

## Endpoint

| Method | Path                       | Keterangan                                              |
|--------|-----------------------------|----------------------------------------------------------|
| GET    | `/health`                  | Cek server hidup                                          |
| GET    | `/api/about`                | Info lokasi, email, LinkedIn, status                      |
| GET    | `/api/skills`               | Daftar kelompok skill                                      |
| GET    | `/api/projects`             | Daftar project                                             |
| POST   | `/api/contact`              | Kirim pesan dari form kontak                                |
| POST   | `/api/analyze-sentiment`    | Proxy ke Python service — analisis sentimen teks (model skripsi) |

## Struktur folder

```
backend/
├── cmd/server/main.go        # entry point, setup router & CORS
├── internal/handlers/        # HTTP handlers
├── internal/models/          # struct request/response
└── internal/data/            # data statis (sementara, sebelum pakai database)
```

## Catatan tentang go.mod

`go.mod` berisi beberapa `replace` directive yang mengarahkan sejumlah
dependency transitif (mis. `golang.org/x/sys`, `gopkg.in/yaml.v3`) ke mirror
GitHub-nya. Ini **hanya diperlukan karena sandbox tempat backend ini pertama
kali dibangun membatasi akses ke domain non-GitHub** (golang.org, gopkg.in,
dll tidak bisa diakses). Di mesin kamu sendiri dengan internet normal, ini
tidak masalah — kamu bisa jalankan `go mod tidy` untuk membiarkan Go
mengambil versi resmi langsung, atau biarkan saja `replace` ini karena
tetap valid dan tidak mengubah versi API yang dipakai.
