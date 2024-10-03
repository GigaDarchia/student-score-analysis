# Student Score Analyzer

This Python project analyzes student scores across various subjects and semesters. It provides functionality to clean the data, identify failed students, calculate average scores, find the top-performing students, and visualize the results.

## Features

- **Clean DataFrame**: Removes rows with all NaN values in the specified subjects and converts subject scores to numeric values.
- **Identify Failed Students**: Returns a DataFrame of students who failed at least one subject.
- **Calculate Average Score by Semester**: Computes the average score by semester for all subjects.
- **Find Best Student**: Identifies the student(s) with the highest average score.
- **Find Hardest Subject**: Determines the subject with the lowest average score.
- **Generate Excel File**: Creates an Excel file containing the average score by semester.
- **Visualize Average Score by Subject**: Generates a bar chart for the average score per subject across all semesters.
- **Visualize Overall Average Score by Semester**: Creates a line graph for the overall average score by semester.

## Requirements

- Python 3
- pandas
- matplotlib

You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the repository**

   ```bash
   git clone https://github.com/GigaDarchia/student-score-analysis.git
   cd student-score-analysis
   ```

2. **Run the script**

   Make sure you have a CSV file named `student_scores_random_names.csv` with the appropriate data structure.

   ```bash
   python main.py
   ```

## Code Structure

The `StudentScoreAnalyzer` class contains all the methods required for data analysis and visualization. Here is a brief overview of its methods:

- `__init__(self, file_path, subjects)`: Initialize with the file path and subjects list.
- `clean_dataframe(self)`: Clean the DataFrame by dropping rows with all NaN subjects and converting subjects to numeric.
- `failed_students(self)`: Return a DataFrame of students who failed at least one subject.
- `average_score_by_semester(self)`: Calculate and return the average score by semester for all subjects.
- `find_best_student(self)`: Find and return the student(s) with the highest average score.
- `find_hardest_subject(self)`: Find and return the subject with the lowest average score.
- `generate_new_excel_file(self)`: Generate an Excel file containing the average score by semester.
- `visualize_average_score_by_subject(self)`: Visualize the average score per subject across all semesters using a bar chart.
- `visualize_overall_average_score_by_semester(self)`: Visualize the overall average score by semester using a line graph.
- `display_results(self)`: Display the various results including failed students, average scores, best students, and hardest subject.

