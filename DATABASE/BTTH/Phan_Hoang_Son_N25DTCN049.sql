-- Tạo và sử dụng cơ sở dữ liệu
CREATE DATABASE IF NOT EXISTS center_management;
USE center_management;

-- YÊU CẦU 1 & 2: THIẾT KẾ CSDL VÀ TẠO BẢNG
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    full_name VARCHAR(100),
    gender VARCHAR(10),
    age INT
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    tuition_fee DECIMAL(15,2)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enroll_date DATE,
    score DECIMAL(5,2),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- YÊU CẦU 3: NHẬP DỮ LIỆU
-- Thêm 10 sinh viên
INSERT INTO students VALUES
(1, 'Nguyen Van A', 'Male', 20),
(2, 'Tran Thi B', 'Female', 21),
(3, 'Le Van C', 'Male', 22),
(4, 'Pham Thi D', 'Female', 19),
(5, 'Hoang Van E', 'Male', 20),
(6, 'Vu Thi F', 'Female', 23),
(7, 'Ngo Van G', 'Male', 21),
(8, 'Do Thi H', 'Female', 20),
(9, 'Bui Van I', 'Male', 24),
(10, 'Dang Thi K', 'Female', 22);

-- Thêm 5 khóa học
INSERT INTO courses VALUES
(1, 'Java', 5000000),
(2, 'Python', 4500000),
(3, 'MySQL', 3000000),
(4, 'ReactJS', 5500000),
(5, 'Testing', 4000000);

-- Thêm 15 bản ghi đăng ký (Một sinh viên học nhiều khóa, một khóa có nhiều sinh viên)
INSERT INTO enrollments VALUES
(1, 1, 1, '2026-06-01', 8.5),
(2, 1, 3, '2026-06-02', 7.0),
(3, 2, 2, '2026-06-01', 9.0),
(4, 3, 1, '2026-06-03', 6.5),
(5, 4, 4, '2026-06-04', 8.0),
(6, 5, 5, '2026-06-05', 7.5),
(7, 6, 1, '2026-06-01', 9.5),
(8, 7, 2, '2026-06-02', 6.0),
(9, 8, 3, '2026-06-03', 8.5),
(10, 9, 4, '2026-06-04', 7.0),
(11, 10, 5, '2026-06-05', 8.0),
(12, 1, 2, '2026-06-10', 7.5),
(13, 2, 4, '2026-06-11', 8.5),
(14, 3, 5, '2026-06-12', 6.0),
(15, 4, 1, '2026-06-15', 9.0);

-- CÁC CÂU TRUY VẤN
-- Câu 1
SELECT * FROM students;

-- Câu 2
SELECT full_name AS 'Tên sinh viên', age AS 'Tuổi' FROM students;

-- Câu 3 (Cập nhật tuổi của sinh viên có mã là 1 thành 25)
UPDATE students SET age = 25 WHERE student_id = 1;

-- Câu 4 (Xóa bản ghi đăng ký có mã 15)
DELETE FROM enrollments WHERE enrollment_id = 15;

-- Câu 5
SELECT COUNT(student_id) AS total_students FROM students;

-- Câu 6
SELECT 
    MAX(score) AS max_score, 
    MIN(score) AS min_score, 
    AVG(score) AS avg_score 
FROM enrollments;

-- Câu 7
SELECT SUM(tuition_fee) AS total_tuition_fee FROM courses;

-- Câu 8
SELECT c.course_name, COUNT(e.student_id) AS total_student 
FROM courses c 
JOIN enrollments e ON c.course_id = e.course_id 
GROUP BY c.course_id, c.course_name;

-- Câu 9
SELECT c.course_name, AVG(e.score) AS avg_score 
FROM courses c 
JOIN enrollments e ON c.course_id = e.course_id 
GROUP BY c.course_id, c.course_name;

-- Câu 10
SELECT c.course_name 
FROM courses c 
JOIN enrollments e ON c.course_id = e.course_id 
GROUP BY c.course_id, c.course_name 
HAVING COUNT(e.student_id) > 2;

-- Câu 11
SELECT s.* FROM students s 
JOIN enrollments e ON s.student_id = e.student_id 
WHERE e.score = (SELECT MAX(score) FROM enrollments);

-- Câu 12
SELECT s.* FROM students s 
JOIN enrollments e ON s.student_id = e.student_id 
WHERE e.score = (SELECT MIN(score) FROM enrollments);

-- Câu 13 (Sử dụng DISTINCT để không lặp sinh viên nếu họ có nhiều môn trên điểm TB)
SELECT DISTINCT s.* FROM students s 
JOIN enrollments e ON s.student_id = e.student_id 
WHERE e.score > (SELECT AVG(score) FROM enrollments);

-- Câu 14
SELECT * FROM courses 
WHERE tuition_fee = (SELECT MAX(tuition_fee) FROM courses);

-- Câu 15
SELECT s.full_name, c.course_name, e.score 
FROM enrollments e 
JOIN students s ON e.student_id = s.student_id 
JOIN courses c ON e.course_id = c.course_id;

-- Câu 16
SELECT s.full_name, c.course_name, e.enroll_date 
FROM enrollments e 
JOIN students s ON e.student_id = s.student_id 
JOIN courses c ON e.course_id = c.course_id;

-- Câu 17 (Tương tự câu 8 nhưng dùng LEFT JOIN để hiển thị cả khóa học chưa có ai đăng ký nếu có)
SELECT c.course_name, COUNT(e.student_id) AS total_student 
FROM courses c 
LEFT JOIN enrollments e ON c.course_id = e.course_id 
GROUP BY c.course_id, c.course_name;

-- Câu 18 (Tương tự câu 9)
SELECT c.course_name, AVG(e.score) AS avg_score 
FROM courses c 
JOIN enrollments e ON c.course_id = e.course_id 
GROUP BY c.course_id, c.course_name;

-- Câu 19
SELECT c.course_name, COUNT(e.student_id) AS total_student 
FROM courses c 
JOIN enrollments e ON c.course_id = e.course_id 
GROUP BY c.course_id, c.course_name 
ORDER BY total_student DESC 
LIMIT 1;

-- Câu 20
SELECT s.full_name, COUNT(e.course_id) AS total_courses 
FROM students s 
JOIN enrollments e ON s.student_id = e.student_id 
GROUP BY s.student_id, s.full_name 
ORDER BY total_courses DESC 
LIMIT 1;

-- Câu 21
SELECT s.full_name, c.course_name, e.score 
FROM enrollments e 
JOIN students s ON e.student_id = s.student_id 
JOIN courses c ON e.course_id = c.course_id 
JOIN (
    SELECT course_id, AVG(score) AS avg_score 
    FROM enrollments 
    GROUP BY course_id
) AS course_avg ON e.course_id = course_avg.course_id 
WHERE e.score > course_avg.avg_score;