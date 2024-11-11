from cache_decorator import expensive_function

print(expensive_function(2))  # Кэшируется
print(expensive_function(2))  # Из кэша
print(expensive_function(3))  # Кэшируется
print(expensive_function(4))  # Кэшируется, вытесняет старейшее значение для LRU
print(expensive_function(2))  # Должно быть пересчитано, так как было вытеснено