from datetime import datetime
from pydantic import BaseModel
from typing import List

class ApplicationUserSchema(BaseModel):
    user_id: int
    role_id: int
    first_name: str
    last_Name: str
    