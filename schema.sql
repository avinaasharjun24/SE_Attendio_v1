CREATE DATABASE IF NOT EXISTS attendance_system;
USE attendance_system;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('Admin', 'Teacher', 'Student') NOT NULL,
    student_id INT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(50) NOT NULL UNIQUE,
    department VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_students_department (department)
);

CREATE TABLE IF NOT EXISTS face_embeddings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    embedding LONGTEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_face_embeddings_student
        FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS attendance_sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subject VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    hour INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NULL,
    INDEX idx_attendance_sessions_dept_start (department, start_time)
);

CREATE TABLE IF NOT EXISTS attendance_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    session_id INT NOT NULL,
    status ENUM('Present', 'Late', 'Absent') NOT NULL,
    timestamp DATETIME NOT NULL,
    CONSTRAINT fk_attendance_logs_student
        FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_attendance_logs_session
        FOREIGN KEY (session_id) REFERENCES attendance_sessions(id)
        ON DELETE CASCADE,
    CONSTRAINT uq_attendance_logs_student_session
        UNIQUE (student_id, session_id),
    INDEX idx_attendance_logs_student_time (student_id, timestamp),
    INDEX idx_attendance_logs_session_time (session_id, timestamp)
);
