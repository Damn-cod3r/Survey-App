# Survey App (In Progress)

A Django-based web application to create, manage, and participate in surveys. The app allows users (e.g., HR professionals) to create surveys, assign them to employees, and track responses. Currently under development.

## Features (In Progress)

- **User Authentication**
  - Signup with email and password
  - Login using email and password
  - Logout functionality

- **Survey Creation**
  - Create new surveys with a name and description
  - Add multiple questions to surveys
  - Templates available (e.g., Employee Engagement Survey, Onboarding Survey)
  - Create surveys from scratch by adding custom questions

- **Question Management**
  - Add questions with multiple answer types: Dropdown, Checkboxes, Radio Buttons, NPS, and Open-ended questions
  - Manage answer options for each question

- **Employee Participation**
  - Employees can fill out surveys assigned to them by HR
  - Anonymous and non-anonymous survey options

- **Survey Management**
  - HR can view survey results and track employee participation
  - Assign surveys to different departments or employee categories

## Installation

### Prerequisites

- Python 3.8+
- Django 5.0.6
- SQLite (default database)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/survey_app.git
    cd survey_app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** (to access the Django admin):
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` in your browser.

## How It Works

1. **Signup**: HR professionals can sign up by providing an email and password.
2. **Login/Logout**: After signing up, users can log in and log out using their email.
3. **Create Survey**: HR can create surveys, either from scratch or by selecting a template.
4. **Add Questions**: Surveys can have multiple types of questions, including multiple-choice, dropdowns, and open-ended questions.
5. **Assign Surveys**: Surveys are assigned to employees based on departments or categories (HR, Engineering, Sales, etc.).
6. **Employee Participation**: Employees fill out surveys, either anonymously or with identifiable information.
7. **View Results**: HR can view results and track survey completion.

## Database Models

### Survey Model
- `name`: Name of the survey.
- `description`: Short description of the survey.

### Question Model
- `survey`: Foreign key to the `Survey` model (many questions belong to one survey).
- `question_text`: Text of the question.
- `options`: Comma-separated string of possible answer options.

### Survey Responses Model
- `survey`: Foreign key to the `Survey` model.
- `employee`: Foreign key to the employee who submitted the response.
- `question`: Foreign key to the `Question` model.
- `answer`: The answer submitted by the employee.

## URL Structure

- `/`: Home page
- `/signup/`: User registration page
- `/login/`: User login page
- `/signout/`: User logout page
- `/dashboard/`: User dashboard page (view surveys created by HR)
- `/survey_detail/<int:survey_id>/`: View and add questions to a specific survey

## Technologies Used

- **Django**: The backend framework for building the app.
- **SQLite**: The default database for development and testing.
- **HTML, CSS**: Basic frontend structure with Django templates.
- **Bootstrap**: For responsive design components (if applicable).

## Contributing

1. Fork this repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -am 'Add feature-name'`.
4. Push to your branch: `git push origin feature-name`.
5. Create a new Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- Django documentation for helping with the framework setup.
- [Bootstrap](https://getbootstrap.com/) for responsive design components.

---

Made with ❤️ by [Chidambaram AKA Damn-cod3r]().
