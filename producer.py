import pika
import random
import json
from pika import ConnectionParameters, BlockingConnection, PlainCredentials

# Функция для генерации случайных данных
def generate_random_data(measurement_type):
    if measurement_type == "temperature":
        return random.uniform(-30, 50)  # случайное значение температуры от -30 до 50
    elif measurement_type == "pressure":
        return random.uniform(950, 1050)  # случайное значение давления от 950 до 1050
    else:
        return random.uniform(0, 100)  # случайное значение для других типов

# Параметры подключения
connection_parms = ConnectionParameters(
    host="localhost",  # Укажите хост
    port=5672,  # Порт для подключения
    credentials=PlainCredentials("user", "password")  # Учетные данные
)

def main():
    with BlockingConnection(connection_parms) as conn:
        with conn.channel() as ch:
            # Выбор типа измерения (temperature или pressure)
            measurement_type = random.choice(["temperature", "pressure"])

            # Создание данных для 5 устройств
            devices = []
            for i in range(5):
                device = {
                    "device_id": random.randint(1000, 5000),
                    "value": generate_random_data(measurement_type),
                    "status": random.choice(["OK", "ERROR"])
                }
                devices.append(device)

            # Создание сообщения
            message = {
                "measuring": measurement_type,
                "timestamp": "2023-01-21T02:05:55.000Z",  # Пример временной метки
                "device": devices
            }

            # Преобразование в JSON
            message_str = json.dumps(message)

            # Отправка сообщения в очередь
            ch.basic_publish(
                exchange="DirectExchange",
                routing_key="temperature" if measurement_type == "temperature" else "pressure",
                body=message_str
            )
            print(f"Сообщение с типом {measurement_type} и значением {json.dumps(message, indent=4)} доставлено в очередь")

if __name__ == '__main__':
    main()
