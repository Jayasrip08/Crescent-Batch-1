# ============================================================
# DEMO 3 — Importing built-in modules
# ============================================================
import math
import random
from datetime import datetime

# math module
print(math.sqrt(64))        # 8.0
print(math.ceil(4.2))       # 5
print(round(math.pi, 2))    # 3.14

# random module
print(random.randint(1, 100))          # random int 1-100
print(random.choice(["A", "B", "C"]))  # random pick

# datetime module -- we'll use this for transaction timestamps today
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
