#!/usr/bin/python3
"""
Log parsing script
"""

import sys


def initialize_stats() -> dict:
    """
    Initialize the statistics dictionary for log parsing.
    """
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    return {code: 0 for code in codes}


def print_stats(stats: dict, file_size: int) -> None:
    """
    Print the current statistics of the log.
    """
    print("File size: {}".format(file_size))
    for code, count in sorted(stats.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def parse_line(line: str, stats: dict) -> int:
    """
    Parse a single log line and update the stats.
    Returns the file size if parsed correctly, otherwise 0.
    """
    data = line.split()
    file_size = 0

    # Extract status code
    status_code = data[-2] if len(data) > 1 else None
    if status_code in stats:
        stats[status_code] += 1

    # Extract file size
    try:
        file_size = int(data[-1])
    except (ValueError, IndexError):
        pass  # Ignore errors for invalid file size

    return file_size


def main():
    """
    Main function to read from stdin and process log lines.
    """
    stats = initialize_stats()
    total_file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            total_file_size += parse_line(line.strip(), stats)

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(stats, total_file_size)

        # Print final stats
        print_stats(stats, total_file_size)

    except KeyboardInterrupt:
        print_stats(stats, total_file_size)
        raise


if __name__ == "__main__":
    main()
