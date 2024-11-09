import time

class CacheManager:
    def __init__(self, strategy, cache_depth, ttl):
        """Инициализация кэша с выбранной стратегией, глубиной и TTL."""
        self.strategy = strategy
        self.cache_depth = cache_depth
        self.ttl = ttl
        self.cache = {}

    def get_cache(self, key):
        """Получить значение из кэша, если оно еще не устарело."""
        if key in self.cache:
            value, timestamp = self.cache[key]
            # Проверка на истечение времени жизни
            if (time.time() - timestamp) < self.ttl:
                return value
            else:
                del self.cache[key]  # Удалить устаревшее значение
        return None

    def set_cache(self, key, value):
        """Сохранить значение в кэш."""
        if self.strategy == 'LRU':
            """ Закомментировано для тестирования (будет добавлено третьим человеком)
            # self._add_to_lru_cache(key, value)"""
        elif self.strategy == 'FIFO':
            """Закомментировано для тестирования (будет добавлено третьим человеком)
            # self._add_to_fifo_cache(key, value)"""

