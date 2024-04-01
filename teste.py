import imaplib
import email

def marcar_emails_como_lidos(usuario, senha, filtro_remetente, filtro_assunto):
    # Conectar ao servidor IMAP do Gmail
    conexao = imaplib.IMAP4_SSL('imap.gmail.com')
    conexao.login(usuario, senha)
    conexao.select('inbox')

    # Buscar e-mails na caixa de entrada
    resultado, data = conexao.search(None, 'UNSEEN')  # Apenas e-mails não lidos
    ids = data[0].split()

    for id in ids:
        resultado, data = conexao.fetch(id, '(RFC822)')
        mensagem = email.message_from_bytes(data[0][1])

        # Verificar filtros por remetente e assunto
        remetente = mensagem['From']
        assunto = mensagem['Subject']

        if filtro_remetente in remetente and filtro_assunto in assunto:
            # Marcar e-mail como lido
            conexao.store(id, '+FLAGS', '\Seen')

    # Fechar conexão
    conexao.close()
    conexao.logout()

# Configurações
usuario = 'seu_email@gmail.com'
senha = 'sua_senha'
filtro_remetente = 'remetente_desejado@exemplo.com'
filtro_assunto = 'Assunto desejado'

# Executar a função para marcar e-mails como lidos
marcar_emails_como_lidos(usuario, senha, filtro_remetente, filtro_assunto)
