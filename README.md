# Astronomy Data Explorer

This is a backend project I'm building to practice Python, Flask, MySQL, and REST APIs to strenght my backend development. It fetches NASA's Astronomy Picture of the Day (APOD) and stores it in a database. I'll add a simple frontend later to search and view the data.

## What is APOD?

APOD stands for **Astronomy Picture of the Day**. It's a service run by NASA that publishes a new astronomy-related image or video every day, along with a short explanation written by an astronomer. The API lets developers fetch that daily content. I'm using it because it's free, reliable, and gives me real data to work with.

## What I'm building

A small web app that:
- Fetches APOD data from NASA's API
- Stores it in a MySQL database
- Lets you search entries by keyword
- Lets you mark entries as favorites
- Exposes a simple REST API
- Has a basic frontend to display the results

## Tech stack

- Python 3
- Flask ( is kind of like a small/micro frameowrk which deals with routing/urls/requets dare i say it's kind of similar to express.js"
- MySQL (using XAMPP)
- mysql-connector-python
- HTML, CSS, Bootstrap, JavaScript (i have not done any frontend work but when i do will be using this languages)
- Git and GitHub

## What I've done so far

- Created the GitHub repo
- Set up my Python environment
- Signed up for a NASA API key
- Written a script that fetches today's APOD and prints the title
- Started planning the database structure

## What I'm planning to do next

- Set up the MySQL database and tables
- Store multiple APOD entries
- Add search and favorites features
- Build API endpoints with Flask
- Create a simple frontend page
- Write clear documentation and add comments

## How to run it (once it's ready)

I'll update this section when the app is working. For now, here's roughly how it will work:

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set up MySQL database using `database/schema.sql`
4. Add your NASA API key to a `.env` file
5. Run `python app.py`
6. Open `http://localhost:5000`

## Database schema (planned)

** the apod table **
- id (INT, PK)
- date (DATE)
- title (VARCHAR)
- explanation (TEXT)
- url (VARCHAR)
- media_type (VARCHAR)

** the favorites table **
- id (INT, PK)
- apod_id (INT, FK)
- created_at (TIMESTAMP)

## API endpoints (planned)

- `GET /fetch` – fetch today's APOD and store it
- `GET /apod` – list all entries
- `GET /apod/<date>` – get entry by date
- `GET /search?q=keyword` – search title and explanation
- `GET /favorites` – list favorites
- `POST /favorites/<date>` – add favorite
- `DELETE /favorites/<date>` – remove favorite

Thanks for checking out my project.
