"""
RECORD CHECK - completed Week 3 lab version

This version implements the Excellent requirements:
- status_of() decides status
- check() calculates difference and percentage
- print_report() prints the report
- a loop allows multiple records and counts OVER LIMIT records
"""

def status_of(percent):
    """Return the status for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return the difference and percentage for a value and limit."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered record-check report."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Percent     : {percent:>9.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


over_limit_count = 0

while True:
    label = input("Record name (or 'quit') : ")
    if label == "quit":
        break

    value = float(input("Value     : "))
    limit = float(input("Limit     : "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"OVER LIMIT records: {over_limit_count}")
