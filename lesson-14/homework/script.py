1. Name ustunini vergul bo‘yicha ajratish – TestMultipleColumns

Masalan: Ali,Valiyev → Ali va Valiyev

SELECT 
    Id,
    LTRIM(RTRIM(PARSENAME(REPLACE(Name, ',', '.'), 2))) AS Ismi,
    LTRIM(RTRIM(PARSENAME(REPLACE(Name, ',', '.'), 1))) AS Familiyasi
FROM TestMultipleColumns;

2. Ichida % belgisi bor satrlarni topish – TestPercent
SELECT *
FROM TestPercent
WHERE Strs LIKE '%[%]%';

3. Nuqta bilan ajratilgan satrlarni ajratish – Splitter

Masalan: a.b → a va b

SELECT 
    Id,
    PARSENAME(REPLACE(Vals, '.', '.'), 2) AS Qism1,
    PARSENAME(REPLACE(Vals, '.', '.'), 1) AS Qism2
FROM Splitter;

4. 2 tadan ko‘p nuqtasi bor satrlar – testDots
SELECT *
FROM testDots
WHERE LEN(Vals) - LEN(REPLACE(Vals, '.', '')) > 2;

5. Matndagi bo‘sh joylar (probel) sonini sanash – CountSpaces
SELECT 
    texts,
    LEN(texts) - LEN(REPLACE(texts, ' ', '')) AS ProbellarSoni
FROM CountSpaces;

6. Boshlig‘idan ko‘p maosh oladigan xodimlar – Employee
SELECT E.Name
FROM Employee E
JOIN Employee M ON E.ManagerId = M.Id
WHERE E.Salary > M.Salary;

7. Ish boshlaganiga 10–15 yil bo‘lgan xodimlar – Employees
SELECT 
    EMPLOYEE_ID,
    FIRST_NAME,
    LAST_NAME,
    HIRE_DATE,
    DATEDIFF(YEAR, HIRE_DATE, GETDATE()) AS IshTajribasi
FROM Employees
WHERE DATEDIFF(YEAR, HIRE_DATE, GETDATE()) BETWEEN 10 AND 14;

✅ O‘rtacha darajadagi topshiriqlar
1. Oldingi kundan issiqroq bo‘lgan kunlar – weather
SELECT w1.Id
FROM weather w1
JOIN weather w2 ON DATEDIFF(DAY, w2.RecordDate, w1.RecordDate) = 1
WHERE w1.Temperature > w2.Temperature;

2. Har bir o‘yinchining birinchi kirgan sanasi – Activity
SELECT player_id, MIN(event_date) AS birinchi_kirish
FROM Activity
GROUP BY player_id;

3. Vergul bilan ajratilgan ro‘yxatdan 3-elementni olish – fruits
SELECT 
    LTRIM(RTRIM(value)) AS UchinchiMeva
FROM fruits
CROSS APPLY STRING_SPLIT(fruit_list, ',')
WITH ORDINALITY
WHERE ordinal = 3;

4. Ish tajribasiga qarab darajani ko‘rsatish – Employees
SELECT 
    EMPLOYEE_ID,
    FIRST_NAME,
    LAST_NAME,
    HIRE_DATE,
    DATEDIFF(YEAR, HIRE_DATE, GETDATE()) AS YillikTajriba,
    CASE 
        WHEN DATEDIFF(YEAR, HIRE_DATE, GETDATE()) < 1 THEN 'Yangi'
        WHEN DATEDIFF(YEAR, HIRE_DATE, GETDATE()) BETWEEN 1 AND 5 THEN 'Junior'
        WHEN DATEDIFF(YEAR, HIRE_DATE, GETDATE()) BETWEEN 6 AND 10 THEN 'Mid'
        WHEN DATEDIFF(YEAR, HIRE_DATE, GETDATE()) BETWEEN 11 AND 20 THEN 'Senior'
        ELSE 'Katta Tajribali'
    END AS Darajasi
FROM Employees;

5. Satrdagi boshidagi sonlarni ajratish – GetIntegers
SELECT 
    Id,
    VALS,
    LEFT(VALS, PATINDEX('%[^0-9]%', VALS + 'X') - 1) AS BoshiSon
FROM GetIntegers
WHERE VALS LIKE '[0-9]%';

✅ Qiyin darajadagi topshiriqlar
1. CSV satrida 1-va 2-elementni joyini almashtirish – MultipleVals
SELECT 
    Id,
    STUFF(STUFF(Vals, 1, 1, SUBSTRING(Vals, CHARINDEX(',', Vals) + 1, 1)),
                CHARINDEX(',', Vals) + 1, 1, LEFT(Vals, 1)) AS Almashtirilgan
FROM MultipleVals;

2. Har bir belgini alohida qatorga chiqarish
DECLARE @str VARCHAR(MAX) = 'sdgfhsdgfhs@121313131';

WITH Numbers AS (
    SELECT TOP (LEN(@str))
        ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_objects
)
SELECT SUBSTRING(@str, n, 1) AS Belgilar
FROM Numbers;

3. Har bir o‘yinchining birinchi kirgan qurilmasi – Activity
SELECT a.player_id, a.device_id
FROM Activity a
JOIN (
    SELECT player_id, MIN(event_date) AS birinchi_kun
    FROM Activity
    GROUP BY player_id
) b ON a.player_id = b.player_id AND a.event_date = b.birinchi_kun;

4. Satrni raqamlar va harflarga ajratish – Masalan: rtcfvty34redt
DECLARE @str VARCHAR(100) = 'rtcfvty34redt';

WITH Numbers AS (
    SELECT TOP (LEN(@str))
        ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_objects
)
SELECT
    STRING_AGG(CASE WHEN SUBSTRING(@str, n, 1) LIKE '[0-9]' THEN SUBSTRING(@str, n, 1) END, '') AS Raqamlar,
    STRING_AGG(CASE WHEN SUBSTRING(@str, n, 1) LIKE '[A-Za-z]' THEN SUBSTRING(@str, n, 1) END, '') AS Harflar
FROM Numbers;
