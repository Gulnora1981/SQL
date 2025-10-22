1. Kompaniyadagi eng kam maosh oladigan xodimlarni toping

Jadval: employees (id, name, salary)

SELECT *
FROM employees
WHERE salary = (SELECT MIN(salary) FROM employees);

2. O‘rtacha narxdan yuqori bo‘lgan mahsulotlarni toping

Jadval: products (id, product_name, price)

SELECT *
FROM products
WHERE price > (SELECT AVG(price) FROM products);


3. “Sales” bo‘limida ishlovchi xodimlarni toping

Jadvallar:

employees (id, name, department_id)

departments (id, department_name)

SELECT *
FROM employees
WHERE department_id = (
    SELECT id FROM departments WHERE department_name = 'Sales'
);

4. Buyurtma qilmagan mijozlarni toping

Jadvallar:

customers (customer_id, name)

orders (order_id, customer_id)

SELECT *
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id FROM orders
);


5. Har bir kategoriyadagi eng qimmat mahsulotlarni toping

Jadval: products (id, product_name, price, category_id)

SELECT *
FROM products p
WHERE price = (
    SELECT MAX(price)
    FROM products
    WHERE category_id = p.category_id
);

6. O‘rtacha maoshi eng yuqori bo‘lgan bo‘limdagi xodimlarni toping

Jadvallar:

departments (id, department_name)

employees (id, name, salary, department_id)

SELECT *
FROM employees
WHERE department_id = (
    SELECT TOP 1 department_id
    FROM employees
    GROUP BY department_id
    ORDER BY AVG(salary) DESC
);


7. O‘z bo‘limidagi o‘rtacha maoshdan ko‘p oladigan xodimlar

Jadval: employees (id, name, salary, department_id)

SELECT *
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);

8. Har bir kurs bo‘yicha eng yuqori baho olgan talabalarni toping

Jadvallar:

students (student_id, name)

grades (student_id, course_id, grade)

SELECT s.*
FROM students s
WHERE EXISTS (
    SELECT 1
    FROM grades g
    WHERE g.student_id = s.student_id
      AND g.grade = (
          SELECT MAX(grade)
          FROM grades
          WHERE course_id = g.course_id
      )
);


9. Har bir kategoriyada uchinchi eng qimmat mahsulotni toping

Jadval: products (id, product_name, price, category_id)

WITH RankedProducts AS (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY category_id ORDER BY price DESC) AS rnk
    FROM products
)
SELECT *
FROM RankedProducts
WHERE rnk = 3;

10. Maoshi kompaniya o‘rtachasidan yuqori, lekin o‘z bo‘limidagi maksimal maoshdan past bo‘lgan xodimlar

Jadval: employees (id, name, salary, department_id)

SELECT *
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees)
  AND salary < (
      SELECT MAX(salary)
      FROM employees
      WHERE department_id = e.department_id
  );
