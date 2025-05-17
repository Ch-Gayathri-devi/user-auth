🏥 Django Multi-User Authentication System (Banao Task 1)

A Django-based web application that allows different types of users — Patients and Doctors — to sign up, log in, and get redirected to their respective dashboards. This was built as part of ATG Banao Task 1.
 📌 Features

- 👥 Two user roles:
  - Patient
  - Doctor
- ✅ Signup with:
  - Full Name
  - Profile Picture
  - Username
  - Email
  - Password & Confirm Password
  - Address (Line 1, City, State, Pincode)
- 🔐 Login with username and password
- 🔁 Redirect to separate dashboards after login
- 🧠 Password confirmation check
- 🖼️ Profile picture upload
- 📄 Dashboards display user's signup info

🛠️ Tech Stack

- Backend: Python, Django
- Frontend: HTML, CSS, Django Templates
- Database: SQLite (default with Django)

▶️ How to Run the Project

1. Clone the repository
   ```bash
   git clone https://github.com/Ch-Gayathri-devi/user-auth.git
   cd user-auth
2. Create and activate virtual environment (optional but recommended)
   python -m venv venv
venv\Scripts\activate  # On Windows
3. Install Django
   pip install django
4. Apply migrations
  python manage.py makemigrations
  python manage.py migrate
5. Run the server
   python manage.py runserver
6. Open your browser and go to http://localhost:8000/

