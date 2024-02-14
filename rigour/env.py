from os import environ as env
from zoneinfo import ZoneInfo
from normality import stringify


def env_str(name: str, default: str) -> str:
    """Ensure the env returns a string even on Windows (#100)."""
    value = stringify(env.get(name))
    return default if value is None else value


def env_int(name: str, default: int) -> int:
    """Ensure the env returns an int."""
    try:
        return int(env.get(name, default))
    except (ValueError, TypeError):
        return default


def env_float(name: str, default: float) -> float:
    """Ensure the env returns an float."""
    try:
        return float(env.get(name, default))
    except (ValueError, TypeError):
        return default


# Timezone information:
TZ_NAME = env_str("TZ", "UTC")
TZ = ZoneInfo(TZ_NAME)


# Levenshtein tolerance settings
LEVENSHTEIN_MAX_EDITS = env_int("RR_LEVENSHTEIN_MAX_EDITS", 4)
LEVENSHTEIN_MAX_PERCENT = env_float("RR_LEVENSHTEIN_MAX_PCT", 0.2)
