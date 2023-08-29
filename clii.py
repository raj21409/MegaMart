from database import read_query
from database import result_query
from database import create_db_connection
from database import create_server_connection
from database import connection

def main():
    choice=0
    while(choice!=3):
        print("***Welcome to our Online retail store-MEGAMART***")
        print("1)log in")
        print("2)Sign up")
        print("3) exit")
        choice=int(input())
        if(choice==1):
            x=input("Enter the username>>")
            y=input("Enter the password>>")
            print("logged in succesfully")
        if(choice==2):
            x=input("Enter the username>>")
            y=input("Enter the password>>")
            print("signed in succesfully")  
        z=0    
        while(z!=8):
            print("***Welcome to the Homepage of Megamart***")
            print()
            print("1)show the top  customer on our website on the basis of purchase value")
            print("2)Top selling products in descending order")
            print()
            print("OLAP Queries" )
            print("3)Total number of orders placed by each user, grouped by month and year")
            print("4)Sales volume by state")
            print("5)Total revenue of all orders by a particular user")
            print("6)TOTAL REVENUE IN A YEAR IN A PARTICULAR MONTH")
            print()
            print("Triggers")
            print("7)Apply triggers to the database")
            print("8) exit")      
            z=int(input())
            
            if(z==1):
                connection=create_db_connection("localhost","root","1102","megamart")
                q1="""
                    SELECT c.uder_id, SUM(p.product_price*p.Cart_Quantity) AS TotalValue
                    FROM user1 c
                    JOIN order_1 o ON c.uder_id = o.uder_id
                    JOIN contains co ON o.order_id = co.order_id
                    JOIN product p ON co.product_id = p.product_id
                    GROUP BY c.uder_id
                    ORDER BY TotalValue DESC
                    LIMIT 1;"""
                print()
                print()
                print("[User_id, total_value]")
                result_query(connection,q1)
                print()
                print()
            if(z==2):
                connection=create_db_connection("localhost","root","1102","megamart")
                q2="""
                    SELECT p.product_id, SUM(p.cart_quantity) AS total_quantity
                    FROM product p
                    JOIN contains oi ON p.product_id = oi.product_id
                    GROUP BY p.product_id
                    ORDER BY total_quantity DESC;
                    """
                print()
                print()
                print("[product_id, total_sales]")
                result_query(connection,q2)
                print()
                print() 
            if(z==3):
                connection=create_db_connection("localhost","root","1102","megamart")
                q3="""
                    SELECT YEAR(o.order_date) AS year, MONTH(o.order_date) AS month, u.username, COUNT(o.order_id) AS Order_quantity
                    FROM order_1 o
                    INNER JOIN user1 u ON o.uder_id = u.uder_id
                    GROUP BY YEAR(o.order_date), MONTH(o.order_date), u.username WITH ROLLUP;
                    """
                print()
                print()
                print("[year, month, username, Order_quantity]")
                result_query(connection,q3)
                print()
                print() 
            if(z==4):
                
                connection=create_db_connection("localhost","root","1102","megamart")
                q4="""
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
                    """
                print()
                print()
                print("[product_id, states, Sales volume]")
                result_query(connection,q4)
                print()
                print()
            if(z==5):
                connection=create_db_connection("localhost","root","1102","megamart")
                q5="""
                    SELECT 
                        u.username, 
                        SUM(o.order_price) AS Total_Revenue
                    FROM 
                        user1 u
                        JOIN order_1 o ON u.uder_id = o.uder_id
                    GROUP BY 
                        u.username WITH ROLLUP;
    
                    """
                print()
                print()
                print("[username, total_revenue]")
                result_query(connection,q5)
                print()
                print() 
            if(z==6):
                connection=create_db_connection("localhost","root","1102","megamart")
                q6="""
                    SELECT 
                        YEAR(o.order_date) AS year, 
                        MONTH(o.order_date) AS month, 
                        SUM(o.order_price) AS Total_Revenue
                    FROM 
                        order_1 o
                    GROUP BY 
                        YEAR(o.order_date), MONTH(o.order_date) WITH ROLLUP;
    
                    """
                print()
                print()
                print("[Year, Month, total_revenue]")
                result_query(connection,q6)
                print()
                print() 
            if(z==7):
                l=0
                while(l!=3):
            
                    print("1)a trigger to check if a customer with the same email address already exists in the database")
                    print("2)a trigger to prevent the deletion of a customer record if the customer has pending orders")
                    print("3) exit")
                    l=int(input())  
                    if(l==1):
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q7=""" 
                            
                            CREATE TRIGGER `check_customer_email_exists` 
                            BEFORE INSERT ON `user1` 
                            FOR EACH ROW 
                            BEGIN
                                IF (SELECT COUNT(*) FROM `user1` WHERE `email` = NEW.email) > 0 
                                THEN
                                    SIGNAL SQLSTATE '45000' 
                                    SET MESSAGE_TEXT = 'A customer with this email already exists.';
                                END IF;
                            END
                           
                        """
                        print()
                        print("Trigger created")
                        read_query(connection,q7)
                        print()
                        print() 
                    if(l==2):
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q8="""
                            CREATE TRIGGER `prevent_customer_deletion1` 
                            BEFORE DELETE ON `user1` 
                            FOR EACH ROW 
                            BEGIN
                                IF (SELECT COUNT(*) FROM `order_1` WHERE `uder_id` = OLD.uder_id AND `Order_Status` = 0) > 0 
                                THEN
                                    SIGNAL SQLSTATE '45000' 
                                    SET MESSAGE_TEXT = 'This customer has pending orders and cannot be deleted.';
                                END IF;
                            END
                            
                        """
                        print()
                        print("Trigger created")
                        read_query(connection,q8)
                        print()
                        print() 



if __name__=="__main__":
    main()
