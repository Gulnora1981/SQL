Puzzle 1: Ikkita ustun bo‘yicha takrorlanmas qiymatlarni topish

Masala: InputTbl jadvalidagi col1 va col2 ustunlari bo‘yicha kombinatsiyalarni ko‘rib chiqamiz. (a,b) va (b,a) bir xil deb hisoblanadi. Shuning uchun bu qiymatlarni tartiblab, takrorlanmas qilib olish kerak.

Yechim 1: LEAST/GREATEST funksiyasi o‘rniga CASE ishlatish
SELECT 
    CASE 
        WHEN col1 < col2 THEN col1 
        ELSE col2 
    END AS col1,
    CASE 
        WHEN col1 < col2 THEN col2 
        ELSE col1 
    END AS col2
FROM InputTbl
GROUP BY 
    CASE WHEN col1 < col2 THEN col1 ELSE col2 END,
    CASE WHEN col1 < col2 THEN col2 ELSE col1 END;

Yechim 2: CONCAT orqali alohida STRING qilib, so‘ngra ajratish
SELECT 
    LEFT(pair, CHARINDEX('-', pair) - 1) AS col1,
    RIGHT(pair, LEN(pair) - CHARINDEX('-', pair)) AS col2
FROM (
    SELECT DISTINCT 
        CASE 
            WHEN col1 < col2 THEN col1 + '-' + col2 
            ELSE col2 + '-' + col1 
        END AS pair
    FROM InputTbl
) AS Sub;

Puzzle 2: Nol bo‘lgan barcha ustunlar mavjud bo‘lgan qatorlarni olib tashlash
SELECT * 
FROM TestMultipleZero
WHERE NOT (ISNULL(A, 0) = 0 AND ISNULL(B, 0) = 0 AND ISNULL(C, 0) = 0 AND ISNULL(D, 0) = 0);


Izoh: Har bir ustun 0 bo‘lsa — qator o‘chirib yuboriladi.

Puzzle 3: Faqat toq id raqamli insonlarni chiqarish
SELECT * FROM section1
WHERE id % 2 = 1;

Puzzle 4: Eng kichik id ga ega bo‘lgan odam
SELECT TOP 1 * FROM section1
ORDER BY id ASC;

Puzzle 5: Eng katta id ga ega bo‘lgan odam
SELECT TOP 1 * FROM section1
ORDER BY id DESC;

Puzzle 6: Ismi b harfi bilan boshlanadigan insonlar (katta-kichik farqsiz)
SELECT * FROM section1
WHERE name LIKE 'b%';


SQL Server defaultda case-insensitive, ya’ni B% ham, b% ham ishlaydi.

Puzzle 7: Underscore _ belgisi bor kodlarni chiqarish (wildcard emas, literal sifatida)
SELECT * FROM ProductCodes
WHERE Code LIKE '%\_%' ESCAPE '\';
