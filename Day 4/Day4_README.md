# Day 4 — Data Structures (Self-Study)

**Phase 01 · Full Stack AI Developer Program · Innolift Ventures**
**Status:** No live class today (Crescent college holiday). Self-paced — work through it today, submit before Day 6.
**Today's build:** **GradeVault** — a brand-new student score manager, all your own build.

---

## Recap: Where You Left Off

| Day | What you learned | What you built |
|---|---|---|
| **Day 1** | Variables, data types, f-strings | Profile Card |
| **Day 2** | if/elif/else, while & for loops, break/continue | ATM Simulator |
| **Day 3** | Functions, scope, modules, file I/O | CampusLib |

Today adds **data structures** — the shape that holds all the data your Day 1–3 programs have been working with. And today's project is a fresh one: **GradeVault**, a student score manager you build from scratch using everything so far.

---

## 1. Lists — an ordered, editable collection

**Definition:** A list stores multiple values in one variable, in order, and you can change it after creating it.

**Syntax:**
```python
my_list = [item1, item2, item3]
```

**Example:**
```python
subjects = ["Python", "Data Structures", "Web Dev"]

print(subjects[0])          # Python (indexing starts at 0)
subjects.append("NumPy")    # add to the end
subjects.remove("Web Dev")  # remove a specific item
print(len(subjects))        # 3
```

---

## 2. Tuples — an ordered, locked collection

**Definition:** Like a list, but **cannot be changed** after creation. Use it for values that should never accidentally get edited.

**Syntax:**
```python
my_tuple = (item1, item2, item3)
```

**Example:**
```python
PASS_CUTOFFS = (35, 50, 75)   # (fail_below, pass_at, distinction_at)
print(PASS_CUTOFFS[1])         # 50
# PASS_CUTOFFS[1] = 60         # ❌ would crash — tuples are locked
```

---

## 3. Dictionaries — labeled data (key → value)

**Definition:** Stores data as **key-value pairs**, accessed by name instead of position. This is exactly the shape a student record, a database row, or an API response takes.

**Syntax:**
```python
my_dict = {"key1": value1, "key2": value2}
```

**Example:**
```python
student = {
    "name": "Afsin Noor",
    "subject": "Python",
    "score": 82
}

print(student["name"])       # Afsin Noor
student["score"] = 85        # update a value
student["status"] = "Distinction"  # add a new key
```

> 💡 A **list of dictionaries** — `[{"name": "...", "score": ...}, {...}, {...}]` — is exactly how you should store a whole class of students. That's the core of today's GradeVault build.

---

## 4. Sets — a collection with no duplicates

**Definition:** Stores values like a list, but automatically removes duplicates and doesn't keep order. Perfect for "give me only the unique values."

**Syntax:**
```python
my_set = {item1, item2, item3}
```

**Example:**
```python
subjects_taught = {"Python", "Data Structures", "Python"}
print(subjects_taught)          # {'Python', 'Data Structures'} -> duplicate auto-removed
print(len(subjects_taught))     # 2 -> unique subject count
```

---

## 🌟 Something New: List Comprehensions

Not strictly required today, but it's one of the most "Pythonic" tricks you'll see, and you'll spot this pattern constantly in real ML/data code later in the program.

**The old way:**
```python
top_scorers = []
for s in students:
    if s["score"] >= 75:
        top_scorers.append(s["name"])
```

**The comprehension way (1 line):**
```python
top_scorers = [s["name"] for s in students if s["score"] >= 75]
```

Read it as: *"give me `s["name"]`, for every `s` in `students`, if the score qualifies."*

---

## 📝 Your Tasks for Today

Work through these **in order**. Tasks 1–4 are small, real-world-useful tools — each one is a genuinely usable mini-tool, not just a syntax drill. Task 5 is today's main mini project — budget the most time for it.

### Task 1 — To-Do List Manager (List)
**Real-world use:** every task app you've ever used is built on this exact pattern.
Create `todo_manager.py`. Build a list of tasks (strings). Write `add_task(task)` to append a new task, and `complete_task(task)` to remove it from the list. Write `pending_count()` that returns how many tasks remain. Print the full pending list, numbered, using a loop.

### Task 2 — App Config Lock (Tuple)
**Real-world use:** every real app has fixed settings that must never change while it's running.
Create `app_config.py`. Store `APP_CONFIG = ("v1.0.3", "en", 30)` — a tuple of `(version, language, session_timeout_minutes)`. Print each value with a clear label using f-strings. Add a comment showing what line would crash the program if someone tried to edit `APP_CONFIG`.

### Task 3 — Digital Business Card (Dictionary)
**Real-world use:** a genuinely reusable tool for your own LinkedIn/resume details.
Create `business_card.py`. Build one dictionary with your `name`, `role`, `email`, `phone`, and `linkedin`. Print a neatly formatted card using f-strings. Update `role` to something new, then reprint the card to confirm the change.

### Task 4 — Duplicate Email Cleaner (Set)
**Real-world use:** cleaning a messy event signup list or mailing list — a real data-cleaning task.
Create `email_cleaner.py`. Build a list of at least 8 email addresses with 2–3 intentional duplicates. Convert it to a set, then print the unique count and how many duplicates were removed (`len(original_list) - len(unique_set)`).

### Task 5 — Main Mini Project: GradeVault

Build a brand-new project — `grade_vault.py` plus `grade_utils.py` — a full student score manager. This is the big one: it pulls together **everything from Days 1–4**, and it should take real effort.

Your GradeVault must:

1. **(Day 4)** Store at least **5 students across at least 2 subjects** as a **list of dictionaries** — each with `name`, `subject`, `score`, and `status`.
2. **(Day 4)** Store fixed pass cutoffs as a **tuple**: `PASS_CUTOFFS = (35, 50, 75)` (fail below 35, pass at 50, distinction at 75), imported from `grade_utils.py`.
3. **(Day 4)** Add `unique_subjects()` that returns a **set** of every subject in the class.
4. **(Day 3)** Write `add_student(name, subject, score)` as a function that appends a new student dict and logs a line to `grades_log.txt` using `with open(...) as f`.
5. **(Day 2)** Inside `add_student()`, use `if/elif/else` against `PASS_CUTOFFS` to set each student's `status`.
6. **(Day 2)** Write `list_students()` that loops over the class and prints each student with their status.
7. **(New)** Write `class_average(subject)` that loops the class, filters to one subject, and returns the average score for just that subject.
8. **(New)** Write `top_scorer()` that loops the class and returns the full record of whoever has the highest score.
9. **(New)** Write `search_student(name)` that returns a student's full record, or `"Not found"` if no match exists.
10. **(Day 1)** All output is printed with f-strings.
11. Add at least **5 comments** explaining the logic, especially in `class_average()` and `top_scorer()`.

**Bonus (optional):** Add `top_scorers()` — every `"Distinction"` student's name, written as a **list comprehension**.

---

## ✅ How to Submit

1. Save `todo_manager.py`, `app_config.py`, `business_card.py`, `email_cleaner.py`, `grade_vault.py`, and `grade_utils.py` in a `Day4` folder.
2. Screenshot your terminal running `list_students()` (showing each student's status), plus `class_average()`, `top_scorer()`, and `search_student()`.
3. Add today's entry to your **single running Daily Task Submission Report**.
4. Submit via InnoTrack whenever you're back online — no rush since it's a holiday, just make sure it's in before Day 6.

---

## 🔜 Next Up

**Day 5 — NumPy Basics.** You'll turn GradeVault's score log into real numbers — GradeVault Analytics.
