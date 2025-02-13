
# Установка и настройка проекта с RabbitMQ

## Шаг 1: Установка Git

Git — это система контроля версий, которая используется для управления исходным кодом проекта. Для начала нужно установить Git.

### На macOS:
```bash
brew install git
```

### На Linux :
```bash
sudo apt update
sudo apt install git
```
### На Windows:
1. Скачайте установщик Git с [официального сайта](https://git-scm.com/download/win).
2. Запустите установщик и следуйте инструкциям.

После установки Git проверьте, что он был установлен корректно:

```bash
git --version
```

## Шаг 2: Клонировать репозиторий

Теперь клонируйте репозиторий, содержащий проект:

```bash
git clone https://github.com/nrud69/RabbitMQ.git
```

## Шаг 3: Создать и активировать виртуальное окружение

Для изоляции зависимостей создайте виртуальную среду Python:

### На macOS:
```bash
python3 -m venv venv
source venv/bin/activate  

```

### На Windows:
```bash
python -m venv venv
.\venv\Scripts\activate

```

## Шаг 4: Установить все зависимости

Установите все зависимости проекта из `requirements.txt`:

```bash
pip install -r requirements.txt

```

## Шаг 5: Установить Docker

Docker — это инструмент для создания, доставки и запуска контейнеров. Для установки Docker выполните следующие шаги.

### На macOS:
1. Скачайте и установите Docker Desktop для macOS с [официального сайта Docker](https://www.docker.com/products/docker-desktop).
2. Откройте Docker после установки.

### На Linux (Ubuntu/Debian):
1. Установите необходимые пакеты:

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce
```

### На Windows:
1. Скачайте и установите Docker Desktop для Windows с [официального сайта Docker](https://www.docker.com/products/docker-desktop).
2. Откройте Docker после установки.

После установки Docker проверьте его работу с помощью:

```bash
docker --version

```

## Шаг 6: Запустить Docker образ с помощью Docker Compose

1. Перейдите в корень вашего проекта, где находится файл `docker-compose.yml`.

2. Запустите контейнеры с помощью команды:

```bash
docker-compose up --build
```

Эта команда создаст и запустит все сервисы, указанные в `docker-compose.yml`, включая RabbitMQ и другие зависимости проекта.

### Проверка работы контейнеров:
Для проверки, что все контейнеры работают, используйте команду:

```bash
docker ps
```
## Шаг 7: Перейти на сайт и залогиниться

1. Перейдите в браузер и откройте сайт проекта. Обычно это будет что-то вроде `http://localhost:15672/` 
   
2. Используйте данные для входа, чтобы залогиниться в приложение:
   - **login**: user
   - **password**: password

