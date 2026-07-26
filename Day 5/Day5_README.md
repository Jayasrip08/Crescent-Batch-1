# Day 5 — NumPy Basics (Self-Study)

**Phase 01 · Full Stack AI Developer Program · Innolift Ventures**
**Status:** No live class today (Crescent college holiday). Self-paced — work through it today, submit before Day 6.
**Today's build:** **FitTrack Analytics** — a brand-new NumPy-powered weekly fitness report.

---

## Recap: Where You Left Off

| Day | What you learned | What you built |
|---|---|---|
| **Day 1** | Variables, data types, f-strings | Profile Card |
| **Day 2** | if/elif/else, while & for loops, break/continue | ATM Simulator |
| **Day 3** | Functions, scope, modules, file I/O | CampusLib |
| **Day 4** | Lists, tuples, dicts, sets | GradeVault |

Today adds **NumPy** — the library almost every ML tool in Phase 2 (scikit-learn, TensorFlow, PyTorch) is quietly built on top of. If Day 4 was "how to organize data," Day 5 is "how to do fast math on data" — the entire point of AI. Today's project is a fresh one too: **FitTrack Analytics**, a standalone script that turns a week of step-count data into a real fitness report.

---

## 1. What Is NumPy, and Why Not Just Use Lists?

**Definition:** NumPy ("Numerical Python") gives Python a new data type — the **array** — built for fast, large-scale number crunching. Unlike a list, a NumPy array lets you apply one operation to *every* element at once, without writing a loop. This is called **vectorization**.

**Setup (once):**
```bash
pip install numpy
```

**Syntax:**
```python
import numpy as np      # "np" is the universal shorthand
```

---

## 2. Creating Arrays

**Syntax:**
```python
arr = np.array([item1, item2, item3])
```

**Example:**
```python
import numpy as np

scores = np.array([82, 58, 30, 91, 67])
print(scores)          # [82 58 30 91 67]
print(type(scores))    # <class 'numpy.ndarray'>

zeros = np.zeros(5)          # array([0., 0., 0., 0., 0.])
counted = np.arange(0, 10, 2)  # array([0, 2, 4, 6, 8])
```

---

## 3. Indexing & Slicing

**Definition:** Just like a list, you can grab one item or a range — and for 2D data (rows and columns, like a spreadsheet), you can access both at once.

**Syntax:**
```python
arr[index]           # single item
arr[start:stop]       # a slice/range
arr2d[row, col]       # 2D array access
```

**Example:**
```python
scores = np.array([82, 58, 30, 91, 67])

print(scores[0])       # 82 -> first student's score
print(scores[1:3])     # [58 30]
print(scores[-1])      # 67 -> last item
```

---

## 4. Vectorized Operations (the whole point of NumPy)

**Definition:** With a plain Python list, applying math to every item means writing a loop. With a NumPy array, you write the operation once and NumPy applies it to every element automatically — and it's dramatically faster.

**Example:**
```python
scores = np.array([82, 58, 30, 91, 67])

print(scores + 5)          # add 5 bonus marks to every score, no loop
print(scores.mean())       # 65.6
print(scores.max())        # 91
print(scores.min())        # 30
print(scores.sum())        # 328

above_avg = scores > scores.mean()
print(above_avg)            # [True False False True True]
print(np.sum(above_avg))    # 3 -> count of students above average
```

---

## 🌟 Something New: Why Is NumPy So Much Faster?

On large datasets, NumPy can be **10–100x faster** than a plain Python loop. This matters enormously once you're training ML models on thousands or millions of data points in Phase 2. Try it yourself:

```python
import numpy as np
import time

size = 1_000_000
python_list = list(range(size))
numpy_array = np.arange(size)

start = time.time()
result_list = [x * 2 for x in python_list]
print("Python loop:", time.time() - start, "seconds")

start = time.time()
result_array = numpy_array * 2
print("NumPy vectorized:", time.time() - start, "seconds")
```

Run it and compare the two printed times — that gap is why NumPy sits underneath almost every AI framework you'll use later in this program.

---

## 📝 Your Tasks for Today

Work through these **in order**. Tasks 1–4 are small, real-world-useful tools — each one is a genuinely usable mini-tool, not just a syntax drill. Task 5 is today's main mini project — budget the most time for it.

### Task 1 — Grocery Bill Calculator (Array Creation + Vectorized Ops)
**Real-world use:** every billing screen you've ever seen does exactly this math.
Create `grocery_bill.py`. Build two NumPy arrays: `prices = np.array([...])` and `quantities = np.array([...])` for at least 5 items. Compute `line_totals = prices * quantities` (vectorized, no loop). Print each item's line total and the `grand_total = line_totals.sum()`.

### Task 2 — Temperature Converter Batch (Vectorized Apply)
**Real-world use:** weather apps convert a whole week of readings at once, not one at a time.
Create `temp_converter.py`. Build `celsius = np.array([...])` with 7 days of temperatures. Convert the whole array to Fahrenheit in one line: `fahrenheit = celsius * 9/5 + 32`. Print both arrays side by side with clear labels.

### Task 3 — Exam Curve Applier (Vectorized + Stats)
**Real-world use:** teachers do this after almost every exam.
Create `curve_applier.py`. Build `raw_scores = np.array([...])` with at least 6 scores. Apply a 4-mark curve to the whole array at once (no loop). Print the original mean and the curved mean side by side.

### Task 4 — Weekly Sales Quick Stats (Stats + Boolean Masking)
**Real-world use:** this is the first real step of small-business or retail analytics.
Create `sales_stats.py`. Build `sales = np.array([...])` with 7 days of sales figures. Print the mean, max, min, and total. Use a boolean mask to find and count how many days were above the weekly average.

### Task 5 — Main Mini Project: FitTrack Analytics

Build a brand-new file — `fittrack_analytics.py` — that turns a week of step-count data into a full fitness report. This is the big one: it pulls together **everything from Days 1–5**, and it should take real effort.

First, create a small log file `steps_log.txt` with 7 lines, one per day, in the format `Monday:8500` (make up your own realistic numbers for all 7 days).

Your FitTrack Analytics must:

1. **(Day 3)** Use `with open("steps_log.txt", "r") as f:` to read every line, handling a missing file with `try/except FileNotFoundError`.
2. **(Day 2)** Use a `for` loop to parse each line and pull out the day name and step count.
3. **(Day 4)** Store the results in a **dictionary**: `{"Monday": 8500, "Tuesday": 6200, ...}`.
4. **(Day 5)** Convert the dictionary's step values into a **NumPy array** and compute the mean, max, and min.
5. **(Day 5)** Use a vectorized operation to compute a **normalized activity score (0–1)** for every day.
6. **(New)** Write `goal_rate()` that uses a boolean mask to compute the percentage of days meeting an 8,000-step goal: `np.sum(steps >= 8000) / len(steps) * 100`.
7. **(New)** Use `np.argmax()` and `np.argmin()` to identify the **most active day** and **least active day** by name.
8. **(New)** Use `np.argsort()` to print the full week **ranked highest to lowest** activity, not just in the order it was read from the file.
9. **(Day 1)** Print a clean report using f-strings throughout.
10. Include at least **5 comments**, especially around `goal_rate()` and the sorting logic.

**Bonus (optional):** Add the timing experiment from the "Something New" section and print how many times faster NumPy was, e.g. *"NumPy was 8.3x faster."*

> 💡 Steps 5–8 (normalization, boolean masking, argmax/argmin, argsort) are all real preprocessing and analysis techniques you'll use on actual datasets in Phase 2 — you're already doing ML groundwork.

---

## ✅ How to Submit

1. Save `grocery_bill.py`, `temp_converter.py`, `curve_applier.py`, `sales_stats.py`, `steps_log.txt`, and `fittrack_analytics.py` in a `Day5` folder.
2. Screenshot your terminal running `fittrack_analytics.py`, showing the full ranked report plus `goal_rate()` and most/least active day.
3. Add today's entry to your **single running Daily Task Submission Report**.
4. Submit via InnoTrack before 5c.

---

## 🔜 Next Up

**Day 6 — Pandas Basics.** You'll move from raw NumPy arrays to DataFrames — reading CSVs and cleaning real tabular data, the format almost every dataset comes in.
