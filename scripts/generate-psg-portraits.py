#!/usr/bin/env python3
"""Generate PSG-styled football portraits from real Linkeo team photos."""
import base64
import json
import os
import subprocess
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path("/Users/Romain/PSG-Challenge-Mai-2026")
RAW = ROOT / "assets/img/raw"
OUT = ROOT / "assets/img/players"
OUT.mkdir(parents=True, exist_ok=True)

ENV = Path("/Users/Romain/OS-Central/.env")
MODEL = "gemini-3.1-flash-image-preview"
API = "https://generativelanguage.googleapis.com/v1beta/models"

PSG_PROMPT_TEMPLATE = (
    "Transform this person into a stunning professional football player portrait. "
    "Preserve EXACTLY their facial features (eyes, nose, mouth, jawline, hairstyle, beard, skin tone) — same person, no face change. "
    "Replace the clothing with an OFFICIAL PSG (Paris Saint-Germain) home jersey 2025-2026: deep navy blue body with bold red vertical stripe down the center, white accents, no visible sponsor logo (clean front). "
    "Add subtle PSG visual identity: small embroidered fleur-de-lys patterns on collar/sleeves, premium fabric texture. "
    "{role_specific} "
    "Studio photography style: dramatic lighting from above-left, deep dark navy gradient background with subtle golden particles/spotlights, professional sports photography mood. "
    "High-end editorial portrait, magazine cover quality, sharp focus on face, slight blur on background, FUT card aesthetic. "
    "Stand confident, slight 3/4 angle, head up, intense determined gaze toward camera or slightly off-camera. "
    "Vertical 3:4 portrait composition, body framed mid-chest up. Photorealistic, ultra detailed, 4K quality."
)

ARSENAL_PROMPT_TEMPLATE = (
    "Transform this person into a stunning professional football player portrait. "
    "Preserve EXACTLY their facial features (eyes, nose, mouth, jawline, hairstyle, beard, glasses, skin tone) — same person, no face change. "
    "Replace the clothing with an OFFICIAL ARSENAL FC home jersey 2025-2026: bold red body with white sleeves, white collar accents, no visible sponsor logo (clean front), small embroidered cannon crest. "
    "{role_specific} "
    "Studio photography style: dramatic lighting from above-left, deep dark red-burgundy gradient background with subtle white/silver particles, professional sports photography mood. "
    "High-end editorial portrait, magazine cover quality, sharp focus on face, slight blur on background, FUT card aesthetic. "
    "Stand confident, slight 3/4 angle, head up, intense determined gaze toward camera. "
    "Vertical 3:4 portrait composition, body framed mid-chest up. Photorealistic, ultra detailed, 4K quality."
)

PLAYERS = [
    ("romain",  "Capitaine PSG — captain armband on left arm in gold, slightly more authoritative pose, hands on hips or arms crossed, leadership aura, gold accent lighting on face.", "psg"),
    ("enzo",    "Striker PSG #9 — dynamic athletic stance, ready to play, focused expression.", "psg"),
    ("alex",    "Midfielder PSG #6 — composed playmaker stance, calm intelligent gaze.", "psg"),
    ("adrien",  "Defender PSG #5 — solid grounded stance, determined defensive posture.", "psg"),
    ("geff",    "Capitaine ARSENAL — captain armband on left arm in red and white, authoritative pose, leadership aura.", "arsenal"),
]


def load_api_key():
    for line in ENV.read_text().splitlines():
        if line.startswith("GOOGLE_AI_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("missing key")


def transform(api_key, slug, role_specific, team):
    src = RAW / f"{slug}.png"
    dst = OUT / f"{slug}-psg.png" if team == "psg" else OUT / f"{slug}-arsenal.png"

    template = PSG_PROMPT_TEMPLATE if team == "psg" else ARSENAL_PROMPT_TEMPLATE
    prompt = template.format(role_specific=role_specific)

    img_b64 = base64.b64encode(src.read_bytes()).decode("utf-8")
    body = {
        "contents": [{"parts": [
            {"text": prompt},
            {"inlineData": {"mimeType": "image/png", "data": img_b64}}
        ]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]},
    }
    url = f"{API}/{MODEL}:generateContent?key={api_key}"
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"}, method="POST")

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                result = json.loads(r.read().decode())
            for part in result["candidates"][0]["content"]["parts"]:
                if "inlineData" in part:
                    dst.write_bytes(base64.b64decode(part["inlineData"]["data"]))
                    return slug, True, str(dst), len(dst.read_bytes())
            return slug, False, "no image in response", 0
        except urllib.error.HTTPError as e:
            err = e.read().decode() if e.fp else ""
            if e.code in (429, 500, 503) and attempt < 2:
                time.sleep(2 ** (attempt + 2))
                continue
            return slug, False, f"HTTP {e.code}: {err[:200]}", 0
        except Exception as e:
            if attempt < 2:
                time.sleep(5)
                continue
            return slug, False, str(e), 0
    return slug, False, "max retries", 0


def main():
    api_key = load_api_key()
    print(f"=== Generating {len(PLAYERS)} PSG/ARSENAL portraits ===\n")
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(transform, api_key, p[0], p[1], p[2]): p[0] for p in PLAYERS}
        for fut in as_completed(futures):
            slug, ok, info, size = fut.result()
            tag = "OK" if ok else "FAIL"
            extra = f" ({size//1024} KB)" if ok else ""
            print(f"  [{tag}] {slug}{extra} — {info}")


if __name__ == "__main__":
    main()
