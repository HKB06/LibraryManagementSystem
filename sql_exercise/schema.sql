
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL
);


CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    credits INT NOT NULL,
    capacity INT NOT NULL
);


CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);


CREATE TRIGGER check_course_capacity
BEFORE INSERT ON Enrollments
FOR EACH ROW
BEGIN
    DECLARE num_enrolled INT;
    SELECT COUNT(*) INTO num_enrolled
    FROM Enrollments
    WHERE course_id = NEW.course_id;
    IF num_enrolled >= (SELECT capacity FROM Courses WHERE course_id = NEW.course_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le cours a atteint sa capacité maximale.';
    END IF;
END;


CREATE TRIGGER check_student_courses
BEFORE INSERT ON Enrollments
FOR EACH ROW
BEGIN
    DECLARE num_courses INT;
    SELECT COUNT(*) INTO num_courses
    FROM Enrollments
    WHERE student_id = NEW.student_id;
    IF num_courses >= 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Un étudiant ne peut pas être inscrit à plus de 5 cours.';
    END IF;
END;

