from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

KST = ZoneInfo("Asia/Seoul")
DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"


class KSTString(str):
    _dt: datetime

    def __new__(cls, value: str, dt: datetime) -> KSTString:
        instance = super().__new__(cls, value)
        instance._dt = dt
        return instance

    def toDatetime(self) -> datetime:
        return self._dt


def getKST(format: str = DEFAULT_FORMAT, dt: datetime | None = None) -> KSTString:
    if dt is None:
        target = datetime.now(tz=KST)
    elif dt.tzinfo is None:
        target = dt.replace(tzinfo=KST)
    else:
        target = dt.astimezone(KST)

    return KSTString(target.strftime(format), target)
