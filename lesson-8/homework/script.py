Oson darajadagi topshiriqlar:
1. Har bir kategoriya bo‘yicha mahsulotlar sonini toping:
SELECT Category, COUNT(*) AS Mahsulot_Soni
FROM Products
GROUP BY Category;

2. 'Electronics' kategoriyasidagi mahsulotlarning o‘rtacha narxini toping:
SELECT AVG(Price) AS Ortacha_Narx
FROM Products
WHERE Category = 'Electronics';

3. Shahar nomi 'L' harfi bilan boshlanadigan mijozlarni chiqaring:
SELECT *
FROM Customers
WHERE City LIKE 'L%';

4. Nomining oxiri 'er' bilan tugaydigan mahsulotlarni toping:
SELECT ProductName
FROM Products
WHERE ProductName LIKE '%er';

5. Davlati 'A' harfi bilan tugaydigan mijozlarni chiqaring:
SELECT *
FROM Customers
WHERE Country LIKE '%A';

6. Eng qimmat mahsulotning narxini ko‘rsating:
SELECT MAX(Price) AS Eng_Qimmat_Narx
FROM Products;

7. Mahsulot zaxirasiga qarab 'Low Stock' va 'Sufficient' deb belgilash:
SELECT ProductName, StockQuantity,
       CASE 
           WHEN StockQuantity < 30 THEN 'Low Stock'
           ELSE 'Sufficient'
       END AS Zahira_Holati
FROM Products;

8. Har bir davlat bo‘yicha mijozlar sonini toping:
SELECT Country, COUNT(*) AS Mijoz_Soni
FROM Customers
GROUP BY Country;

9. Buyurtmalar jadvalidan eng kam va eng ko‘p buyurtma miqdorini toping:
SELECT MIN(Quantity) AS Eng_Kam, MAX(Quantity) AS Eng_Kop
FROM Orders;

O‘rta darajadagi topshiriqlar:
10. 2023 yil yanvar oyida buyurtma bergan lekin hisob-fakturasi bo‘lmagan mijoz IDlarini toping:
SELECT DISTINCT o.CustomerID
FROM Orders o
LEFT JOIN Invoices i ON o.CustomerID = i.CustomerID
    AND MONTH(i.InvoiceDate) = 1 AND YEAR(i.InvoiceDate) = 2023
WHERE MONTH(o.OrderDate) = 1 AND YEAR(o.OrderDate) = 2023
  AND i.CustomerID IS NULL;

11. Products va Products_Discounted jadvallaridagi barcha mahsulot nomlarini (takrorlar bilan) birlashtiring:
SELECT ProductName FROM Products
UNION ALL
SELECT ProductName FROM Products_Discounted;

12. Products va Products_Discounted jadvallaridagi mahsulot nomlarini (takrorsiz) birlashtiring:
SELECT ProductName FROM Products
UNION
SELECT ProductName FROM Products_Discounted;

13. Har yil bo‘yicha buyurtmalarning o‘rtacha summasini toping:
SELECT YEAR(OrderDate) AS Yil, AVG(TotalAmount) AS Ortacha_Summa
FROM Orders
GROUP BY YEAR(OrderDate);

14. Mahsulot narxiga qarab guruhlab, mahsulot nomi va narx guruhini chiqaring:
SELECT ProductName, Price,
       CASE 
           WHEN Price < 100 THEN 'Low'
           WHEN Price BETWEEN 100 AND 500 THEN 'Mid'
           ELSE 'High'
       END AS Narx_Guruhi
FROM Products;

15. City_Population jadvalidan pivot qilish (yillar ustun bo‘lib chiqsin) va yangi jadvalga saqlash:
SELECT * 
INTO Population_Each_Year
FROM (
    SELECT district_name, year, population
    FROM city_population
) AS SourceTable
PIVOT (
    SUM(population) FOR year IN ([2012], [2013])
) AS PivotTable;

16. Har bir mahsulot ID bo‘yicha umumiy savdoni toping:
SELECT ProductID, SUM(SaleAmount) AS Umumiy_Savdo
FROM Sales
GROUP BY ProductID;

17. Nomida 'oo' bo‘lgan mahsulotlarni toping:
SELECT ProductName
FROM Products
WHERE ProductName LIKE '%oo%';

18. City_Population jadvalidan pivot qilish (shaharlar ustun bo‘lib chiqsin) va natijani yangi jadvalga saqlash:
SELECT * 
INTO Population_Each_City
FROM (
    SELECT year, district_name, population
    FROM city_population
) AS SourceTable
PIVOT (
    SUM(population) FOR district_name IN ([Bektemir], [Chilonzor], [Yakkasaroy])
) AS PivotTable;

Qiyin darajadagi topshiriqlar:
19. Eng ko‘p sarflagan 3 nafar mijozni (CustomerID va umumiy sarf) toping:
SELECT TOP 3 CustomerID, SUM(TotalAmount) AS TotalSpent
FROM Invoices
GROUP BY CustomerID
ORDER BY TotalSpent DESC;

20. Population_Each_Year jadvalidan asl holatiga (City_Population) qaytaring:
SELECT district_name, [2012] AS population, '2012' AS year FROM Population_Each_Year
UNION ALL
SELECT district_name, [2013], '2013' FROM Population_Each_Year;

21. Mahsulot nomlari va ularning necha marta sotilganini chiqarish (JOIN bilan):
SELECT p.ProductName, COUNT(s.SaleID) AS Sotilgan_Soni
FROM Sales s
JOIN Products p ON s.ProductID = p.ProductID
GROUP BY p.ProductName;

22. Population_Each_City jadvalidan asl holatiga (City_Population) qaytaring:
SELECT 'Bektemir' AS district_name, Bektemir AS population, year FROM Population_Each_City
UNION ALL
SELECT 'Chilonzor', Chilonzor, year FROM Population_Each_City
UNION ALL
SELECT 'Yakkasaroy', Yakkasaroy, year FROM Population_Each_City;
