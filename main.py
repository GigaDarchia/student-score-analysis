import pandas as pd
import matplotlib.pyplot as plt

class StudentScoreAnalyzer:

    def __init__(self, file_path, subjects):
        """Initialize with the file path and subjects list."""
        self.df = pd.read_csv(file_path)
        self.subjects = subjects
        self.clean_dataframe()

    def clean_dataframe(self):
        """Clean the DataFrame by dropping rows with all NaN subjects and converting subjects to numeric."""
        self.df = self.df.dropna(subset=self.subjects, how="all")
        self.df.loc[:, self.subjects] = self.df[self.subjects].apply(pd.to_numeric, errors="coerce")

    def failed_students(self):
        """Return a DataFrame of students who failed at least one subject."""
        failed_students = self.df[self.subjects].apply(lambda x: (x < 50)).any(axis=1)
        failed_df = self.df[failed_students]
        return failed_df.drop_duplicates("Student")

    def average_score_by_semester(self):
        """Calculate and return the average score by semester for all subjects."""
        average_score = self.df.groupby("Semester")[self.subjects].apply(lambda x: x.replace(-1, pd.NA).mean())
        return average_score

    def find_best_student(self):
        """Find and return the student(s) with the highest average score."""
        self.df['Average_Score'] = self.df[self.subjects].mean(axis=1)
        best_students = self.df[self.df['Average_Score'] == self.df['Average_Score'].max()][
            ['Student', 'Average_Score']]
        return best_students

    def find_hardest_subject(self):
        """Find and return the subject with the lowest average score."""
        average_score = self.df[self.subjects].mean()
        hardest_subject = average_score.idxmin()
        return hardest_subject

    def generate_new_excel_file(self):
        """Generate an Excel file containing the average score by semester."""
        average_score = self.average_score_by_semester()
        average_score.to_excel("average_score_by_semester.xlsx", sheet_name="Average Score By Semester")
        print("Excel file was generated successfully.")

    def visualize_average_score_by_subject(self):
        """Visualize the average score per subject across all semesters using a bar chart."""
        avg_scores = self.average_score_by_semester()
        avg_scores_all_semesters = avg_scores.mean()

        avg_scores_all_semesters.plot(kind='bar', color="red")

        plt.title("Average Score per Subject Across All Semesters")
        plt.xlabel("Subjects")
        plt.ylabel("Average Score")
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.savefig("avg_score_per_subject.png")
        plt.show()

    def visualize_overall_average_score_by_semester(self):
        """Visualize the overall average score by semester using a line graph."""
        avg_scores = self.average_score_by_semester()
        overall_avg_by_semester = avg_scores.mean(axis=1)

        plt.figure(figsize=(10, 5))
        plt.plot(overall_avg_by_semester.index, overall_avg_by_semester, marker='o', linestyle='-')

        plt.title("Average Overall Score by Semester")
        plt.xlabel("Semesters")
        plt.ylabel("Average Overall Score")
        plt.grid(True)
        plt.xticks(overall_avg_by_semester.index)
        plt.savefig("avg_overall_score_by_semester.png")
        plt.show()

    def display_results(self):
        """Display the various results including failed students, average scores, best students, and hardest subject."""
        failed_df = self.failed_students()
        avg = self.average_score_by_semester()
        best_students = self.find_best_student()
        hardest_subject = self.find_hardest_subject()

        print(f"Failed Students: \n{failed_df}\n{'-' * 85}")
        print(f"Average Score By Semester: \n{avg}\n{'-' * 85}")
        print(f"Student(s) with best average score: \n{best_students}\n{'-' * 85}")
        print(f"Hardest Subject: {hardest_subject}\n{'-' * 85}")


def main():
    """Main function to execute the student score analysis."""
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    subjects = ["Math", "Physics", "English", "Chemistry", "Biology"]

    analyzer = StudentScoreAnalyzer("student_scores_random_names.csv", subjects)
    analyzer.display_results()
    analyzer.generate_new_excel_file()
    analyzer.visualize_average_score_by_subject()
    analyzer.visualize_overall_average_score_by_semester()


if __name__ == '__main__':
    main()
