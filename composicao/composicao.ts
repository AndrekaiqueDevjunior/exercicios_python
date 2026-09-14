// - COMPOSIÇÃO


// COMPOSICAO SIGNIFICA CRIAR UMA CLASSE USANDO OUTRAS CLASSES.

//UMA ORDEM DE SERVICO PODE POSSUIR VARIOS ITENS

class ItemServico{
    constructor(
        public descricao: string,
        public quantidade: number,
        public precoUnitario: number
    ) {}

    calcularSubTotal(): number {
        return this.quantidade * this.precoUnitario;
    }
}

class OrdemServico{
    private itens: ItemServico[] = [];


    adicionarItem(item: ItemServico): void {
        this.itens.push(item);
    }
}

//Aqui 

OrdemServico

// é composta por vários:

ItemServico

// em projetos modernos, composicao costuma ser mais utilizada  do que herança