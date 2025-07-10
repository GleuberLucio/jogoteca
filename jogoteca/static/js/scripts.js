$('form input[type="file"]').change(event => {
    let arquivos = event.target.files;
    if (arquivos.length === 0) {
        console.log('sem imagem pra mostrar')
    } else {
        // Lista de tipos MIME aceitos para imagens
        const tiposAceitos = [
            'image/jpeg',
            'image/jpg',
            'image/png',
            'image/gif',
            'image/webp',
            'image/bmp'
        ];

        if (tiposAceitos.includes(arquivos[0].type)) {
            $('img').remove();
            let imagem = $('<img class="img-fluid">');
            imagem.attr('src', window.URL.createObjectURL(arquivos[0]));
            $('figure').prepend(imagem);
        } else {
            alert('Formato não suportado. Aceitos: JPG, JPEG, PNG, GIF, WebP, BMP')
        }
    }
});

// Scripts para a página de lista de jogos
document.addEventListener('DOMContentLoaded', function () {
    // Controle de alternância entre visualizações (cards/tabela)
    const btnCards = document.getElementById('btn-cards');
    const btnTable = document.getElementById('btn-table');
    const cardsView = document.querySelector('.row.g-4');
    const tableView = document.getElementById('table-view');

    if (btnCards && btnTable) {
        btnCards.addEventListener('click', function () {
            cardsView.classList.remove('d-none');
            tableView.classList.add('d-none');
            btnCards.classList.add('active');
            btnTable.classList.remove('active');
        });

        btnTable.addEventListener('click', function () {
            cardsView.classList.add('d-none');
            tableView.classList.remove('d-none');
            btnTable.classList.add('active');
            btnCards.classList.remove('active');
        });
    }
});

// Função para filtrar jogos dinamicamente
function filtrarJogos(plataforma) {
    // Remove active de todos os botões
    document.querySelectorAll('.btn-group .btn').forEach(btn => {
        btn.classList.remove('active');
    });

    // Adiciona active ao botão clicado
    event.target.classList.add('active');

    // URL da API - será definida dinamicamente no template
    let url;
    if (plataforma === 'todos') {
        url = window.urlApiJogos; // Definido no template
    } else {
        url = window.urlFiltroPlataforma.replace('PLACEHOLDER', plataforma); // Definido no template
    }

    // Fazer requisição AJAX
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                renderizarJogos(data.jogos);
            } else {
                console.error('Erro ao carregar jogos');
            }
        })
        .catch(error => {
            console.error('Erro na requisição:', error);
        });
}

// Função para renderizar os jogos
function renderizarJogos(jogos) {
    const cardsContainer = document.querySelector('.row.g-4');
    const tableBody = document.querySelector('#table-view tbody');

    // Limpar containers
    cardsContainer.innerHTML = '';
    if (tableBody) tableBody.innerHTML = '';

    // Renderizar cards
    jogos.forEach(jogo => {
        const cardHtml = `
            <div class="col-md-6 col-lg-4">
                <div class="card h-100 border-0 shadow-sm hover-elevation">
                    <div class="position-relative">
                        <img src="${window.urlImagem}${jogo.capa}" class="card-img-top" alt="${jogo.nome}">
                        <div class="position-absolute top-0 end-0 m-2">
                            <span class="badge bg-primary rounded-pill">${jogo.plataforma.toUpperCase()}</span>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <h5 class="card-title mb-0">${jogo.nome}</h5>
                            <span class="badge bg-secondary">${jogo.ano}</span>
                        </div>
                        <p class="card-text text-muted small mb-2">Desenvolvedora: ${jogo.desenvolvedora}</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="badge bg-light text-dark border">${jogo.genero}</span>
                            <small class="text-muted">#${jogo.id}</small>
                        </div>
                    </div>
                    <div class="card-footer bg-white border-top-0 d-flex justify-content-between">
                        <a href="#" class="btn btn-sm btn-outline-primary"><i class="bi bi-eye me-1"></i>Detalhes</a>
                        <div>
                            <a href="${window.urlEditar.replace('0', jogo.id)}" class="btn btn-sm btn-outline-warning me-1">
                                <i class="bi bi-pencil-square"></i>
                            </a>
                            <form action="${window.urlExcluir.replace('0', jogo.id)}" method="post" style="display:inline;">
                                <button type="submit" class="btn btn-sm btn-outline-danger" 
                                       onclick="return confirm('Tem certeza que deseja excluir ${jogo.nome}?')">
                                    <i class="bi bi-trash3-fill"></i>
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        `;
        cardsContainer.innerHTML += cardHtml;

        // Renderizar linha da tabela se existir
        if (tableBody) {
            const rowHtml = `
                <tr>
                    <td class="ps-3">${jogo.id}</td>
                    <td>${jogo.nome}</td>
                    <td>${jogo.ano}</td>
                    <td>${jogo.desenvolvedora}</td>
                    <td>${jogo.genero}</td>
                    <td><span class="badge bg-primary">${jogo.plataforma.toUpperCase()}</span></td>
                    <td class="text-end pe-3">
                        <a href="${window.urlEditar.replace('0', jogo.id)}" class="btn btn-sm btn-outline-secondary me-1">
                            <i class="bi bi-pencil"></i>
                        </a>
                        <form action="${window.urlExcluir.replace('0', jogo.id)}" method="post" style="display:inline;">
                            <button type="submit" class="btn btn-sm btn-outline-danger"
                                   onclick="return confirm('Tem certeza que deseja excluir ${jogo.nome}?')">
                                <i class="bi bi-trash"></i>
                            </button>
                        </form>
                    </td>
                </tr>
            `;
            tableBody.innerHTML += rowHtml;
        }
    });
}