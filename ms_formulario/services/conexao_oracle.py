import oracledb

try:
    # Conectando ao banco de dados Oracle
    conn = oracledb.connect(
        user="xxxxxx", password="xxxxx", dsn="ORACLE.FIAP.COM.BR:1521/ORCL"
    )
except oracledb.DatabaseError as e:
    # Tratando erro de conexão
    error_obj, = e.args
    print("Erro de conexão com o Oracle:")
    print(f"Erro código: {error_obj.code}")
    print(f"Mensagem de erro: {error_obj.message}")
    conexao = False
else:
    conexao = True
    print("Conexão feita com sucesso!")
