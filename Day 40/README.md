# Days 36–40 — Code Bundle

Runnable Flask + MySQL code for each day, matching `Day36_40_Backend_Guide.md`.

```bash
pip install -r requirements.txt
```

| Folder | What's inside | Run |
|---|---|---|
| `Day36/` | Full CRUD API (`items` table) | `mysql < schema.sql` then `python app.py` |
| `Day37/` | User registration + password hashing | `mysql < schema.sql` then `python app.py` |
| `Day38/` | Full login/logout/session flow | reuses Day37's `users` table, then `python app.py` |
| `Day39/` | Skeleton for YOUR individual project | edit `db.py`, `schema.sql`, `routes_plan.md`, then build in `app.py` |
| `Day40/` | Submission checklist + README template | no code — final QA before pushing to GitHub |

Each `app.py` is self-contained and builds directly on the previous day. Update the MySQL password in every `db.py` before running.
