from fakepintrest import database, app

from fakepintrest.models import Usuario, Foto  
# Devemos importar as tabelas que queremos criar

# Criação das tabelas no banco de dados
with app.app_context():
    database.create_all()
    print("Tabelas criadas com sucesso!")