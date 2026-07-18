import csv
import sys


def consumed(row):
    requests = int(row["requests"])
    failures = int(row["failures"])
    allowed_failures = requests * float(row["error_budget_pct"]) / 100
    return round(failures / allowed_failures, 2) if allowed_failures else 0


def status(row):
    value = consumed(row)
    return "exhausted" if value >= 1 else "watch" if value >= 0.75 else "ok"


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['endpoint']} {status(row)} {consumed(row)}")


if __name__ == "__main__":
    main(sys.argv[1])
