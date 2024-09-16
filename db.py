import psycopg2
from psycopg2 import sql

class DB:
    def create_db(db_name):
        # Define your database connection parameters
        db_host = 'test-vec-db-instance-1.czmj15zygnmm.us-west-2.rds.amazonaws.com'
        db_user = 'postgres'
        db_password = 'Cymonix.1234'
        db_port = '5432'

        try:
        # Establish the connection to the default database (e.g., 'postgres')
            connection = psycopg2.connect(
            host=db_host,
            database='postgres',  # Connect to the default database
            user=db_user,
            password=db_password,
            port=db_port
            )

        # Set autocommit to True
            connection.autocommit = True

        # Create a cursor object
            cursor = connection.cursor()

        # Define the database name
            new_db_name = db_name

        # Execute the CREATE DATABASE command
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(
                sql.Identifier(new_db_name)
            ))

            print(f"Database '{new_db_name}' created successfully.")

        except Exception as e:
            print(f"Error while connecting to PostgreSQL: {e}")

        finally:
        # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def drop_db(db_name):
        db_host = 'test-vec-db-instance-1.czmj15zygnmm.us-west-2.rds.amazonaws.com'
        db_user = 'postgres'
        db_password = 'Cymonix.1234'
        db_port = '5432'

        try:
        # Establish the connection to the default database (e.g., 'postgres')
            connection = psycopg2.connect(
            host=db_host,
            database='postgres',  # Connect to the default database
            user=db_user,
            password=db_password,
            port=db_port
            )

        # Set autocommit to True
            connection.autocommit = True

        # Create a cursor object
            cursor = connection.cursor()

        # Define the database name
            db_name_to_drop = db_name

        # Terminate all connections to the target database
            terminate_connections_query = sql.SQL(
            "SELECT pg_terminate_backend(pid) "
            "FROM pg_stat_activity "
            "WHERE datname = %s"
            )
            cursor.execute(terminate_connections_query, (db_name_to_drop,))

        # Drop the database
            drop_db_query = sql.SQL("DROP DATABASE {}").format(
                sql.Identifier(db_name_to_drop)
            )
            cursor.execute(drop_db_query)

            print(f"Database '{db_name_to_drop}' dropped successfully.")

        except Exception as e:
            print(f"Error while connecting to PostgreSQL: {e}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()



