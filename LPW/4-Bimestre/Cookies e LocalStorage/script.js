document.getElementById("meuFormulario").addEventListener("submit", (event) => {
    event.preventDefault();
    
    let nome = document.getElementById('nome').value;
    
    document.cookie = `username=${nome}; path=/; max-age=1000`;

    const username = document.cookie
        .split('; ')
        .find(row => row.startsWith('username='))
        ?.split('=')[1]; // O operador ?. evita erro caso o cookie não exista

    localStorage.setItem('age', document.getElementById('idade').value);

    console.log(`Olá ${username}, você tem ${localStorage.getItem('age')} anos`);

});


document.addEventListener('DOMContentLoaded', () => {
    verificarTema(); // Aplica o tema salvo no localStorage ao carregar a página
});

function verificarTema() {
    const checkbox = document.getElementById('tema');
    const temaSalvo = localStorage.getItem('tema');

    if (temaSalvo === 'true') {
        document.body.style.backgroundColor = 'black';
        checkbox.checked = true;
    } else {
        document.body.style.backgroundColor = 'white';
        checkbox.checked = false;

    }
}

function mudarTema() {
    const checkbox = document.getElementById('tema');
    
    if (checkbox.checked) {
        localStorage.setItem('tema', 'true');
        document.body.style.backgroundColor = 'black';
    } else {
        localStorage.setItem('tema', 'false');
        document.body.style.backgroundColor = 'white';
    }
}
