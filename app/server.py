from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.m_bank import router as m_bank


def get_app() -> FastAPI:
    fast_app = FastAPI()

    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    fast_app.include_router(m_bank.router)
    return fast_app


app = get_app()
