OSON DARAJADAGI TOPSHIRIQLAR
-- 1. Mahsulot nomini "Name" deb nomlash (alias berish)
SELECT ProductName AS Name FROM Products;

-- 2. Customers jadvaliga "Client" deb alias berish
SELECT * FROM Customers AS Client;

-- 3. Products va Products_Discounted jadvallaridagi mahsulot nomlarini birlashtirish (takrorlanmas holda)
SELECT ProductName FROM Products
UNION
SELECT ProductName FROM Products_Discounted;

-- 4. Har ikkala jadvalda mavjud bo‘lgan mahsulotlar (INTERSECT)
SELECT ProductName FROM Products
INTERSECT
SELECT ProductName FROM Products_Discounted;

-- 5. Takrorlanmas mijoz ismlari va ularning mamlakatlari
SELECT DISTINCT FirstName + ' ' + LastName AS CustomerName, Country FROM Customers;

-- 6. Narxiga qarab "High" yoki "Low" deb baholash (CASE)
SELECT ProductName, Price,
       CASE 
           WHEN Price > 1000 THEN 'High'
           ELSE 'Low'
       END AS PriceLevel
FROM Products;

-- 7. Skladdagi soniga qarab "Yes" yoki "No" degan ustun qo‘shish (IIF)
SELECT ProductName, StockQuantity,
       IIF(StockQuantity > 100, 'Yes', 'No') AS InStock
FROM Products_Discounted;

O‘RTACHA DARAJADAGI TOPSHIRIQLAR
-- 1. Yana bir marta birlashtirish (UNION)
SELECT ProductName FROM Products
UNION
SELECT ProductName FROM Products_Discounted;

-- 2. Products jadvalidagi, lekin Products_Discounted da yo‘q mahsulotlar (EXCEPT)
SELECT ProductName FROM Products
EXCEPT
SELECT ProductName FROM Products_Discounted;

-- 3. Narxiga qarab "Expensive" yoki "Affordable" deb yozish (IIF)
SELECT ProductName, Price,
       IIF(Price > 1000, 'Expensive', 'Affordable') AS PriceTag
FROM Products;

-- 4. 25 yoshdan kichik yoki maoshi 60000 dan yuqori bo‘lgan xodimlar

-- SELECT * FROM Employees WHERE Age < 25 OR Salary > 60000;

-- 5. HR bo‘limidagi yoki EmployeeID = 5 bo‘lgan xodimlarning maoshini oshirish
--  Employees jadvali yo‘qligi sababli bu kod faqat misol:
-- UPDATE Employees
-- SET Salary = Salary * 1.10
-- WHERE Department = 'HR' OR EmployeeID = 5;

QIYIN DARAJADAGI TOPSHIRIQLAR
-- 1. SaleAmount ga qarab "Top Tier", "Mid Tier", yoki "Low Tier" deb baholash
SELECT SaleID, SaleAmount,
       CASE 
           WHEN SaleAmount > 500 THEN 'Top Tier'
           WHEN SaleAmount BETWEEN 200 AND 500 THEN 'Mid Tier'
           ELSE 'Low Tier'
       END AS SaleTier
FROM Sales;

-- 2. Buyurtma bergan, lekin sotuvlar jadvalida yo‘q mijozlar
SELECT DISTINCT o.CustomerID
FROM Orders o
EXCEPT
SELECT DISTINCT s.CustomerID
FROM Sales s;

-- 3. Buyurtma miqdoriga qarab chegirma foizi hisoblash
SELECT CustomerID, Quantity,
       CASE
           WHEN Quantity = 1 THEN '3%'
           WHEN Quantity BETWEEN 2 AND 3 THEN '5%'
           ELSE '7%'
       END AS DiscountPercentage
FROM Orders;
