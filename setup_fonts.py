#!/usr/bin/env python3
"""
Setup script to download and register custom fonts.
Run this after installing requirements: python setup_fonts.py
"""
import os
import urllib.request
from pathlib import Path

def download_patrick_hand():
    """Download Patrick Hand font from Google Fonts GitHub"""
    font_url = "https://github.com/google/fonts/raw/main/ofl/patrickhand/PatrickHand-Regular.ttf"
    font_path = Path(__file__).parent / "PatrickHand.ttf"
    
    if font_path.exists():
        print(f"✓ PatrickHand.ttf already exists")
        return
    
    print(f"Downloading Patrick Hand font...")
    try:
        urllib.request.urlretrieve(font_url, font_path)
        print(f"✓ Successfully downloaded PatrickHand.ttf")
    except Exception as e:
        print(f"✗ Error downloading font: {e}")
        raise

def download_great_vibes():
    """Download Great Vibes font from Google Fonts GitHub"""
    font_url = "https://github.com/google/fonts/raw/main/ofl/greatvibes/GreatVibes-Regular.ttf"
    font_path = Path(__file__).parent / "GreatVibes-Regular.ttf"
    
    if font_path.exists():
        print(f"✓ GreatVibes-Regular.ttf already exists")
        return
    
    print(f"Downloading Great Vibes font...")
    try:
        urllib.request.urlretrieve(font_url, font_path)
        print(f"✓ Successfully downloaded GreatVibes-Regular.ttf")
    except Exception as e:
        print(f"✗ Error downloading font: {e}")
        raise

if __name__ == "__main__":
    download_patrick_hand()
    download_great_vibes()
