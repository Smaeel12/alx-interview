#!/usr/bin/python3
"""
Log parsing script
"""

import sys
import re


def initialize_log() -> dict:
    """
    Initialize the log structure for storing file size and
    status code frequency.
    """
    return {
        "file_size": 0,
        "code_frequency": {
            str(code): 0 for code in [
                200,
                301,
                400,
                401,
                403,
                404,
                405,
                500]}}


def parse_line(line: str, log: dict) -> None:
    """
    Parse a single line of log and update the log metrics.
    """
    regex = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r' - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] '
        r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

    match = regex.fullmatch(line.strip())
    if match:
        code = match.group(3)  # Status code
        file_size = int(match.group(4))  # File size

        # Update metrics
        log["file_size"] += file_size
        if code in log["code_frequency"]:
            log["code_frequency"][code] += 1


def output(log: dict) -> None:
    """
    Display the current statistics from the log.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


def main():
    log = initialize_log()
    line_count = 0

    try:
        for line in sys.stdin:
            parse_line(line, log)
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                output(log)

    except KeyboardInterrupt:
        output(log)

    finally:
        output(log)


if __name__ == "__main__":
    main()
