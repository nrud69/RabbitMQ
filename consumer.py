import pika
import json
from pika import ConnectionParameters, BlockingConnection, PlainCredentials

# Параметры подключения
connection_parms = ConnectionParameters(
    host="localhost",  # Укажите хост
    port=5672,  # Порт для подключения
    credentials=PlainCredentials("user", "password")  # Учетные данные
)

# Функция для обработки сообщений
def callback(ch, method, properties, body):
    try:
        # Десериализация сообщения из JSON
        message = json.loads(body)
        measuring_type = message.get("measuring", "Unknown")
        timestamp = message.get("timestamp", "Unknown")
        devices = message.get("device", [])

        # Обработка данных (например, вывод в консоль)
        print(f"Получено сообщение с типом измерения: {measuring_type}")
        print(f"Временная метка: {timestamp}")
        print("Данные с устройств:")
        for device in devices:
            print(f"Device ID: {device['device_id']}, Value: {device['value']}, Status: {device['status']}")

        # Подтверждение успешной обработки сообщения
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("Сообщение успешно обработано и подтверждено.")
    except Exception as e:
        print(f"Ошибка при обработке сообщения: {e}")
        # При ошибке не подтверждаем, что сообщение обработано
        ch.basic_nack(delivery_tag=method.delivery_tag)
        print("Сообщение не было подтверждено.")

def main():
    with BlockingConnection(connection_parms) as conn:
        with conn.channel() as ch:

            # Подписка на очередь 'temperature'
            ch.basic_consume(queue='temperature', on_message_callback=callback, auto_ack=False)
            ch.basic_consume(queue='pressure', on_message_callback=callback, auto_ack=False)

            print('Ожидание сообщений. Для выхода нажмите Ctrl+C')
            ch.start_consuming()

if __name__ == '__main__':
    main()
