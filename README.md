# Nutrient Tracker App

**Note**: This project is currently under development. Some features may be incomplete or subject to change.

---

The Nutrient Tracker App helps users track their food intake and calculate nutrient consumption. The app has two primary modes:
1. **General intake tracking** – Users can log their daily meals and monitor the intake of calories, proteins, fats, and carbohydrates, helping them maintain a balanced diet.
2. **Ferrum intake tracking** – Specifically designed for individuals with low hemoglobin levels, this mode focuses on tracking iron-rich foods and providing tailored recommendations to support users with anemia or other iron deficiency-related conditions.

By using this app, users can monitor their nutritional intake, track progress, and receive food recommendations based on their specific health needs.

---

## Installation

To set up the project locally, follow these steps:

1. **Build the Docker image**:
    ```bash
    docker build -t nutrient-tracker .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 5000:5000 nutrient-tracker
    ```

3. **Access the application**:
    Open a web browser and go to `http://localhost:5000`.

---