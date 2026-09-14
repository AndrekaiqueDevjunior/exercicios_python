// associacao entre objetos

//em sistemAS  reais, os objetos se relacionam


//uma ordem de servicos pertence a um cliente:


class Cliente{
    constructor(
        public id: number,
        public nome: String
    ) {}

}

class OrdemServico{
    constructor(
        public numero: number,
        public cliente: cliente, // isso significa que
        public descricao: string
    ) {}
}

//uso:

const cliente = new  Cliente(1, "André");

const ordem = new OrdemServico(
    1001,
    cliente,
    "Manutencao do computador"
);

// agora a os contem um objeto Cliente, e nao apenas uma string.

console.log(ordem.cliente.nome)

// isso é muito importante para entender sistemas reais.

