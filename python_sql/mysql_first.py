import mysql.connector


host = "localhost"
user = "user_dev_jr"
password = "123456"

db = "escola_curso"
port = 3306

con = mysql.connector.connect(host=host, user=user, password=password, database=db, port=port)


c = con.cursor(dictionary=True)


# CRUD - SELECT/READ
def select(fields, tables, where=None):
    
    global c
    
    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()


# CRUD - CREATE/INSERT
def insert(values, table, fields=None):
    
    global c, con
    
    query = "INSERT INTO " + table
    if (fields):
        query = query + " (' + fields + ') "
    
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])
    
    print(query)
    
    c.execute(query)
    con.commit()


# CRUD - UPDATE
def update(sets, table, where=None):
    
    global c, con
    
    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
    if (where):
        query = query + " WHERE " + where
    
    c.execute(query)
    con.commit()
    
    print(query)
    

# CRUD - Delete
def delete(table, where):
    
    global c, con
    
    query = "DELETE FROM " + table + " WHERE " + where
    
    c.execute(query)
    con.commit()


print(select("*", "alunos"))
delete("alunos", "id_aluno = 1")
print(select("*", "alunos", "id_aluno=1"))

#update({"nome": "João Martins", "cidade": "Curitiba"}, "alunos", "id_aluno = 1")
        
    

values = ["DEFAULT, 'João Pereira', '2000-01-01', 'AV das Pedras, 123', 'Betim', 'MG', '12345678911'",
          "DEFAULT, 'Maria Pereira', '2000-01-01', 'AV das Pedras, 123', 'Betim', 'MG', '12345678910'"]


#insert(values, "alunos")
#result = select("nome, cpf", "alunos", "id_aluno = 1")
result = select("*", "alunos")
print(result)
