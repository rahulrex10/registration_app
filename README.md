# registration_app
 INI8 LABS PVT LTD      Backend Task:   SOFTWARE DEVELOPER INTERN ASSESSMEN
Registration App
This project demonstrates a basic Flask-based backend with a MySQL database to handle user registrations, and a frontend to interact with the API. Follow the steps below to run the project locally.

Backend (Flask + MySQL)
Prerequisites:
Python (version 3.x)
MySQL installed and running on your machine
Pip installed for managing Python packages
Setup Instructions:
Clone the repository:

bash
Copy code
git clone https://github.com/your-repository-link.git
cd registration_app/backend
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv
Activate the virtual environment:

On Windows:
 
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install the required dependencies:

 
pip install -r requirements.txt
Configure MySQL:

Ensure MySQL is installed and running.

Open your MySQL terminal and log in with your credentials:

bash
Copy code
mysql -u root -p
Create the database and table:

sql
 
CREATE DATABASE testdb;
USE testdb;

CREATE TABLE Registration (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    dob DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Update MySQL configuration in app.py:

In backend/app.py, modify the database credentials to match your MySQL setup:

python
 
app.config['MYSQL_HOST'] = 'http://localhost:3000'
app.config['MYSQL_USER'] = 'rahul'          # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'yourpassword'  # Your MySQL password
app.config['MYSQL_DB'] = 'testdb'          # Database name
Run the Flask backend server:

 
python app.py
The Flask app will now be running at http://127.0.0.1:5000.

API Endpoints:
Create a registration (POST): http://127.0.0.1:5000/register
Get all registrations (GET): http://127.0.0.1:5000/registrations
Get a registration by ID (GET): http://127.0.0.1:5000/registration/<id>
Update a registration by ID (PUT): http://127.0.0.1:5000/registration/<id>
Delete a registration by ID (DELETE): http://127.0.0.1:5000/registration/<id>
Frontend
Prerequisites:
Node.js (version 12 or higher)
npm (Node package manager)
Setup Instructions:
Navigate to the frontend directory:

 
 
cd ../frontend
Install the required packages:
 
npm install
Run the frontend development server:

bash
Copy code
npm start
The frontend will be running at http://localhost:3000.

Testing the Frontend:
The frontend should now be able to interact with the backend API.
Use the registration form in the frontend to create new users, which will be stored in the MySQL database via the Flask backend.
Common Errors and Troubleshooting:
Database connection issues: Ensure MySQL is running and your credentials in app.py are correct.
Port conflicts: If 5000 or 3000 are already in use, modify the port number in the Flask or React configuration files.
Additional Notes:
For production deployment, use a production WSGI server (like Gunicorn or uWSGI) for Flask and a reverse proxy like Nginx or Apache.

The frontend can be built for production using:

 
npm run build
This will create an optimized production build in the build/ folder, ready to be deployed