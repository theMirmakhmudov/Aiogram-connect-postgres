import psycopg2

conn = psycopg2.connect(database="users",
                        user="postgres",
                        password="mirmakhmudov",
                        host="localhost",
                        port=5432)

cursor = conn.cursor()  # creating a cursor
cursor.execute("""
CREATE TABLE IF NOT EXISTS new
(
    id serial PRIMARY KEY NOT NULL,
    fullname VARCHAR(255)  NOT NULL,
    username VARCHAR(255) NOT NULL,
    user_id BIGINT NOT NULL
)
""")


class Database:
    def __init__(self, db_file, user, password, host, port):
        self.connection = psycopg2.connect(database=db_file, user=user, password=password, host=host, port=port)
        self.cursor = self.connection.cursor()

    def add_user(self, full_name, username, user_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO new (fullname, username, user_id) VALUES (%s, %s, %s)',
                                       (full_name, username, user_id))

    def check_user(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT user_id FROM new WHERE user_id = %s", (user_id,))
            return self.cursor.fetchone()


conn.commit()
conn.close()
