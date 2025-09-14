# Olá, me chamo Davi, este é o meu desafio para entrar na Fábrica de Software

**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**

## 📋 Sobre o Projeto
- O projeto é uma operação CRUD (Create, Read, Update, Delete)
- Onde você pode gerenciar pokemons e seus ataques.
- As nomenclaturas usadas na web são tematizadas com pokemons <br> 

**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**

## 🚀 Funcionalidades

- **Criar Pokémon:** Cadastre seus pokémons preferidos e ensine ataques a eles.  
- **Editar Pokémon:** Atualize informações de pokémons existentes.  
- **Visualizar Pokémon:** Veja os detalhes dos pokémons cadastrados.  
- **Deletar Pokémon:** Remova pokémons do sistema.

**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** Django
- **Banco de Dados:** SQLite

**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**

## 📦 Instalação Normal

1. Clone o repositório: 
   ```sh
   git clone https://github.com/Davi-Madruga/wsBackend-Fabrica25.1.git
   ```
2. Crie um ambiente virtual:
   ```sh
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows:
     ```sh
     .\venv\Scripts\activate
     ```
     se der erro use 
     ```sh
     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
     .\venv\Scripts\activate
     ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt 
   ```
   se tiver tendo problemas use 
   ```sh
   pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
   ```
5. Faça as migrações:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```
7. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:8000
   ```
## 🐳 Instalação Docker
se você tiver o docker instalado na sua máquina fica mais facil ainda
1. Clone o repositório: 
   ```sh
   git clone https://github.com/Davi-Madruga/wsBackend-Fabrica25.1.git
   ```
2. Entre no diretório:
   ```sh
   cd docker
   ```
3. Levante o container:
   ```sh
   docker-compose up --build
   ```
**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**
## Os ataques são entidades relacionas aos pokemons de uma forma One-to-Many um Pokemon pode ter vários ataques. <br> Tentei ao máximo habientar a aplicação com o tema de Pokemon para ficar mais realista, aproveite a aplicação!
**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**

## 🕸 Referências:
- PokeApi:
   https://pokeapi.co/
   https://www.youtube.com/watch?v=JVQNywo4AbU&ab_channel=BroCode
- Projeto Django:
   https://docs.djangoproject.com/pt-br/5.2/
   https://www.youtube.com/watch?v=1nrDeZejufg&list=PLFOqHo8oIjzewcT23HCxJV0xWO451CTJe&ab_channel=VamosCodar-WandersonReis
   https://www.youtube.com/watch?v=gLfEa-3cvKw&t=995s&ab_channel=PythonDeveloper-0.1
   https://joaolucasgpc.notion.site/Workshop-Backend-Fabrica-1a499b0a3ac580189ab8df719589852e
- Docker:
   https://www.youtube.com/watch?v=ntbpIfS44Gw&t=294s&ab_channel=Diolinux
   https://www.youtube.com/watch?v=D_ha0g9yS2E&t=61s&ab_channel=FernandaKipper%7CDev
