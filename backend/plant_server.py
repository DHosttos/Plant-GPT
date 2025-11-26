from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
client = OpenAI(api_key="sk-ALGO_ALGO_ALGO")
app = FastAPI()


# ====== MODELO DE DATOS QUE ENVÍA FLUTTER ======
class SensorData(BaseModel):
    temp: float
    hum: float
    soil: float
    plant: str  # 👈 tipo de planta (Orquídea, Suculenta, etc.)


# ====== LÓGICA DE PLANT-GPT ======
def analizar_planta(temp: float, hum: float, soil: float, plant: str) -> str:
    prompt = f"""
Eres Plant-GPT, un modelo de IA para monitorear la salud de plantas.

Tipo de planta: {plant}

Datos de sensores:
- Temperatura: {temp} °C
- Humedad ambiental: {hum} %
- Humedad del suelo: {soil} %

Ten en cuenta el tipo de planta al evaluar el estado, porque cada especie
tiene rangos diferentes.

Devuélveme:
1. Estado de la planta (OK / Riesgo / Crítico)
2. Explicación breve
3. Recomendación práctica
"""

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Eres un experto en cuidado de plantas.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_tokens=200,
        store=True,
    )

    return completion.choices[0].message.content


# ====== ENDPOINT QUE USA FLUTTER ======
@app.post("/plant")
def plant_endpoint(data: SensorData):
    respuesta = analizar_planta(
        data.temp,
        data.hum,
        data.soil,
        data.plant,
    )
    return {"respuesta": respuesta}

