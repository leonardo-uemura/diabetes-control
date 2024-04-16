# Gestational Diabetes Glycemia Monitoring System

This project is a web application designed to help monitor glycemia values for individuals diagnosed with gestational diabetes. The system allows users to insert and track their glycemia readings over time, providing valuable insights for managing gestational diabetes during pregnancy.

## Motivation

Gestational diabetes is a common condition that can develop during pregnancy, affecting the body's ability to regulate blood sugar levels. Monitoring glycemia levels regularly is crucial for managing gestational diabetes effectively. This project was developed to provide a convenient and user-friendly tool for individuals, like my wife, diagnosed with gestational diabetes to track their glycemia values and share them with healthcare professionals.

## Features

- **User Authentication**: Secure user authentication system to ensure only authorized users can access and manage their glycemia data.
- **Glycemia Data Entry**: Allows users to enter their glycemia readings along with additional details such as time of measurement, value, title, and description.
- **Glycemia Monitoring**: Provides a dashboard for users to view their glycemia history and trends over time through interactive charts and graphs.
- **Personalized Insights**: Offers personalized insights and recommendations based on glycemia readings to support diabetes management during pregnancy.
- **User-Friendly Interface**: Designed with a clean and intuitive interface for easy navigation and data entry, especially during pregnancy.

## Technologies Used

- **Django**: Backend framework for building the web application and managing data models.
- **Django REST Framework**: Facilitates the creation of RESTful APIs for handling data interactions.
- **React.js (or other frontend framework)**: Frontend library for building the user interface and interactive components.
- **Chart.js (or similar)**: JavaScript library for visualizing glycemia data with interactive charts and graphs.
- **SQLite (or PostgreSQL)**: Database system for storing user data securely.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/gestational-diabetes-monitoring.git
   cd gestational-diabetes-monitoring
   ```

2. **Install Dependencies**:

   ```bash
    # Assuming you have Python and pip installed
    pip install -r requirements.txt
    # Install frontend dependencies (if applicable)
    # npm install or yarn install
   ```

3. **Database Setup**:

   ```bash
    python manage.py migrate
   ```

4. **Run the Development Server**:

   ```bash
    python manage.py runserver
    # Frontend development server (if applicable)
    # npm start or yarn start
   ```

5. **Access the Aplication**:

   Open your web browser and navigate to http://localhost:8000 to access the application locally.

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or find any issues, please open an issue or submit a pull request. Let's work together to improve this project for individuals managing gestational diabetes.

## License

This project is licensed under the MIT License.
