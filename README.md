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

## 📦 Instalação

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

**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**

## ⚙️ Usando

1. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```
2. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:8000
   ```

**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**

## Os ataques são entidades relacionas aos pokemons de uma forma One-to-Many um Pokemon pode ter vários ataques. <br> Tentei ao máximo habientar a aplicação com o tema de Pokemon para ficar mais realista, aproveite a aplicação!
**-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-**
