# CONEXÃO SQLSERVER
import pyodbc

#CRIANDO CONEXAO (BASE DE DAODS, SERVIDOR)
server = 'DESKTOP-A29H50Q\DBDADOS' 
database = 'dbBase' 

cnxn = pyodbc.connect('DRIVER={SQL Server}; SERVER='+server+'; DATABASE='+database+'; TrustedConnection=yes;')
cursor = cnxn.cursor()

#CREAT
def creat():
    time = input("Insiria uma franquia: ")
    comand = f"INSERT INTO tb_teams(team) VALUES ('{time}')"
    cursor.execute(comand)
    cnxn.commit()
    
    print("Franquia inserida com sucesso!")


#READ
# SELECT SIMPLES
def read():
    cursor.execute('select * from tb_teams') 
    row = cursor.fetchone()
    while row: 
       print(row[0], row[1])
       row = cursor.fetchone()
    
#UPDATE
def update():
    time = input("Insiria uma franquia que você deseja alterar: ")
    codigo = input("Insira o código da franquia que você deseja alterar: ")
    
    comand = f"UPDATE tb_teams SET team= ('{time}') WHERE codigo= ('{codigo}')"
    cursor.execute(comand)
    cnxn.commit()
    
    print("Registro alterado com sucesso! ")
    
#DELETE
def delete():
    time = input("Insiria uma franquia que voce deseja deletar: ")
    comand = f"DELETE tb_teams WHERE team= ('{time}')"
    cursor.execute(comand)
    cnxn.commit()
    
    print("Deletado com sucesso!")
    
read()

#ENCERRANDO CONEXÕES
cursor.close()
cnxn.close()