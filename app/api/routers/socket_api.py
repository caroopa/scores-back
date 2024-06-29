from fastapi import WebSocket, WebSocketDisconnect, APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from app.schemas.schemas import Score as ScoreSch
import app.services.general_service as service

router = APIRouter()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)


@router.put(
    "/calculate_total/{competitor_id}",
    summary="Calculate total score of current competitor.",
)
async def calculate_total(
    competitor_id: int, new_score: ScoreSch, db: Session = Depends(get_db)
):
    result = service.calculate_total(db, competitor_id, new_score)
    await manager.send_message(f"Total score updated for competitor {competitor_id}")
    return result
