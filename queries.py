import connection


def get_all_supermarkets():
    return connection.execute_select("""
    SELECT *
    FROM supermarket
    """)


def get_products_by_supermarket_id(supermarket_id):
    return connection.execute_select("""
    SELECT *
    FROM products
    WHERE supermarket_id = %(supermarket_id)s
    """, {'supermarket_id': supermarket_id})


def insert_register_request(request):
    connection.execute_dml_statement("""
        INSERT INTO requests (username, password, user_status_id, name, email, phone_number,address)
        VALUES ( %(username)s,
        %(password)s,
        %(status)s,
        %(name)s,
        %(email)s,
        %(phone_number)s,
        %(address)s
        )
    """, request)


def confirm_register_request(request_id):
    connection.execute_dml_statement("""
        INSERT INTO users (username, password, user_status_id, name, email, phone_number, cui_number)  
        (SELECT username, password, user_status_id, name, email, phone_number, cui_number         
         FROM requests WHERE request_id = %(request_id)s);
         INSERT INTO supermarket(name, address, user_id)  SELECT name, address, 
                (SELECT last_value FROM users_user_id_seq) as user_id FROM requests WHERE request_id = %(request_id)s;
         DELETE FROM requests WHERE  request_id = %(request_id)s;
    """, {"request_id": request_id})
    return connection.execute_select("""SELECT email, name FROM users 
    WHERE user_id = (SELECT last_value FROM users_user_id_seq);""")


def confirm_register_request_for_organisation(request_id):
    connection.execute_dml_statement("""
        INSERT INTO users (username, password, user_status_id, name, email, phone_number, cui_number)  
        (SELECT username, password, user_status_id, name, email, phone_number, cui_number         
         FROM requests WHERE request_id = %(request_id)s);
         INSERT INTO user_cart(user_id)  SELECT last_value FROM users_user_id_seq;
         DELETE FROM requests WHERE  request_id = %(request_id)s;
    """, {"request_id": request_id})
    return connection.execute_select("""SELECT email, name FROM users 
    WHERE user_id = (SELECT last_value FROM users_user_id_seq);""")


def get_user(username):
    return connection.execute_select("""
        SELECT user_id, username, password , users.name, us.name as status 
        FROM users
        JOIN user_status us on us.user_status_id = users.user_status_id
        WHERE username = %(username)s
    """, {"username": username})


def get_address():
    return connection.execute_select("""
    SELECT *
    FROM supermarket
    """)


def get_register_requests():
    return connection.execute_select("""
        SELECT requests.request_id, requests.username, requests.user_status_id, requests.name, 
            requests.email, requests.phone_number, requests.cui_number, us.name as status
        FROM requests
        JOIN user_status us on us.user_status_id = requests.user_status_id;
    """)


def reject_register_request(request_id):
    user = connection.execute_select("SELECT name, email FROM requests WHERE request_id=%(request_id)s",
                                     {"request_id": request_id})
    connection.execute_dml_statement("""
        DELETE FROM requests
        WHERE request_id=%(request_id)s;
    """, {"request_id": request_id})
    return user

