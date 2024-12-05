SELECT s.name AS student_name, c.course_name, c.credits
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Courses c ON e.course_id = c.course_id;

SELECT name AS student_name
FROM Students
WHERE student_id NOT IN (SELECT DISTINCT student_id FROM Enrollments);

SELECT c.course_name, COUNT(e.enrollment_id) AS number_of_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id;

SELECT c.course_name
FROM Courses c
JOIN (
    SELECT course_id, COUNT(enrollment_id) AS num_enrolled
    FROM Enrollments
    GROUP BY course_id
) AS enrollment_count
ON c.course_id = enrollment_count.course_id
WHERE num_enrolled > c.capacity / 2;

SELECT s.name, COUNT(e.course_id) AS courses_enrolled
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id
ORDER BY courses_enrolled DESC
LIMIT 1;

SELECT s.name, SUM(c.credits) AS total_credits
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
GROUP BY s.student_id;

SELECT course_name
FROM Courses
WHERE course_id NOT IN (SELECT DISTINCT course_id FROM Enrollments);

DELETE FROM Enrollments
WHERE course_id = 2; 

DELETE FROM Students
WHERE student_id NOT IN (SELECT DISTINCT student_id FROM Enrollments);