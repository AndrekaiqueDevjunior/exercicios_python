//metodo que retorna um valor
//tambem podemos criar metodos que devolvem informacoes


calcularValorComDesconto(desconto: number): number{
    return this.valor - desconto;
}

class OrdemServico{
    cliente: string;
    descricao: string;
    valor: number;
    status: string;


    constructor(
        cliente: string,
        descricao: string,
        valor: number,

    ){
        this.cliente = cliente;
        this.descricao = descricao;
        this.valor = valor;
        this.status = "ABERTA";
    }
    finalizar(): void{
        this.status = "FINALIZADA";
    }
    atualizarValor(novoValor: number): void{
        this.valor = novoValor;
    }


    calcularValorComDesconto(desconto: number): number{
        return this.valor - desconto;;
    }
}

//Uso:

const ordem1 = new OrdemServico(
    "André  kaique dell isola",
    "Formatação de computador",
    250

);

const valorFinal = ordem1.calcularValorComDesconto(50); // o que estamos fazendo aqui é chamando o metodo calcularValorComDesconto 
// e passando o valor 50 como parametro, que é o desconto que queremos aplicar no valor da ordem de serviço. 
// O metodo vai retornar o valor final da ordem de serviço com o desconto aplicado, que no caso é 200.

//obviamente o valor do servico era 250 e aplicamos um desconto de 50 reais, entao o valor final da ordem de servico é de 200 reais.



console.log(valorFinal); //chamando o metodo calcularValorComDesconto e passando o valor 50 como parametro, 
// que é o desconto que queremos aplicar no valor da ordem de serviço.

//resultado: 
//200'


