from pathlib import Path
path = Path(__file__).resolve().parents[1] / "records_sample.txt"
with open(path) as file:
    print(file.read())
