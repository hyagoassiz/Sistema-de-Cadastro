def cadastrar(status, nome, tel_1, tel_2, email, cpf, rg, nascimento, sexo, observacao,
    cep, logradouro, numero, bairro, cidade, uf, referencia,
    data_matricula, curso, ano, turno):
        import pyodbc
        dados_conexao = ("Driver={SQLite3 ODBC Driver};"
        "Server=localhost;"
        "Database=data/cadastros.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()


        comando = f"""INSERT INTO alunos (status, nome, tel_1, tel_2, email, cpf, rg, nascimento, sexo, observacao,
        cep, logradouro, numero, bairro, cidade, uf, referencia,
        data_matricula, curso, ano, turno)
        VALUES ('{status}', '{nome}', {tel_1}, {tel_2}, '{email}', {cpf}, {rg}, '{nascimento}', '{sexo}', '{observacao}',
        {cep}, '{logradouro}', {numero}, '{bairro}', '{cidade}', '{uf}', '{referencia}',
        '{data_matricula}', '{curso}', {ano}, '{turno}')"""
        cursor.execute(comando)
        cursor.commit()
        #abrir para visualizar dados

        cursor.close() # utilzados para encerrar a conexão
        conexao.close()

def verificar_cadastro(cpf):
        import pyodbc
        dados_conexao = ("Driver={SQLite3 ODBC Driver};"
        "Server=localhost;"
        "Database=data/cadastros.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        try:
                comando = f'SELECT * FROM alunos WHERE cpf = "{cpf}"'        
                cursor.execute(comando)
                valores = cursor.fetchall()
                resultado = valores[0][6]

                cursor.close() # utilzados para encerrar a conexão
                conexao.close()
                return True
        except:
                cursor.close() # utilzados para encerrar a conexão
                conexao.close()
                return False

def atualizar(status, nome, tel_1, tel_2, email, cpf, rg, nascimento, sexo, observacao,
    cep, logradouro, numero, bairro, cidade, uf, referencia,
    data_matricula, curso, ano, turno):
        import pyodbc
        dados_conexao = ("Driver={SQLite3 ODBC Driver};"
        "Server=localhost;"
        "Database=data/cadastros.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        comando = f"""UPDATE alunos SET         
        status = '{status}',
        nome = '{nome}',
        tel_1 = {tel_1},
        tel_2 = {tel_2},
        email = '{email}',
        rg = {rg},
        nascimento = '{nascimento}',
        sexo = '{sexo}',
        observacao = '{observacao}',
        cep = {cep},
        logradouro = '{logradouro}',
        numero = {numero},
        bairro = '{bairro}',
        cidade = '{cidade}',
        uf = '{uf}',
        referencia = '{referencia}',
        data_matricula = '{data_matricula}',
        curso = '{curso}',
        ano = {ano},
        turno = '{turno}'
        WHERE cpf = {cpf}"""
        cursor.execute(comando)
        cursor.commit()

        cursor.close() 
        conexao.close()

def limpar(window):
        #Dados pessoais
        window['Nome'].update('')
        window['Tel_1'].update('')
        window['Tel_2'].update('')
        window['Email'].update('')
        window['CPF'].update('')
        window['RG'].update('')
        window['Nascimento'].update('')
        window['Observacao'].update('')
        #Endereco
        window['CEP'].update('')
        window['Logradouro'].update('')
        window['Numero'].update('')
        window['Bairro'].update('')
        window['Cidade'].update('')
        window['UF'].update('')
        window['Referencia'].update('')
        window['DataMatricula'].update('')
        #Curso
        window['Curso'].update('')
        window['Ano'].update('')
        window['Turno'].update('')
        #Localizar
        window['LocalizarCPF'].update('') 

def excluir(cpf):
        import pyodbc
        dados_conexao = ("Driver={SQLite3 ODBC Driver};"
        "Server=localhost;"
        "Database=data/cadastros.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        comando = f'DELETE FROM alunos WHERE cpf = {cpf}'
        cursor.execute(comando)
        cursor.commit()

        cursor.close() 
        conexao.close()

def encontrar(window, cpf):
        import pyodbc
        dados_conexao = ("Driver={SQLite3 ODBC Driver};"
        "Server=localhost;"
        "Database=data/cadastros.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()

        comando = f"SELECT * FROM alunos WHERE cpf = '{cpf}'"
        cursor.execute(comando)
        valores = cursor.fetchall()

        window['Status'].update(valores[0][1])
        window['Nome'].update(valores[0][2])
        window['Tel_1'].update('{:.0f}'.format(valores[0][3]))
        window['Tel_2'].update('{:.0f}'.format(valores[0][4]))
        window['Email'].update(valores[0][5])
        window['CPF'].update('{:.0f}'.format(valores[0][6]))
        window['RG'].update('{:.0f}'.format(valores[0][7]))
        window['Nascimento'].update(valores[0][8])
        window['Sexo'].update(valores[0][9])
        window['Observacao'].update(valores[0][10])
        window['CEP'].update('{:.0f}'.format(valores[0][11]))
        window['Logradouro'].update(valores[0][12])
        window['Numero'].update('{:.0f}'.format(valores[0][13]))
        window['Bairro'].update(valores[0][14])
        window['Cidade'].update(valores[0][15])
        window['UF'].update(valores[0][16])
        window['Referencia'].update(valores[0][17])
        window['DataMatricula'].update(valores[0][18])
        window['Curso'].update(valores[0][19])
        window['Ano'].update('{:.0f}'.format(valores[0][20]))
        window['Turno'].update(valores[0][21])

        cursor.close()
        conexao.close()






