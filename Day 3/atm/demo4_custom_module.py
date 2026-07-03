# ============================================================
# DEMO 4 — Importing OUR OWN module
# bank_utils.py must be in the same folder as this file.
# ============================================================
import bank_utils

print(bank_utils.format_currency(5000))          # Rs. 5,000.00
print(bank_utils.is_valid_amount(-50))           # False
print(bank_utils.build_log_line("DEPOSIT", 500, 5500))

# Cleaner import style -- import only what you need
from bank_utils import format_currency

print(format_currency(12345.5))  # Rs. 12,345.50
