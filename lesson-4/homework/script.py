TOP 5 mahsulotlar eng katta savdo summasiga ko‘ra (Sales jadvalidan)
Faraz qilaylik “SaleAmount” — bu har bir sotuv summasi; biz ProductID bo‘yicha guruhlab, umumiy savdo summasini topib, yuqoridan 5 ni olamiz:

SELECT TOP (5)
  p.ProductID,
  p.ProductName,
  SUM(s.SaleAmount) AS TotalSales
FROM Products p
  JOIN Sales s ON p.ProductID = s.ProductID
GROUP BY p.ProductID, p.ProductName
ORDER BY SUM(s.SaleAmount) DESC;


FirstName va LastName ni birlashtirib FullName ustuni yaratish

SELECT
  EmployeeID,
  FirstName + ' ' + LastName AS FullName,
  DepartmentName,
  Salary,
  Age
FROM Employees;


(Agar FirstName yoki LastName NULL bo‘lishi mumkin bo‘lsa, COALESCE bilan ishlatish mumkin:
COALESCE(FirstName, '') + ' ' + COALESCE(LastName, ''))

Distinct ustunlar: Category, ProductName, Price — faqat narxi > 50 bo‘lgan mahsulotlar

SELECT DISTINCT Category, ProductName, Price
FROM Products
WHERE Price > 50;


Price < 10% ga teng bo‘lgan mahsulotlarni olish — ya’ni, narxi < 0.1 * (avg narx)

SELECT *
FROM Products
WHERE Price < (0.1 * (SELECT AVG(Price) FROM Products));


Age < 30 va DepartmentName HR yoki IT bo‘lgan xodimlar

SELECT *
FROM Employees
WHERE Age < 30
  AND DepartmentName IN ('HR', 'IT');


Emailida ‘@gmail.com’ domeni bo‘lgan mijozlar

SELECT *
FROM Customers
WHERE Email LIKE '%@gmail.com%';


ALL operatori bilan: Sales bo‘limidagi barcha xodimlardan yuqori Salary‑ga ega xodimlar
Misol: “xodimlarning maoshi barcha Sales bo‘limidagi xodimlardan katta bo‘lishi”

SELECT *
FROM Employees e
WHERE Salary > ALL (
  SELECT Salary
  FROM Employees
  WHERE DepartmentName = 'Sales'
);


— agar ‘Sales’ bo‘limi mavjud bo‘lsa. Agar bo‘lmasa, bu so‘rov bo‘sh natija beradi.

Orders jadvalidan, oxirgi 180 kun ichida joylashtirilgan buyurtmalarni filtrlash
“Current date”ni olish uchun GETDATE() (agar datetime) yoki CAST(GETDATE() AS DATE) (faqat sana) ishlatiladi.
Faraz qilaylik Orders.OrderDate tipida DATE.

SELECT *
FROM Orders
WHERE OrderDate BETWEEN DATEADD(DAY, -180, CAST(GETDATE() AS DATE))
                    AND CAST(GETDATE() AS DATE);


Agar “LATEST_DATE” ustuni bo‘lsa (masalan Orders jadvalidagi eng katta sanani), unda:

DECLARE @MaxDate DATE;
SELECT @MaxDate = MAX(OrderDate) FROM Orders;

SELECT *
FROM Orders
WHERE OrderDate BETWEEN DATEADD(DAY, -180, @MaxDate)
                    AND @MaxDate;
