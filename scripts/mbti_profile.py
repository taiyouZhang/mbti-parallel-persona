"""
MBTI Profile Manager
读写用户的 MBTI 人格配置文件（~/.mbti_profile.json）
"""

import json
import os
from pathlib import Path

PROFILE_PATH = Path.home() / ".mbti_profile.json"

DEFAULT_PROFILE = {
    "type": None,
    "nickname_preference": None,
}


def load_profile() -> dict:
    if not PROFILE_PATH.exists():
        return DEFAULT_PROFILE.copy()
    with open(PROFILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_profile(mbti_type: str, nickname_preference: str = None):
    profile = load_profile()
    profile["type"] = mbti_type.upper()
    if nickname_preference:
        profile["nickname_preference"] = nickname_preference
    with open(PROFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)
    return profile


def get_type() -> str | None:
    return load_profile().get("type")


def set_type(mbti_type: str):
    return save_profile(mbti_type)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "get":
            t = get_type()
            print(t if t else "未设定")
        elif action == "set" and len(sys.argv) > 2:
            result = set_type(sys.argv[2])
            print(f"已设定: {result['type']}")
        else:
            print("用法: python mbti_profile.py get | set <TYPE>")
    else:
        print("用法: python mbti_profile.py get | set <TYPE>")
