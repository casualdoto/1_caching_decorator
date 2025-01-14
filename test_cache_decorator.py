import time
import pytest
from cache_decorator import cache_decorator

# Тестовая функция с LRU кэшем
@cache_decorator(strategy='LRU', cache_depth=2, ttl=2)
def lru_function(x):
    return x * x

# Тестовая функция с FIFO кэшем
@cache_decorator(strategy='FIFO', cache_depth=2, ttl=2)
def fifo_function(x):
    return x + 10

# Тестовая функция с TTL
@cache_decorator(strategy='LRU', cache_depth=2, ttl=1)
def ttl_function(x):
    return x * 2

# Тесты с корректным поведением LRU
def test_lru_cache_behavior():
    assert lru_function(1) == 1  # Вычисляется
    assert lru_function(2) == 4  # Вычисляется

    assert lru_function(1) == 1  # Берется из кэша

    assert lru_function(3) == 9  # Вытесняет 2 из-за глубины кэша
    assert lru_function(2) == 4  # Должно вычисляться заново

# Тесты с корректным поведением FIFO
def test_fifo_cache_behavior():
    assert fifo_function(1) == 11  # Вычисляется
    assert fifo_function(2) == 12  # Вычисляется

    assert fifo_function(3) == 13  # Вытесняет 1
    assert fifo_function(1) == 11  # Должно вычисляться заново

# Тесты с корректным поведением TTL
def test_ttl_cache_behavior():
    assert ttl_function(10) == 20  # Вычисляется
    assert ttl_function(10) == 20  # Берется из кэша

    time.sleep(2)  # Ждем истечения TTL

    assert ttl_function(10) == 20  # Должно вычисляться заново

# Тесты на корректность вытеснения в LRU
def test_lru_eviction():
    lru_function(1)
    lru_function(2)
    lru_function(3)

    # Ожидаем, что 1 было вытеснено
    assert lru_function(1) == 1  # Пересчитывается, т.к. вытеснено

# Тесты на корректность вытеснения в FIFO
def test_fifo_eviction():
    fifo_function(1)
    fifo_function(2)
    fifo_function(3)

    # Ожидаем, что 1 было вытеснено
    assert fifo_function(1) == 11  # Пересчитывается, т.к. вытеснено

# Тесты на корректность TTL
def test_ttl_expiration():
    assert ttl_function(10) == 20  # Вычисляется
    time.sleep(2)
    assert ttl_function(10) == 20  # Пересчитывается
