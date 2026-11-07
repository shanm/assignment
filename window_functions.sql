SELECT name, department, salary, ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_number FROM employees 

SELECT name, department, salary, RANK() OVER (ORDER BY salary DESC) as rank from employees

SELECT name, department, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as dense_salary FROM employees

SELECT name, department, salary, ROW_NUMBER() OVER(PARTITION BY department ORDER BY salary DESC) AS row_number
FROM employees;