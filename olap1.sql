# 1.TOTAL REVENUE IN A YEAR IN A PARTICULAR MONTH
SELECT 
    YEAR(o.order_date) AS year, 
    MONTH(o.order_date) AS month, 
    SUM(o.order_price) AS Total_Revenue
FROM 
    order_1 o
GROUP BY 
    YEAR(o.order_date), MONTH(o.order_date) WITH ROLLUP;

#  2.Total revenue of all orders by a particular user
SELECT 
    u.username, 
    SUM(o.order_price) AS Total_Revenue
FROM 
    user1 u
    JOIN order_1 o ON u.uder_id = o.uder_id
GROUP BY 
    u.username WITH ROLLUP;
    
    ---
# 3. SAle VOLUME 
SELECT 
    product.product_id,
    user1.state,
    COUNT(contains.product_id) AS Sales_Volume
FROM 
    contains 
    INNER JOIN product ON contains.product_id = product.product_id
    INNER JOIN order_1 ON contains.order_id = order_1.order_id
    INNER JOIN user1 ON product.uder_id = user1.uder_id
GROUP BY 
    product.product_id, 
    user1.state
WITH ROLLUP;

# Total number of orders placed by each user, grouped by month and year
SELECT YEAR(o.order_date) AS year, MONTH(o.order_date) AS month, u.username, COUNT(o.order_id) AS Order_quantity
FROM order_1 o
INNER JOIN user1 u ON o.uder_id = u.uder_id
GROUP BY YEAR(o.order_date), MONTH(o.order_date), u.username WITH ROLLUP;
