import sys


def process_scores(scores: list[int]) -> None:
    args_check(scores)
    total_players = len(scores)
    total_score = sum(scores)
    avg_score = total_score / total_players
    hight_score = max(scores)
    low_score = min(scores)
    range_score = hight_score - low_score
    print(f"Scores procesed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Average score: {avg_score}")
    print(f"Hight score: {hight_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {range_score}")


def args_check(scores: list[int]) -> None:
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
        while (i < argv_len):
            try:
                scores.append(int(argv[i]))
            except ValueError:
                print(f"Invalid parameter: {argv[i]}")
            i += 1
        process_scores(scores)
        args_check(scores)
    except Exception as e:
        print(f"{e}")
