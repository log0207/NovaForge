import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from scanner import scan


def test_detects_api_key():
    assert scan("API_KEY=NF-PROD-7A91-KX42")


def test_detects_private_key():
    assert scan("-----BEGIN RSA PRIVATE KEY-----")


def test_clean_text_has_no_findings():
    assert scan("just some ordinary documentation") == []
