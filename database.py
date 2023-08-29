
from decimal import Decimal
import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name,user_name,user_password):
    connection=None
    try:
        connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_password)
        print("MYSQL Database connection successful")

    except Error as err:
        print(f"Error: '{err}'")
    return connection 

pw="1102"


def create_db_connection(host_name,user_name,user_password,db_name):
    connectioin=None
    try:
        connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_password,database=db_name)
        print("MySql database connection successfull ")

    except Error as err:
        print(f"Error:'{err}'")
    return connection

connection=create_db_connection("localhost","root",pw,"megamart")

def read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        connection.commit()
        result=cursor.fetchall()
        return result
    except Error as err:
        print(f"Error:'{err}'")

def result_query(connection,query):
    z=read_query(connection,query)
    output = []
    for row in z:
        row_data = []
        for data in row:
            # if type(data) is Decimal:
                # row_data.append(float(data))
            # if:
                row_data.append(str(data))
        output.append(row_data)       
    for q in output:        
        print(q)
        print()

#query1--show the top  customer on our website on the basis of purchase value
# q1="""
# SELECT c.uder_id, SUM(p.product_price*p.Cart_Quantity) AS TotalValue
# FROM user1 c
# JOIN order_1 o ON c.uder_id = o.uder_id
# JOIN contains co ON o.order_id = co.order_id
# JOIN product p ON co.product_id = p.product_id
# GROUP BY c.uder_id
# ORDER BY TotalValue DESC
# LIMIT 1;"""

#query2 --Top selling products in descending order
# q2="""
# SELECT p.product_id, SUM(p.cart_quantity) AS total_quantity
# FROM product p
# JOIN contains oi ON p.product_id = oi.product_id
# GROUP BY p.product_id
# ORDER BY total_quantity DESC;
# """

#result_query(connection,q1)
# result_query(connection,q2)
