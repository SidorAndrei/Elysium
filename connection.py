import os
import psycopg2
import psycopg2.extras


def establish_connection(connection_data=None):
    if connection_data is None:
        connection_data = get_connection_data()
    try:
        connect_str = "dbname={} user={} host={} password={}".format(
            connection_data["dbname"],
            connection_data["user"],
            connection_data["host"],
            connection_data["password"],
        )
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn


def get_unset_vars(var_names):
    return [name for name in var_names if os.environ.get(name) is None]


def unset_var_error_msg(env_vars):
    return f'You should set environmental variables: {", ".join(env_vars)}'


def ensure_var(name):
    value = os.environ.get(name)

    if not value:
        raise ValueError(f"Environmental variable should be set: {name}")
    return value


def get_connection_data(db_name=None):
    if db_name is None:
        db_name = ensure_var("MY_PSQL_DBNAME")

    return {
        "dbname": db_name,
        "host": ensure_var("MY_PSQL_HOST"),
        "password": ensure_var("MY_PSQL_PASSWORD"),
        "user": ensure_var("MY_PSQL_USER"),
    }


def execute_select(statement, variables=None, fetchall=True):
    result_set = []
    with establish_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall() if fetchall else cursor.fetchone()
    return result_set


def execute_dml_statement(statement, variables=None):
    result = None
    with establish_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(statement, variables)
            try:
                result = cursor.fetchone()
            except psycopg2.ProgrammingError as pe:
                pass
    return result
