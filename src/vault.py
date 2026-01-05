"""Core vault operations for OpenVault."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

VAULT_DIR = Path.home() / ".openvault"


class Vault:
    """A tiny key-value vault for storing secrets locally."""

    def __init__(self, root: Path = VAULT_DIR) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str) -> Path:
        digest = hashlib.sha256(key.encode()).hexdigest()[:16]
        return self.root / f"{digest}.json"

    def store(self, key: str, value: str) -> None:
        blob = {"key": key, "value": base64.b64encode(value.encode()).decode()}
        self._path(key).write_text(json.dumps(blob))

    def retrieve(self, key: str) -> str | None:
        path = self._path(key)
        if not path.exists():
            return None
        blob = json.loads(path.read_text())
        return base64.b64decode(blob["value"]).decode()
