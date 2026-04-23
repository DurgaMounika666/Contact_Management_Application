📇 Contact Management Application

A simple Contact Management Web Application built using Python (Flask), PostgreSQL, and Bootstrap that allows users to perform CRUD operations with proper validation.

🚀 Features

✅ Create new contacts

✅ View all contacts

✅ Update existing contacts

✅ Delete contacts

✅ Email validation

✅ Phone number validation (10 digits only)

✅ Prevent duplicate email entries

✅ Responsive UI using Bootstrap

✅ Persistent storage using PostgreSQL


🛠️ Tech Stack

Backend: Python (Flask)

Frontend: HTML, CSS, Bootstrap

Database: PostgreSQL

ORM: SQLAlchemy


📂 Project Structure

Contact-Management/

    │── app.py

    │── templates/
    
    │   ├── index.html
    
    │   ├── display.html
    
    │── static/ (optional)
    
    │── README.md


⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/contact-management.git

cd contact-management


2️⃣ Install Dependencies

pip install flask flask_sqlalchemy psycopg2


3️⃣ Setup PostgreSQL Database

Open PostgreSQL and run:

CREATE DATABASE contact_db;


4️⃣ Configure Database

Update your database URI in app.py:

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/contact_db'


5️⃣ Run the Application

python app.py


Open in browser:

http://127.0.0.1:5000/


📖 Usage
  
  ➕ Add a contact using the form
  
  📋 View all contacts on display page
  
  ✏️ Edit contact using Edit button
  
  ❌ Delete contact using Delete button


🔐 Validations Implemented

  ✔️ Email format validation using Regex

  ✔️ Phone number must contain exactly 10 digits

  ✔️ Duplicate email prevention


💡 Challenges Faced
  
  Implementing form validation (email & phone number)
  
  Handling modal-based updates
  
  Preventing duplicate entries in database

  Integrating Flask with PostgreSQL using SQLAlchemy


🔮 Future Enhancements

  🔍 Search contacts
  
  📄 Pagination

  🔐 User authentication
  
  📱 Mobile-friendly UI improvements
