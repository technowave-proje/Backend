# app/schemas/city.py
from typing import Optional
from pydantic import BaseModel, Field

class CityCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Şehir adı")
    country: str = Field(..., min_length=2, max_length=100, description="Ülke")
    latitude: float = Field(..., ge=-90, le=90, description="Enlem (-90..90)")
    longitude: float = Field(..., ge=-180, le=180, description="Boylam (-180..180)")
    population: Optional[int] = Field(0, ge=0, description="Nüfus (pozitif)")

    model_config = {
        "extra": "forbid"  # bilinmeyen alan varsa hata ver
    }

class CityRead(CityCreate):
    id: int = Field(..., description="Otomatik ID")
