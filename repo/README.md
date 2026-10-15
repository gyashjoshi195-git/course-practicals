# Diploma Sem 5 - Practicals

Shri Labhubhai Trivedi Institute of Engineering & Technology, Rajkot - Diploma CSE (GTU), Academic Year 2026-27

| Folder | Subject |
|---|---|
| `WDP/` | DI05000091 - Web Development using Python |
| `DAA/` | DI05031011 - Design and Analysis of Algorithm |

## WDP - Web Development using Python
Install: `pip install flask django djangorestframework gunicorn`

| # | Practical | Path | Run |
|---|---|---|---|
| 1 | OOP: classes, objects, attributes, methods | `p01_oop_basics.py` | `python p01_oop_basics.py` |
| 2 | Inheritance, polymorphism, abstract classes | `p02_oop_advanced.py` | `python p02_oop_advanced.py` |
| 3 | SQLite connectivity + basic SQL | `p03_sqlite_basics.py` | `python p03_sqlite_basics.py` |
| 4 | SQLite CRUD, parameterized queries | `p04_sqlite_crud.py` | `python p04_sqlite_crud.py` |
| 5 | Flask Hello World + project structure | `p05_flask_hello/` | `python app.py` |
| 6 | Flask forms GET/POST + Bootstrap | `p06_flask_forms/` | `python app.py` |
| 7 | Flask CRUD with SQLite | `p07_flask_crud/` | `python app.py` |
| 8 | Flask login system with sessions | `p08_flask_login/` | `python app.py` |
| 9 | Django install + Hello World | `p09_django_hello/` | `python manage.py runserver` |
| 10 | Django models + database | `p10_to_p14_django_project/` | `python manage.py makemigrations && python manage.py migrate` |
| 11 | Django admin panel | same project | `python manage.py createsuperuser` -> `/admin/` |
| 12 | Django auth with CSRF | same project | `/accounts/login/`, `/accounts/signup/` |
| 13 | Django CRUD with ModelForms | same project | `/` (login required) |
| 14 | REST API with DRF | same project | `/api/students/` |
| 15 | Deployment (Flask/Django) | `p15_deployment/` | see `DEPLOYMENT.md` |

For Flask apps: `cd` into the folder, run `python app.py`, open http://127.0.0.1:5000.
For Django: `cd` into the folder, run `python manage.py runserver`, open http://127.0.0.1:8000.

## DAA - Design and Analysis of Algorithm
Run any file with `python <file>.py`.

| Q | Topic | File |
|---|---|---|
| 1 | Bubble sort + time complexity | `q1_bubble_sort.py` |
| 2 | Merge sort (divide and conquer) | `q2_merge_sort.py` |
| 3 | Binomial coefficient (DP) | `q3_binomial_coefficient.py` |
| 4 | Coin change (DP) | `q4_coin_change.py` |
| 5 | LCS (DP) | `q5_lcs.py` |
| 6 | Fractional knapsack (greedy) | `q6_knapsack_greedy.py` |
| 7 | MST - Kruskal and Prim | `q7_minimum_spanning_tree.py` |
| 8 | BFS and DFS | `q8_bfs_dfs.py` |
