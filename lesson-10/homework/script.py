Oson darajadagi vazifalar (Easy-Level Tasks)
1. Ishchilar va bo‘limlar jadvalidan 50,000 dan yuqori maosh oluvchi ishchilar va ularning bo‘lim nomlarini chiqarish.
SELECT 
    E.EmployeeName, 
    E.Salary, 
    D.DepartmentName
FROM Employees E
JOIN Departments D ON E.DepartmentID = D.DepartmentID
WHERE E.Salary > 50000;

2. Mijozlar va buyurtmalar jadvalidan 2023-yilda berilgan buyurtmalarni va mijoz ismlarini ko‘rsatish.
SELECT 
    C.FirstName, 
    C.LastName, 
    O.OrderDate
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
WHERE YEAR(O.OrderDate) = 2023;

3. Barcha ishchilar va ularning bo‘limlarini ko‘rsatish. Agar ishchining bo‘limi bo‘lmasa ham ko‘rsatiladi.
SELECT 
    E.EmployeeName, 
    D.DepartmentName
FROM Employees E
LEFT JOIN Departments D ON E.DepartmentID = D.DepartmentID;

4. Yetkazib beruvchilar va ularning yetkazib beradigan mahsulotlarini ko‘rsatish. Mahsulot yetkazib bermagan yetkazib beruvchilar ham ko‘rinadi.
SELECT 
    S.SupplierName, 
    P.ProductName
FROM Suppliers S
LEFT JOIN Products P ON S.SupplierID = P.SupplierID;

5. Buyurtmalar va to‘lovlar jadvalidan barcha buyurtmalar va ular bilan bog‘liq to‘lovlarni ko‘rsatish. To‘lov bo‘lmagan buyurtmalar va buyurtmasiz to‘lovlar ham chiqadi.
SELECT 
    O.OrderID, 
    O.OrderDate, 
    P.PaymentDate, 
    P.Amount
FROM Orders O
FULL OUTER JOIN Payments P ON O.OrderID = P.OrderID;

6. Ishchilar va ularning boshliqlari ismlarini ko‘rsatish.
SELECT 
    E.EmployeeName, 
    M.EmployeeName AS ManagerName
FROM Employees E
LEFT JOIN Employees M ON E.ManagerID = M.EmployeeID;

7. Talabalar, kurslar va yozuvlar jadvalidan 'Math 101' kursida o‘qiyotgan talabalar ismini va kurs nomini chiqarish.
SELECT 
    S.StudentName, 
    C.CourseName
FROM Students S
JOIN Enrollments E ON S.StudentID = E.StudentID
JOIN Courses C ON E.CourseID = C.CourseID
WHERE C.CourseName = 'Math 101';

8. Mijozlar va buyurtmalar jadvalidan 3 tadan ortiq mahsulot buyurtma qilgan mijozlarning ismi va buyurtma miqdorini chiqarish.
SELECT 
    C.FirstName, 
    C.LastName, 
    O.Quantity
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
WHERE O.Quantity > 3;

9. Ishchilar va bo‘limlar jadvalidan 'Human Resources' bo‘limida ishlayotgan ishchilarni ko‘rsatish.
SELECT 
    E.EmployeeName, 
    D.DepartmentName
FROM Employees E
JOIN Departments D ON E.DepartmentID = D.DepartmentID
WHERE D.DepartmentName = 'Human Resources';

O‘rta darajadagi vazifalar (Medium-Level Tasks)
1. Bo‘limlarda 5 tadan ortiq ishchi bor bo‘lgan bo‘limlar va ishchilar sonini ko‘rsatish.
SELECT 
    D.DepartmentName, 
    COUNT(E.EmployeeID) AS EmployeeCount
FROM Departments D
JOIN Employees E ON D.DepartmentID = E.DepartmentID
GROUP BY D.DepartmentName
HAVING COUNT(E.EmployeeID) > 5;

2. Mahsulotlar va sotuvlar jadvalidan hech qachon sotilmagan mahsulotlarni topish.
SELECT 
    P.ProductID, 
    P.ProductName
FROM Products P
LEFT JOIN Sales S ON P.ProductID = S.ProductID
WHERE S.ProductID IS NULL;

3. Mijozlar va buyurtmalar jadvalidan kamida 1 ta buyurtma bergan mijozlarni va ularning buyurtmalar sonini chiqarish.
SELECT 
    C.FirstName, 
    C.LastName, 
    COUNT(O.OrderID) AS TotalOrders
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.FirstName, C.LastName;

4. Ishchilar va bo‘limlar jadvalidan faqat bo‘limi bor ishchilarni va bo‘lim nomlarini ko‘rsatish (NULL bo‘lmagan).
SELECT 
    E.EmployeeName, 
    D.DepartmentName
FROM Employees E
JOIN Departments D ON E.DepartmentID = D.DepartmentID
WHERE E.DepartmentID IS NOT NULL;

5. Bitta boshliqga biriktirilgan ishchilar juftligini topish (bir xil boshliqda ishlaydigan ishchilar).
SELECT 
    E1.EmployeeName AS Employee1, 
    E2.EmployeeName AS Employee2, 
    E1.ManagerID
FROM Employees E1
JOIN Employees E2 ON E1.ManagerID = E2.ManagerID AND E1.EmployeeID <> E2.EmployeeID
ORDER BY E1.ManagerID;

6. 2022-yilda berilgan buyurtmalar va ularni bergan mijozlarning ismini ko‘rsatish.
SELECT 
    O.OrderID, 
    O.OrderDate, 
    C.FirstName, 
    C.LastName
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID
WHERE YEAR(O.OrderDate) = 2022;

7. 'Sales' bo‘limida ishlaydigan va maoshi 60000 dan yuqori bo‘lgan ishchilarni chiqarish.
SELECT 
    E.EmployeeName, 
    E.Salary, 
    D.DepartmentName
FROM Employees E
JOIN Departments D ON E.DepartmentID = D.DepartmentID
WHERE D.DepartmentName = 'Sales' AND E.Salary > 60000;

8. Buyurtmalar va to‘lovlar jadvalidan faqat to‘lov qilingan buyurtmalarni ko‘rsatish.
SELECT 
    O.OrderID, 
    O.OrderDate, 
    P.PaymentDate, 
    P.Amount
FROM Orders O
JOIN Payments P ON O.OrderID = P.OrderID;

9. Mahsulotlar va buyurtmalar jadvalidan hech qachon buyurtma qilinmagan mahsulotlarni topish.
SELECT 
    P.ProductID, 
    P.ProductName
FROM Products P
LEFT JOIN Orders O ON P.ProductID = O.ProductID
WHERE O.ProductID IS NULL;

1. O‘z bo‘limidagi o‘rtacha maoshdan yuqori maosh oladigan xodimlarni topish:

SELECT Name AS EmployeeName, Salary
FROM Employees E
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
    WHERE DepartmentID = E.DepartmentID
);


2. 2020-yildan oldin berilgan, ammo to‘lov qilinmagan buyurtmalarni ro‘yxati:

SELECT O.OrderID, O.OrderDate
FROM Orders O
LEFT JOIN Payments P ON O.OrderID = P.OrderID
WHERE O.OrderDate < '2020-01-01' AND P.OrderID IS NULL;


3. Kategoriyasi mavjud bo‘lmagan mahsulotlarni topish:

SELECT ProductID, ProductName
FROM Products
WHERE Category NOT IN (SELECT DepartmentName FROM Departments);
-- E’tibor bering, agar Categories jadvali bo‘lsa, undan foydalanish kerak.


4. Bir xil boshliq ostida ishlaydigan va maoshi 60000 dan yuqori bo‘lgan xodimlarni topish:

SELECT E1.Name AS Employee1, E2.Name AS Employee2, E1.ManagerID, E1.Salary
FROM Employees E1
JOIN Employees E2 ON E1.ManagerID = E2.ManagerID AND E1.EmployeeID <> E2.EmployeeID
WHERE E1.Salary > 60000 AND E2.Salary > 60000;


5. Bo‘lim nomi "M" harfi bilan boshlanadigan bo‘limlarda ishlaydigan xodimlarni topish:

SELECT E.Name AS EmployeeName, D.DepartmentName
FROM Employees E
JOIN Departments D ON E.DepartmentID = D.DepartmentID
WHERE D.DepartmentName LIKE 'M%';


6. Sotuvlar jadvalidan 500 dan yuqori summadagi sotuvlar va mahsulot nomlarini chiqarish:

SELECT S.SaleID, P.ProductName, S.SaleAmount
FROM Sales S
JOIN Products P ON S.ProductID = P.ProductID
WHERE S.SaleAmount > 500;


7. 'Math 101' kursiga yozilmagan talabalarni topish:

SELECT S.StudentID, S.StudentName
FROM Students S
WHERE S.StudentID NOT IN (
    SELECT E.StudentID
    FROM Enrollments E
    JOIN Courses C ON E.CourseID = C.CourseID
    WHERE C.CourseName = 'Math 101'
);


8. To‘lov tafsilotlari mavjud bo‘lmagan buyurtmalarni chiqarish:

SELECT O.OrderID, O.OrderDate, P.PaymentID
FROM Orders O
LEFT JOIN Payments P ON O.OrderID = P.OrderID
WHERE P.PaymentID IS NULL;


9. 'Electronics' yoki 'Furniture' kategoriyasiga tegishli mahsulotlar ro‘yxati:

SELECT P.ProductID, P.ProductName, P.Category AS CategoryName
FROM Products P
WHERE P.Category IN ('Electronics', 'Furniture');
