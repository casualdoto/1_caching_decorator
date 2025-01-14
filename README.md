# 1_quaternions
группа 5130203/20101

casualdoto - Хрестьяновский Даниил

Tonya-Lyub - Антонина Любецкая

shmel9va - Шмелева Мария

Репозитории с задачами:

1_quaternions - https://github.com/casualdoto/1_quaternions

1_caching_decorator - https://github.com/casualdoto/1_caching_decorator

1_figures - https://github.com/casualdoto/1_figures

# Декоратор для кэширования

Этот проект предоставляет реализацию декоратора кэширования в Python с поддержкой стратегий LRU и FIFO, а также TTL.

## Структура проекта

```
project_root/
├── cache_decorator.py     # Реализация декоратора кэширования
├── test_cache_decorator.py # Тесты для декоратора
└── requirements.txt       # Требования для проекта
```

## Возможности

- **Стратегии кэширования**:
  - LRU (Least Recently Used) — вытесняет наименее используемые элементы.
  - FIFO (First In, First Out) — вытесняет самые старые элементы.
- **Поддержка TTL (Time-To-Live):**:
  - Элементы удаляются из кэша, если их время жизни истекло.
- **Гибкая настройка:**:
  - Максимальная глубина кэша (cache_depth).
  - Время жизни элементов (ttl).

## Запуск

Настройте виртуальное окружение:

1. Откройте терминал или командную строку.

2. Клонируйте репозиторий:
```bash
git clone https://github.com/casualdoto/1_caching_decorator
```

3. Перейдите в директорию проекта:
```bash
cd путь/к/проекту
```

4. Создайте виртуальное окружение:
```bash
python -m venv venv
```

5. Активируйте виртуальное окружение:
```bash
venv\\Scripts\\activate
```

6. Установите зависимости:
```bash
pip install -r requirements.txt
```

7. Запустите тесты:
```bash
pytest test_cache_decorator.py
```

## Тестирование

Тесты находятся в файле test_cache_decorator.py и используют pytest. Они покрывают следующие случаи:

1. **LRU и FIFO:** Проверяется корректность вытеснения элементов из кэша при его заполнении.

2. **TTL:** Проверяется удаление устаревших элементов после истечения времени жизни.

3. **Гибкость настроек:** Тестируется поведение при разных значениях cache_depth и ttl.



## Примеры использования

### Использование декоратора с LRU
```python
from cache_decorator import cache_decorator

@cache_decorator(strategy='LRU', cache_depth=3, ttl=10)
def square(x):
    return x * x

print(square(2))  # 4 (вычисляется)
print(square(3))  # 9 (вычисляется)
print(square(2))  # 4 (берется из кэша)
```

### Использование декоратора с FIFO
```python
from cache_decorator import cache_decorator

@cache_decorator(strategy='FIFO', cache_depth=2, ttl=5)
def add(a, b):
    return a + b

print(add(1, 2))  # 3 (вычисляется)
print(add(3, 4))  # 7 (вычисляется)
print(add(5, 6))  # 11 (вытесняет старое значение)
```

### Удаление элементов по TTL
from cache_decorator import cache_decorator
import time

@cache_decorator(strategy='LRU', cache_depth=2, ttl=2)
def multiply(a, b):
    return a * b

print(multiply(2, 3))  # 6 (вычисляется)
time.sleep(3)
print(multiply(2, 3))  # 6 (пересчитывается, так как TTL истек)
```

