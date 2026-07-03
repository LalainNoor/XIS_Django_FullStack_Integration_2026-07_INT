import logging
from pathlib import Path

project_root = Path(__file__).resolve().parents[3]

log_dir = project_root / "results" / "logs"

log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_dir / "application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("InferenceLogger")