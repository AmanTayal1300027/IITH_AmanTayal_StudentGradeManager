# IITH_AmanTayal_StudentGradeManager
CLI based python program to manage student grades

Please do note that the CSV file that you create will be in assets/other-assets folder

## Installation
```bash
git clone https://github.com/AmanTayal1300027/IITH_AmanTayal_StudentGradeManager.git
cd IITH_AmanTayal_StudentGradeManager
pip install -r requirements.txt
python src/main.py
```
## Design Choices
This project was designed with simplicity, clarity, and modularity in mind to simulate a real-world CLI-based student record management system.

- **CSV File for Storage:** Chosen for its simplicity and ease of use. It allows direct viewing and editing of student records without needing a complex database. The file is stored in `assets/other-assets/students.csv` for organized separation of code and data.

- **`tabulate` Library:** Used for presenting student data in a clean, readable tabular format. It improves user experience when working in a terminal environment.

- **Modular Code Structure:** Functions were separated logically (e.g., `add`, `update`, `display`, `remove`) for better readability, maintainability, and future modular expansion into separate modules.

- **Validation Functions:** Input validation ensures that grades are always floating-point values. This avoids runtime crashes and maintains data integrity.

- **Simple CLI Interface:** A menu-driven interface using input prompts provides a basic but effective way for users to navigate the application.


## Features & Functionality
- **Add New Students –** Add a new student by providing ID, name, and grade. Prevents duplicate IDs.

- **Update Grades –** Modify the grade of any student by ID with input validation.

- **Delete Student –** Remove student records by ID.

- **View Records –** Display all records in a clean tabular format or search by ID.

- **Text-based Bar Chart –** Visually compare student grades using proportional bars.

- **Statistics Calculation –** Compute and append average and highest grades to the data at end.

- **Persistent Storage –** All changes are saved in a CSV file for future access and analysis.

## Learnings

- **Practical CSV Handling –** Gained hands-on experience in reading from, writing to, and updating CSV files programmatically.

- **Modular Programming –** Improved ability to write clean, modular, and testable code.

- **User Input Validation –** Learned techniques for validating and sanitizing input in command-line applications.

- **CLI Interface Design –** Understood how to design a usable interface without relying on GUI libraries.

- **Data Visualization with ASCII –** Practiced building simple visualizations in text format, enhancing UX in terminal environments.

- **Code Structure & Documentation –** Learned to create structured codebases and maintain proper documentation like `README.md` and `requirements.txt`.

