import oracledb

# Configuração de conexão com o banco Oracle
dsn = oracledb.makedsn("oracle.fiap.com.br", 1521, service_name="ORCL")
conn = oracledb.connect(user="pf0707", password="fiap25", dsn=dsn)

def create_user(username: str, email: str, password_hash: str):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO USERS_FASTAPI (USERNAME, EMAIL, PASSWORD_HASH)
        VALUES (:username, :email, :password_hash)
    """, [username, email, password_hash])
    conn.commit()
    cursor.close()

def get_user_by_username(username: str):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USERS_FASTAPI WHERE USERNAME = :username", [username])
    result = cursor.fetchone()
    cursor.close()
    return result
