CREATE DATABASE uy_vazifa1db;

create database SchoolDB;

USE SchoolDB;

create table Students (StudentID int primary key, name varchar(50),age int);

SELECT * FROM Students;

INSERT INTO Students VALUES (1, 'Ali', 20);
UPDATE Students SET Age = 21 WHERE StudentID = 1;
DELETE FROM Students WHERE StudentID = 1;

CREATE TABLE Courses (CourseID INT, CourseName VARCHAR(50));
ALTER TABLE Students ADD Email VARCHAR(100);
DROP TABLE Courses;

GRANT SELECT ON Students TO User1;
REVOKE SELECT ON Students FROM User1;

BEGIN TRAN;
UPDATE Students SET Age = 22 WHERE StudentID = 2;
COMMIT;

INSERT INTO Students (StudentID, Name, Age) VALUES (1, 'Ali', 20);
INSERT INTO Students (StudentID, Name, Age) VALUES (2, 'Laylo', 22);
INSERT INTO Students (StudentID, Name, Age) VALUES (3, 'Jamshid', 21);
