document.getElementById('predictBtn').addEventListener('click', function() {
    // Obter os valores dos campos
    const classif_bairro = document.getElementById('classif_bairro').value;
    const area_terreno = document.getElementById('area_terreno').value;
    const area_construida = document.getElementById('area_construida').value;
    const quartos = document.getElementById('quartos').value;
    const banheiros = document.getElementById('banheiros').value;
    const classif_casa = document.getElementById('classif_casa').value;
    const casa_predio = document.getElementById('casa_predio').value;
    const energ_solar = document.getElementById('energ_solar').value;
    const mov_planejados = document.getElementById('mov_planejados').value;

    // Criar o objeto com os dados
    const data = {
        classif_bairro: classif_bairro,
        area_terreno: area_terreno,
        area_construida: area_construida,
        quartos: quartos,
        banheiros: banheiros,
        classif_casa: classif_casa,
        casa_predio: casa_predio,
        energ_solar: energ_solar,
        mov_planejados: mov_planejados
    };

    // Enviar os dados para o backend usando fetch
    fetch('http://127.0.0.1:5000/predict', { // Garanta que a porta corresponde à que o Flask está rodando
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // Exibir o preço previsto na página
        document.getElementById('preco').textContent = result.preco;
    })
    .catch(error => {
        console.error('Erro:', error);
        document.getElementById('preco').textContent = 'Erro ao prever preço';
    });
});