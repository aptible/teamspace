# T E A M S P A C E

Teamspace is a social media clone, meant for demonstrating
security vulnerabilities in Django.

## Documented Vulnerabilities

* SQL Injection, fixed in https://github.com/aptible/teamspace/pull/1
* HTML Sanitization, fixed in https://github.com/aptible/teamspace/pull/2
* Overly permissive `ALLOWED_HOSTS` and an open redirect on login, fixed in https://github.com/aptible/teamspace/pull/3
* Static, public `SECRET_KEY`, fixed in https://github.com/aptible/teamspace/pull/4

## Environment Variables

| Variable                          | Required? | Default Value      |
|-----------------------------------|-----------|--------------------|
| `DATABASE_URL`                    | True      |                    | 
| `DEFAULT_FROM_EMAIL`              | False     | `test@example.com` | 
| `EVIL` (include evil login pages) | False     | False              |
| `POSTMARK_API_KEY`                | False     |                    |
| `SECRET_KEY`                      | True      |                    | 
| `TEST_MODE` (for postmarker)      | False     | False              |

## How to run

### Locally

These instructions require [Docker Compose](https://docs.docker.com/compose/).

1. Build the Docker Image: `docker compose build`
2. Run migrations: `docker compose run teamspace python manage.py migrate`
3. Run the server: `docker compose up`
4. (Optional) Create a user: `docker compose run teamspace python manage.py createsuperuser`
