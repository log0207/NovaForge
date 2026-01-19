import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from vault import Vault


def test_store_and_retrieve(tmp_path):
    vault = Vault(tmp_path)
    vault.store("demo", "hello")
    assert vault.retrieve("demo") == "hello"


def test_missing_key_returns_none(tmp_path):
    vault = Vault(tmp_path)
    assert vault.retrieve("nope") is None
