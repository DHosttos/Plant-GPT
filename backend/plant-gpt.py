from openai import OpenAI
client = OpenAI(api_key="sk-ALGO_ALGO_ALGO")
def analizar_planta(temp, hum, soil):
    prompt = f"""
Eres Plant-GPT, un modelo de IA para monitorear la salud de plantas.

Datos de sensores:
- Temperatura: {temp} °C
- Humedad ambiental: {hum} %
- Humedad del suelo: {soil} %

Devuélveme:
1. Estado de la planta (OK / Riesgo / Crítico)
2. Explicación breve
3. Recomendación práctica
"""

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un experto en cuidado de plantas."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=200,
        store=True,
    )

    respuesta = completion.choices[0].message.content
    return respuesta


# ---- LLAMADO DE PRUEBA ----
print(analizar_planta(27.5, 60, 35))

