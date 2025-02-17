import random
import numpy as np

# Tamaño del tablero
N = 8

# Función de evaluación: cuenta el número de conflictos entre las reinas
def fitness(board):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:  # Reinas en la misma columna
                conflicts += 1
            if abs(board[i] - board[j]) == j - i:  # Reinas en la misma diagonal
                conflicts += 1
    return conflicts

# Inicialización: genera una población de soluciones aleatorias
def generate_population(size):
    population = []
    for _ in range(size):
        individual = random.sample(range(N), N)  # Permutación aleatoria de las columnas
        population.append(individual)
    return population

# Selección de padres: selecciona dos padres usando un torneo
def select_parents(population):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda x: fitness(x))
    return tournament[0], tournament[1]  # Los dos mejores padres

# Crossover: combina los padres para crear un hijo
def crossover(parent1, parent2):
    crossover_point = random.randint(1, N-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutación: intercambia dos posiciones en el hijo
def mutate(child):
    mutation_rate = 0.1
    if random.random() < mutation_rate:
        i, j = random.sample(range(N), 2)
        child[i], child[j] = child[j], child[i]  # Intercambiar dos posiciones
    return child

# Algoritmo Genético
def genetic_algorithm(population_size, generations):
    population = generate_population(population_size)
    
    for generation in range(generations):
        # Ordenar la población por fitness
        population.sort(key=lambda x: fitness(x))
        
        # Si encontramos una solución perfecta, detenernos
        if fitness(population[0]) == 0:
            print(f"Solución encontrada en la generación {generation}:")
            print(population[0])
            return population[0]
        
        # Crear nueva población con selección, crossover y mutación
        new_population = population[:2]  # Los dos mejores padres se pasan a la siguiente generación
        
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population  # La población de la siguiente generación
    
    # Si no encontramos solución, retornamos la mejor solución
    print(f"No se encontró solución en {generations} generaciones. Mejor solución encontrada:")
    print(population[0])
    return population[0]

# Ejecutar el algoritmo genético
if __name__ == "__main__":
    population_size = 100  # Tamaño de la población
    generations = 1000  # Número de generaciones
    genetic_algorithm(population_size, generations)
