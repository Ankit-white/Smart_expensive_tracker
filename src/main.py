from fastapi import FastAPI
from .routes import router

app=FastAPI(title = "Smart expense tracker API",
version="1.0.0",
description="RestAPI for managing personal expenses",)

app.include_router(router)