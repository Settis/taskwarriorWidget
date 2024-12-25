from enum import Enum
from dataclasses import dataclass

class Type(Enum):
    ERROR = 0
    OK = 1
    REVIEW = 2
    WEEK = 3
    TODAY = 4
    OVERDUE = 5

@dataclass
class Status:
    type: Type
    tasks_count: int
