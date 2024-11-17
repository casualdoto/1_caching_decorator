import time
from functools import wraps
from collections import OrderedDict, deque

class CacheManager:
    def __init__(self, strategy, cache_depth, ttl):
        """Инициализация кэша с выбранной стратегией, глубиной и TTL."""
        self.strategy = strategy
        self.cache_depth = cache_depth
        self.ttl = ttl
        self.cache = OrderedDict() if strategy == 'LRU' else {}
        self.order = deque() if strategy == 'FIFO' else None

    def get_cache(self, key):
        """Получить значение из кэша, если оно еще не устарело."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            # Проверка на истечение времени жизни
            if (time.time() - timestamp) < self.ttl:
                # Перемещаем элемент в конец для LRU
                if self.strategy == 'LRU':
                    self.cache.move_to_end(key)
                return value
            else:
                del self.cache[key]  # Удалить устаревшее значение
        return None

    def set_cache(self, key, value):
        """Сохранить значение в кэш."""
        if self.strategy == 'LRU':
            self._add_to_lru_cache(key, value)
        elif self.strategy == 'FIFO':
            self._add_to_fifo_cache(key, value)

    def _add_to_lru_cache(self, key, value):
        """Добавить значение в кэш с использованием стратегии LRU."""
        # Проверка на максимальную глубину кэша
        if len(self.cache) >= self.cache_depth:
            self.cache.popitem(last=False)  # Удалить самый старый элемент
        self.cache[key] = (value, time.time())
        self.cache.move_to_end(key)

    def _add_to_fifo_cache(self, key, value):
        """Добавить значение в кэш с использованием стратегии FIFO."""
        # Проверка на максимальную глубину кэша
        if len(self.cache) >= self.cache_depth:
            oldest_key = self.order.popleft()
            del self.cache[oldest_key]
        self.cache[key] = (value, time.time())
        self.order.append(key)

# Декоратор для кэширования
def cache_decorator(strategy='LRU', cache_depth=10, ttl=60):  # Значения по умолчанию
    """Декоратор для кэширования результатов функций."""
    cache_managers = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Создание уникального ключа для каждого вызова функции
            key = (args, frozenset(kwargs.items()))
            if func not in cache_managers:
                cache_managers[func] = CacheManager(strategy, cache_depth, ttl)

            cache_manager = cache_managers[func]
            cached_result = cache_manager.get_cache(key)
            if cached_result is not None:
                return cached_result

            # Вычисление результата и кэширование
            result = func(*args, **kwargs)
            cache_manager.set_cache(key, result)
            return result

        return wrapper

    return decorator
