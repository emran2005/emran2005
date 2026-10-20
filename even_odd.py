"""Tell the user whether a chosen whole number is even or odd.

Run it with:  python3 even_odd.py
Or pass the number directly:  python3 even_odd.py 7
"""

import sys


def is_even(n):
    """Return True if n is even, False if it is odd."""
    # A number is even when dividing by 2 leaves no remainder.
    return n % 2 == 0


def main():
    # Use a command-line argument if one was given, otherwise ask.
    if len(sys.argv) > 1:
        entry = sys.argv[1]
    else:
        try:
            entry = input("Enter a whole number: ")
        except EOFError:  # no input at all, e.g. Ctrl-D or an empty pipe
            print("\nError: no input received.", file=sys.stderr)
            return 1

    # int() rejects things like "abc", "3.5" and "", so catch that
    # and give a friendly message instead of a traceback.
    try:
        number = int(entry.strip())
    except ValueError:
        print(f"Error: {entry.strip()!r} is not a whole number. "
              "Please enter an integer like 4 or -7.", file=sys.stderr)
        return 1

    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    return 0


if __name__ == "__main__":
    sys.exit(main())
