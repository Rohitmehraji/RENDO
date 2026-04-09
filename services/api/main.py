from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="RENDO API", version="2.0.0")


class GameMode(str, Enum):
    battle_royale = "battle_royale"
    story = "story"
    social = "social"
    war_sim = "war_sim"
    dream_mode = "dream_mode"


class HighlightTrigger(str, Enum):
    clutch_kill = "clutch_kill"
    betrayal = "betrayal"
    last_survivor = "last_survivor"
    streak = "streak"


class AvatarCloneRequest(BaseModel):
    player_id: UUID
    face_asset_uri: str
    voice_asset_uri: str
    motion_asset_uri: str
    consent_token: str


class QueueRequest(BaseModel):
    player_id: UUID
    mode: GameMode
    region: str = Field(min_length=2, max_length=16)
    mmr: float | None = None


class NpcDialogueRequest(BaseModel):
    npc_id: UUID
    player_id: UUID
    player_utterance: str = Field(min_length=1, max_length=512)
    mood_hint: str | None = None


class HighlightJobRequest(BaseModel):
    player_id: UUID
    match_id: str = Field(min_length=6, max_length=64)
    trigger_type: HighlightTrigger
    replay_uri: str
    aspect_ratio: str = Field(pattern=r"^(16:9|9:16|1:1)$")
    include_subtitles: bool = True


class VoiceCommandRequest(BaseModel):
    player_id: UUID
    session_id: str = Field(min_length=6, max_length=64)
    transcript: str = Field(min_length=1, max_length=128)
    locale: str = "en-US"
    confidence: float | None = Field(default=None, ge=0, le=1)


class MemoryEventRequest(BaseModel):
    actor_id: str
    target_id: str
    event_type: str
    intensity: int = Field(ge=1, le=100)
    witness_count: int = Field(default=0, ge=0)


class EmotionSignalRequest(BaseModel):
    player_id: UUID
    arousal: float = Field(ge=0, le=1)
    valence: float = Field(ge=-1, le=1)
    stress: float = Field(ge=0, le=1)


class BehaviorPredictionRequest(BaseModel):
    player_id: UUID
    recent_events: list[str] = Field(default_factory=list, max_length=25)


@app.get("/healthz")
def healthcheck() -> dict[str, str]:
    return {"status": "ok", "time": datetime.now(timezone.utc).isoformat()}


@app.post("/v1/avatar-clone/jobs")
def create_clone_job(payload: AvatarCloneRequest) -> dict[str, str]:
    if not payload.consent_token.strip():
        raise HTTPException(status_code=400, detail="consent_token is required")

    return {
        "job_id": str(uuid4()),
        "state": "queued",
        "player_id": str(payload.player_id),
    }


@app.post("/v1/matchmaking/queue")
def enqueue(payload: QueueRequest) -> dict[str, str | int]:
    return {
        "ticket_id": str(uuid4()),
        "estimated_wait_seconds": 22,
        "mode": payload.mode.value,
        "region": payload.region,
    }


@app.post("/v1/npc/dialogue")
def npc_dialogue(payload: NpcDialogueRequest) -> dict[str, str]:
    response = (
        "I remember what happened in the old harbor. "
        "If you're here to make peace, I can help."
    )
    if payload.mood_hint == "hostile":
        response = "You expect trust after that betrayal? Prove yourself first."

    return {
        "npc_id": str(payload.npc_id),
        "player_id": str(payload.player_id),
        "response": response,
        "emotion": "guarded",
        "memory_ref": str(uuid4()),
    }


@app.post("/v1/cinematic/highlights/jobs")
def create_highlight_job(payload: HighlightJobRequest) -> dict[str, str]:
    return {
        "job_id": str(uuid4()),
        "state": "rendering",
        "trigger_type": payload.trigger_type.value,
        "share_ready_uri": f"s3://rendo-highlights/{uuid4()}.mp4",
    }


@app.post("/v1/voice/commands")
def execute_voice_command(payload: VoiceCommandRequest) -> dict[str, str | float]:
    lowered = payload.transcript.lower()
    intent = "unknown"
    if "backup" in lowered:
        intent = "call_backup"
    elif "scan" in lowered:
        intent = "scan_area"
    elif "hold" in lowered and "fire" in lowered:
        intent = "hold_fire"

    if intent == "unknown":
        raise HTTPException(status_code=422, detail="unsupported command")

    return {
        "command_id": str(uuid4()),
        "status": "executed",
        "intent": intent,
        "confidence": payload.confidence if payload.confidence is not None else 0.87,
    }


@app.post("/v1/memory/events")
def append_memory_event(payload: MemoryEventRequest) -> dict[str, str | int]:
    return {
        "memory_event_id": str(uuid4()),
        "state": "persisted",
        "event_type": payload.event_type,
        "intensity": payload.intensity,
    }


@app.post("/v1/emotion/signals")
def ingest_emotion_signal(payload: EmotionSignalRequest) -> dict[str, str | bool]:
    return {
        "signal_id": str(uuid4()),
        "state": "accepted",
        "triggered_intervention": payload.stress > 0.85,
    }


@app.post("/v1/behavior/predict")
def predict_behavior(payload: BehaviorPredictionRequest) -> dict[str, str | float]:
    churn_risk = min(0.95, 0.15 + 0.03 * len(payload.recent_events))
    return {
        "player_id": str(payload.player_id),
        "predicted_state": "fatigue_risk" if churn_risk > 0.6 else "engaged",
        "churn_risk": round(churn_risk, 2),
    }
