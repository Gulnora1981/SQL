1. Products va Suppliers jadvalidan barcha mahsulot va yetkazib beruvchilar kombinatsiyalarini ko‘rsatish (Cartesian product)
SELECT P.ProductName, S.SupplierName
FROM Products P
CROSS JOIN Suppliers S;

2. Departments va Employees jadvalidan barcha bo‘lim va xodim kombinatsiyalarini ko‘rsatish
SELECT D.DepartmentName, E.Name
FROM Departments D
CROSS JOIN Employees E;

3. Products va Suppliers jadvalidan faqat haqiqatan mahsulotni yetkazib beruvchi yetkazib beruvchilarni ko‘rsatish
SELECT S.SupplierName, P.ProductName
FROM Products P
INNER JOIN Suppliers S ON P.SupplierID = S.SupplierID;

4. Orders va Customers jadvalidan har bir mijoz va uning buyurtma identifikatorlarini ko‘rsatish
SELECT C.FirstName, C.LastName, O.OrderID
FROM Orders O
INNER JOIN Customers C ON O.CustomerID = C.CustomerID;

5. Courses va Students jadvalidan barcha talaba va kurs kombinatsiyalarini ko‘rsatish
SELECT C.CourseName, S.StudentName
FROM Courses C
CROSS JOIN Students S;

6. Products va Orders jadvalidan mahsulotlar va ularning buyurtmalari, ProductID mos kelganda
SELECT P.ProductName, O.OrderID
FROM Products P
INNER JOIN Orders O ON P.ProductID = O.ProductID;

7. Departments va Employees jadvalidan faqat mos keluvchi DepartmentID ga ega bo‘lgan xodimlarni ko‘rsatish
SELECT E.Name, D.DepartmentName
FROM Employees E
INNER JOIN Departments D ON E.DepartmentID = D.DepartmentID;

8. Students va Enrollments jadvalidan talaba nomlari va ularning kurslari (Enrollments) ni ko‘rsatish
SELECT S.StudentName, E.CourseID
FROM Students S
INNER JOIN Enrollments E ON S.StudentID = E.StudentID;

9. Payments va Orders jadvalidan to‘lovga ega buyurtmalarni ko‘rsatish
SELECT O.OrderID, P.PaymentID, P.Amount
FROM Orders O
INNER JOIN Payments P ON O.OrderID = P.OrderID;

10. Orders va Products jadvalidan narxi 100 dan ko‘p bo‘lgan buyurtmalarni ko‘rsatish
SELECT O.OrderID, P.ProductName, P.Price
FROM Orders O
INNER JOIN Products P ON O.ProductID = P.ProductID
WHERE P.Price > 100;
O‘rta darajadagi misollar

1. Employees va Departments jadvallari: Turli DepartmentIDga ega xodim va bo‘limlarni ro‘yxatlash (DepartmentIDlar teng emas).

SELECT e.Name AS XodimIsmi, d.DepartmentName AS Bo‘limNomi
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID <> d.DepartmentID;


2. Orders va Products jadvallari: Buyurtmadagi miqdor (quantity) mahsulot omboridagi mavjud miqdordan katta bo‘lganlar.

SELECT o.OrderID, p.ProductName, o.Quantity, p.StockQuantity
FROM Orders o
INNER JOIN Products p ON o.ProductID = p.ProductID
WHERE o.Quantity > p.StockQuantity;


3. Customers va Sales jadvallari: Savdo summasi 500 yoki undan ko‘p bo‘lgan mijozlar va mahsulotlar ro‘yxati.

SELECT c.FirstName AS Ism, c.LastName AS Familiya, s.ProductID, s.SaleAmount AS SavdoSummasi
FROM Customers c
INNER JOIN Sales s ON c.CustomerID = s.CustomerID
WHERE s.SaleAmount >= 500;


4. Courses, Enrollments, Students jadvallari: Talabalar va ularning ro‘yxatdan o‘tgan kurslari.

SELECT st.Name AS TalabaIsmi, c.CourseName AS KursNomi
FROM Students st
INNER JOIN Enrollments e ON st.StudentID = e.StudentID
INNER JOIN Courses c ON e.CourseID = c.CourseID;


5. Products va Suppliers jadvallari: Yetkazib beruvchi nomida “Tech” so‘zi bor mahsulotlar va yetkazib beruvchilar.

SELECT p.ProductName AS MahsulotNomi, s.SupplierName AS YetkazibBeruvchi
FROM Products p
INNER JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE s.SupplierName LIKE '%Tech%';

1. Ranking (tartiblash) va agregat funksiyalar bilan

Talabalar jadvalidan har bir fan bo‘yicha eng yaxshi 3 ball olgan talabalar ro‘yxatini chiqarish.

WITH RankedScores AS (
  SELECT
    StudentID,
    CourseID,
    Score,
    RANK() OVER (PARTITION BY CourseID ORDER BY Score DESC) AS RankNum
  FROM Scores
)
SELECT
  StudentID,
  CourseID,
  Score
FROM RankedScores
WHERE RankNum <= 3;


Izoh:
RANK() funksiyasi yordamida har bir kurs bo‘yicha ballar yuqori tartibda saralanadi va eng yaxshi 3 talaba olinadi.

2. Rekursiv so‘rov (Recursive CTE)

Tashkilotdagi xodimlar va ularning boshliqlari daraxt ko‘rinishida (hierarchy) ko‘rsatiladi.

WITH RECURSIVE EmployeeHierarchy AS (
  SELECT EmployeeID, ManagerID, Name, 1 AS Level
  FROM Employees
  WHERE ManagerID IS NULL  -- Yuqori boshliq (CEO)

  UNION ALL

  SELECT e.EmployeeID, e.ManagerID, e.Name, eh.Level + 1
  FROM Employees e
  INNER JOIN EmployeeHierarchy eh ON e.ManagerID = eh.EmployeeID
)
SELECT * FROM EmployeeHierarchy ORDER BY Level, ManagerID;


Izoh:
Bu so‘rov tashkilotning boshliq-xodim munosabatini daraxt ko‘rinishida chiqaradi.

3. Ko‘p darajali guruhlash (GROUP BY bilan HAVING)

Har bir mijoz uchun yil bo‘yicha umumiy sotuv summasini hisoblab, 10000dan ortiq summaga ega bo‘lgan yil va mijozlarni ko‘rsatish.

SELECT CustomerID, YEAR(SaleDate) AS SaleYear, SUM(SaleAmount) AS TotalSale
FROM Sales
GROUP BY CustomerID, YEAR(SaleDate)
HAVING SUM(SaleAmount) > 10000;

4. JSON ma'lumotlar bilan ishlash (agar DBMS qo‘llab-quvvatlasa)

Agar jadvalda JSON formatdagi ma’lumotlar saqlangan bo‘lsa, masalan, mahsulotlarning tafsilotlari:

SELECT ProductID,
       JSON_VALUE(ProductDetails, '$.weight') AS Ogirligi,
       JSON_VALUE(ProductDetails, '$.color') AS Rangi
FROM Products
WHERE JSON_VALUE(ProductDetails, '$.weight') > 10;

5. Window functions bilan — oynalik sotuvlar summasi

Har bir mijoz uchun oxirgi 3 oylik oynalik (monthly rolling) sotuv summasini hisoblash.

SELECT
  CustomerID,
  SaleDate,
  SUM(SaleAmount) OVER (
    PARTITION BY CustomerID
    ORDER BY SaleDate
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS Rolling3MonthSales
FROM Sales;
