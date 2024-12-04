import psycopg2

def insert_data(coordinate : dict, conn, cursor) -> None:
    try:
        insert_query = """
        INSERT INTO coordinates (ip, latitude, longitude)
        VALUES (%s, %s, %s)
        """

        cursor.execute(insert_query, (coordinate['ip'], coordinate['latitude'], coordinate['longitude']))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def connect(db_params : dict):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        return conn, cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def fetch_data(query : str, conn, cursor, query_arg_list : list[str]) -> dict:
    try:
        query_args = (arg for arg in query_arg_list)
        cursor.execute(query, query_args)
        query_result = cursor.fetchall()
        query_result = [[query_result[i][j] for j in range(len(query_result[0]))] for i in range(len(query_result))] # list of list of data
        return query_result

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def disconnect(conn, cursor):
    try:
        cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")