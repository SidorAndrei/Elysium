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
        INSERT INTO requests (username, password, user_status_id, name, email, phone_number)
        VALUES ( %(username)s,
        %(password)s,
        %(status)s,
        %(name)s,
        %(email)s,
        %(phone_number)s
        )
    """, request)


def confirm_register_request(request_id):
    return connection.execute_dml_statement("""
        INSERT INTO users (username, password, user_status_id, name, email, phone_number, cui_number)  
        (SELECT username, password, user_status_id, name, email, phone_number, cui_number         
         FROM requests WHERE request_id = %(request_id)s);
         DELETE FROM requests WHERE  request_id = %(request_id)s;
         SELECT email, name FROM users WHERE user_id = (SELECT last_value FROM users_user_id_seq);
    """, {"request_id": request_id})


def get_user(username):
    return connection.execute_dml_statement("""
        SELECT username, password , name
        FROM users
        WHERE username = %(username)s
    """, {"username": username})


def get_address():
    return connection.execute_select("""
    SELECT address
    FROM supermarket
    """)
