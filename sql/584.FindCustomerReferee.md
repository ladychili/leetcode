# 584.\(Easy\) Find Customer Referee

Write a query to return the list of customers **NOT** referred by the person with id '2'.   
Include those has no referee.

```text
customer
+------+------+-----------+
| id   | name | referee_id|
+------+------+-----------+
|    1 | Will |      NULL |
|    2 | Jane |      NULL |
|    3 | Alex |         2 |
|    4 | Bill |      NULL |
|    5 | Zack |         1 |
|    6 | Mark |         2 |
+------+------+-----------+

output
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
```

```sql
SELECT name
FROM customer
WHERE referee_id IS NULL OR
      referee_id <> 2
```

