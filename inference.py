#!/usr/bin/env python3
"""
Simple crowd-density demo script (CPU-friendly).
This script implements a deterministic, explainable heuristic to estimate
relative crowd density in a single image and produces an annotated output image.

Usage example:
    python inference.py --image sample_images/test1.jpg --output output.jpg

Note: This is an educational demo, not a production counting model.
"""

import argparse
import logging
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2


def estimate_crowd_by_edge_density(image_bgr: np.ndarray) -> int:
    """
    Estimate a relative crowd count using edge density and texture heuristics.

    Steps (heuristic):
    1. Convert to grayscale and apply a median blur to reduce noise.
    2. Use Canny edge detector to get an edge map.
    3. Compute the ratio of edge pixels to total pixels and scale to an integer.

    This yields a stable, explainable proxy for crowdedness that works as a demo.
    """
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 5)
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

    edge_pixels = int(np.count_nonzero(edges))
    total_pixels = edges.size
    edge_ratio = edge_pixels / total_pixels

    # Scale ratio to a human-readable integer (tunable constant)
    estimated_count = int(edge_ratio * 2000)
    return estimated_count


def annotate_and_save(pil_img: Image.Image, text: str, out_path: Path) -> None:
    """Annotate the image with the provided text and save to disk."""
    draw = ImageDraw.Draw(pil_img)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", size=28)
    except Exception:
        font = ImageFont.load_default()

    # Draw semi-transparent rectangle behind text for readability
    text_size = draw.textsize(text, font=font)
    padding = 8
    rect_xy = (10, 10, 10 + text_size[0] + padding * 2, 10 + text_size[1] + padding * 2)
    draw.rectangle(rect_xy, fill=(0, 0, 0, 160))
    draw.text((10 + padding, 10 + padding), text, fill=(255, 255, 255), font=font)

    pil_img.save(out_path)


def main():
    parser = argparse.ArgumentParser(description="Run a simple crowd-density demo on a single image.")
    parser.add_argument("--image", required=True, help="Path to the input image file")
    parser.add_argument("--output", default="output.jpg", help="Path to the annotated output image")
    args = parser.parse_args()

    input_path = Path(args.image)
    output_path = Path(args.output)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if not input_path.exists():
        logging.error("Input image not found: %s", input_path)
        return

    # Open and convert to OpenCV BGR format
    pil_img = Image.open(input_path).convert("RGB")
    image_np = np.array(pil_img)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    estimated = estimate_crowd_by_edge_density(image_bgr)
    logging.info("Estimated count (approx.): %d", estimated)

    annotate_and_save(pil_img, f"Estimated count: {estimated}", output_path)
    logging.info("Annotated output saved to %s", output_path)


if __name__ == "__main__":
    main()
