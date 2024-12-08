export function charCounter(text){
    return text.length
}

export function wordCounter(text){
    const numeroDePalavras = text.split(/\s+/).filter((palavra) => palavra.length > 0);
    return `Número de palavras: ${numeroDePalavras.length}`

}