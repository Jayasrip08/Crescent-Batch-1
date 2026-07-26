# ============================================================
# DEMO 5 — File I/O: read, write, append
# ============================================================

# WRITE (overwrites the file each time)
with open("notes.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

# READ (whole file at once)
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# READ line by line
with open("notes.txt", "r") as f:
    for line in f:
        print("LINE:", line.strip())

# APPEND (adds to the end, doesn't erase existing content)
with open("notes.txt", "a") as f:
    f.write("Third line, added later\n")

# Handling a missing file safely
try:
    with open("does_not_exist.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("That file doesn't exist yet -- handled gracefully.")

# Why 'with'? It automatically closes the file for you,
# even if an error happens partway through.
