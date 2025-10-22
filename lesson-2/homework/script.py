1. Employees jadvalini yaratish:

CREATE TABLE Employees (
    EmpID INT,
    Name VARCHAR(50),
    Salary DECIMAL(10,2)
);

2. 3 ta yozuv qo‘shish:

INSERT INTO Employees (EmpID, Name, Salary) VALUES (1, 'Ali', 6000.00);
INSERT INTO Employees (EmpID, Name, Salary) 
VALUES 
(2, 'Laylo', 5000.00),
(3, 'Jamshid', 5500.00);

3. EmpID = 1 bo‘lgan xodimning oyligini 7000 ga o‘zgartirish:

UPDATE Employees 
SET Salary = 7000.00 
WHERE EmpID = 1;

4. EmpID = 2 bo‘lgan xodimni o‘chirish:

DELETE FROM Employees 
WHERE EmpID = 2;

5. DELETE, TRUNCATE, DROP farqlari (qisqacha):
DELETE	Faqat kerakli qatorlarni o‘chiradi. WHERE ishlatish mumkin. Struktura saqlanadi.
TRUNCATE	Barcha qatorlarni tezda o‘chiradi. WHERE ishlamaydi. Identifikatorlar (identity) qayta boshlanadi.
DROP	Jadvalni butunlay o‘chiradi (strukturasi ham, ma'lumotlari ham).

6. Name ustunini 100 belgigacha kengaytirish:

ALTER TABLE Employees 
ALTER COLUMN Name VARCHAR(100);

8. Salary ustunining turini FLOAT ga o‘zgartirish:

ALTER TABLE Employees 
ALTER COLUMN Salary FLOAT;

9. Departments jadvalini yaratish:

CREATE TABLE Departments (DepartmentID INT PRIMARY KEY,DepartmentName VARCHAR(50));

10. Employees jadvalidagi barcha yozuvlarni o‘chirish, strukturasini saqlab qolish:

TRUNCATE TABLE Employees;

1. Departments jadvaliga 5 ta yozuv qo‘shish (INSERT INTO SELECT bilan):

INSERT INTO Departments (DepartmentID, DepartmentName)
SELECT 1, 'HR' UNION ALL
SELECT 2, 'IT' UNION ALL
SELECT 3, 'Sales' UNION ALL
SELECT 4, 'Finance' UNION ALL
SELECT 5, 'Marketing';

2. Oyligi 5000 dan yuqori bo‘lganlarga bo‘lim sifatida 'Management' yozish:

UPDATE Employees 
SET Department = 'Management' 
WHERE Salary > 5000;

3. Employees jadvalidan barcha yozuvlarni o‘chirish, lekin jadval o‘zi qolishi kerak:
TRUNCATE TABLE Employees;

4. Department ustunini o‘chirish:
ALTER TABLE Employees 
DROP COLUMN Department;

5. Employees jadvalini StaffMembers deb o‘zgartirish:
EXEC sp_rename 'Employees', 'StaffMembers';

6. Departments jadvalini butunlay bazadan o‘chirish:
DROP TABLE Departments;

1. Products jadvalini yaratish (kamida 5 ta ustun):
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2),
    Description VARCHAR(255)
);

2. Narx 0 dan katta bo‘lishi uchun CHECK qo‘shish:
ALTER TABLE Products 
ADD CONSTRAINT CHK_Price_Positive CHECK (Price > 0);

3. StockQuantity ustunini qo‘shish, default qiymati 50:
ALTER TABLE Products 
ADD StockQuantity INT DEFAULT 50;

4. Category ustunini ProductCategory deb o‘zgartirish:
EXEC sp_rename 'Products.Category', 'ProductCategory', 'COLUMN';

5. 5 ta mahsulot yozuvi qo‘shish:
INSERT INTO Products (ProductID, ProductName, ProductCategory, Price, Description)
VALUES 
(1, 'Noutbuk', 'Elektronika', 1200.00, 'Zamonaviy noutbuk'),
(2, 'Telefon', 'Elektronika', 800.00, '5G telefon'),
(3, 'Stul', 'Mebel', 150.00, 'Ofis uchun stul'),
(4, 'Kitob', 'Kantselyariya', 20.00, 'Biologiya darsligi'),
(5, 'Ruchka', 'Kantselyariya', 2.00, 'Moviy siyohli ruchka');

6. Products jadvalidan Products_Backup degan nusxa olish (SELECT INTO bilan):
SELECT * INTO Products_Backup 
FROM Products;

7. Products jadvalini Inventory deb o‘zgartirish:
EXEC sp_rename 'Products', 'Inventory';

8. Price ustunining turini DECIMAL dan FLOAT ga o‘zgartirish:
ALTER TABLE Inventory 
ALTER COLUMN Price FLOAT;

9. IDENTITY bo‘lgan ProductCode ustunini Inventory jadvaliga qo‘shish (1000 dan boshlanib, 5 ga oshib boradi):
1. Yangi jadval yaratamiz:
CREATE TABLE Inventory_New (
    ProductCode INT IDENTITY(1000,5) PRIMARY KEY,
    ProductID INT,
    ProductName VARCHAR(100),
    ProductCategory VARCHAR(50),
    Price FLOAT,
    Description VARCHAR(255),
    StockQuantity INT
);

2. Eski jadvaldan yangi jadvalga ma'lumotlarni ko‘chiramiz:
INSERT INTO Inventory_New (ProductID, ProductName, ProductCategory, Price, Description, StockQuantity)
SELECT ProductID, ProductName, ProductCategory, Price, Description, StockQuantity
FROM Inventory;

3. Eski jadvalni o‘chiramiz va yangi nomini o‘zgartiramiz:
DROP TABLE Inventory;

EXEC sp_rename 'Inventory_New', 'Inventory';
