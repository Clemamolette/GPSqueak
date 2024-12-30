import psycopg2

import logging
LOG = logging.Logger("API db lib")

def connect(db_params : dict):
    """establishes connection to the database
    
    Keyword arguments:
    db_params -- dictionary of the necessary info to connect to the database ('db_name', 'user', 'password', 'host', 'port')
    Return: None
    """
    
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        LOG.error(f"Error: {error}")
        return None

def fetch_data(query : str, cursor) -> list[list]:
    """fetches data from the conected database based on the provided query
    
    Keyword arguments:
    query -- query to be passed on the database to fecth data. To insert data, please use insert_data
    query_args -- arguments that should fill the query
    Return: results of the query in the form list of list
    """
    
    try:
        cursor.execute(query)
        query_result = cursor.fetchall()
        try:
            query_result = [[query_result[i][j] for j in range(len(query_result[i]))] for i in range(len(query_result))] # list of list of data
        except:
            pass
        return query_result

    except (Exception, psycopg2.DatabaseError) as error:
        LOG.error(f"Error: {error}")

def disconnect(conn, cursor):
    """diconnects from the connected database
    
    Keyword arguments:
    conn -- current connection to the database (generated from the connect function)
    cursor -- current cursor to the connection (generated from the connect function)
    Return: None
    """
    try:
        cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        LOG.error(f"Error: {error}")

def fetch_all_positions(id : str, cursor) -> list:
    query = """
        SELECT coordinates.latitude, coordinates.longitude FROM coordinates
        WHERE coordinates.id_mouse = '%s' """ % id
        
    return fetch_data(query, cursor)

def fetch_last_position(id : str, cursor) -> list:
    query = """
        SELECT coordinates.latitude, coordinates.longitude FROM coordinates
        WHERE coordinates.id_mouse = '%s'
        ORDER BY coordinates.t_stamp DESC
        LIMIT 1
        """ % id

    res = fetch_data(query, cursor)
    return res

def fetch_id_list(cursor) -> dict:
    query = """
        SELECT name, MIN(id) AS id
        FROM mouses
        GROUP BY name;
        """
    res = fetch_data(query, cursor)
    return res

def fetch_name_list(cursor) -> dict:
    query = """
        SELECT DISTINCT name
        FROM mouses;
        """
    res = fetch_data(query, cursor)
    return res

def fetch_id_from_name(name : str, cursor) -> dict:
    query = """
        SELECT id
        FROM mouses
        WHERE name = '%s';
        """ % name
    res = fetch_data(query, cursor)
    return res