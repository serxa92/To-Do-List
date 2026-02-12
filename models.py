from pydantic import BaseModel, Field
from typing import Optional,Annotated


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Annotated[int, Field(ge=1, le=3)] = 2
    
    
# Modelo de datos para la tarea con ID y estado.

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
    priority: Annotated[int, Field(ge=1, le=3)] = 2
    created_at: str
    