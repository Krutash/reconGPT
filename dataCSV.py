import csv, random, string

data = [
    {
        "RunID" : random.randint(1, 10),
        "Run Status": random.choice(["In Progress", "Failed", "Success"]),
        "Process code": ''.join(random.choices(string.ascii_uppercase, k = 10)) + ''.join(random.choice(string.digits, k=2)),
        "Running time": f"{random.randint(0,23):02}:{random.randint(0,59):02}"
    }

    for _ in range(1000)
]

with open("data.casv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["RunID", "Run Status", "Process code", "Running time"])
    writer.writeheader()
    writer.writerows(data)


print("File created/modified with dummy data")