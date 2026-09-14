//#-- ENCAPSULAMENTO

//ESTE DEVE SER O PROXIMO ESTUDO.

//VOCE PRECISA ENTENDER O CONCEITO DE ENCAPSULAMENTO, 
// POIS ELE É UM DOS PILARES DA POO (PROGRAMAÇÃO ORIENTADA A OBJETOS).

// - PUBLIC
// - PRIVATE;
// - PROTECTED;

// - POR QUE NAO DEVEMOS ALTERAR QUALQUER ATRIBUTO DE UM OBJETO DIRETAMENTE?
//VALIDACAO DENTRO DOS METODOS;

//GETTERS E SETTERS: METODOS QUE PERMITEM ACESSAR E MODIFICAR ATRIBUTOS PRIVADOS DE UM OBJETO,
// DE FORMA CONTROLADA, GARANTINDO QUE O OBJETO MANTENHA SUA INTEGRIDADE E CONSISTENCIA.
 //EXEMPLO:


class OrdemServico{ // aqui estamos criando a classe ordem Servico
    private valor: number; // decidindo que o a variavel Valor será number(numero)

    constructor(valorInicial: number){
        this.valor = valorInicial; // passando o valor  
    }

    atualizarValor(novoValor: number): void {
        if (novoValor <= 0 ){
            throw new Error("O valor deve ser maior que zero.");
        }

        this.valor = novoValor;
    }
    obterValor(): number { // aqui
        return this.valor;
    }
}

//# aqui nao podemos fazer:

ordem.valor = -500;

// como valor é private, ele so pode ser alterado pela PROPRIA CLASSE.

//isso protege a regra de negocio.

