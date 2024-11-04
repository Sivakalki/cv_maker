# CV Maker 📄

**CV Maker** is a web-based application built using **Django** and **HTML templates**. The purpose of this project is to create professional resumes effortlessly through an interactive form. Once the form is submitted, the resume will animate into view, sliding from top to bottom, creating a smooth user experience.

---

## 🌟 Features

- Dynamic form for inputting resume details.
- Interactive animations displaying the resume from top to bottom after submission.
- Clean and minimalistic design.

---

## 🛠️ Technologies Used

- **Django**: Backend framework
- **HTML**: Frontend templates
- **CSS**: Styling and animations
- **JavaScript**: For smooth animations and form handling.

---

## 🎬 How to Launch the Application

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

3. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database**:
   - Apply migrations to set up the database:
     ```bash
     python manage.py migrate
     ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Open your web browser and go to `http://127.0.0.1:8000` to view the CV Maker application.

---

## ✨ Additional Features to Explore

- **Preview Mode**: Review your resume before saving or downloading to ensure everything looks perfect.
- **Export to PDF**: Generate a PDF version of your resume to download and share with potential employers.
- **Responsive Design**: Optimized for viewing on both desktop and mobile devices.
- **Customizable Templates**: Choose from a variety of clean and professional templates to suit your style.

---

## 📂 Project Structure

- `templates/` - Contains HTML templates for rendering the resume form and display.
- `static/` - Stores CSS, JavaScript, and image files for styling and interactivity.
- `views.py` - Contains the logic for handling form data and displaying the resume.
- `models.py` - Defines any database models used in the application.

---
