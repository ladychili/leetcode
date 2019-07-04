# 185. 部门工资前三高的员工（困难）



#### Step 1 选出整体的top 3薪水

意味着对于选出的salary，比它大的**不超过3个**

```sql
SELECT 
    e1.Salary
FROM 
    Employee e1
WHERE 3 > (SELECT
                COUNT(DISTINCT e2.Salary)
           FROM 
                Employee e2
           WHERE
                e2.Salary > e1.Salary)
```

这里如果把line 5的 `3 >` 换成

* n &gt; , 相当于 top n
* n = , 相当于 第 n + 1

 

#### Step 2 结合部门信息的top 3

```sql
SELECT 
    d.Name Department,
    e1.Name Employee,
    e1.Salary Salary
FROM 
    Employee e1 INNER JOIN Department d
    ON e1.DepartmentId = d.Id           
WHERE 3 > (SELECT
               COUNT(DISTINCT e2.Salary)
           FROM
               Employee e2
           WHERE
               e1.Salary < e2.Salary AND
               e1.DepartmentID = e2.DepartmentId) -- 对应上部门信息（选取部门内top 3）
```

