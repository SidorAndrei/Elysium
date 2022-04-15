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


def get_address():
    return connection.execute_select("""
    SELECT address
    FROM supermarket
    """)
