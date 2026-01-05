"""Command-line interface for OpenVault."""

import argparse
import sys

from scanner import scan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="openvault",
                                     description="Infrastructure security toolkit")
    sub = parser.add_subparsers(dest="command")
    scan_p = sub.add_parser("scan", help="scan a file for leaked secrets")
    scan_p.add_argument("path")
    args = parser.parse_args(argv)

    if args.command == "scan":
        with open(args.path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        findings = scan(text)
        if not findings:
            print("No secrets detected.")
            return 0
        for kind, hit in findings:
            print(f"[{kind}] {hit}")
        return 1
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
