# ============================================================
# DEMO 2 — Local vs Global scope
# The #1 source of "why isn't my variable updating" bugs.
# ============================================================

balance = 5000  # global variable

def show_balance_wrong():
    # This creates a NEW local variable, doesn't touch the global one
    balance = 0
    print(f"Inside function: {balance}")

show_balance_wrong()
print(f"Outside function (unchanged): {balance}")  # still 5000

def deposit_wrong(amount):
    balance = balance + amount  # ERROR! Python sees 'balance' is assigned
    return balance               # locally -> UnboundLocalError

# deposit_wrong(100)  # <-- uncomment to show the error live

def deposit_correct(current_balance, amount):
    new_balance = current_balance + amount
    return new_balance

balance = deposit_correct(balance, 100)
print(f"Correct pattern: {balance}")  # 5100

# Rule of thumb we teach: functions should take what they need as
# parameters and return results -- avoid relying on global variables.
