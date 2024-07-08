# Comprehensive Django Project Management System

A feature-rich, modular project management system built with Django, designed to help organizations efficiently manage projects, tasks, resources, and personnel. This system provides a user-friendly interface for project planning, tracking, and resource allocation, with powerful visualization tools like Gantt charts for project timelines.

## Features

- User authentication and authorization with role-based access control
- Project and task management with status tracking, start and end dates, and completion percentage
- Resource management for materials, equipment, and human resources
- Resource allocation with conflict detection
- Project timeline visualization using Gantt charts
- Reporting and analytics for project progress and resource utilization
- Responsive design using Bootstrap for mobile-friendly user interface
- RESTful API for integration with other systems and potential mobile app development
- Document management with file uploads and version control
- Comments and discussion functionality for communication within the system
- Notification system with email and in-app notifications
- Search functionality across projects, tasks, and resources
- Customizable user preferences and dashboard layout
- Audit logging for user actions and system events
- Internationalization and localization support
- Comprehensive testing, documentation, and security measures

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Klodi1379/project_managements.git
   ```

2. Change into the project directory:
   ```
   cd project_managements/ProjectManagement
   ```

3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up the database:
   ```
   python manage.py migrate
   ```

6. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application through your web browser at `http://localhost:8000`.

## Usage

1. Log in using the superuser account or create new user accounts.
2. Create projects, tasks, and manage resources through the user interface.
3. Use the Gantt chart view for project timeline visualization.
4. Generate reports and analyze project progress and resource utilization.

## Contributing

We welcome contributions to improve and expand the functionality of this project management system. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request detailing your changes.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact
