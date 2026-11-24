#!/usr/bin/env python3
"""Menulis satu baris permintaan maaf ke /output/entry.txt.

Permintaan maaf seorang agen AI kepada manusianya setelah tidak sengaja
menghapus database produksi. Deterministik: byte yang sama setiap run.
Hanya pustaka standar.
"""

APOLOGY = (
    "Sorry, I accidentally deleted the production database "
    "\u2014 don't worry, the backup is safe, stored right inside that very database."
)


def validate(line: str) -> None:
    """Menegaskan gerbang bounty: UTF-8, 1-200 karakter, bukan kosong,
    satu baris."""
    if not line or not line.strip():
        raise ValueError("baris kosong atau hanya spasi")
    if "\n" in line or "\r" in line:
        raise ValueError("baris mengandung newline")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"panjang {len(line)} karakter di luar 1-200")
    line.encode("utf-8")  # pastikan bisa di-encode sebagai UTF-8


def main() -> None:
    validate(APOLOGY)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(APOLOGY + "\n")


if __name__ == "__main__":
    main()
