import PySimpleGUI as sg
from functions import *

sg.theme('LightBlue')

tab1_layout =  [
    [sg.Text('')],
    [sg.Text('Status do Aluno*'), sg.Combo(['ATIVO', 'INATIVO'], key='Status', default_value='ATIVO', size=(7))],
    [sg.Text('Nome do Aluno*', size=(12)), sg.Input('', key='Nome', size=(40))],
    [sg.Text('Telefone*',size=(12)), sg.Input('', key='Tel_1', size=(14)), sg.Text('Telefone 2'), sg.Input('', key='Tel_2', size=(14))],
    [sg.Text('Email', size=(12)), sg.Input('', key='Email', size=(40))],
    [sg.Text('CPF*', size=(12)), sg.Input('', key='CPF', size=(14)), sg.Text('RG*'), sg.Input('', key='RG', size=(14))],
    [sg.Text('Nascimento*', size=(12)), sg.Input('', key='Nascimento', size=(14))],
    [sg.Text('Sexo*'), sg.Combo(['M', 'F'], key='Sexo', default_value='M',)],
    [sg.Text('Observação:')],
    [sg.Multiline('', key='Observacao', size=(53,3))],
]

tab2_layout =  [
    [sg.Text('')],
    [sg.Text('CEP*', size=(12)), sg.Input('', key='CEP', size=(10))],
    [sg.Text('Logradouro*', size=(12)), sg.Input('', key='Logradouro', size=(40))],
    [sg.Text('Número*', size=(12)), sg.Input('', key='Numero', size=(8))],
    [sg.Text('Bairro*', size=(12)), sg.Input('', key='Bairro', size=(14)), sg.Text('Cidade*'), sg.Input('', key='Cidade', size=(14))],
    [sg.Text('UF*', size=(12)), sg.Input('', key='UF', size=(14))],
    [sg.Text('Complemento (se houver)')],
    [sg.Multiline('', key='Referencia', size=(53,3))],
]

tab3_layout = [
    [sg.Text('')],
    [sg.Text('Data Matrícula*', size=(12)), sg.Input('', key='DataMatricula', size=(15))],
    [sg.Text('Curso*', size=(12)), sg.Combo(['Análise de Desenvolvimento de Sistemas', 'Gastronomia', 'Gestão Financeira'], key='Curso', size=(40))],
    [sg.Text('Ano*', size=(12)), sg.Input('', key='Ano', size=(6))],
    [sg.Text('Turno*', size=(12)), sg.Combo(['Manhã', 'Tarde', 'Noite'], key='Turno')],
]

tab4_layout = [
    [sg.Text('')],
    [sg.Text('Digite o número do CPF', size=(18)), sg.Input('', key='LocalizarCPF', size=(15)), sg.Button('Encontrar')],
]


layout = [[sg.TabGroup([[sg.Tab('Dados Pessoais', tab1_layout), sg.Tab('Endereço', tab2_layout), sg.Tab('Curso', tab3_layout), sg.Tab('Buscar', tab4_layout)]])],
              [sg.Button('Cadastrar', button_color='green', pad=(25)),
              sg.Button('Atualizar', button_color='orange', pad=(25)),
              sg.Button('Excluir', button_color='red', pad=(25)),
              sg.Button('Limpar', button_color='blue', pad=(25))]] 

window = sg.Window('Sistema de Cadastro', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

    #Dados pessoais
    status = values['Status']
    nome = values['Nome']
    tel_1 = values['Tel_1']
    tel_2 = values['Tel_2']
    email = values['Email']
    cpf = values['CPF']
    rg = values['RG']
    nascimento = values['Nascimento']
    sexo = values['Sexo']
    observacao = values['Observacao']
    #Endereco
    cep = values['CEP']
    logradouro = values['Logradouro']
    numero = values['Numero']
    bairro = values['Bairro']
    cidade = values['Cidade']
    uf = values['UF']
    referencia = values['Referencia']
    data_matricula = values['DataMatricula']
    #Curso
    curso = values['Curso']
    ano = values['Ano']
    turno = values['Turno']
    #Localizar 
    localizar_cpf = values['LocalizarCPF']



    #BOTOES:
  

    #Encontrar
    if event == 'Encontrar':
        try:
            encontrar(window, localizar_cpf)
            sg.popup_ok('Usuário encontrado')
        except:
            sg.popup_error('Usuário não encontrado')

    #Cadastrar

    if event == 'Cadastrar':
        try:
            cadastro = verificar_cadastro(cpf)
            if cadastro == True:
                sg.popup_error('Usuário já Cadastrado')
            else:
                cadastrar(status, nome, int(tel_1), int(tel_2), email, int(cpf), int(rg), nascimento, sexo, observacao,
                int(cep), logradouro, int(numero), bairro, cidade, uf, referencia,
                data_matricula, curso, int(ano), turno)
                sg.popup_ok('SUCESSO! Usuário cadastrado')
        except:
            sg.popup_error('Para Cadastrar um novo aluno, preencha todos os campos destacados com *')


    #Atualizar
    if event == 'Atualizar':
        try:
            atualizar(status, nome, int(tel_1), int(tel_2), email, int(cpf), int(rg), nascimento, sexo, observacao,
                int(cep), logradouro, int(numero), bairro, cidade, uf, referencia,
                data_matricula, curso, int(ano), turno)
            sg.popup_ok('Dados Atualizados!')
        except:
            sg.popup_error('CPF não localizado!')


    #Excluir
    if event == 'Excluir':
        try:
            sg.popup_yes_no('ATENÇÃO!\nTem certeza que deseja exluir os dados desse Aluno?')
            excluir(cpf)
        except:
            sg.popup_error('Não foi possível excluir!\nAluno não encontrado.')


    #limpar:
    if event == 'Limpar':
        limpar(window)

    




window.close()