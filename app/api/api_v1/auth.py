from fastapi import APIRouter
from app.main import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/passcode")
def login_passcode(passcode: str):
    # TODO: implement hashing for the passcode
    if passcode == settings.PASSCODE:
        return {"success": True}
