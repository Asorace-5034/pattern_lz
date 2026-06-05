class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.config = {"Тема": "темная", "volume": 80} 

    def Change_volume(self, key, value):
        self.config[key] = value
        print(f"[LOG]: Настройка '{key}' изменена на '{value}'")
    
    def get_config(self):
        return self.config


