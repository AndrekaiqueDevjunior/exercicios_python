
//#Uma classe pode implementar várias interfaces


interface Finalizavel {
    finalizar(): void;
}

interface Cancelavel{
    cancelar(): void;
}


class OrdemServico implements Finalizavel, Cancelavel{
    status: string = "ABERTA";

    finalizar(): void { // estamos criando o metodo finalizar que nao recebe nenhum parametro e nao retorna nenhum valor apenas this.status = "FINALIZADA"
        //que vem da interface Finalizavel
        this.status = "FINALIZADA"; //  this status significa que o status da ordem eh FINALIZADA
    }

    cancelar(): void { // estamos criando o metodo cancelar que nao recebe nenhum parametro e nao retorna nenhum valor apenas this.status = "CANCELADA"
        //que vem da interface Cancelavel

        this.status = "CANCELADA";  // this status significa que o status da ordem eh CANCELADA
    }
}

//a classe precisa cumprir os dois contratos definidos pelas interfaces:
// quais sao os contratos:  eles sao o que a classe precisa fazer para cumprir as interfaces que sao chamados de contratos, e esses contratos é o : 


//Finalizavel e Cancelavel.

