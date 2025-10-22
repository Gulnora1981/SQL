1. 2022 yildan keyingi barcha buyurtmalar va ularni joylagan mijozlar
SELECT o.OrderID, CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE YEAR(o.OrderDate) > 2022;

2. Sales yoki Marketing bo‘limida ishlovchi xodimlar
SELECT e.Name AS EmployeeName, d.DepartmentName
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName IN ('Sales', 'Marketing');

3. Har bir bo‘limdagi eng yuqori maosh
SELECT d.DepartmentName, MAX(e.Salary) AS MaxSalary
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;

4. 2023 yilda buyurtma qilgan AQShlik mijozlar
SELECT CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, o.OrderID, o.OrderDate
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE c.Country = 'USA' AND YEAR(o.OrderDate) = 2023;

5. Har bir mijoz qancha buyurtma qilgan
SELECT CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, COUNT(o.OrderID) AS TotalOrders
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName, c.LastName;

6. "Gadget Supplies" yoki "Clothing Mart" yetkazib beruvchilari tomonidan ta’minlangan mahsulotlar
SELECT p.ProductName, s.SupplierName
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE s.SupplierName IN ('Gadget Supplies', 'Clothing Mart');

7. Har bir mijozning eng so‘nggi buyurtmasi (buyurtmasi bo‘lmagan mijozlar ham)
SELECT 
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, 
    MAX(o.OrderDate) AS MostRecentOrderDate
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.FirstName, c.LastName;

1. CustomerName, OrderTotal

Topshiriq: 500 dan yuqori umumiy buyurtma summasi bilan buyurtma qilgan mijozlarni ko‘rsatish.
Jadvallar: Orders, Customers

SELECT 
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, 
    o.TotalAmount AS OrderTotal
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE o.TotalAmount > 500;

2. ProductName, SaleDate, SaleAmount

Topshiriq: 2022 yilda sotilgan yoki 400 dan yuqori summa bo‘lgan mahsulotlarni ko‘rsatish.
Jadvallar: Products, Sales

SELECT 
    p.ProductName, 
    s.SaleDate, 
    s.SaleAmount
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
WHERE YEAR(s.SaleDate) = 2022 OR s.SaleAmount > 400;

3. ProductName, TotalSalesAmount

Topshiriq: Har bir mahsulot bo‘yicha jami sotuv summasini ko‘rsatish.
Jadvallar: Sales, Products

SELECT 
    p.ProductName, 
    SUM(s.SaleAmount) AS TotalSalesAmount
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY p.ProductName;

4. EmployeeName, DepartmentName, Salary

Topshiriq: HR bo‘limida ishlaydigan va maoshi 60000 dan yuqori bo‘lgan xodimlarni ko‘rsatish.
Jadvallar: Employees, Departments

SELECT 
    e.Name AS EmployeeName, 
    d.DepartmentName, 
    e.Salary
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'Human Resources' AND e.Salary > 60000;

5. ProductName, SaleDate, StockQuantity

Topshiriq: 2023 yilda sotilgan va sotuv vaqtida omborda 100 dan ortiq mahsulot bo‘lganlarni ko‘rsatish.
Jadvallar: Products, Sales

SELECT 
    p.ProductName, 
    s.SaleDate, 
    p.StockQuantity
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
WHERE YEAR(s.SaleDate) = 2023 AND p.StockQuantity > 100;


(Agar StockQuantity ustuni Products jadvalida mavjud bo‘lmasa, iltimos ma'lumot bering)

6. EmployeeName, DepartmentName, HireDate

Topshiriq: Sales bo‘limida ishlaydigan yoki 2020 yildan keyin ishga qabul qilingan xodimlarni ko‘rsatish.
Jadvallar: Employees, Departments

SELECT 
    e.Name AS EmployeeName, 
    d.DepartmentName, 
    e.HireDate
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'Sales' OR e.HireDate > '2020-12-31';

Qiyin daraja (Hard-Level) Tasks
1. CustomerName, OrderID, Address, OrderDate

Topshiriq: Manzili 4 raqam bilan boshlanuvchi AQSh mijozlarining buyurtmalarini ko‘rsatish.
Jadvallar: Customers, Orders

SELECT 
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, 
    o.OrderID, 
    c.Address, 
    o.OrderDate
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Country = 'USA' AND c.Address LIKE '[0-9][0-9][0-9][0-9]%';

2. ProductName, Category, SaleAmount

Topshiriq: Elektronika kategoriyasidagi mahsulotlar yoki 350 dan yuqori summa bo‘lgan sotuvlarni ko‘rsatish.
Jadvallar: Products, Sales, Categories

SELECT 
    p.ProductName, 
    c.CategoryName AS Category, 
    s.SaleAmount
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Electronics' OR s.SaleAmount > 350;

3. CategoryName, ProductCount

Topshiriq: Har bir kategoriya bo‘yicha mahsulotlar soni.
Jadvallar: Products, Categories

SELECT 
    c.CategoryName, 
    COUNT(p.ProductID) AS ProductCount
FROM Categories c
LEFT JOIN Products p ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName;

4. CustomerName, City, OrderID, Amount

Topshiriq: Los Angeles shahridagi mijozlar va 300 dan yuqori buyurtma summasi.
Jadvallar: Customers, Orders

SELECT 
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, 
    c.City, 
    o.OrderID, 
    o.TotalAmount AS Amount
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.City = 'Los Angeles' AND o.TotalAmount > 300;

5. EmployeeName, DepartmentName

Topshiriq: HR yoki Finance bo‘limida ishlaydigan yoki ismi kamida 4 unli tovushli xodimlar.
Jadvallar: Employees, Departments

SELECT 
    e.Name AS EmployeeName, 
    d.DepartmentName
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName IN ('Human Resources', 'Finance')
   OR LEN(REPLACE(REPLACE(REPLACE(REPLACE(LOWER(e.Name), 'a', ''), 'e', ''), 'i', ''), 'o', '')) <= LEN(e.Name) - 4;


Izoh: Bu yerda ismda kamida 4 ta unli tovush borligini aniqlash uchun, ismdan a, e, i, o harflari olib tashlanadi va ularning soni 4 dan katta ekanligi tekshiriladi. Agar kerak bo‘lsa, bu qismni yanada aniqroq qilsa bo‘ladi.

6. EmployeeName, DepartmentName, Salary

Topshiriq: Sales yoki Marketing bo‘limida ishlaydigan va maoshi 60000 dan yuqori bo‘lgan xodimlar.
Jadvallar: Employees, Departments

SELECT 
    e.Name AS EmployeeName, 
    d.DepartmentName, 
    e.Salary
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName IN ('Sales', 'Marketing') AND e.Salary > 60000;
