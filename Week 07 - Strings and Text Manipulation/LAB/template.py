"""Completed IT-lane record-check mini-project. Run: python template.py"""

def parse_line(raw_line):
    """Clean and parse one messy IT status record."""
    hostname_part, rest = raw_line.strip().split(",", 1)
    record = {"hostname": hostname_part.strip().lower()}
    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        record[key.strip().lower()] = float(value.strip())
    if "used" not in record or "total" not in record:
        raise ValueError("Each record must contain used and total")
    return {"hostname": record["hostname"], "used": record["used"], "total": record["total"]}

def status_of(used, total, warning_at=90):
    """Classify a server usage percentage."""
    if total <= 0:
        raise ValueError("total must be greater than zero")
    percentage = used / total * 100
    if percentage >= 100: return "OVER LIMIT"
    if percentage >= warning_at: return "WARNING"
    return "OK"

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=120,TOTAL=100",
    "  srv-03,used=45 ,total=100",
    "Srv-04 , used = 93 , total=100",
    "  SRV-05 , TOTAL=200 , USED=150  ",
]
results = []
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["used"], record["total"])
    results.append((record, status))
    print(record, "|", status)
flagged = sum(status != "OK" for _, status in results)
print(f"Summary: {len(results)} records, {flagged} flagged.")
