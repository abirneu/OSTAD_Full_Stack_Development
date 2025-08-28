

SELECT * FROM courses;

SELECT students.student_id, students.first_name, students.last_name, students.gpa 
FROM students;



-- ORDER BY
SELECT students.student_id, students.first_name, students.last_name, students.gpa 
FROM students
WHERE students.gpa = 4.00
ORDER BY students.gpa DESC
;


-- LIMIT
SELECT students.student_id, students.first_name, students.last_name, students.gpa 
FROM students
ORDER BY students.gpa ASC
LIMIT 3
;


-- LIKE
SELECT students.student_id, students.first_name, students.last_name, students.gpa 
FROM students
WHERE students.last_name LIKE "D%"
;


SELECT 
    students.student_id, 
    students.first_name, 
    students.last_name, 
    students.gpa 
FROM students
WHERE students.first_name LIKE "%a%"
;

SELECT students.student_id, students.first_name, students.last_name, students.gpa 
FROM students
WHERE students.first_name LIKE "J___"
;


SELECT COUNT(*)
FROM students;


-- Grouping
SELECT students.course_id, COUNT(*)
FROM students
GROUP BY students.course_id
;



SELECT students.course_id, AVG(students.gpa)
FROM students
GROUP BY students.course_id
HAVING AVG(students.gpa) > 3.5
;

SELECT * FROM students;

-- HAVING
SELECT students.course_id, COUNT(*)
FROM students
GROUP BY students.course_id
HAVING COUNT(*) > 1
;





-- INNER JOIN
SELECT
    students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id
;


-- LEFT JOIN
SELECT
    -- students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.course_id
;


-- RIGHT JOIN
SELECT
    -- students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
RIGHT JOIN courses
ON students.course_id = courses.course_id
;



-- FULL JOIN
SELECT
    -- students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.course_id

UNION

SELECT
    -- students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
RIGHT JOIN courses
ON students.course_id = courses.course_id
;
