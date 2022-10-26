import mysql.connector as mysql

def conf(tipo) -> mysql.connection_cext.CMySQLConnection:
    connection = None
    if tipo != "4dd":
        connection = mysql.connect(host="127.0.0.1", user="sel", db="Users", password=f"{tipo}@sec21")
        return connection
    elif tipo != "s3l":
        connection = mysql.connect(host="127.0.0.1", user="add", db="Users", password=f"{tipo}@sec21")
        return connection  
    else:
        raise mysql.errors.ProgrammingError()
