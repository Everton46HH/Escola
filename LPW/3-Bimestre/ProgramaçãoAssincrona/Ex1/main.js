const minhaPromise = new Promise((resolve, reject) => {
    const sucesso = true; // Simulação de uma operação bem-sucedida
    if (sucesso) {
        resolve(5); // Passe o valor que desejar
    } else {
        reject("Houve um erro");
    }
});

minhaPromise
    .then((resultado) => {
        console.log("Sucesso:", resultado);
        return resultado * 2;
    })
    .then((dobro) => {
        console.log('Dobro:', dobro);
    })
    .catch((erro) => {
        console.log("Erro:", erro);
    })
    .finally(() => {
        console.log("Concluído");
    });

    