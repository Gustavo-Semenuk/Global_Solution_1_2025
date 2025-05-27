import services.conexao_oracle as oraclefiap


def insert_formulario(formulario):
    try:
        with oraclefiap.conn.cursor() as c_insert:
            # Query SQL usando bind variables para segurança
            cmd = """
                INSERT INTO T_SOFIA_CAD_CLIENTE 
                (name_user, email, estado, contexto, name_company, site, segmento)
                VALUES 
                (:nome, :email, :estado, :contexto, :nome_empresa, :site, :segmento)
            """

            # Executando a query com os valores do formulário
            c_insert.execute(cmd, {
                "nome": Formulario.nome,
                "email": Formulario.email,
                "estado": Formulario.estado,
                "contexto": Formulario.contexto,
                "nome_empresa": Formulario.nome_empresa,
                "site": Formulario.site,
                "segmento": Formulario.segmento
            })

            # Confirmando a transação
            oraclefiap.conn.commit()

    except Exception as e:
        # Em caso de erro, faz rollback da transação
        print(f"Erro ao inserir dados: {e}")
