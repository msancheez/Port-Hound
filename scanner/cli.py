import argparse
import sys
from scanner.core import run_scanner

def main() -> None:
    # Parameters configuration
    parser = argparse.ArgumentParser(
        description="TCP PORT SCANNER",
        epilog="Example: python main.py -t 127.0.0.1 -p 1000 -w 50"
    )

    # -t / --target [needed]
    parser.add_argument("-t", "--target",
                        type=str,
                        required=True,
                        help="Target IP Address (Ex. 127.0.0.1)")

    # -p / --ports [optional]
    parser.add_argument("-p", "--ports",
                        type=int,
                        default=1024,
                        help="Max Port to scann (1-x). 1024 by default")

    # -w / --workers [optional]
    parser.add_argument("-w", "--workers",
                        type=int,
                        default=100,
                        help="Number of threads. Add more threads for faster (It also could saturate the device)")

    # If there are no arguments
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    print("/" * 100)
    print("/" * 43 ," PORT-HOUND ", "/" * 43)
    print(" " * 36," python based port scanner ", " " * 22, "by msancheez")
    print ("/" * 100, "\n")

    try:
        run_scanner(args.target, args.ports, args.workers)
    except KeyboardInterrupt:
        print("\n[!] Scann interrupted by user. Leaving...\n")
        sys.exit(1)