raw_line = "srv-01,used=unknown,total=100"
host, rest = raw_line.split(",", 1)
for piece in rest.split(","):
    key, value = piece.split("=", 1)
    try:
        print(key.strip(), float(value.strip()))
    except ValueError:
        print(f"Cannot convert {key.strip()}={value.strip()!r} to a number")
