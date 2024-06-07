# Gerenciador de Tarefas

Bem-vindo ao Gerenciador de Tarefas, uma aplicação API desenvolvida por Karython Gomes. Esta API permite que você gerencie tarefas, projetos e associações entre eles. Ele também inclui autenticação de usuário com geração de token JWT para proteção dos endpoints.

## Funcionalidades Principais

- **Cadastro de Tarefas**: Cadastre novas tarefas com informações detalhadas, como título, descrição e data de expiração.
- **Associação de Tarefas a Projetos**: Associe tarefas específicas a projetos para uma melhor organização.
- **Associação de Projetos a Funcionários**: Atribua projetos a funcionários para melhor distribuição de tarefas.
- **Autenticação de Usuário**: Faça login com credenciais válidas para acessar recursos protegidos.
- **Geração de Token JWT**: Após o login bem-sucedido, um token de acesso JWT é gerado para autorizar e proteger os endpoints da API.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/seu_projeto.git
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure o banco de dados MySQL de acordo com as configurações fornecidas no arquivo `.env`.

4. Execute a aplicação:

   ```bash
   python app.py
   ```

## Uso

- Acesse os endpoints da API para realizar operações CRUD relacionadas a tarefas, projetos e usuários.
- Autentique-se usando o endpoint `/login` para obter um token JWT.
- Use o token JWT para acessar recursos protegidos que exigem autenticação.

## Exemplos de Requisições

### Cadastro de Tarefa

```http
POST /tarefa
Content-Type: application/json

{
  "titulo": "Implementar autenticação JWT",
  "descricao": "Implementar a funcionalidade de autenticação JWT na API",
  "data_expiracao": "2024-05-31",
  "projeto": 1
}
```

### Login de Usuário

```http
POST /login
Content-Type: application/json

{
  "email": "usuario@example.com",
  "senha": "sua_senha_segura"
}
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para relatar problemas ou enviar pull requests com melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Desenvolvido por Karython Gomes | [LinkedIn](https://www.linkedin.com/in/karythongomes/)
```

