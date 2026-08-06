#!/usr/bin/env python3

import sys


def args_check(scores: list) -> None:
    if len(scores) == 0:
        raise Exception(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
                        )


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argv = sys.argv
    argv_len = len(argv)
    scores: list[int] = []
    i = 1
    try:
        while(i < argv_len):
            try:
                scores.append(int(argv[i]))
            except ValueError as e:
                print(f"Invalid parameter: {argv[i]}")
            i += 1
        args_check(scores)
    except Exception as e:
        print(f"eee\n {e}")
