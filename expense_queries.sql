CREATE DATABASE expense_tracker;
USE expense_tracker;

CREATE TABLE expenses (
    Date DATE,
    Category VARCHAR(50),
    Description VARCHAR(100),
    Amount INT,
    Payment_Mode VARCHAR(20),
    Budget INT
);

INSERT INTO expenses VALUES
('2024-01-05','Food','Lunch',150,'Cash',3000),
('2024-01-07','Transport','Bus Pass',500,'UPI',1500),
('2024-01-10','Shopping','Clothes',1200,'Card',2500),
('2024-01-15','Food','Dinner',300,'Cash',3000),
('2024-02-02','Entertainment','Movie',400,'UPI',1000),
('2024-02-05','Food','Grocery',800,'Card',3000),
('2024-02-10','Bills','Electricity Bill',950,'UPI',2000),
('2024-02-18','Transport','Auto',250,'Cash',1500),
('2024-03-01','Food','Snacks',100,'Cash',3000),
('2024-03-05','Shopping','Shoes',2000,'Card',2500);

-- Total Spending
SELECT SUM(Amount) AS Total_Spending
FROM expenses;

-- Category-wise Spending
SELECT Category, SUM(Amount) AS Total_Spent
FROM expenses
GROUP BY Category
ORDER BY Total_Spent DESC;

-- Monthly Spending Trend
SELECT MONTH(Date) AS Month, SUM(Amount) AS Monthly_Spending
FROM expenses
GROUP BY MONTH(Date)
ORDER BY Month;

-- Budget vs Actual
SELECT Category,
    SUM(Amount) AS Total_Spent,
    SUM(Budget) AS Total_Budget,
    SUM(Amount) - SUM(Budget) AS Over_Spend
FROM expenses
GROUP BY Category;

-- Overspending Categories
SELECT Category,
       SUM(Amount) - SUM(Budget) AS Over_Spend
FROM expenses
GROUP BY Category
HAVING Over_Spend > 0;






