from gerSenhas_db import *

db = Gerenciador()

# insert = ("INSERT INTO main "
# "(usuario, nomedoservico, senha) "
# " VALUES (%s, %s, %s)")
# values = ('1', '2', '3')

# db.cadastrar("Juan", "MySQL", "763527")

db.executar()

# db.executar("Create TABLE main "
#             "(id int(3) auto_increment, "
#             "usuario varchar(30), "
#             "servico varchar(30), "
#             "senha varchar(30), "
#             "primary key(id))")

# db.executar(insert, values)

db.fechar()
