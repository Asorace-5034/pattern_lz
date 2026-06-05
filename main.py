from pattern import Singleton

def main():
    s1 = Singleton()
    s2 = Singleton()
    a = int(input("На сколько изменить volume: "))
    print("--- Меняем громкость ---")
    s1.Change_volume("volume", a)
    print(f"Текущие настройки в s2: {s2.get_config()}")



if __name__ == "__main__":
    main()