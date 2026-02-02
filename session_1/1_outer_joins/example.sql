-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 university.db
-- 2. Load this script: .read example.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
SELECT name, COUNT(student_id) AS TotalStudents FROM Courses 
LEFT JOIN StudentCourses ON Courses.id = StudentCourses.course_id 
GROUP BY name HAVING TotalStudents < 20;

SELECT Students.name AS students, Department.name AS department 
FROM 
Students JOIN Department 
ON Students.department_id = Department.id
ORDER BY department;
