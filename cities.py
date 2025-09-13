# app/api/routers/cities.py
from typing import List
from fastapi import APIRouter, HTTPException, status
from app.schemas.city import CityCreate, CityRead

router = APIRouter(prefix="/api/v1/cities", tags=["cities"])

# basit in-memory "DB" (sadece örnek için)
_db: List[dict] = []
_next_id = 1

@router.post("/", response_model=CityRead, status_code=status.HTTP_201_CREATED)
def create_city(payload: CityCreate):
    """
    Yeni şehir oluşturur.
    İş kuralı örneği: aynı isimde şehir zaten varsa 400 dön.
    """
    global _next_id
    # iş-kuralı doğrulaması -> 400 dönecek
    if any(c["name"].strip().lower() == payload.name.strip().lower() for c in _db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Aynı isimde bir şehir zaten mevcut."
        )

    # payload'ı dict'e çevir (Pydantic v2)
    new_city = payload.model_dump()
    new_city["id"] = _next_id
    _next_id += 1

    _db.append(new_city)
    return new_city

@router.get("/", response_model=List[CityRead])
def list_cities():
    """Tüm şehirleri döner."""
    return _db
