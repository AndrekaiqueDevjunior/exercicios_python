// polimorfismo na pratica

// o polimofirsmo fica mais claro usando pagamento ou notificacoes;

interface Notificador {
    enviar(mensagem: string): void;
}

class NotificadorEmail implements Notificador {
    enviar(mensagem: string): void {
        console.log(`Enviando e-mail: ${mensagem}`);
    }
}

class NotificadorWhatsapp implements Notificador {
    enviar(mensagem: string): void {
        console.log(`Ènviando Whatsapp: ${mensagem}`);
    }

}

//as duas classes possuem o me  todo:

enviar()

// mas cada uma executa de uma maneira diferente.


///////////////////////////////////////////////////////////////////////////////////////////////////////////
// interface é um contrato que define o que uma classe ou objeto precisa poissuir

//ela descreve:

// quais atributos devem existir

// quais metodos devem existir;

// quais tipos esses atributos e metodos utilizam

// mas a interface normalmente nao define como o metodo funciona


//exemplo:


interface Pagamento{
    processar(valor: number): void;
}


//essa interface determina:
//todo pagamento deve possuir um metodo chamado processar, que recebe um number, e nao retorna nenhum valor.

//observe que nao existe implementação

processar(valor: number): void;

//nao temos:

{

    //código

}

// a interfce apenas define a assinatura


