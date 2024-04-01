import imaplib
import email

def marcar_emails_como_lidos(usuario, senha, filtro_remetente):
    # Conectar ao servidor IMAP do Gmail
    conexao = imaplib.IMAP4_SSL('imap.gmail.com')
    conexao.login(usuario, senha)
    conexao.select('inbox')

    # Buscar e-mails na caixa de entrada
    resultado, data = conexao.search(None, 'UNSEEN', '1:100')  # Processar apenas os primeiros 100 e-mails não lidos
    ids = data[0].split()

    for id in ids:
        resultado, data = conexao.fetch(id, '(RFC822)')
        mensagem = email.message_from_bytes(data[0][1])

        # Verificar filtros por remetente e assunto
        remetente = mensagem['From']
        assunto = mensagem['Subject']

        if filtro_remetente in remetente:
            # Marcar e-mail como lido
            conexao.store(id, '+FLAGS', '\Seen')

    # Fechar conexão
    conexao.close()
    conexao.logout()

# Configurações
usuario = 'fe.guimaraes972@gmail.com'
senha = 'zjuy voqu jwzw hbwm'
filtro_remetente = 'jobalerts-noreply@linkedin.com'

# Executar a função para marcar e-mails como lidos
marcar_emails_como_lidos(usuario, senha, filtro_remetente)
print('Terminado')