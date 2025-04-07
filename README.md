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

- **Salary Prediction**: Predict software developer salaries based on:
  - Country
  - Education Level
  - Years of Experience
- **Data Exploration**: Interactive visualizations including:
  - Country-wise distribution of developers
  - Experience vs Salary analysis
  - Education level impact on salary
- **Interactive UI**: User-friendly interface with:
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
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Use the sidebar to switch between:
   - **Predict**: Get salary predictions based on your inputs
   - **Explore**: View interactive visualizations of the salary data

## Data Source

The application uses data from the Stack Overflow Developer Survey, processed and cleaned for accurate predictions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Your chosen license]

## Contact

[Your contact information]