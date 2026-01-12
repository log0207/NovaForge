"""Secret scanning for OpenVault — detects leaked credentials in text."""

from __future__ import annotations

import re

PATTERNS = {
    "api_key": re.compile(
        r"\b(?:API[_-]?KEY|APITOKEN)\s*[:=]\s*([A-Z0-9]{8,})",
        re.IGNORECASE,
    ),
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "generic_secret": re.compile(r"\b(?:SECRET|PASSWORD|TOKEN)\s*[:=]\s*\S+", re.IGNORECASE),
}


def scan(text: str) -> list[tuple[str, str]]:
    """Return (kind, matched_text) pairs for every pattern hit."""
    findings: list[tuple[str, str]] = []
    for name, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            findings.append((name, match.group(0)))
    return findings
