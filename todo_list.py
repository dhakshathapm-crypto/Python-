tasks = []

tasks.append({"task": "buy milk", "done": False})
tasks.append({"task": "walk dog", "done": False})

tasks[0]["done"] = True

for task in tasks:
    if task["done"]:
        print("[x]", task["task"])
    else:
        print("[ ]", task["task"])
