class Heroi {
    constructor(nome, idade, tipo) {
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }

    atacar() {
        let ataque = "";
        switch (this.tipo) {
            case "mago":
                ataque = " magia";
                break;
            case "guerreiro":
                ataque = " espada";
                break;
            case "monge":
                ataque = " artes marciais";
                break;
            case "ninja":
                ataque = " shuriken";
                break;
            default:
                ataque = " um ataque desconhecido";
        }
        console.log(`O ${this.tipo} atacou usando ${ataque}`);
    }
}

function main() {
    // Exemplos de uso
    const mago = new Heroi("Merlin", 100, "mago");
    const guerreiro = new Heroi("Arthur", 35, "guerreiro");
    const monge = new Heroi("Shaolin", 40, "monge");
    const ninja = new Heroi("Hattori", 29, "ninja");

    mago.atacar();      // O mago atacou usando magia
    guerreiro.atacar(); // O guerreiro atacou usando espada
    monge.atacar();     // O monge atacou usando artes marciais
    ninja.atacar();     // O ninja atacou usando shuriken
}

// Executa o main
main();
