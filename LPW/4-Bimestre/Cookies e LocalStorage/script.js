document.getElementById("meuFormulario").addEventListener("submit", (event) => {
    event.preventDefault();
    
    let nome = document.getElementById('nome').value;
    
    document.cookie = `username=${nome}; path=/; max-age=10`;

    const username = document.cookie
        .split('; ')
        .find(row => row.startsWith('username='))
        ?.split('=')[1]; // O operador ?. evita erro caso o cookie não exista

    document.getElementById('nomeResp').innerHTML = `Olá, ${username}!`;

    console.log(username); // Mostra o valor do cookie no console
});
