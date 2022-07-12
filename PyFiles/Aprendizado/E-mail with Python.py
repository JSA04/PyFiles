import win32com.client as win32

# Criar Integração com o Outlook
outlook = win32.Dispatch("outlook.application")

# Criar E-mail
email = outlook.CreateItem(0)

# Informações do Correio eletrónico
email.To = "juan110588@gmail.com"  # Destinatário
email.Subject = "Teste de E-mail com Python"  # Assunto
email.HTMLBody = "<p>Enviando E-mail com Python</p>"

# Enviar E-mail

# Descomentar para enviar o email

# try:
#     email.Send()
# except Exception as Error:
#     print("It was not possible to send the email.")
#     print(f"Erro: {Error}")
# else:
#     print("The E-mail was sent successfully.")
