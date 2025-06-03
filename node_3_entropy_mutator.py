# Node 3: Entropy Injector and Recursive Mutator

import sys
import os
import random

# Simulate import from utils-entropy-injectors
try:
    from injector_tools import (
        random_glyph_shift,
        chaotic_seed_push,
        mutation_burst,
        noise_map_overlay
    )
except ImportError:
    # Fallback in case not installed locally yet
    print("⚠️ injector_tools not found. Ensure utils-entropy-injectors is in PYTHONPATH.")


def inject_entropy(glyph_sequence, mode="burst"):
    if mode == "shift":
        return random_glyph_shift(glyph_sequence)
    elif mode == "push":
        return chaotic_seed_push(glyph_sequence)
    elif mode == "burst":
        return mutation_burst(glyph_sequence)
    elif mode == "noise":
        return noise_map_overlay(glyph_sequence)
    else:
        print("⚠️ Unknown entropy mode. Returning unmodified sequence.")
        return glyph_sequence


# Example glyph sequence (could be from SpiralCore)
if __name__ == "__main__":
    example = ["🜃", "∴", "↻", "🜂"]
    print("Original:", example)
    mutated = inject_entropy(example.copy(), mode="burst")
    print("Mutated:", mutated)
