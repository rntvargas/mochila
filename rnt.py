import streamlit as st

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

def find_path(start, end):
    # Suponiendo un simple camino directo de A a B
    return f"Path from {start} to {end}: {start} -> {end}"

st.title("problema de la Mochila con Recorrido de Punto A a B")

st.header("configuración del Problema de la Mochila")

num_items = st.number_input("numero de objetos", min_value=1, value=1, step=1)

values = []
weights = []
for i in range(num_items):
    value = st.number_input(f"Valor del objeto {i+1}", min_value=0)
    weight = st.number_input(f"Peso del objeto {i+1}", min_value=0)
    values.append(value)
    weights.append(weight)

capacity = st.number_input("Capacidad de la mochila", min_value=0)

if st.button("Resolver problema de la mochila"):
    max_value = knapsack(values, weights, capacity)
    st.success(f"El valor máximo que se puede obtener es: {max_value}")

st.header("Recorrido de un punto A a un punto B")

start_point = st.text_input("Punto de inicio (A)")
end_point = st.text_input("Punto de destino (B)")

if st.button("Calcular recorrido"):
    path = find_path(start_point, end_point)
    st.success(path)
