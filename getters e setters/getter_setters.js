// getters e setters

// sao formas controladas de consultar e alterar atributos.

class OrdemServico{
    private _valor: Number;

    constructor(valor: number){
        this._valor = valor;
    }


    get valor(): number {
        return this._valor;

    }



    set valor(novoValor:number) {
        if (novoValor <= 0){
            throw new Error("Valor Inválido");
        }

        this._valor = novoValor;
    }
}

//uso:

const ordem = new OrdemServico(200);

console.log(ordem.valor);


ordem.valor = 300;

// apesar de parecer uma alteracao direta, o setter executa a validação.

// preciso aprofundar mais meu conhecimentos em getters e setters