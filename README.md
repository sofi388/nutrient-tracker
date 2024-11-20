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

1. **Create a Conda environment**:
    ```bash
    conda create --name nutrition_tracker python=3.9
    ```

2. **Activate the environment**:
    ```bash
    conda activate nutrition_tracker
    ```

3. **Install dependencies**:
    - From the project directory, install required packages listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

---

## Run the App

```
flask run
```