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


### On Aptible (CLI)

These instructions require the [Aptible CLI](https://www.aptible.com/docs/cli)
and assume you have already created an account.

1. Create a database: `aptible db:create --type postgresql teamspace`. Pay attention to the URL output at the end!
2. Create an app: `aptible apps:create teamspace`
3. Set the configuration for the app: `aptible config:set --app teamspace DATABASE_URL='URL_FROM_STEP_1' FORCE_SSL=1 SECRET_KEY='YOUR_SECRET_KEY'`
4. Deploy the app `aptible deploy --app teamspace --docker-image aptible/teamspace`
5. Add an endpoint: `aptible endpoints:https:create --default-domain --app teamspace cmd `
6. (Optional) Create a user: `aptible ssh --app teamspace python manage.py createsuperuser`
