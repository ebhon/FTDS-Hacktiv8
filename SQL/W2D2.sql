----------------------------
--Data Definition Language--
----------------------------

-- Create Server --
-- Servers (klik kanan) -> register server -> server... --
-- Tab General -> isi nama server
-- Tab Connection -> Host Name : localhost, Password (optional) Port :5432

----------------------------

-- Create Database --
CREATE DATABASE DB_RMT036;
CREATE DATABASE "DB_RMT036";

--  Delete Database --
DROP DATABASE "DB_RMT036";

-- Create Table --
-- Penulisannya <nama_kolom tipe_data constrain>
-- tipe_data (String, Number, Date)
	-- String (CHAR, VARCHAR, TEXT)
		-- CHAR (10) -> "Yosef     "
		-- VARCHAR (10) -> "Yosef"
	-- Number (INT, BIGINT, FLOAT, DOUBLE)
	-- Date (DATE, TIMESTAMP)
		-- DATE - > Satuan terkecilnya HARI/TANGGAL
		-- TIMESTAMP -> Satuan terkecilnya setidaknya JAM
-- constrain (PRIMARY KEY, FOREIGN KEY/REFERENCES, NOT NULL, UNIQUE)
-- bikin table tanpa FK terlebih dahulu--
CREATE TABLE campus (
	id SERIAL PRIMARY KEY,
	campus_name VARCHAR (50),
	batch VARCHAR (10),
	start_date DATE
);

CREATE TABLE students (
	id SERIAL PRIMARY KEY,
	name VARCHAR (50),
	age INTEGER,
	campus_id INTEGER REFERENCES campus (id),
	total_grade FLOAT
);

-- Delete Table
--Hapus dulu table yang ada FOREIGN KEY
DROP TABLE students;
DROP TABLE campus;

-- Alter --
-- Remame Column Name--
ALTER TABLE students
	RENAME COLUMN total_grade TO grade;

-- Truncate --
-- Menghapus semua data tapi tidak dengan table dan relasinya
TRUNCATE TABLE students, campus;

--------------------------------
-- Data Manipulation Language --
--------------------------------

-- Insert Data -
-- Sama seperti create tabe, masukin data yang ga ada FOREIGN KEY dulu --
-- Insert data into the campus table
INSERT INTO campus (campus_name, batch, start_date)
VALUES
    ('Remote', 'RMT-1', '2023-01-01'),
    ('Jakarta', 'HCK-2', '2023-02-01'),
    ('BSD', 'BSD-4', '2023-03-01'),
    ('Surabaya', 'SUB-1', '2023-04-01'),
    ('Singapore', 'SIN-1', '2023-05-01');

-- Insert data into the students table
INSERT INTO students (name, age, campus_id, grade)
VALUES
    ('Rafif Iman', 20, 11, 85.5),
    ('Hana Arisona', 21, 12, 90.2),
    ('Raka Purnomo', 19, 11, 78.9),
    ('Danu Irfansyah', 20, 13, 92.7),
    ('Rachman Ardhi', 22, 12, 88.1);

--Update --
-- Update Age
UPDATE students
	SET age = 22
	WHERE name = 'Rafif Iman';

-- Delete --
DELETE FROM students
	WHERE id = 18;
-- Delete semua data --
DELETE FROM students;

-- Explain & Explain Analysis
--Explain memberikan informasi query
EXPLAIN
SELECT * FROM campus;
-- Explain Analysis memberikan informasi query & waktunya
EXPLAIN ANALYZE
SELECT * FROM students;

-- Untuk lihat isi data --
SELECT * FROM campus;
SELECT * FROM students;