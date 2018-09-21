import sqlite3, time

connect=sqlite3.connect('pessoafisica.db')
c=connect.cursor()

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

def inserirDados(n, cpf, end, e):
    c.execute('INSERT INTO cadastro VALUES(?, ?, ?, ?)', (n, cpf, end, e))
    connect.commit()

#############################################
###FUNÇÃO CONSULTA DADOS NO BANCO DE DADOS###
#############################################

def pesquisaDados(pesquisardb):
    sql='SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql, (pesquisardb,)):
        print(row)
    connect.commit()

######################################
###SELECIONA FUNCAO A SER EXECUTADA###
######################################

funcao=int(input('1 - Cadastrar Pessoa Física\n2 - Consultar Cadastro PF\nSelecione a opção desejada:'))

###############################
###SE OPÇÃO 1 FOR ESCOLHIDA####
###############################
              
if funcao == 1:
    try:
        print('Cadastrar Pessoa Física - JCAVI Treinamentos')
        time.sleep(1)
        n=str(input('Digite o nome: '))
        cpf=str(input('Digite o CPF: '))
        end=str(input('Digite o endereço: '))
        e=str(input('Digite o email: '))
        inserirDados(n, cpf, end, e)
    except:
        print('Erro ao realizar cadastro do cliente')
    else:
        print('{}, foi cadastrado com sucesso.'.format(n))
                
###############################
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
