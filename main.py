# app/main.py
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api.routers import cities

app = FastAPI(title="Cities API")

# router'ı uygula
app.include_router(cities.router)

# HTTPException için özel handler (istemciye tutarlı JSON döndürmek için)
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )

# Request validation hatalarını (Pydantic/FastAPI) yakalayıp 400 döndürmek istersen:
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Uyarı: FastAPI varsayılanı 422'dir; burada örnek olarak 400 döndürüyoruz.
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"errors": exc.errors()}
    )

# Genel hata handler (prod'da stack trace vermemek için)
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    # burada loglama yapılmalı (ör: logger.exception(...))
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal server error"}
    )
