// Função principal que orquestra o cálculo e a exibição do resultado
function calcularRankeadas(vitorias, derrotas) {
    const saldoVitorias = calcularSaldo(vitorias, derrotas);
    const nivel = determinarNivel(vitorias);
    exibirMensagem(saldoVitorias, nivel);
}

// Função para calcular o saldo de vitórias
function calcularSaldo(vitorias, derrotas) {
    return vitorias - derrotas;
}

// Função para determinar o nível com base nas vitórias usando switch
function determinarNivel(vitorias) {
    switch (true) {
        case (vitorias < 10):
            return "Ferro";
        case (vitorias >= 11 && vitorias <= 20):
            return "Bronze";
        case (vitorias >= 21 && vitorias <= 50):
            return "Prata";
        case (vitorias >= 51 && vitorias <= 80):
            return "Ouro";
        case (vitorias >= 81 && vitorias <= 90):
            return "Diamante";
        case (vitorias >= 91 && vitorias <= 100):
            return "Lendário";
        default:
            return "Imortal";
    }
}

// Função para exibir a mensagem final
function exibirMensagem(saldoVitorias, nivel) {
    console.log(`O Herói tem de saldo de ${saldoVitorias} e está no nível de ${nivel}`);
}

// Função main que inicia o programa
function main() {
    // Exemplos de entrada (pode ser modificado conforme necessário)
    const vitorias = 55;
    const derrotas = 30;

    // Chama a função principal
    calcularRankeadas(vitorias, derrotas);
}

// Executa a função main
main();
