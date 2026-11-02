# API da Casa de Sucos

API em python utilizando FastAPI, capaz de criar sucos, mostrar informações e calcular as calorias e açucar de cada um deles.

## Funcionalidade

- Consulta de frutas(nome, calorias e açucar)
- Cadastrar sucos novos
- Calcular o total de calorias e açúcar do suco
- Listar todos os sucos
- Atualizar as frutas de um suco e recalcular os valoraes (bônus)
- Retornar erro 404 com mensagem amigável quando a fruta não é encontrada

## Como executar 

1. Criar e ativar a o ambiente virtual: 

```
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Instalar as dependencias:

```
pip install -r requirements.txt
```
 
3. Iniciar a API:

```
uvicorn casa_de_sucos:app --reload
```

4. Abrir no navegador para testar: http://127.0.0.1:8000/docs

obs algumas frutas tem nomes em português que fiz pra testar, porém utilize de preferencia e inglês para realizar as pesquisas, porque o fruityvice reconhece em inglês

## Rotas
 
| Método | Rota | O que faz |
|--------|------|-----------|
| GET | /frutas/{nome} | Consulta uma fruta |
| POST | /sucos | Cadastra um suco |
| GET | /sucos | Lista os sucos |
| PUT | /sucos/{id} | Atualiza as frutas de um suco |
 
Os sucos ficam guardados em memória, e são apagados quando a API reinicia
 
## Exemplos de teste (Swagger)

### GET /frutas/banana
 
```json
{
  "nome": "Banana",
  "calorias": 96,
  "acucar": 17.2
}
```

### POST /sucos
 
Corpo:
 
```json
{
  "nome": "Vitamina Tropical",
  "frutas": ["banana", "strawberry"],
  "tem_gosto_de": "Tamarindo"
}
```
 
Resposta:
 
```json
{
  "id": 1,
  "nome": "Vitamina Tropical",
  "frutas": ["banana", "strawberry"],
  "tem_gosto_de": "Tamarindo",
  "total_calorias": 125,
  "total_acucar": 22.6
}
```

### GET /sucos
 
Retorna a lista com todos os sucos cadastrados.
 
### PUT /sucos/1
 
Corpo:
 
```json
{
  "frutas": ["banana", "apple"]
}
```
 
Resposta: o suco com as frutas novas e o total recalculado.
 
### Erro 404 (fruta não encontrada)
 
GET /frutas/abc
 
```json
{
  "detail": "Fruta 'abc' não encontrada"
}
```
 
### Erro 404 (suco não encontrado)
 
PUT /sucos/99
 
```json
{
  "detail": "Suco não encontrado"
}
```