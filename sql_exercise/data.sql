INSERT INTO Students (student_id, name, age, gender) VALUES
(1, 'Alice', 20, 'Female'),
(2, 'Bob', 22, 'Male'),
(3, 'Charlie', 19, 'Male'),
(4, 'Diana', 21, 'Female'),
(5, 'Eve', 23, 'Female');

INSERT INTO Courses (course_id, course_name, credits, capacity) VALUES
(1, 'Mathematics', 3, 2),
(2, 'Physics', 4, 3),
(3, 'Chemistry', 3, 2),
(4, 'Biology', 2, 3);

INSERT INTO Enrollments (student_id, course_id) VALUES
(1, 1), (1, 2), (2, 1), (2, 3),
(3, 2), (3, 4), (4, 2), (5, 4);
