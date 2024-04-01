import imaplib
import email
from email.utils import parseaddr

def marcar_emails_como_lidos(usuario, senha, filtro_remetente):
    # Conecta ao servidor IMAP do Gmail
    conexao = imaplib.IMAP4_SSL('imap.gmail.com')
    conexao.login(usuario, senha)
    conexao.select('inbox')

    # Busca e-mails na caixa de entrada
    resultado, data = conexao.search(None, 'UNSEEN')  # Apenas e-mails não lidos
    ids = data[0].split()
    ids.reverse()
    print(f'Resultado da conexão: {resultado}')
    print(f'Trabalhando...')
    limite = 0
    contador = 0
    for id in ids:
        if limite >= 20: # Limite para ler 50 emails
          break

        resultado, data = conexao.fetch(id, '(RFC822)')
        mensagem = email.message_from_bytes(data[0][1])

        # Verificar filtros por remetente
        remetente = parseaddr(mensagem['From'])[1]
        if filtro_remetente == remetente:
            # Marcar e-mail como lido
            conexao.store(id, '+FLAGS', '\\Seen')
            contador +=1
        else:
            # Marca e-mail como não lido caso não seja o remetente alvo
            conexao.store(id, '-FLAGS', '\\Seen')
        limite += 1


    # Fecha conexão
    conexao.close()
    conexao.logout()
    print(f'\033[32m {contador} Emails marcados como lido \033[m')

# Configurações
## É importante lembrar que, caso sua conta tenha verificação duas etapas, será necessário configurar uma senha para aplicativo na sessão autenticação por duas etapas. 
usuario = 'exemplo_de_email@gmail.com'
senha = 'senha' # Senha do email ou senha para aplicativo
filtro_remetente = 'jose@gmail.com' # Remetente alvo

# Executa a função para marcar e-mails como lidos
marcar_emails_como_lidos(usuario, senha, filtro_remetente)
print('Terminado')
