import mysql.connector



def conectar():
    database = mysql.connector.connect(
        host = "192.168.0.33",
        user = "python",
        passwd = "pepe2912",
        database = "master_python"
    )
    
    cursor = database.cursor(buffered=True)
    
    return[database, cursor]