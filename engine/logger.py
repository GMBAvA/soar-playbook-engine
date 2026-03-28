import logging
import json
from datetime import datetime, timezone


def get_logger(name: str) -> logging.Logger:
    """Returns a configured logger that outputs structured JSON."""
    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

    return logger


class JsonFormatter(logging.Formatter):
    """Formats log records as JSON — readable by Splunk and SIEMs."""

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "module": record.name,
            "message": record.getMessage()
        }
        return json.dumps(log_entry)