1. "100-Steven King" formatida chiqish (emp_id + first_name + last_name)
SELECT 
    CAST(emp_id AS VARCHAR) + '-' + first_name + ' ' + last_name AS EmployeeInfo
FROM employees;


Izoh:
emp_id raqamni VARCHAR ga o‘zgartirib, '100-Steven King' ko‘rinishida bog‘laymiz.

2. employees jadvalidagi phone_number ichidagi '124' ni '999' ga almashtirish
UPDATE employees
SET phone_number = REPLACE(phone_number, '124', '999');


Izoh:
REPLACE funktsiyasi yordamida telefon raqam ichidagi '124' qismi '999' ga o‘zgartiriladi.

3. Ismi 'A', 'J' yoki 'M' bilan boshlanuvchi xodimlarning ismi va ismining uzunligini chiqarish
SELECT 
    first_name AS FirstName,
    LEN(first_name) AS NameLength
FROM employees
WHERE LEFT(first_name, 1) IN ('A', 'J', 'M')
ORDER BY first_name;


Izoh:
LEFT yordamida ismining birinchi harfi tekshiriladi. LEN ismining uzunligini beradi.

4. Har bir menejer uchun jami maoshni topish
SELECT 
    manager_id,
    SUM(salary) AS TotalSalary
FROM employees
GROUP BY manager_id;


Izoh:
manager_id bo‘yicha guruhlab, salary summasi hisoblanadi.

5. TestMax jadvalidan har bir qatorda yildan tashqari Max1, Max2, Max3 ustunlaridan eng kattasini topish
SELECT
    year,
    (SELECT MAX(val)
     FROM (VALUES (Max1), (Max2), (Max3)) AS value(val)) AS HighestValue
FROM TestMax;


Izoh:
VALUES orqali har bir ustun qiymatlari qator sifatida olinib, MAX yordamida eng kattasi topiladi.

6. Kino jadvalidan (cinema) id juft emas va description boring emas bo‘lgan kinolar
SELECT *
FROM cinema
WHERE id % 2 = 1 AND description NOT LIKE '%boring%';


Izoh:
id % 2 = 1 — toq sonlarni oladi, NOT LIKE orqali boring so‘zi yo‘qligi tekshiriladi.

7. Id bo‘yicha saralash, lekin id = 0 doimo oxirida bo‘lsin
SELECT *
FROM SingleOrder
ORDER BY CASE WHEN id = 0 THEN 1 ELSE 0 END, id;


Izoh:
CASE yordamida id=0 bo‘lganlar alohida guruhga olinadi va oxirida chiqadi.

8. Person jadvalidan birinchi null bo‘lmagan ustunni olish
SELECT 
    COALESCE(column1, column2, column3, ...) AS FirstNonNullValue
FROM person;


Izoh:
COALESCE birinchi NULL bo‘lmagan qiymatni qaytaradi, hamma NULL bo‘lsa, NULL qaytadi.

Lesson 13: Medium Tasks
1. FullName ni 3 qismga ajratish (Firstname, Middlename, Lastname) (Students jadvali)

Masalan, FullName = 'John Michael Smith'

SELECT 
    FullName,
    PARSENAME(REPLACE(FullName, ' ', '.'), 3) AS FirstName,
    PARSENAME(REPLACE(FullName, ' ', '.'), 2) AS MiddleName,
    PARSENAME(REPLACE(FullName, ' ', '.'), 1) AS LastName
FROM Students;


Izoh:
PARSENAME funksiyasi faqat to‘rt qismga bo‘linadigan nomlar uchun ishlaydi va nuqta bilan bo‘linadi, shuning uchun REPLACE yordamida bo‘shliq . ga almashtiriladi.

Agar FullName tarkibida faqat ikki yoki uch so‘z bo‘lsa, natija shunga mos bo‘ladi.

2. California ga yetkazilgan mijozlarning Texas ga buyurtmalari
SELECT DISTINCT o1.*
FROM Orders o1
JOIN Orders o2 ON o1.customer_id = o2.customer_id
WHERE o2.delivery_state = 'California'
AND o1.delivery_state = 'Texas';


Izoh:
Bir mijozning California ga buyurtmasi bo‘lsa, ularning Texas ga buyurtmalari chiqariladi.

3. Qiymatlarni guruhlab (group concatenate) birlashtirish (DMLTable)
SELECT
    some_column,
    STRING_AGG(value_column, ', ') AS ConcatenatedValues
FROM DMLTable
GROUP BY some_column;


Izoh:
STRING_AGG SQL Server 2017+ versiyasidan boshlab mavjud. Agar eski versiya bo‘lsa, FOR XML PATH usuli ishlatiladi.

4. Ism va familiyani birlashtirib, undagi "a" harfi kamida 3 marta bo‘lgan xodimlarni topish
SELECT *
FROM employees
WHERE LEN(first_name + last_name) - LEN(REPLACE(first_name + last_name, 'a', '')) >= 3;


Izoh:
Harflar sonini topish uchun avval umumiy uzunlikdan a lar olib tashlangan uzunlik ayiriladi.

5. Har bir bo‘limdagi xodimlar soni va 3 yildan ko‘p ishlaganlar foizi
SELECT
    department_id,
    COUNT(*) AS TotalEmployees,
    100.0 * SUM(CASE WHEN DATEDIFF(year, hire_date, GETDATE()) > 3 THEN 1 ELSE 0 END) / COUNT(*) AS PercentMoreThan3Years
FROM employees
GROUP BY department_id;

1. Har bir qatorda o‘z qiymati va oldingi qatorlar qiymatlarining yig‘indisini chiqarish (Students jadvalidan)
SELECT
    student_id,
    value,
    SUM(value) OVER (ORDER BY student_id) AS running_total
FROM
    Students;


Bu yerda SUM() OVER (ORDER BY ...) funktsiyasi qator bo‘yicha yig‘indini hisoblaydi.

2. Tug‘ilgan kunlari bir xil bo‘lgan talabalarni topish (Student jadvalidan)
SELECT
    s1.student_id,
    s1.name,
    s1.birthday
FROM
    Student s1
JOIN
    Student s2 ON s1.birthday = s2.birthday AND s1.student_id <> s2.student_id
GROUP BY
    s1.student_id, s1.name, s1.birthday;


Bu yerda o‘ziga o‘xshash tug‘ilgan kunlari bo‘lgan talabalar juftligi olinadi.

3. Har bir noyob o‘yinchi juftligi uchun ballarni yig‘ish (PlayerScores jadvalidan)
SELECT
    CASE WHEN player_a < player_b THEN player_a ELSE player_b END AS player1,
    CASE WHEN player_a < player_b THEN player_b ELSE player_a END AS player2,
    SUM(score) AS total_score
FROM
    PlayerScores
GROUP BY
    CASE WHEN player_a < player_b THEN player_a ELSE player_b END,
    CASE WHEN player_a < player_b THEN player_b ELSE player_a END;


Bu yerda o‘yinchilar juftligi tartiblangan holda olinib, ballar yig‘iladi.

4. Stringdagi katta harflar, kichik harflar, raqamlar va boshqa belgilarni ajratish
SELECT
    REGEXP_REPLACE('tf56sd#%OqH', '[^A-Z]', '', 'g') AS uppercase_letters,
    REGEXP_REPLACE('tf56sd#%OqH', '[^a-z]', '', 'g') AS lowercase_letters,
    REGEXP_REPLACE('tf56sd#%OqH', '[^0-9]', '', 'g') AS numbers,
    REGEXP_REPLACE('tf56sd#%OqH', '[A-Za-z0-9]', '', 'g') AS other_chars;


Bu yerda REGEXP_REPLACE funksiyasi yordamida kerakli belgilar ajratiladi.

5. Employees jadvalini yaratish va ma'lumot kiritish
CREATE TABLE Employees (
    EMPLOYEE_ID int,
    FIRST_NAME varchar(50),
    LAST_NAME varchar(50),
    EMAIL varchar(255),
    PHONE_NUMBER varchar(50),
    HIRE_DATE date,
    JOB_ID varchar(50),
    SALARY float,
    COMMISSION_PCT float,
    MANAGER_ID int,
    DEPARTMENT_ID int
);

-- Siz berilgan INSERT INTO so'rovlarini bajaring
INSERT INTO Employees VALUES
(100, 'Steven', 'King', 'SKING', '515.123.4567', '1987-06-17', 'AD_PRES', 24000.00, 0.00, 0, 90),
(101, 'Neena', 'Kochhar', 'NKOCHHAR', '515.123.4568', '1987-06-18', 'AD_VP', 17000.00, 0.00, 100, 90),
-- va boshqalar...
;
