from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Home Management API",
    description="API cho hệ thống Quản lý Nhà chung",
    version="1.0.0"
)

# Cấu hình CORS để frontend có thể gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trong môi trường thực tế, nên giới hạn lại domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Chào mừng đến với API Quản lý Nhà chung"
    }
