import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
      print(f'Conectado ao MySQL Server versão {conn.get_server_info()}')
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute("CREATE DATABASE `jogoteca`;")

cursor.execute("USE `jogoteca`;")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
      CREATE TABLE `jogos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `ano` varchar(4) NOT NULL,
      `desenvolvedora` varchar(40) NOT NULL,
      `genero` varchar(20) NOT NULL,
      `plataforma` varchar(20) NOT NULL,
      `capa` varchar(150) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `nome` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `senha` varchar(30) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Gleuber Lucio", "Glbad", "123"),
      ("Thalyta Machado", "Gatinha", "321"),
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, ano, desenvolvedora, genero, plataforma, capa) VALUES (%s, %s, %s, %s, %s, %s)'
jogos = [
      ('Alex Kidd in Miracle World', '1986', 'SEGA', 'Plataforma', 'Master System', 'https://upload.wikimedia.org/wikipedia/en/5/5a/Alex_Kidd_In_Miracle_World_Box.jpg'),
      ('Sonic the Hedgehog', '1991', 'SEGA', 'Plataforma', 'Master System', 'https://upload.wikimedia.org/wikipedia/en/b/bf/Sonic_the_Hedgehog_8-Bit_Boxart.jpg'),
      ('Wonder Boy III: The Dragon’s Trap', '1989', 'Westone Bit Entertainment', 'Ação / Aventura', 'Master System', 'https://upload.wikimedia.org/wikipedia/en/d/d5/Wonder_Boy_III_cover.jpg'),
      ('Super Mario World', '1990', 'Nintendo', 'Plataforma', 'Super Nintendo', 'https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png'),
      ('The Legend of Zelda: A Link to the Past', '1991', 'Nintendo', 'Ação / Aventura', 'Super Nintendo', 'https://upload.wikimedia.org/wikipedia/en/0/0b/The_Legend_of_Zelda_A_Link_to_the_Past_SNES_Game_Cover.jpg'),
      ('Donkey Kong Country', '1994', 'Rare', 'Plataforma', 'Super Nintendo', 'https://upload.wikimedia.org/wikipedia/en/0/06/Donkey_Kong_Country_Coverart.png'),
      ('Final Fantasy VII', '1997', 'Square', 'RPG', 'PlayStation 1', 'https://upload.wikimedia.org/wikipedia/en/2/20/Final_Fantasy_VII_Box_Art.jpg'),
      ('Metal Gear Solid', '1998', 'Konami', 'Ação / Stealth', 'PlayStation 1', 'https://upload.wikimedia.org/wikipedia/en/6/6e/Metal_Gear_Solid_cover_art.png'),
      ('Crash Bandicoot 3: Warped', '1998', 'Naughty Dog', 'Plataforma', 'PlayStation 1', 'https://upload.wikimedia.org/wikipedia/en/3/3c/Crash_Bandicoot_3_Warped.jpg')
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
