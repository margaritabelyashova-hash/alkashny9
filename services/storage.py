def save_registry(data):
    with open("data/registry.txt", "a") as f:
        f.write(data + "\n")
