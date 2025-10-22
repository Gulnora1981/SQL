Oson‑darajadagi yechimlar

Mahsulotlarning eng arzon narxini topish

SELECT MIN(Price) AS MinPrice
FROM Products;


Xodimlar jadvalidan eng yuqori maoshni topish

SELECT MAX(Salary) AS MaxSalary
FROM Employees;


Mijozlar jadvalidagi umumiy mijozlar soni

SELECT COUNT(*) AS TotalCustomers
FROM Customers;


Mahsulot kategoriyalari ichidan noyob kategoriyalar sonini hisoblash

SELECT COUNT(DISTINCT Category) AS UniqueCategoryCount
FROM Products;


Sales jadvalidan ProductID = 7 bo‘lgan mahsulot uchun umumiy savdo summasi

SELECT SUM(SaleAmount) AS TotalSalesForProduct7
FROM Sales
WHERE ProductID = 7;


Xodimlarning o‘rtacha yoshini hisoblash

SELECT AVG(Age * 1.0) AS AvgEmployeeAge
FROM Employees;


Eslatma: AVG(Age * 1.0) deb yozish orqali kasrli natija olish uchun sonni numeric ko‘rinishda ishlatamiz.

Har bir bo‘limdagi xodimlar sonini hisoblash

SELECT DepartmentName, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY DepartmentName;


Mahsulotlar jadvalidan har bir kategoriya bo‘yicha eng arzon va eng qimmat mahsulot narxini ko‘rsatish

SELECT Category,
       MIN(Price) AS MinPrice,
       MAX(Price) AS MaxPrice
FROM Products
GROUP BY Category;


Sales jadvalidan har bir mijoz uchun umumiy savdo summasini hisoblash

SELECT CustomerID, SUM(SaleAmount) AS TotalSalesPerCustomer
FROM Sales
GROUP BY CustomerID;


Employees jadvalidan 5 tadan ortiq xodimi bo‘lgan bo‘limlarni chiqarish

SELECT DepartmentName, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY DepartmentName
HAVING COUNT(*) > 5;

Har bir mahsulot kategoriyasi uchun umumiy va o‘rtacha savdoni hisoblash:

SELECT p.Category,
       SUM(s.SaleAmount) AS TotalSales,
       AVG(s.SaleAmount) AS AvgSales
FROM Products p
JOIN Sales s ON p.ProductID = s.ProductID
GROUP BY p.Category;


HR bo‘limidagi xodimlar sonini hisoblash:

SELECT COUNT(*) AS HR_EmployeeCount
FROM Employees
WHERE DepartmentName = 'HR';


Har bir bo‘limda eng yuqori va eng past maoshni topish:

SELECT DepartmentName,
       MAX(Salary) AS MaxSalary,
       MIN(Salary) AS MinSalary
FROM Employees
GROUP BY DepartmentName;


Har bir bo‘lim uchun o‘rtacha maoshni hisoblash:

SELECT DepartmentName,
       AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY DepartmentName;


Har bir bo‘limdagi ishchilar uchun o‘rtacha maosh va ishchi sonini chiqaring:

SELECT DepartmentName,
       COUNT(*) AS EmployeeCount,
       AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY DepartmentName;


O‘rtacha mahsulot narxi 400 dan yuqori bo‘lgan kategoriyalarni toping:

SELECT Category,
       AVG(Price) AS AvgPrice
FROM Products
GROUP BY Category
HAVING AVG(Price) > 400;


Har bir yil uchun umumiy savdoni hisoblang:

SELECT YEAR(SaleDate) AS SaleYear,
       SUM(SaleAmount) AS TotalSalesYear
FROM Sales
GROUP BY YEAR(SaleDate);


Har bir mijozni 3 yoki undan ortiq buyurtma berganlar ro‘yxatini ko‘rsating:

SELECT CustomerID,
       COUNT(*) AS OrderCount
FROM Orders
GROUP BY CustomerID
HAVING COUNT(*) >= 3;


O‘rtacha maosh xarajatlari 60000 dan ortiq bo‘lgan bo‘limlarni ko‘rsating:

SELECT DepartmentName,
       AVG(Salary) AS AvgSalary,
       SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY DepartmentName
HAVING AVG(Salary) > 60000;

Har bir mahsulot kategoriyasi uchun o‘rtacha narxni hisoblab, 150 dan yuqori bo‘lganlarini tanlang.

SELECT Category,
       AVG(Price) AS AvgPrice
FROM Products
GROUP BY Category
HAVING AVG(Price) > 150;


Har bir mijoz uchun umumiy savdo summasini hisoblab, 1500 dan yuqori bo‘lganlarini chiqarish.

SELECT CustomerID,
       SUM(SaleAmount) AS TotalSales
FROM Sales
GROUP BY CustomerID
HAVING SUM(SaleAmount) > 1500;


Har bir bo‘limdagi (DepartmentName bo‘yicha) xodimlar uchun umumiy va o‘rtacha maoshni hisoblang, faqat o‘rtacha maoshi 65000 dan yuqori bo‘lgan bo‘limlarni ko‘rsating.

SELECT DepartmentName,
       SUM(Salary) AS TotalSalary,
       AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY DepartmentName
HAVING AVG(Salary) > 65000;


tsql2012.sales.orders jadvalidan har bir mijoz uchun Freight > 50 bo‘lgan buyurtmalar bo‘yicha umumiy summani va eng kam xaridni ko‘rsating.
(Agar sizda TSQL2012 bazasi mavjud bo’lsa)

SELECT CustomerID,
       SUM(Freight) AS TotalFreight,
       MIN(TotalAmount) AS MinPurchase
FROM tsql2012.sales.orders
WHERE Freight > 50
GROUP BY CustomerID;


Orders jadvalidan har bir yil va oy bo‘yicha umumiy savdo va noyob mahsulotlar sonini hisoblab, kamida 2 xil mahsulot sotilgan oylarni ko‘rsating.

SELECT 
  YEAR(OrderDate) AS SaleYear,
  MONTH(OrderDate) AS SaleMonth,
  SUM(TotalAmount) AS TotalSales,
  COUNT(DISTINCT ProductID) AS UniqueProducts
FROM Orders
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
HAVING COUNT(DISTINCT ProductID) >= 2;


Orders jadvalidan har bir yil bo‘yicha eng kam va eng ko‘p buyurtma miqdorini (Quantity) toping.

SELECT 
  YEAR(OrderDate) AS SaleYear,
  MIN(Quantity) AS MinQuantity,
  MAX(Quantity) AS MaxQuantity
FROM Orders
GROUP BY YEAR(OrderDate);
