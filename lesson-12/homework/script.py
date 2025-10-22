1. Ikkita jadvalni birlashtirish (LEFT JOIN)

Vazifa: Person jadvalidagi har bir insonning ismi, familiyasi va manzili (Address jadvalidan) chiqarilsin. Manzil yo‘q bo‘lsa, NULL chiqsin.

SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId
ORDER BY p.personId;


Izoh: LEFT JOIN bilan Person jadvalidagi barcha yozuvlar olinadi, Address jadvalidan mos keladigan manzillar qo‘shiladi, agar bo‘lmasa NULL.

2. Menejerlaridan ko‘p maosh oladigan xodimlar

Vazifa: Employee jadvalidan o‘z menejeridan ko‘p maosh oladigan xodimlarni toping.

SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;


Izoh: Employee jadvalidan o‘zini menejer sifatida ko‘rsatadigan xodimni JOIN qilamiz va maoshlarni solishtiramiz.

3. Takroriy email manzillarni topish

Vazifa: Person jadvalidan takrorlanuvchi email manzillarni toping.

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;


Izoh: GROUP BY va HAVING yordamida bir nechta marta uchragan email'lar chiqariladi.

4. Takroriy email manzillarni o‘chirish (faqat eng kichik id saqlansin)

Vazifa: Person jadvalidan takroriy email manzillarni o‘chiring, faqat eng kichik id qoldiring.

DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);


Izoh: Har bir email uchun eng kichik id qoldiriladi, qolganlari o‘chiriladi.

5. Faqat qiz farzandlari bor ota-onalar

Vazifa: Faqat qizlari bor ota-onalar ismini toping. Ya'ni, bu ota-onalarning hech qachon o‘g‘il farzandi bo‘lmagan.

SELECT DISTINCT g.ParentName
FROM girls g
WHERE g.ParentName NOT IN (
    SELECT b.ParentName FROM boys b
);


Izoh: girls jadvalidan barcha ota-onalar olinadi, lekin boys jadvalidagi ota-onalar bundan chiqarib tashlanadi.

6. 50 dan og‘ir buyurtmalar uchun jami summa va eng kichik vazn

Vazifa: 50 dan og‘ir buyurtmalar bo‘yicha har bir mijoz uchun jami summani va eng kichik buyurtma vaznini toping. (TSQL2012 Sales.Orders jadvali)

SELECT 
    customer_id,
    SUM(total_due) AS TotalSales,
    MIN(weight) AS LeastWeight
FROM Sales.Orders
WHERE weight > 50
GROUP BY customer_id;


Izoh: Shartga mos kelgan buyurtmalar bo‘yicha guruhlab, summa va minimal vazn olinadi.

7. Savatdagi mahsulotlarni birlashtirish (FULL OUTER JOIN)

Vazifa: Cart1 va Cart2 jadvallaridagi mahsulotlarni birlashtiring, har ikkala jadvallarda bo‘lsa yonma-yon ko‘rsating.

SELECT
    c1.Item AS [Item Cart 1],
    c2.Item AS [Item Cart 2]
FROM Cart1 c1
FULL OUTER JOIN Cart2 c2 ON c1.Item = c2.Item
ORDER BY
    COALESCE(c1.Item, c2.Item);


Izoh: FULL OUTER JOIN ikkala jadvaldagi barcha elementlarni to‘liq qamrab oladi.

8. Hech qachon buyurtma qilmagan mijozlar

Vazifa: Customers jadvalidan hech qachon buyurtma qilmagan mijozlarni toping.

SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;


Izoh: LEFT JOIN va NULL filtri yordamida buyurtmasi bo‘lmagan mijozlar aniqlanadi.

9. Talaba va fanlar bo‘yicha imtihonlar soni

Vazifa: Har bir talaba va har bir fan bo‘yicha u imtihonga necha marta kirganini chiqaring.
Agar imtihonga kirmagan bo‘lsa, 0 chiqsin.

SELECT 
    s.student_id,
    s.student_name,
    subj.subject_name,
    COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects subj
LEFT JOIN Examinations e ON s.student_id = e.student_id AND subj.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, subj.subject_name
ORDER BY s.student_id, subj.subject_name;
