# 📌 API de Gerenciamento de Tarefas (Flask)

API REST desenvolvida em **Python** utilizando **Flask** para gerenciamento de tarefas (**CRUD**). A API permite criar, visualizar, atualizar e excluir tarefas, armazenando-as em memória. Além disso, conta com **testes automatizados** usando `pytest`.

## 🚀 Tecnologias Utilizadas

- **Python 3.10**
- **Flask**
- **pytest**
- **requests**

## 📦 Instalação e Configuração

### **1️⃣ Clonar o Repositório**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### **2️⃣ Instalar Dependências**

```bash
pip install -r requirements.txt
```

## ▶️ Executando a API

Após instalar as dependências, execute o servidor Flask:

```bash
python app.py
```

A API estará disponível em: [**http://127.0.0.1:5000**](http://127.0.0.1:5000)

## 📌 Endpoints da API

| Método   | Rota          | Descrição                 |
| -------- | ------------- | ------------------------- |
| `POST`   | `/tasks`      | Criar uma nova tarefa     |
| `GET`    | `/tasks`      | Listar todas as tarefas   |
| `GET`    | `/tasks/<id>` | Buscar uma tarefa pelo ID |
| `PUT`    | `/tasks/<id>` | Atualizar uma tarefa      |
| `DELETE` | `/tasks/<id>` | Remover uma tarefa        |

### **📌 Exemplo de Payload (**``**):**

```json
{
  "title": "Estudar Python",
  "description": "Criar uma API REST com Flask"
}
```

## ✅ Testes Automatizados

Os testes são feitos com **pytest** e **requests**.

### **1️⃣ Executar os Testes**

```bash
pytest tests.py
```

Se todos os testes passarem, você verá uma saída semelhante a esta:

```bash
tests.py::test_create_task PASSED
tests.py::test_get_tasks PASSED
tests.py::test_get_task PASSED
tests.py::test_update_task PASSED
tests.py::test_delete_task PASSED
```
---

Feito em conjunto com o curso da @rocketseat [https://app.rocketseat.com.br/]

