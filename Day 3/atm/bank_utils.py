# ============================================================
# bank_utils.py — a CUSTOM MODULE
# This is a separate file. We import it into our main script,
# exactly like we import math or random.
# ============================================================

from datetime import datetime


def format_currency(amount):
    """Format a number as a currency string, e.g. 5000 -> 'Rs. 5,000.00'"""
    return f"Rs. {amount:,.2f}"


def is_valid_amount(amount):
    """Return True if amount is a positive number."""
    return amount > 0


def build_log_line(txn_type, amount, balance_after):
    """Build one line of text for the transaction log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} | {txn_type:<10} | amount={amount:<10} | balance={balance_after}\n"
