from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

KST = ZoneInfo("Asia/Seoul")
DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"


def getKST(format: str = DEFAULT_FORMAT, dt: datetime | None = None) -> str:
    if dt is None:
        target = datetime.now(tz=KST)
    elif dt.tzinfo is None:
        target = dt.replace(tzinfo=KST)
    else:
        target = dt.astimezone(KST)

    return target.strftime(format)
