# Day 40 — Submission Checklist

Go through every box before you submit.

- [ ] Every route from your Day 39 plan is implemented and working
- [ ] Every endpoint tested in Postman — screenshot each request + response
- [ ] Passwords (if your project has auth) are hashed, never plaintext
- [ ] Database actually persists data — restart the server and confirm data is still there
- [ ] `.gitignore` excludes secrets (DB passwords, `venv/`, `__pycache__/`)
- [ ] Code pushed to GitHub with a clear `README.md` explaining how to run it
- [ ] Commit history shows real incremental progress, not one giant commit
- [ ] `requirements.txt` included (`pip freeze > requirements.txt`)

## Suggested `.gitignore`
```
venv/
__pycache__/
*.pyc
.env
```

## Suggested README.md for your project repo
```markdown
# [Your Project Name]

## What it does
[1-2 sentence description]

## Tech stack
Flask, MySQL, [your ML library]

## Setup
1. pip install -r requirements.txt
2. Create the database using schema.sql
3. python app.py

## API Endpoints
| Method | Route | Description |
|---|---|---|
| ... | ... | ... |
```
