import time
import random
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt


# задание 1
class Graph:
    def __init__(self):
        self.nodes = set()  # множество для хранения вершин
        self.edges = {}  # словарь для хранения ребер

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))


def dijkstra(graph, start):
    # Инициализация
    distance = {node: float('infinity') for node in graph.nodes}
    distance[start] = 0
    unvisited_nodes = list(graph.nodes)

    while unvisited_nodes:
        # Извлечение вершины с наименьшим расстоянием
        current_node = min(unvisited_nodes, key=lambda node: distance[node])
        unvisited_nodes.remove(current_node)

        # Обновление расстояний для соседей текущей вершины
        for neighbor, weight in graph.edges[current_node]:
            new_distance = distance[current_node] + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

    return distance


# задание 2
def read_graph_from_file():
    graph = Graph()
    with open("graph_matrix.txt", 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            row_values = list(map(int, line.split()))
            graph.add_node(str(i))
            for j, value in enumerate(row_values):
                if value != 0:
                    graph.add_edge(str(i), str(j), value)
    return graph


# задание 3
def visualize_graph(graph):
    G = nx.Graph()
    for node in graph.nodes:
        G.add_node(node)
        for neighbor, weight in graph.edges[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black",
            font_weight="bold", font_family="arial")
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Визуализация графа")
    plt.show()


def show_shortest_distance(graph, start, end):
    shortest_distances = dijkstra(graph, start)
    result_label.config(text=f"Кратчайшее расстояние от {start} до {end}: {shortest_distances[end]}")


def on_submit():
    start_node = start_var.get()
    end_node = end_var.get()
    show_shortest_distance(graph, start_node, end_node)


def visualize_graph_button():
    visualize_graph(graph)


def read_and_visualize_graph():
    global graph
    graph = read_graph_from_file()
    visualize_graph(graph)


# задание 4
# Функция для измерения времени выполнения
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


def generate_graph(nodes, edges):
    graph = Graph()

    for i in range(nodes):
        graph.add_node(str(i))

    for _ in range(edges):
        from_node = str(random.randint(0, nodes - 1))
        to_node = str(random.randint(0, nodes - 1))
        weight = random.randint(1, 10)
        graph.add_edge(from_node, to_node, weight)

    return graph


# Пример использования 1
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")

graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 2)
graph.add_edge("C", "D", 1)
graph.add_edge("A", "D", 3)

start_node = "A"
end_node = "D"

shortest_distances = dijkstra(graph, start_node)

print(f"1) Кратчайшее расстояние от {start_node} до {end_node}: {shortest_distances[end_node]}")
print("_________________________________")

# Пример использования 2
graph = read_graph_from_file()

start_node = "0"  # Выберите начальную вершину
end_node = "3"  # Выберите конечную вершину

shortest_distances = dijkstra(graph, start_node)

print(f"2) Кратчайшее расстояние от {start_node} до {end_node}: {shortest_distances[end_node]}")
print("_________________________________")

# Пример использования 3
# Создаем GUI
root = tk.Tk()
root.title("Граф и кратчайшее расстояние")

# Фрейм для ввода вершин
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Label и Entry для начальной вершины
start_label = ttk.Label(input_frame, text="Начальная вершина:")
start_label.grid(row=0, column=0, padx=5, pady=5)
start_var = tk.StringVar()
start_entry = ttk.Entry(input_frame, textvariable=start_var)
start_entry.grid(row=0, column=1, padx=5, pady=5)

# Label и Entry для конечной вершины
end_label = ttk.Label(input_frame, text="Конечная вершина:")
end_label.grid(row=0, column=2, padx=5, pady=5)
end_var = tk.StringVar()
end_entry = ttk.Entry(input_frame, textvariable=end_var)
end_entry.grid(row=0, column=3, padx=5, pady=5)

# Кнопка для запуска алгоритма
submit_button = ttk.Button(input_frame, text="Найти кратчайшее расстояние", command=on_submit)
submit_button.grid(row=0, column=4, padx=5, pady=5)

# Кнопка для визуализации графа
visualize_button = ttk.Button(input_frame, text="Визуализировать граф", command=visualize_graph_button)
visualize_button.grid(row=0, column=5, padx=5, pady=5)

# Кнопка для визуализации графа из файла
visualize_file_button = ttk.Button(input_frame, text="Визуализировать граф из файла", command=read_and_visualize_graph)
visualize_file_button.grid(row=0, column=6, padx=5, pady=5)

# Label для отображения результата
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

# Пример использования 4
node_counts = [10, 50, 100]  # Список с разным числом узлов
edge_counts = [20, 100, 200]  # Список с разным числом рёбер

# Таблица для хранения результатов
results_table = []

for nodes in node_counts:
    for edges in edge_counts:
        graph = generate_graph(nodes, edges)  # Замените generate_graph на свою функцию создания графа

        # Измерение времени выполнения для функции dijkstra
        execution_time = measure_time(dijkstra, graph, start_node)

        # Сохранение результатов в таблицу
        results_table.append({'Nodes': nodes, 'Edges': edges, 'Time': execution_time})

# Вывод результатов
print("Results Table:")
print("Nodes\tEdges\tTime")
for result in results_table:
    print(f"{result['Nodes']}\t\t{result['Edges']}\t\t{result['Time']}")
