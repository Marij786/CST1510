"""Week 5 record check mini-project (excellent level)."""
from pathlib import Path

class Record:
    def __init__(self, label, value, limit):
        """Store the record details."""
        self.label, self.value, self.limit = label, value, limit

    def summary(self):
        """Return a short record description."""
        return f"{self.label}: {self.value}/{self.limit}"

    def percent(self):
        """Calculate percentage of the limit."""
        return self.value / self.limit * 100

    def status(self):
        """Categorize the record's value."""
        pct = self.percent()
        return "OVER LIMIT" if pct >= 100 else "WARNING" if pct >= 90 else "OK"

    def is_over(self):
        """Return whether the record reached its limit."""
        return self.value >= self.limit

def load_records(path):
    """Load comma-separated records from a text file."""
    result = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            if line.strip():
                label, value, limit = line.strip().split(",")
                result.append(Record(label, float(value), float(limit)))
    return result

def main():
    """Load records and print their status reports."""
    records = load_records(Path(__file__).with_name("records_sample.txt"))
    over_count = 0
    for record in records:
        print("\n" + "=" * 34)
        print(f"  RECORD CHECK  -  {record.label}")
        print("=" * 34)
        print(f"  Value : {record.value}")
        print(f"  Limit : {record.limit}")
        print(f"  Status: {record.status()}")
        print("=" * 34)
        if record.is_over():
            over_count += 1
    print(f"\nOVER LIMIT: {over_count} of {len(records)} records")

if __name__ == "__main__":
    main()
