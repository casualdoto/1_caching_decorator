from cache_decorator import cache_decorator

# Использование LRU-кэша
@cache_decorator(strategy='LRU', cache_depth=3, ttl=10)
def square(x):
    print(f"Calculating square of {x}")
    return x * x

print(square(2))  # Вычисляется
print(square(3))  # Вычисляется
print(square(2))  # Берется из кэша
print(square(4))  # Вычисляется
print(square(5))  # Вычисляется, из-за глубины кэша (3) удаляется 3
print(square(3))  # Снова вычисляется, так как удалено из-за LRU

# Использование FIFO-кэша
@cache_decorator(strategy='FIFO', cache_depth=3, ttl=10)
def multiply(a, b):
    print(f"Calculating multiply({a}, {b})")
    return a * b

print(multiply(2, 3))  # Вычисляется
print(multiply(4, 5))  # Вычисляется
print(multiply(6, 7))  # Вычисляется
print(multiply(8, 9))  # Вычисляется, удаляется (2, 3)
print(multiply(2, 3))  # Снова вычисляется

# Использование значений по умолчанию (LRU + глубина 10 + TTL 60)
@cache_decorator()
def power(base, exp):
    print(f"Calculating power({base}, {exp})")
    return base ** exp

print(power(2, 3))  # Вычисляется
print(power(2, 3))  # Берется из кэша
print(power(3, 2))  # Вычисляется
print(power(4, 2))  # Вычисляется

# Несколько функций с разными стратегиями

@cache_decorator(strategy='LRU', cache_depth=2, ttl=10)
def add(a, b):
    print(f"Calculating add({a}, {b})")
    return a + b

@cache_decorator(strategy='FIFO', cache_depth=2, ttl=10)
def subtract(a, b):
    print(f"Calculating subtract({a}, {b})")
    return a - b

# Вызовы для функции add (с LRU-стратегией)
print(add(1, 2))     # Вычисляется: результат добавляется в кэш
print(add(3, 4))     # Вычисляется: результат добавляется в кэш
print(add(1, 2))     # Берется из кэша
print(add(5, 6))     # Вычисляется: из-за глубины удаляется (3, 4)
print(add(3, 4))     # Снова вычисляется, так как был удален из кэша

# Вызовы для функции subtract (с FIFO-стратегией)
print(subtract(10, 5))  # Вычисляется: результат добавляется в кэш
print(subtract(20, 10)) # Вычисляется: результат добавляется в кэш
print(subtract(10, 5))  # Берется из кэша
print(subtract(30, 20)) # Вычисляется: из-за глубины удаляется (10, 5)
print(subtract(20, 10)) # Берется из кэша
print(subtract(10, 5))  # Снова вычисляется, так как был удален из кэша
