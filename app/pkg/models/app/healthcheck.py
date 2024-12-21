from dataclasses import dataclass

__all__ = ("HEALTHCHECK_STATUS",)


@dataclass(frozen=True)
class HealthcheckStatus:
    status: str = "ok"


HEALTHCHECK_STATUS = HealthcheckStatus()
