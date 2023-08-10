import numpy as np
from time import perf_counter
import json

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def linear_search_file(file_obj, x):
    file_obj.seek(0, 2)
    total_elements = file_obj.tell() // 8  
    file_obj.seek(0)

    for index in range(total_elements):
        num = np.fromfile(file_obj, dtype=np.uint64, count=1)[0]
        if num == x:
            return index
    return -1

def binary_search_file(file_obj, x):
    low = 0
    high = (file_obj.seek(0, 2) // 8) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        file_obj.seek(mid * 8)
        num = np.fromfile(file_obj, dtype=np.uint64, count=1)[0]

        if num < x:
            low = mid + 1
        elif num < x:
            high = mid - 1
        else:
            return mid
    return -1

def performance(function, args, repetitions=10):
    total_time = 0
    for _ in range(repetitions):
        start = perf_counter()
        r = function(*args)
        stop = perf_counter()
        total_time += (stop - start)
    avg_time = total_time / repetitions
    return avg_time, r

def display_time(avg_time):
    scientific_format = "{:.10e}".format(avg_time)
    decimal_format = "{:.7f}".format(avg_time)
    return f"{scientific_format} ou {decimal_format}"

def save_to_json(data, filename="results.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    results = {}
    while True:
        print("\nMenu:")
        print("1. Testar Busca Linear em Array")
        print("2. Testar Busca Binária em Array")
        print("3. Testar Busca Linear em Arquivo")
        print("4. Testar Busca Binária em Arquivo")
        print("5. Executar Todos os Testes")
        print("6. Exibir Resultados")
        print("7. Salvar Resultados em JSON")
        print("8. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "8":
            break

        try:
            if choice != "6" and choice != "7":
                desired_mb = int(input("\nDigite o tamanho desejado em MB para os dados: "))
                num_elements = (desired_mb * 1024 * 1024) // 8
                arr = np.arange(num_elements, dtype=np.uint64)
                search_value = int(input("Digite o valor que deseja buscar: "))

            if choice == "1":
                avg_time, _ = performance(linear_search, (arr, search_value))
                results["Linear Array"] = {"Tempo médio": display_time(avg_time), "RAM": desired_mb, "Elemento": search_value}
                print(f"\nBusca Linear em Array(ram): Tempo médio: {display_time(avg_time)}s")
            elif choice == "2":
                avg_time, _ = performance(binary_search, (arr, search_value))
                results["Binary Array"] = {"Tempo médio": display_time(avg_time), "RAM": desired_mb, "Elemento": search_value}
                print(f"\nBusca Binária em Array(ram): Tempo médio: {display_time(avg_time)}s")
            elif choice == "3":
                path = 'data.bin'
                arr.tofile(path)
                with open(path, 'rb') as rf:
                    avg_time, _ = performance(linear_search_file, (rf, search_value))
                    results["Linear File"] = {"Tempo médio": display_time(avg_time), "RAM": desired_mb, "Elemento": search_value}
                    print(f"\nBusca Linear em Arquivo: Tempo médio: {display_time(avg_time)}s")
            elif choice == "4":
                path = 'data.bin'
                arr.tofile(path)
                with open(path, 'rb') as rf:
                    avg_time, _ = performance(binary_search_file, (rf, search_value))
                    results["Binary File"] = {"Tempo médio": display_time(avg_time), "RAM": desired_mb, "Elemento": search_value}
                    print(f"\nBusca Binária em Arquivo: Tempo médio: {display_time(avg_time)}s")
            elif choice == "5":
                avg_time, _ = performance(linear_search, (arr, search_value))
                results["Linear Array"] = {"Tempo médio": display_time(avg_time), "RAM": desired_mb, "Elemento": search_value}
                avg_time, _ = performance(binary_search, (arr, search_value))
                results["Binary Array"] = {"Tempo médio": display_time(avg_time), "RAM": desired_mb, "Elemento": search_value}
                path = 'data.bin'
                arr.tofile(path)
                with open(path, 'rb') as rf:
                    avg_time, _ = performance(linear_search_file, (rf, search_value))
                    results["Linear File"] = {"Tempo médio": display_time(avg_time), "RAM": desired_mb, "Elemento": search_value}
                    avg_time, _ = performance(binary_search_file, (rf, search_value))
                    results["Binary File"] = {"Tempo médio": display_time(avg_time), "RAM": desired_mb, "Elemento": search_value}
                print("\nTodos os testes foram executados!")
            elif choice == "6":
                print("\nResultados:")
                for key, value in results.items():
                    print(f"{key}: Tempo médio: {value['Tempo médio']}s, RAM: {value['RAM']}MB, Elemento: {value['Elemento']}")
            elif choice == "7":
                save_to_json(results)
                print("\nResultados salvos em 'results.json'")
        except ValueError:
            print("Insira um valor válido")

if __name__ == "__main__":
    main()
