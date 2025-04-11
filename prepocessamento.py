import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import pickle
import numpy as np  # Importe numpy

# 1. Carregar os dados do arquivo CSV
try:
    df = pd.read_csv("T1 RODRIGO.csv", sep=';')
except FileNotFoundError:
    print("Erro: Arquivo 'T1 RODRIGO.csv' não encontrado. Certifique-se de que o arquivo está no mesmo diretório do script.")
    exit()

# 2. Limpar a coluna 'preco'
df['preco'] = df['preco'].str.replace('.', '', regex=False)
df['preco'] = df['preco'].astype(float)

# 3. Definir as variáveis independentes (X) e a variável dependente (y)
X = df[['classif_bairro', 'area_terreno', 'area_construida', 'quartos', 'banheiros', 'classif_casa', 'casa_predio', 'energ_solar', 'mov_planejados']]
y = df['preco']

# 4. Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Avaliar o modelo
y_pred = model.predict(X_test)

# Calcular R² Score
r2 = r2_score(y_test, y_pred)

# Calcular RMSE (Root Mean Squared Error)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))


print(f"R² Score: {r2}")
print(f"RMSE: {rmse}")

# Verificar se a acurácia atende ao mínimo de 80% (0.8)
if r2 >= 0.8:
    print("Acurácia do modelo atende ao mínimo de 80%.")
else:
    print("Acurácia do modelo não atende ao mínimo de 80%.")

# 7. Salvar o modelo treinado
filename = 'modelo_preco_casas.pkl'
pickle.dump(model, open(filename, 'wb'))

print(f"Modelo treinado e salvo como '{filename}'")