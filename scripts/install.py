#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

HOME = Path.home()
CONFIG_PLUGINS = HOME / ".gemini" / "config" / "plugins" / "delta-skills"
REPO_ROOT = Path(__file__).resolve().parent.parent

def install():
    print(f"Installing delta-skills into {CONFIG_PLUGINS}...")
    CONFIG_PLUGINS.mkdir(parents=True, exist_ok=True)
    shutil.copy(REPO_ROOT / "plugin.json", CONFIG_PLUGINS / "plugin.json")
    skills_dest = CONFIG_PLUGINS / "skills"
    if skills_dest.exists():
        shutil.rmtree(skills_dest)
    shutil.copytree(REPO_ROOT / "skills", skills_dest)
    print("✅ Successfully installed delta-skills!")

if __name__ == "__main__":
    install()
