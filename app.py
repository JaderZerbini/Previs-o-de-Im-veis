from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates') # Importante adicionar essa linha e o render_template

@app.route('/')  # Rota para a página inicial
def index():
    return render_template('index.html')

# Carregar o modelo treinado
filename = 'modelo_preco_casas.pkl'
try:
    model = pickle.load(open(filename, 'rb'))
except FileNotFoundError:
    print(f"Erro: Arquivo '{filename}' não encontrado. Certifique-se de que o arquivo está no mesmo diretório do script.")
    exit()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obter os dados do request
        data = request.get_json()

        # Extrair os valores das características do imóvel
        classif_bairro = float(data['classif_bairro'])
        area_terreno = float(data['area_terreno'])
        area_construida = float(data['area_construida'])
        quartos = float(data['quartos'])
        banheiros = float(data['banheiros'])
        classif_casa = float(data['classif_casa'])
        casa_predio = float(data['casa_predio'])
        energ_solar = float(data['energ_solar'])
        mov_planejados = float(data['mov_planejados'])

        # Criar um array com os dados para a predição
        features = np.array([[classif_bairro, area_terreno, area_construida, quartos, banheiros, classif_casa, casa_predio, energ_solar, mov_planejados]])

        # Fazer a predição
        prediction = model.predict(features)[0]

        # Formatar a predição
        prediction = round(prediction, 3)

        # Retornar a predição como JSON
        return jsonify({'preco': prediction})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
