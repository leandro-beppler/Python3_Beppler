#"""Desenvolver um menu de múltipla escolha usando as funções if, elif else"""
 #print("""
 #     Menu: 
#1) Para cadastrar novo usuário
#2) Para editar dados de usuários
#3) Deletar usuário
#4) Criar novo banco de dados
#5) Exibir relatório
#0) Para sair 

import sqlite3, time

connect=sqlite3.connect('pessoafisica.db')
c=connect.cursor()
#users=('SELECT nome FROM cadastro')

def criar_db():
    c.execute('CREATE TABLE IF NOT EXISTS cadastro (nome text, cpf varchar, endereco text, email text)')
try:
    criar_db()
except:
    print('Erro ao criar Database.')
else:
    print('Database criada com sucesso.')

############################################
###FUNÇÃO INSERIR DADOS NO BANCO DE DADOS###
############################################

def inserirDados(n, cpf, end, e, tel, empresa, cargo):
    c.execute('INSERT INTO cadastro VALUES(?, ?, ?, ?, ?, ?, ?)', (n, cpf, end, e, tel, empresa, cargo))
    connect.commit()

#############################################
###FUNÇÃO CONSULTA DADOS NO BANCO DE DADOS###
#############################################

def pesquisaDados(pesquisardb):
    sql='SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql, (pesquisardb,)):
        print(row)
    connect.commit()

#############################################
###FUNÇÃO RELATAR DADOS DO BANCO DE DADOS####
#############################################

def relatarUsers(relatardb):
    rel_sql='SELECT nome FROM cadastro'
    for row_rel in c.execute(rel_sql, (relatardb,)):
        print(row_rel)
    connect.commit()

#############################################
###FUNÇÃO DELETA DADOS NO BANCO DE DADOS#####
#############################################

#def deletarUsers(pesquisardb1):
 #   sql_del='DELETE nome FROM cadastro WHERE = ?'
  #  for row in c.execute(sql, (pesquisardb,)):
   #     print()
    #connect.commit()

######################################
###SELECIONA FUNCAO A SER EXECUTADA###
######################################

funcao=int(input('1 - Cadastrar Pessoa Física\n2 - Consultar Cadastro PF\n3 - Relatório Usuários\n4 - Remover Usuário\n5 - Para sair\nSelecione a opção desejada:'))

########CADASTRAR USER#########
###SE OPÇÃO 1 FOR EXECUTADA####
###############################
              
if funcao == 1:
    try:
        print('Cadastrar Pessoa Física - JCAVI Treinamentos')
        time.sleep(1)
        n=str(input('Digite o nome: '))
        cpf=str(input('Digite o CPF: '))
        end=str(input('Digite o endereço: '))
        e=str(input('Digite o email: '))
        tel=str(input('Digite o telefone:'))
        empresa=str(input('Digite o nome da empresa:'))
        cargo=str(input('Qual o seu cargo?'))
        inserirDados(n, cpf, end, e, tel, empresa, cargo)
    except:
        print('Erro ao realizar cadastro do cliente')
    else:
        print('{}, foi cadastrado com sucesso.'.format(n))
                
########CONSULTAR USER#########
###SE OPÇÃO 2 FOR EXECUTADA####
###############################
              
if funcao == 2:
    try:
        print('Consultar dados no Database...')
        time.sleep(1)
        pesquisardb=str(input('Digite o nome a ser localizado: '))
        pesquisaDados(pesquisardb)
    except:
        print('{} não foi localizado no cadastro'.format(pesquisardb))

##########RELATAR USER#########
###SE OPÇÃO 3 FOR EXECUTADA####
###############################

if funcao == 3:
    try:
        print('Relatório de usuários cadastrados no sistema:')
        time.sleep(1)
        relatarUsers(pesquisardb)
        time.sleep(3)
        print('Pesquisa concluída.')
    except:
        print('Não foi possível realizar a consulta!')

##########DELETAR USER#########
###SE OPÇÃO 4 FOR EXECUTADA####
###############################

#if funcao == 4:    
########FECHAR PROGRAM#########
###SE OPÇÃO 5 FOR EXECUTADA####
###############################
