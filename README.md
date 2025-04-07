# Software Developer Salary Prediction

A Streamlit-based web application that predicts software developer salaries based on various factors and provides interactive data exploration capabilities.

## Description

This project is a comprehensive salary prediction and analysis tool specifically designed for software developers. It leverages machine learning techniques to provide accurate salary estimates based on key factors such as geographical location, educational background, and professional experience. The application is built with a dual-purpose interface:

1. **Prediction Module**: Users can input their specific details (country, education level, and years of experience) to receive an estimated salary prediction. The prediction is accompanied by an interactive visualization that helps users understand how their salary compares to industry standards.

2. **Exploration Module**: This section provides detailed insights into the software development industry through interactive visualizations. Users can explore:
   - Salary distributions across different countries
   - The relationship between experience and compensation
   - The impact of education level on earning potential
   - Industry trends and patterns

The application uses real-world data from the Stack Overflow Developer Survey, ensuring that predictions and insights are based on current industry standards. The interface is designed to be intuitive and user-friendly, making it accessible to both technical and non-technical users.

## Features

- Salary Prediction: Predict software developer salaries based on:
  - Country
  - Education Level
  - Years of Experience
- Data Exploration: Interactive visualizations including:
  - Country-wise distribution of developers
  - Experience vs Salary analysis
  - Education level impact on salary
- Interactive UI: User-friendly interface with:
  - Dropdown selections
  - Sliders for experience
  - Real-time predictions
  - Animated visualizations

## Technologies Used

- Python
- Streamlit (Web Framework)
- Scikit-learn (Machine Learning)
- Plotly (Interactive Visualizations)
- Pandas (Data Processing)
- NumPy (Numerical Computing)

## Installation

1. Clone the repository:
git clone [your-repository-url]
cd [repository-name]

2. Install the required packages:
pip install -r requirements.txt

## How to Run

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Step-by-Step Guide

1. Set up the Environment
   - Create a virtual environment: python -m venv venv
   - Activate the virtual environment:
     - Windows: venv\Scripts\activate
     - macOS/Linux: source venv/bin/activate

2. Install Dependencies
   pip install -r requirements.txt

3. Prepare the Data
   - Ensure you have the survey_result.csv file in your project directory
   - Make sure the saved_steps.pkl file is present (this contains the trained model), you can get it by running the Salary_Prediction.ipynb file.

4. Run the Application
   streamlit run app.py

5. Access the Application
   - Open your web browser
   - Navigate to http://localhost:8501
   - The application should now be running and accessible

### Troubleshooting

If you encounter any issues:

1. Missing Dependencies
   pip install streamlit pandas numpy scikit-learn plotly

2. File Not Found Errors
   - Ensure survey_result.csv and saved_steps.pkl are in the correct directory
   - Check file permissions

3. Port Already in Use
   - If port 8501 is already in use, Streamlit will automatically try the next available port
   - You can specify a different port using: streamlit run app.py --server.port 8502

### Development Mode

For development purposes, you can run the application with hot-reloading enabled:
streamlit run app.py --server.runOnSave true

## Usage

1. Run the Streamlit app:
streamlit run app.py

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Use the sidebar to switch between:
   - Predict: Get salary predictions based on your inputs
   - Explore: View interactive visualizations of the salary data

## Data Source

The application uses data from the Stack Overflow Developer Survey, processed and cleaned for accurate predictions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Your chosen license]

## Contact

[Your contact information]
