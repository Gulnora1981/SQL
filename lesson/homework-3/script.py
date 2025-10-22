1. BULK INSERT nima va nima uchun ishlatiladi?

🔹 BULK INSERT — bu SQL Server buyruq bo‘lib, tashqi fayldan (odatda .txt, .csv) ma'lumotlarni jadvalga tezda yuklash uchun ishlatiladi.

2. SQL Server’ga import qilish mumkin bo‘lgan 4 ta fayl formati:

.txt

.csv

.xls / .xlsx

.xml

3. Products jadvalini yaratish:
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10,2)
);
4. Products jadvaliga 3 ta yozuv qo‘shish:
INSERT INTO Products VALUES (1, 'Laptop', 1200.00);
INSERT INTO Products VALUES (2, 'Mouse', 25.50);
INSERT INTO Products VALUES (3, 'Keyboard', 40.00);

5. NULL va NOT NULL o‘rtasidagi farq:
NULL	NOT NULL
Qiymat yo‘qligini bildiradi	Qiymat bo‘lishi majburiy
Default qiymat bo‘lishi mumkin	Har doim qiymat berilishi kerak

6. ProductName ustuniga UNIQUE cheklov qo‘shish:
ALTER TABLE Products 
ADD CONSTRAINT UQ_ProductName UNIQUE(ProductName);

7. Komment yozish:
-- Ushbu so‘rov Products jadvalidan barcha ma’lumotlarni olib keladi
SELECT * FROM Products;

8. Products jadvaliga CategoryID ustuni qo‘shish:
ALTER TABLE Products 
ADD CategoryID INT;

9. Categories jadvalini yaratish:
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(50) UNIQUE
);

10. IDENTITY ustuni nima uchun kerak?

IDENTITY — bu SQL Server’ga har bir yangi qator uchun avtomatik tarzda tartib raqam (ID) berishni aytadi. Masalan: IDENTITY(1,1) boshlanishi 1, har safar 1 ga oshadi.

O‘rta darajadagi topshiriqlar (10 ta)
1. BULK INSERT orqali .txt fayldan ma’lumot yuklash:
BULK INSERT Products
FROM 'C:\data\products.txt'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);


Izoh: Fayl yo‘li mos ravishda sizning kompyuteringizga qarab o‘zgartiriladi.

2. Products jadvaliga FOREIGN KEY qo‘shish:
ALTER TABLE Products
ADD CONSTRAINT FK_Products_Categories
FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID);

3. PRIMARY KEY va UNIQUE KEY farqlari:
PRIMARY KEY	UNIQUE KEY
Bitta ustun yoki kombinatsiyada bo‘ladi	Bir nechta UNIQUE bo‘lishi mumkin
NULL qabul qilmaydi	1 ta NULL qabul qiladi
Jadvalni noyob identifikatsiya qiladi	Faqat noyob qiymatni ta’minlaydi
4. CHECK constraint bilan narx > 0 bo‘lishini tekshirish:
ALTER TABLE Products
ADD CONSTRAINT CHK_Price_Positive CHECK (Price > 0);

5. Products jadvaliga Stock ustunini qo‘shish (NOT NULL):
ALTER TABLE Products
ADD Stock INT NOT NULL DEFAULT 0;

6. ISNULL yordamida NULL qiymatni 0 ga almashtirish:
SELECT ProductID, ProductName, ISNULL(Price, 0) AS Price
FROM Products;

7. FOREIGN KEY cheklovi nima?

FOREIGN KEY — bu bir jadvaldagi ustunni boshqa jadvaldagi PRIMARY KEY yoki UNIQUE ustun bilan bog‘lab, ma’lumotlar yaxlitligini ta’minlaydi.

Murakkab darajadagi topshiriqlar (10 ta)
1. Customers jadvali, CHECK bilan Age ≥ 18:
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FullName VARCHAR(100),
    Age INT CHECK (Age >= 18)
);

2. IDENTITY bilan jadval yaratish (100 dan boshlanadi, 10 ga oshadi):
CREATE TABLE Orders (
    OrderID INT IDENTITY(100,10) PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT
);

3. OrderDetails jadvalida kompozit PRIMARY KEY yaratish:
CREATE TABLE OrderDetails (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID)
);

4. COALESCE va ISNULL funksiyalari farqi:
Funksiya	Tavsifi
ISNULL(value, default)	1 ta qiymatni tekshiradi, agar NULL bo‘lsa, defaultni qaytaradi
COALESCE(val1, val2, ...)	Bir nechta qiymatdan birinchi NULL bo‘lmagan qiymatni qaytaradi

Misol:

SELECT ISNULL(NULL, 'A')       -- Natija: 'A'
SELECT COALESCE(NULL, NULL, 'B') -- Natija: 'B'

5. Employees jadvali: PRIMARY KEY (EmpID), UNIQUE (Email):
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    FullName VARCHAR(100),
    Email VARCHAR(100) UNIQUE
);

6. FOREIGN KEY yaratish ON DELETE CASCADE va ON UPDATE CASCADE bilan:
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
