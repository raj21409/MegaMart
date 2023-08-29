from database import read_query
from database import read_query1
from database import read_query2
from database import read_query3
from database import result_query
from database import create_db_connection
from database import create_server_connection
from database import connection
from datetime import datetime


from decimal import Decimal
import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name,user_name,user_password):
    connection=None
    try:
        connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_password)
        #print("MYSQL Database connection successful")

    except Error as err:
        print(f"Error: '{err}'")
    return connection 

pw="1102"


def create_db_connection(host_name,user_name,user_password,db_name):
    connectioin=None
    try:
        connection=mysql.connector.connect(host=host_name,user=user_name,passwd=user_password,database=db_name)
       # print("MySql database connection successfull ")

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
        print(f"")

def read_query1(connection,query):
    cursor=connection.cursor()
    
    cursor.execute(query)
    # connection.commit()
    result=cursor.fetchall()
    
    for row in result:
        print(row)
        print("\n")
   
def read_query2(connection,query):
    cursor=connection.cursor()
    
    cursor.execute(query)
    result=cursor.fetchall()
    return result

def read_query3(connection,query):
    cursor=connection.cursor()
    
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result

def read_query4(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        for _ in cursor.execute(query, multi=True): pass
        connection.commit()
        result=cursor.fetchall()
        return result
    except Error as err:
        print("")

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

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d')

print("********************************************************************************")
print("                              Welcome to MEAGAMART")
print("********************************************************************************")
print("\n")
print("\n")
i0=0
while i0!=3:
    print("1)Enter as a admin")
    print("2)Enter as a user")
    print("3)exit")
    i0=int(input())
    i1=0
    if i0==1:
        while i1!=3:
    
            print("1)Sign up")
            print("2)Login")
            print("3)exit")
            i1=int(input())
            
            
            if i1==1:
                print("Enter the username=")
                admin_username=input()
                print("Enter the password=")
                admin_pass=input()
                connection=create_db_connection("localhost","root","1102","megamart")
                q1=f"""INSERT INTO admin_1(user_name, user_Password) VALUES {admin_username, admin_pass}"""
                print()
                read_query(connection,q1)
                connection=create_db_connection("localhost","root","1102","megamart")
                q1=f"""select admin_id from admin_1 where user_name='{admin_username}'"""
                cursor=connection.cursor()
                cursor.execute(q1)
                result=cursor.fetchall()
                print(f"your admin id is {result[0][0]}")
                print()
                print("registered!!")

                i2=0
                while i2 != 7:
                    print("Welcome " + admin_username)
                    print("1) Add category")
                    print("2) Delete category")
                    print("3) Add Product")
                    print("4) Delete Product")
                    print("5) Updating product price")
                    print("6) Updating product quantity")
                    print("7) Back")
                    i2=int(input())
                    if i2==1:
                        print("Enter the category id=")
                        cat_id=int(input())
                        print("Enter the category name=")
                        cat_name=input()
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q3=f"""INSERT INTO product_category(category_id, category_name)  VALUES {cat_id, cat_name};"""
                        print()
                        read_query(connection,q3)
                        print("category succesfully added !")
                    if i2==2:
                        print("Enter the category id=")
                        cat1_id=int(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q4=f"""DELETE from product_category WHERE category_id={cat1_id} """
                        print()
                        read_query(connection,q4)
                        print("category succesfully deleted !")
                    if i2==3:
                        print("Enter the product price=")
                        prod_price=int(input())
                        print("Enter the product info=")
                        prod_info=input()
                        print("Enter the cart quantity=")
                        qty=int(input())
                        print("Enter the product status=")
                        stat=bool(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q2=f"""INSERT INTO product(product_price, product_info, Cart_Quantity, uder_id, product_status)  Values {prod_price, prod_info, qty,12, stat};"""
                        print()
                        read_query(connection,q2)
                        print("Product succesfully added !")
                        
                    if i2==4:
                        print("Enter the product id=")
                        prod1_id=int(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q5=f"""DELETE from product WHERE product_id={prod1_id} """
                        print()
                        read_query(connection,q5)
                        print("product succesfully deleted !")
                    if i2==5:
                        print("Enter the product id=")
                        prod2_id=int(input())
                        print("Enter the updated price=")
                        prod1_price=int(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q6=f"""UPDATE product SET product_price={prod1_price} WHERE product_id={prod2_id} """
                        print()
                        read_query(connection,q6)
                        print("price succesfully updated !")
                    if i2==6:
                        print("Enter the product id=")
                        prod3_id=int(input())
                        print("Enter the updated quantity=")
                        qty1=int(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q7=f"""UPDATE product SET Cart_Quantity={qty1} WHERE product_id={prod3_id} """
                        print()
                        read_query(connection,q7)
                        print("quantity succesfully updated !")


            
            if i1==2:
                print("Enter the admin id=")
                admin_id1=int(input())
                print("Enter the password=")
                admin_pass1=input()
                q15=f"""SELECT * FROM admin_1 WHERE admin_id = {admin_id1} AND user_password = '{admin_pass1}'"""
                x=read_query2(connection,q15)
                if not x:
                    print("Wrong details entered!")

                else:
                    q2=2
                    print("Logged in Succesfully!")

                i2=0
                while i2 != 7:
                    print("Welcome ")
                    print("1) Add category")
                    print("2) Delete category")
                    print("3) Add Product")
                    print("4) Delete Product")
                    print("5) Updating product price")
                    print("6) Updating product quantity")
                    print("7) Back")
                    i2=int(input())
                    if i2==1:
                        print("Enter the category id=")
                        cat_id=int(input())
                        print("Enter the category name=")
                        cat_name=input()
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q3=f"""INSERT INTO product_category(category_id, category_name)  VALUES {cat_id, cat_name};"""
                        print()
                        read_query(connection,q3)
                        print("category succesfully added !")
                    if i2==2:
                        print("Enter the category id=")
                        cat1_id=int(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q4=f"""DELETE from product_category WHERE category_id={cat1_id} """
                        print()
                        read_query(connection,q4)
                        print("category succesfully deleted !")
                    if i2==3:
                        print("Enter the product price=")
                        prod_price=int(input())
                        print("Enter the product info=")
                        prod_info=input()
                        print("Enter the cart quantity=")
                        qty=int(input())
                        print("Enter the product status=")
                        stat=bool(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q2=f"""INSERT INTO product(product_price, product_info, Cart_Quantity, uder_id, product_status)  Values {prod_price, prod_info, qty,12, stat};"""
                        print()
                        read_query(connection,q2)
                        print("Product succesfully added !")
                    
                    if i2==4:
                        print("Enter the product id=")
                        prod1_id=int(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q5=f"""DELETE from product WHERE product_id={prod1_id} """
                        print()
                        read_query(connection,q5)
                        print("product succesfully deleted !")
                    if i2==5:
                        print("Enter the product id=")
                        prod2_id=int(input())
                        print("Enter the updated price=")
                        prod1_price=int(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q6=f"""UPDATE product SET product_price={prod1_price} WHERE product_id={prod2_id} """
                        print()
                        read_query(connection,q6)
                        print("price succesfully updated !")
                    if i2==6:
                        print("Enter the product id=")
                        prod3_id=int(input())
                        print("Enter the updated quantity=")
                        qty1=int(input())
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q7=f"""UPDATE product SET Cart_Quantity={qty1} WHERE product_id={prod3_id} """
                        print()
                        read_query(connection,q7)
                        print("quantity succesfully updated !")

        # dbms ki check karne ki query dalegi
    i3=0
    if i0==2:
        while i3!=3:
            print("1)Sign up")
            print("2)Login")
            print("3)exit")
            i3=int(input())

            if i3==1:
                print("Enter the user id=")
                user_id=int(input())
                print("Enter the username=")
                username=input()
                print("Enter the password=")
                user_pass=input()
                print("Enter the user phone=")
                user_phone=input()
                print("Enter the user address=")
                user_address=input()
                print("Enter the state=")
                user_state=input()
                print("Enter the pincode=")
                user_pin=int(input())
                print("Enter the email=")
                user_email=input()
                connection=create_db_connection("localhost","root","1102","megamart")
                q8=f"""INSERT INTO user1(uder_id, username, user_pass, user_phone, user_address, state,pincode,email) values {user_id, username, user_pass,  user_phone, user_address, user_state,user_pin,user_email};"""
                print()
                read_query(connection,q8)
                print("user registered succesfully!!")
                i4=0
                while i4!=6:
                    print("Welcome " + username)
                    print("1) browse products")
                    print("2) add a product in  to cart")
                    print("3) view cart")
                    print("4) empty cart")
                    print("5) cart Total")
                    print("6) checkout of the cart")
                    print("7) back")
                    i4=int(input())
                    if i4==1:
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q9="""SELECT * FROM product"""
                        read_query1(connection,q9)
                    
                    if i4==2:
                        print("Enter the product id you want to add in cart=")
                        add_prod=int(input())
                        
                        print("Enter the quantity of the product=")
                        qty=int(input())

                        connection=create_db_connection("localhost","root","1102","megamart")
                        q21=f"""SELECT Cart_Quantity FROM product WHERE product_id = {add_prod};"""
                        present_qty=read_query3(connection,q21)
                        print(present_qty)
                        if qty>present_qty:
                            print("TOO much quantity, we only have "+str(present_qty)+" products")
                        else:
                            connection=create_db_connection("localhost","root","1102","megamart")
                            q10=f"""INSERT INTO  cart (product_id, uder_id, quantity) values {add_prod,user_id,qty};"""
                            read_query(connection,q10)
                            print("product successfully added into cart")

                    if i4==3:
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q11=f"""SELECT * FROM cart WHERE uder_id ={user_id};"""
                        print("cart_id, product id, user id, quantity")
                        read_query1(connection,q11)
                        
                    if i4==4:
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q12=f"""DELETE FROM cart WHERE uder_id = {user_id};"""
                        read_query(connection,q12)
                        print("cart is emptied")
                        
                    if i4==5:
                        connection=create_db_connection("localhost","root","1102","megamart")
                        q13=f"""SELECT SUM(product.product_price * cart.quantity) AS total_value
                                FROM cart
                                JOIN product ON cart.product_id = product.product_id
                                WHERE cart.uder_id = {user_id};"""
                        print("your total cart price is:")
                        tt=read_query3(connection,q13)
                        print(tt)
                        
                    
                    
                    if i4==6:
                            connection=create_db_connection("localhost","root","1102","megamart")
                            q16=f"""SELECT * FROM cart WHERE uder_id = {user_id};"""
                            read_query(connection,q16)
                            connection1=create_db_connection("localhost","root","1102","megamart")
                            q17=f"""SELECT SUM(product.product_price * cart.quantity) AS total_value
                                        FROM cart
                                        JOIN product ON cart.product_id = product.product_id
                                        WHERE cart.uder_id = {user_id};"""
                            total=read_query3(connection1,q17)
                            print("Total price of your order is:")
                            print(total)
                            connection2=create_db_connection("localhost","root","1102","megamart")
                            q18=f"""INSERT INTO order_1(order_price, order_date,uder_id,Order_Status) VALUES {int(total),formatted_date,user_id,1}; """
                            read_query(connection2,q18)
                            connection3=create_db_connection("localhost","root","1102","megamart")
                            q19=f""" UPDATE product
                                    JOIN cart ON cart.product_id = product.product_id
                                    SET Cart_Quantity = Cart_Quantity - cart.quantity
                                    WHERE cart.uder_id = {user_id};
                                    """
                            read_query(connection3,q19)
                            connection4=create_db_connection("localhost","root","1102","megamart")
                            q20=f"""DELETE FROM cart WHERE uder_id = {user_id};"""
                            read_query(connection4,q20)
                            print("checkout done succesfully")
                    
            if i3==2:
                q2=1
                while q2==1:
                    print("Enter the user id=")
                    userid=int(input())
                    print("Enter the password=")
                    user_pass=input()
                    connection=create_db_connection("localhost","root","1102","megamart")
                    q14=f"""SELECT * FROM user1 WHERE uder_id = {userid} AND user_pass = '{user_pass}'"""
                    x=read_query2(connection,q14)
                    if not x:
                        print("Wrong details entered!")

                    else:
                        q2=2
                        print("Logged in Succesfully!")
                        i4=0
                        while i4!=10:
                            print("Welcome " )
                            print("1) browse products")
                            print("2) add a product in  to cart")
                            print("3) view cart")
                            print("4) empty cart")
                            print("5) cart Total")
                            print("6) checkout of the cart")
                            print("7) Non conflicting transaction-a")
                            print("8) Non conflicting transaction-b")
                            print("9) 3rd non conflict")
                            print("10) back")
                            i4=int(input())
                            if i4==1:
                                connection=create_db_connection("localhost","root","1102","megamart")
                                q9="""SELECT * FROM product"""
                                read_query1(connection,q9)
                                
                            
                            if i4==2:
                                
                                
                                
                                print("Enter the product id you want to add in cart=")
                                add_prod=int(input())
                                
                                print("Enter the quantity of the product=")
                                qty=int(input())

                                connection=create_db_connection("localhost","root","1102","megamart")
                                q21=f"""SELECT Cart_Quantity FROM product WHERE product_id = {add_prod};"""
                                present_qty=read_query3(connection,q21)

                                if qty>present_qty:
                                    print("TOO much quantity, we only have "+present_qty+" products")
                                else:
                                    connection=create_db_connection("localhost","root","1102","megamart")
                                    q10=f"""INSERT INTO  cart (product_id, uder_id, quantity) values {add_prod,userid,qty};"""
                                    read_query(connection,q10)
                                    print("product successfully added into cart")

                            if i4==3:
                                connection=create_db_connection("localhost","root","1102","megamart")
                                q11=f"""SELECT * FROM cart WHERE uder_id ={userid};"""
                                print("cart_id, product id, user id, quantity")
                                read_query1(connection,q11)
                                
                            if i4==4:
                                connection=create_db_connection("localhost","root","1102","megamart")
                                q12=f"""DELETE FROM cart WHERE uder_id = {userid};"""
                                read_query(connection,q12)
                                print("cart is emptied")
                            
                            if i4==5:
                                connection=create_db_connection("localhost","root","1102","megamart")
                                q13=f"""SELECT SUM(product.product_price * cart.quantity) AS total_value
                                            FROM cart
                                            JOIN product ON cart.product_id = product.product_id
                                            WHERE cart.uder_id = {userid};"""
                                total1=read_query3(connection,q13)
                                print("your total cart price is:")
                                print(total1)
                            
                            if i4==6:
                                connection=create_db_connection("localhost","root","1102","megamart")
                                q16=f"""SELECT * FROM cart WHERE uder_id = {userid};"""
                                read_query(connection,q16)
                                connection1=create_db_connection("localhost","root","1102","megamart")
                                q17=f"""SELECT SUM(product.product_price * cart.quantity) AS total_value
                                            FROM cart
                                            JOIN product ON cart.product_id = product.product_id
                                            WHERE cart.uder_id = {userid};"""
                                total=read_query3(connection1,q17)
                                print("Total price of your order is:")
                                print(total)
                                connection2=create_db_connection("localhost","root","1102","megamart")
                                q18=f"""INSERT INTO order_1(order_price, order_date,uder_id,Order_Status) VALUES {int(total),formatted_date,userid,1}; """
                                read_query(connection2,q18)
                                connection3=create_db_connection("localhost","root","1102","megamart")
                                q19=f""" UPDATE product
                                        JOIN cart ON cart.product_id = product.product_id
                                        SET Cart_Quantity = Cart_Quantity - cart.quantity
                                        WHERE cart.uder_id = {userid};
                                        """
                                read_query(connection3,q19)
                                connection4=create_db_connection("localhost","root","1102","megamart")
                                q20=f"""DELETE FROM cart WHERE uder_id = {userid};"""
                                read_query(connection4,q20)
                                print("checkout done succesfully")


                            if i4==7:
                                connection33=create_db_connection("localhost","root","1102","megamart")
                                q21=f"""
                                    START TRANSACTION;
                                    INSERT INTO cart (product_id,uder_id, quantity) VALUES (100,1, 1);
                                    COMMIT;

                                    
                                    START TRANSACTION;
                                    INSERT INTO cart (product_id, uder_id, quantity) VALUES (100,2, 1);
                                    COMMIT;"""
                                read_query4(connection,q21)

                            if i4==8:
                                connection1=create_db_connection("localhost","root","1102","megamart")
                                q17=f"""SELECT SUM(product.product_price * cart.quantity) AS total_value
                                            FROM cart
                                            JOIN product ON cart.product_id = product.product_id
                                            WHERE cart.uder_id = 1;"""
                                total=read_query3(connection1,q17)
                                print(total)
                                connection1=create_db_connection("localhost","root","1102","megamart")
                                q17=f"""SELECT SUM(product.product_price * cart.quantity) AS total_value
                                            FROM cart
                                            JOIN product ON cart.product_id = product.product_id
                                            WHERE cart.uder_id = 2;"""
                                total2=read_query3(connection1,q17)
                                print(total2)
                                
                                connection=create_db_connection("localhost","root","1102","megamart")
                                q22=f"""
                                    START TRANSACTION;
                                    INSERT INTO order_1(order_price, order_date,uder_id,Order_Status) VALUES {int(total),formatted_date,1,1};
                                    COMMIT;
                                    
                                    START TRANSACTION;
                                    INSERT INTO order_1(order_price, order_date,uder_id,Order_Status) VALUES {int(total2),formatted_date,2,1};
                                    COMMIT;
                                    ; """
                                read_query4(connection,q22)

                            if i4==9:
                                connection=create_db_connection("localhost","root","1102","megamart")
                                q23=f"""
                                    START TRANSACTION;
                                    SELECT Cart_Quantity FROM product WHERE product_id = 100;
                                    COMMIT;

                                    -- Process User A's order
                                    START TRANSACTION;
                                    UPDATE product SET Cart_Quantity = Cart_Quantity - 1 WHERE product_id = 100;
                                    COMMIT;

                                    -- Process User B's order
                                    START TRANSACTION;
                                    UPDATE product SET Cart_Quantity = Cart_Quantity -1 WHERE product_id = 100;
                                    COMMIT;
                                    ; """
                                read_query4(connection,q23)



                
                
                
                



