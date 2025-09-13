# Backend

# main.py

FastAPI uygulamasını başlatır.

API router’larını (cities) include eder.

Uygulamanın giriş noktasıdır.

# cities.py

APIRouter kullanarak cities endpointlerini tanımlar.

Şu an 2 endpoint var:

GET cities → Tüm şehirleri listele.

POST cities → Yeni şehir ekle.

Basit bir cities_db listesi kullanır (in-memory).

# city.py

Pydantic modelleri (şemalar) içerir.

CityCreate → İstek (request) için şehir modeli.

CityRead → Yanıt (response) için şehir modeli.

# API Kullanımı

Uygulamayı çalıştır:

# NOT : main dosyası app klasörünün içinde olursa çalışır 
uvicorn app.main:app --reload

Swagger UI’ye git:
👉 http://127.0.0.1:8000/docs

Örnek POST isteği:
{
  "name": "Düzce",
  "country": "Türkiye",
  "latitude": 40.8438,
  "longitude": 31.1565,
  "population": 400000
}

Örnek GET cevabı:
  {
    "name": "Düzce",
    "country": "Türkiye",
    "latitude": 40.8438,
    "longitude": 31.1565,
    "population": 400000,
    "id": 0
  }

