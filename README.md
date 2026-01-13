# Apollo Solutions Backend API

API RESTful desenvolvida com **FastAPI** e **SQLModel**, utilizando um container em Docker com banco de dados PostgreSQL para gerenciamento de dados de vendas.

## Versão e Dependências

- [Python 3.10+]
- [FastAPI] - Framework web selecionado.
- [SQLModel] - ORM.
- [PostgreSQL] - Banco de dados relacional.
- [Pandas] - Processamento e leitura de arquivos CSV.
- [Docker] - Containerização do Banco de Dados.

---

## Inicializando o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/luan-services/apollo-solutions-backend-task.git
cd apollo-solutions-backend-task
```

### 2. Criar e Ativar o Ambiente Virtual (.venv)

**No Windows**

```powershell
python -m venv .venv
.\.venv\Scripts\activate

```
É recomendável usar um ambiente virtual para isolar as dependências. Rode os comandos na mesma pasta que o projeto foi clonado. A estrutura deve ser:

```
> .venv
> app
```

### 3. Instalar Dependências

Com o ambiente virtual ativo, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt

```

As dependências podem ser encontradas no arquivo requirements.txt.

### 4. Configurar Variáveis de Ambiente (.env)

Crie um arquivo chamado `.env` na raiz do projeto para conectar à string do banco de dados.

**Conteúdo do arquivo `.env`:**

Utilize a string fornecida do banco de dados online no Supabase, se preferir crie sua própria ou utilize um container docker.

```ini
# Exemplo de conexão: postgresql://usuario:senha@localhost:porta/nome_do_banco
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/smartmart_db
```

## Como Rodar a Aplicação

Para iniciar o servidor de desenvolvimento, execute:

```bash
fastapi dev app/main.py

```

O terminal exibirá logs indicando que a aplicação subiu em `http://127.0.0.1:8000`)

---

## Documentação e Uso

A API possui uma documentação interativa gerada automaticamente (Swagger UI).

### Acessando a Documentação

Abra o navegador e acesse: **http://127.0.0.1:8000/docs**

Lá você poderá testar todas as rotas diretamente pelo navegador (botão "Try it out").

### Importação de Dados via Arquivo CSV

O sistema suporta upload de arquivos CSV para popular o banco de dados.

Para manter a integridade dos dados, é necessário respeitar as constraints de foreign keys, então siga a ordem de importação abaixo:

1. **Categories** (`POST /api/v1/categories/import_csv`)
2. **Products** (`POST /api/v1/products/import_csv`)
3. **Sales** (`POST /api/v1/sales/import_csv`)

### Endpoints Principais

A API é organizada em três recursos principais, se desejar, você pode testar os endpoints usando cUrl no command prompt ou algum
serviço online como o postman.

| Método | Endpoint | Descrição |
| --- | --- | --- |
| **GET** | `/api/v1/products/` | Lista todos os produtos |
| **GET** | `/api/v1/products/{id}` | Lista um produto específico |
| **POST** | `/api/v1/products/` | Cria um novo produto (ID gerado auto) |
| **POST** | `/api/v1/products/import_csv` | Importa produtos via CSV (ID preservado) |
| **PUT** | `/api/v1/products/{id}` | Atualiza dados de um produto |
| **DELETE** | `/api/v1/products/{id}` | Remove um produto |

Os mesmos métodos se aplicam para `/categories` e `/sales`.

---

## Estrutura do Projeto

```

├── .venv/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── categories.py
│   │   │   ├── products.py
│   │   │   └── sales.py
│   │   └── main.py
│   ├── config/
│   │   └── database.py
│   ├── models/
│   │   ├── category.py
│   │   ├── product.py
│   │   └── sale.py
│   └── main.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt


```
