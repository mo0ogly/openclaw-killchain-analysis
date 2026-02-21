#!/usr/bin/env python3
"""OpenClaw — Run all 21 figure scripts to generate 42 PNG."""
import os, sys, subprocess

here = os.path.dirname(os.path.abspath(__file__))
scripts = sorted(f for f in os.listdir(here) if f.startswith("fig") and f.endswith(".py"))

print(f"OpenClaw — {len(scripts)} figure scripts")
print("=" * 50)

errors = []
for s in scripts:
    print(f"\n>>> {s}")
    ret = subprocess.run([sys.executable, os.path.join(here, s)])
    if ret.returncode != 0:
        errors.append(s)

print("\n" + "=" * 50)
if errors:
    print(f"Errors: {errors}")
else:
    print(f"All {len(scripts)} scripts OK — 42 PNG in openclaw_figures/")
