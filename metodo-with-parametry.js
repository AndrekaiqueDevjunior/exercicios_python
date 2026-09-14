class ordemServico{
    cliente: string;
    descricao: string;
    valor: number;
    status: string;


    constructor(
        cliente: string,
        descricao: string,
        valor: number,
        status: string
    ){
        this.cliente = cliente;
        this.descricao = descricao;
        this.valor = valor;
        this.status = "ABERTA";
    }
    atualizarValor(novoValor: number): void{
        this.valor = novoValor;
    }

    finalkizar(): void{
        this.status = "FINALIZADA";
    }
}

//USO:

 const ordem1 = new OrdemServico(
    "André  kaique dell isola",
    "Formatação de computador",
    250

 );

 ordem1.atualizarValor(300);


 //agora:

 console.log(ordem1.valor);

 //resultado: 
 //300

//assinatura do metodo é:
atualizarValor(novoValor: number): void

//significa:
// o metodo recebe um numero e nao retorna nenhum valor, apenas atualiza o valor do atributo valor da classe.

//void significa que o metodo nao retorna nenhum valor, apenas realiza uma ação, 
// nesse caso, atualizar o valor do atributo valor da classe. que nosso caso é o STATUS = "ABERTA" e depois atualizamos para 300.






