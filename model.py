from typing import Any
from pydantic import BaseModel

class Measurement(BaseModel):
    user_profile: dict[str, Any]
    measurement: dict[str, Any]

class UserProfile(BaseModel):
    timestamp: str
    user_id: str
    user_height: str
    user_weight: str