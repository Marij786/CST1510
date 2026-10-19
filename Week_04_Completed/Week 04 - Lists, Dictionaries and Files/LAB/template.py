"""Week 4 record checker: IT lane, Excellent tier."""
from pathlib import Path


def check_record(value, limit):
    """Return difference, percentage and status for a record."""
    difference = value - limit
    percent = value / limit * 100 if limit else float("inf")
    status = "OVER LIMIT" if value > limit else "WARNING" if percent >= 90 else "OK"
    return difference, percent, status


def print_report(label, difference, percent, status):
    """Print a formatted record report."""
    print(f"{label}: {status} | difference={difference:.1f} | usage={percent:.1f}%")


def load_records(path):
    """Load records from a comma-separated text file safely."""
    records = []
    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                label, value, limit = line.strip().split(",")
                records.append({"label": label, "value": float(value), "limit": float(limit)})
    except FileNotFoundError:
        print(f"File not found: {path}")
    return records


def main():
    """Check all records, print reports and save results."""
    records = load_records(Path(__file__).with_name("my_records.txt"))
    over_limit = 0
    results = []
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], difference, percent, status)
        over_limit += status == "OVER LIMIT"
        results.append(f"{record['label']},{status}\n")
    print(f"{over_limit} of {len(records)} were over limit")
    with open(Path(__file__).with_name("project_results.txt"), "w", encoding="utf-8") as file:
        file.writelines(results)


if __name__ == "__main__":
    main()
