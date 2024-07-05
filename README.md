# hospital-app
Fullstack web app for a fictional hospital.

> ***The app targets python 3***
## Start here
To use the app, you would need django 5.0.3, pip and a postgreSQL database.

# Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/Lonercode/hospital-app.git
cd hospital-app
```
2. Create a Virtual Environment
```bash
pip install virtualenv
virtualenv env

# On Windows
env\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Set Up PostgreSQL Database
Find setup instructions: <a href = https://www.postgresql.org>www.postgresql.com</a>
Ensure PostgreSQL is installed and running on your local machine.
Create a new database and note down the credentials (database name, username, password).

5. Configure Django Settings
Rename .env.example to .env.
Edit .env file with your PostgreSQL database credentials:

NAME=your_database_name<br/>
USER=your_database_username<br/>
PASSWORD=your_database_password<br/>
HOST=localhost<br/>
PORT=5432

6. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
7. Create a Superuser 
```bash
python manage.py createsuperuser
```
You can then login to admin and add data to the following pages: pricing.html, blogPost.html and doctors.html.

8. Run the Development Server
```bash
python manage.py runserver
```

9. Access the Application
Open your web browser and go to http://localhost:8000/ (or another port if specified).