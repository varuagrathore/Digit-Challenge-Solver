# 🧮 Digit Challenge Solver

This Python script helps you solve any equation like those you might get in P and G online assessments.

![image](https://github.com/user-attachments/assets/7dff9a7e-a75d-4587-a045-210c5640278b)

Welcome to the Digit Challenge Solver! This web-based application, built with Flask, allows users to input equations with missing digits represented by underscores (_). The solver then replaces the underscores with the appropriate digits to make the equation valid.

## 📜 Overview

The Digit Challenge Solver is a fun and educational tool designed to help users solve equations with missing digits. It's perfect for anyone interested in math challenges, from students to professionals.

## 🛠️ Prerequisites

Before you get started, make sure you have the following installed on your machine:

- **Python 3.x**: 🐍 Ensure you have Python 3 installed. [Download Python](https://www.python.org/downloads/)
- **pip**: 📦 Python package installer, typically included with Python 3 installations.
- **Git**: 🗂️ Version control system to manage code and deploy to Heroku. [Install Git](https://git-scm.com/)
- **Heroku CLI**: ☁️ Command line interface for managing Heroku apps. [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

## 🚀 Getting Started

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/digit-challenge-solver.git
   cd digit-challenge-solver
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   flask run
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## 🌐 Deploying to Heroku

To deploy the application to Heroku, follow these steps:

1. **Log in to Heroku**:
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**:
   ```bash
   heroku create
   ```

3. **Deploy the code**:
   ```bash
   git push heroku main
   ```

4. **Open the app in your browser**:
   ```bash
   heroku open
   ```

## 📚 How to Use

1. **Input an equation**: Enter an equation with missing digits represented by underscores (_).
2. **Solve**: Click the "Solve" button to find the appropriate digits that make the equation valid.
3. **View Results**: The application will display the solved equation with the missing digits filled in.

## 🗣️ Feedback

If you have any feedback or suggestions, feel free to open an issue or reach out to me directly at [quote1503@gmail.com](mailto:quote1503@gmail.com).

---

Enjoy solving digit challenges! Happy coding! 💻✨

---

This README file is designed to be both informative and engaging, making it easy for users to set up and use your Digit Challenge Solver project.
