# ETL Insurance Project

## Overview
This project demonstrates a complete ETL (Extract, Transform, Load) process using a dataset of insurance records. The project includes the creation of a SQL database, data extraction and transformation using Python, and visualization through a Streamlit dashboard.

## Table of Contents
- Overview
- Project Structure
- Technologies Used
- Setup Instructions
- ETL Process
- Data Analysis
- Dashboard
- Contributing
- License

## Project Structure


ETL-Insurance-Project/ │ ├── data/ │ ├── insurance.csv │ ├── scripts/ │ ├── etl.py │ ├── dashboard.py │ ├── style.css ├── config.toml ├── README.md ├── requirements.txt └── .gitignore


## Technologies Used
- **SQL Server**: For database management.
- **Python**: For data extraction, transformation, and loading.
- **Pandas**: For data manipulation.
- **SQLAlchemy**: For database connection.
- **Streamlit**: For creating interactive dashboards.
- **OpenAI**: For implementing the chat feature.
- **Visual Studio Code**: As the code editor.

## Setup Instructions

### Prerequisites
- SQL Server and SQL Server Management Studio (SSMS)
- Python 3.x
- Visual Studio Code

### Step-by-Step Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mendesalex89/ETL_project
   cd ETL_project

Data Analysis
Key Questions Addressed
What factors most influence the cost of health insurance?
Analysis of the impact of age, BMI, number of children, smoking, and region on the cost.
Is there transparency between smoking and insurance costs?
Compare the average cost between smokers and non-smokers.
How does the cost of insurance vary by region?
Analyze the distribution of costs in different regions.
What is the distribution of BMI between different age groups and how does this impact costs?
Check how obesity (high BMI) at different ages influences the cost of insurance.
What is the typical profile of those expected to have higher insurance costs?
Identify common characteristics in beneficiaries who pay more for insurance.
Interactive Chat Feature
The dashboard now includes an interactive chat feature powered by OpenAI that allows users to ask questions about the dataset and receive real-time responses. This feature enhances user engagement and provides instant insights into the data.