from fastapi import FastAPI
import openai  # Importación correcta
from pydantic import BaseModel

# Configura la clave de la API de OpenAI desde un archivo de entorno o variable segura
openai.api_key = "tu openAI key"  # Usa variables de entorno para mayor seguridad

app = FastAPI()

# Modelo para manejar la entrada de preguntas del usuario
class QuestionRequest(BaseModel):
    question: str

@app.get("/")
async def execute_haiku():
    """Genera un haiku sobre recursión en programación."""
    try:
        completion = openai.ChatCompletion.create (
            model="text-moderation-007",  # Nombre del modelo correcto
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Write a haiku about recursion in programming."}
            ]
        )
        return {"response": completion.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}

@app.get("/respostaoutra")
async def get_prime_minister():
    """Obtiene información sobre el Primer Ministro de Canadá."""
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Quem é o primeiro ministro do Canadá?"}
            ]
        )
        return {"response": completion.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}

@app.post("/question")
async def custom_question(request: QuestionRequest):
    """Responde preguntas personalizadas del usuario."""
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente virtual especialista em finanças."},
                {"role": "user", "content": request.question}
            ]
        )
        return {"response": completion.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}
