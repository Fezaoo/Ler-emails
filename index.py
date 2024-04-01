import imaplib
import email
from email.utils import parseaddr

def marcar_emails_como_lidos(usuario, senha, filtro_remetente):
    # Conectar ao servidor IMAP do Gmail
    conexao = imaplib.IMAP4_SSL('imap.gmail.com')
    conexao.login(usuario, senha)
    conexao.select('inbox')

    # Buscar e-mails na caixa de entrada
    resultado, data = conexao.search(None, 'UNSEEN')  # Apenas e-mails não lidos
    print(resultado)
    ids = data[0].split()
    ids.reverse()

    contador = 0

    for id in ids:
        if contador >= 50:
          break

        print(id)
        resultado, data = conexao.fetch(id, '(RFC822)')
        mensagem = email.message_from_bytes(data[0][1])

        # Verificar filtros por remetente
        remetente = parseaddr(mensagem['From'])[1]
        print(remetente)
        print(filtro_remetente)
        if filtro_remetente == remetente:
            # Marcar e-mail como lido
            conexao.store(id, '+FLAGS', '\\Seen')
            print('\033[32m Marcado como lido com sucesso \033[m')
        else:
            conexao.store(id, '-FLAGS', '\\Seen')
        contador += 1


    # Fechar conexão
    conexao.close()
    conexao.logout()

# Configurações
usuario = 'fe.guimaraes972@gmail.com'
senha = 'wgozvjjlcqfkxncf'
filtro_remetente = 'jobalerts-noreply@linkedin.com'

# Executar a função para marcar e-mails como lidos
marcar_emails_como_lidos(usuario, senha, filtro_remetente)
print('Terminado')
