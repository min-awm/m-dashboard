from enum import Enum


class TokenType(str, Enum):
    access = "ACCESS"
    refresh = "REFRESH"
