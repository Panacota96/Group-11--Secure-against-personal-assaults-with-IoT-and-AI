import random
import time

# Umbrales de ritmo cardíaco (igual que antes)
lower_heart_rate_threshold = 50  # 50 bpm
upper_heart_rate_threshold = 150  # 150 bpm

# Función para simular un valor de ritmo cardíaco
def simulate_heart_rate():
    return random.randint(40, 180)  # Generar un valor aleatorio entre 40 y 180 bpm

# Función para activar la alerta
def alert_if_heart_rate_abnormal(heart_rate):
    print(f"Ritmo cardíaco simulado: {heart_rate} bpm")
    if heart_rate < lower_heart_rate_threshold or heart_rate > upper_heart_rate_threshold:
        print("¡Alerta! Ritmo cardíaco anómalo detectado.")
    else:
        print("Ritmo cardíaco dentro de los parámetros normales.")

# Simulación de lectura de ritmo cardíaco durante 10 segundos
for _ in range(10):
    simulated_heart_rate = simulate_heart_rate()
    alert_if_heart_rate_abnormal(simulated_heart_rate)
    time.sleep(1)  # Esperar un segundo antes de simular el siguiente dato
