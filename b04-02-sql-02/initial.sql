-- Active: 1741508230714@@127.0.0.1@3306@ostad_test_1
-- Create students table with various data types
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    enrollment_date DATE,
    gpa DECIMAL(3,2),
    active BOOLEAN,
    course_id INT
);

-- Create courses table
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    instructor VARCHAR(50),
    credits INT,
    department VARCHAR(50)
);

-- Insert data into courses table
INSERT INTO courses VALUES
(101, 'Introduction to Programming', 'Dr. Smith', 3, 'Computer Science'),
(102, 'Database Fundamentals', 'Dr. Johnson', 4, 'Information Systems'),
(103, 'Web Development', 'Prof. Brown', 3, 'Computer Science'),
(104, 'Data Structures', 'Dr. Davis', 4, 'Computer Science'),
(105, 'Business Analytics', 'Prof. Wilson', 3, 'Business');

-- Insert data into students table
INSERT INTO students VALUES
(1, 'John', 'Doe', '2000-05-15', '2022-09-01', 3.75, true, 101),
(2, 'Jane', 'Smith', '2001-08-22', '2022-09-01', 3.90, true, 102),
(3, 'Mike', 'Johnson', '1999-11-30', '2021-09-01', 3.45, true, 101),
(4, 'Sarah', 'Williams', '2002-02-18', '2022-09-01', 4.00, true, 103),
(5, 'David', 'Brown', '2000-07-09', '2021-09-01', 3.20, false, 104),
(6, 'Emily', 'Davis', '2001-04-25', '2022-01-15', 3.80, true, 102),
(7, 'Chris', 'Wilson', '1999-09-14', '2021-09-01', 2.90, true, 105),
(8, 'Jessica', 'Taylor', '2002-06-30', '2022-09-01', 3.50, true, 103),
(9, 'Ryan', 'Anderson', '2000-12-03', '2021-01-15', 3.10, false, NULL),
(10, 'Amanda', 'Thomas', '2001-10-17', '2022-09-01', 3.65, true, NULL);
