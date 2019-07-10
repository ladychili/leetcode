# 577.\(Easy\) Employee Bonus

```text
Employee

+-------+--------+-----------+--------+
| empId |  name  | supervisor| salary |
+-------+--------+-----------+--------+
|   1   | John   |  3        | 1000   |
|   2   | Dan    |  3        | 2000   |
|   3   | Brad   |  null     | 4000   |
|   4   | Thomas |  3        | 4000   |
+-------+--------+-----------+--------+

Bonus

+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+

output
+-------+-------+
| name  | bonus |
+-------+-------+
| John  | null  |
| Dan   | 500   |
| Brad  | null  |
+-------+-------+
```

```sql
SELECT
    e.name,
    b.bonus
FROM
    Employee e LEFT JOIN Bonus b ON
    e.empid = b.empid
WHERE
    b.bonus < 1000 OR 
    b.bonus IS NULL
```

