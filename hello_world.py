# ASCI Art for Hello World initializing Github

import time
import sys

# ─────────────────────────────────────────────
#  Color palette  (ANSI escape codes)
# ─────────────────────────────────────────────
RESET  = "\033[0m"
DIM    = "\033[2m"
BOLD   = "\033[1m"
WHITE  = "\033[97m"
SLATE  = "\033[38;5;245m"
GOLD   = "\033[33m"


# ─────────────────────────────────────────────
#  ASCII art  (thin-stroke, geometric)
# ─────────────────────────────────────────────
ART = [
    "  ██╗  ██╗███████╗██╗     ██╗      ██████╗ ",
    "  ██║  ██║██╔════╝██║     ██║     ██╔═══██╗",
    "  ███████║█████╗  ██║     ██║     ██║   ██║",
    "  ██╔══██║██╔══╝  ██║     ██║     ██║   ██║",
    "  ██║  ██║███████╗███████╗███████╗╚██████╔╝",
    "  ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ",
    "",
    "  ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ ",
    "  ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗",
    "  ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║",
    "  ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║",
    "  ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝",
    "   ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ",
]

RULE   = "  " + "─" * 46
BYLINE = "  a beginning  ·  v1.0.0  ·  2026"


def write(text, color=WHITE, delay=0.03):
    """Stream a line character by character."""
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")


def main():
    print()
    print(DIM + RULE + RESET)
    print()

    # Stream each row of the ASCII art
    for i, row in enumerate(ART):
        color = GOLD if i < 6 else WHITE
        write(row, color=color, delay=0.012)

    print()
    write(RULE, color=DIM + SLATE, delay=0.005)
    print()
    write(BYLINE, color=SLATE, delay=0.03)
    print()
    print(DIM + RULE + RESET)
    print()


if __name__ == "__main__":
    main()
