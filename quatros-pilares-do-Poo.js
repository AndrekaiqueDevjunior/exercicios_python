// os quatros pilares da POO são: 1 encapsulamento, 2 herança, 3 polimorfismo e 4 abstração.
// a poo normalmente é ensinada por meios de quatros pilartes:


// #1 -  ENCAPSULAMENTO
// protege os dados e controla como eles podem ser alterados e acessados, garantindo que o estado do objeto seja consistente e seguro.

private valor: number;

//em vez de permitir:
ordem.valor = -500;

// criamos um metodo que valida o novo valor:

atualizarValor(novoValor: number): void { // estamos criando um metodo chamado atualizarValor que recebe um parametro chamado
//  novoValor do tipo number e nao retorna nenhum valor, apenas atualiza o valor do atributo valor da classe.
    if(novoValor < 0){
        throw new Error("O valor nao pode ser negativo"); // se o novo valor for menor que 0, lançamos um erro com a mensagem "O valor nao pode ser negativo"
    }


    this.valor = novoValor; // o this.valor se refere ao atributo valor da classe, e estamos atualizando ele com o novo valor passado como parametro do metodo.

    // o que isso significa: estamos protegendo o atributo valor da classe, garantindo que ele nunca tenha um valor negativo.
    // o this significa que estamos nos referindo ao objeto atual da classe, ou seja, o objeto que chamou o metodo atualizarValor.


}

// #2 - HERANÇA
// permite que uma classe aproveite as características de outra classe, promovendo a reutilização de código e a criação de hierarquias de classes.

class Usuario {
    Constructor(
        public nome: string,
        public email: string
    ) {}
}

class Funcionario extends Usuario { // a classe Funcionario herda os atributos e métodos da classe Usuario, ou seja, ela é uma subclasse de Usuario.
// o extends significa que a classe Funcionario é uma subclasse da classe Usuario, ou seja, ela herda os atributos e métodos da classe Usuario.
//extends serve para criar uma relação de herança entre classes, permitindo que uma classe herde os atributos e métodos de outra classe, promovendo a reutilização de código e a criação de hierarquias de classes.
// em python usamos a palavra chave "class Funcionario(Usuario):" para indicar que a classe Funcionario herda da classe Usuario

// para que vamos criar uma classe Funcionario que herda da classe Usuario ? 
// para que possamos criar objetos do tipo Funcionario que tenham os atributos e métodos da classe Usuario,
//  além de seus próprios atributos e métodos.
//qual a vantagem disso? a vantagem é que podemos criar objetos do tipo Funcionario que tenham os atributos e métodos da classe Usuario,
//  além de seus próprios atributos e métodos, sem precisar reescrever o código da classe Usuario.
// eu posso herdar de uma classe filha, e a classe filha pode ter seus próprios atributos e métodos, além dos herdados da classe pai.
// existe uma classe vô e uma classe filha, a classe filha herda os atributos e métodos da classe pai, e pode ter seus próprios atributos e métodos, além dos herdados da classe pai.




    constructor(
        nome: string,
        email: string,
        public cargo: string
    ) {
        super(nome, email); // o super é usado para chamar o construtor da classe pai (usuario) e inicializar os atributos herdados (nome e email) na classe filha
        // classe filha (Funcionario) pode ter seus próprios atributos e métodos, além dos herdados da classe pai (Usuario).
    }
    )

}   

//#funcionario herda nome e email de usuario.


//#3 - POLIMORFISMO
// permite que diferentes classes respondam ao mesmo metodo de formas diferentes, 
// permitindo que objetos de diferentes tipos sejam tratados de maneira uniforme.

class Pagamento{ // estamos criando a classe pagamento, que é a classe pai, e ela possui um método chamado processar, que é o método que será sobrescrito pelas classes filhas.
    processar(): void { // void significa que o método não retorna nenhum valor, apenas realiza uma ação, nesse caso, processar o pagamento.
        console.log("Processando pagamento");
    }
}

class PagamentoPix extends Pagamento{ // a classe PagamentoPix herda o método processar da classe Pagamento, 
// mas sobrescreve ele para implementar um comportamento específico para pagamentos via Pix.
    processar(): void { // void significa que o método não retorna nenhum valor, apenas realiza uma ação, nesse caso, processar o pagamento via Pix.
        console.log("Processando pagamento via Pix"); // console.log é usado para imprimir uma mensagem no console, nesse caso, estamos imprimindo a mensagem "Processando pagamento via Pix" quando o método processar é chamado na classe PagamentoPix.
    }
}

class PagamentoCartao extends Pagamento{ // a classe PagamentoCartao herda o método processar da classe Pagamento, 
// mas sobrescreve ele para implementar um comportamento específico para pagamentos via cartão.
    processar(): void { // void significa que o método não retorna nenhum valor, apenas realiza uma ação, nesse caso, processar o pagamento via cartão.
        console.log("Processando pagamento via Cartão");
    }
}
// entao teremos duas classes que herdam de pagamento, as formas de pagamentos será Cartao e a outra PIX, que sao classes filhas da classe Pagamento, 
// 
// e cada uma implementa o método processar de forma diferente, ou seja, cada uma tem um comportamento diferente para o mesmo método processar().

// o metodo possui o mesmo nome:
//processar()  que encontramos na classe pagamewnto, classe pagamentoPix que herda atributos da classe pagamento, 
// e na classe pagamentoCartao que herda atributos da classe pagamento, mas cada uma implementa o metodo de forma diferente, ou seja, 
// cada uma tem um comportamento diferente para o mesmo metodo processar().

///# mas cada classe executa uma ação diferente quando o método processar() é chamado, dependendo do tipo de pagamento que está sendo processado, seja via Pix ou via cartão.


//#4 - ABSTRAÇÃO

//mostra apenas o necessário e esconde a compĺexidade interna

//por exemplo:

pagamento.processar(); // aqui estamos chamando o método processar() da classe Pagamento, 
// mas não precisamos nos preocupar com os detalhes de como o pagamento é processado, seja via Pix ou via cartão.

//#quem usa esse metodo nao precisa saber internamente:
// - como a api do banco foi chamada;
// - como o token foi gerado;
// - como o pix foi criado ;
// - como a transacao foi validada;


// a pessoa apenas chama: 
processar() // e o sistema se encarrega de fazer todo o resto,
//  sem que a pessoa precise se preocupar com os detalhes internos do processo de pagamento.

// # - PARA ANOTAR NO CADERNO.

// # POO - SIGNIFICA : PROGRAMAÇÃO ORIENTADA A OBJETOS.


//CLASSE:
// É O MOLDE UTILIZADO PARA CRIAR OBJETOS, DEFININDO SEUS ATRIBUTOS E MÉTODOS.

//OBJETO:
// É UMA INSTANCIACRIADA A PARTIR DE UMA CLASSE.

//ATRIBUTO:
//É UMA INFORMAÇÃO OU DADO DO OBJETO


//METODO:
//É UMA FUNCAO QUE PERTENCE AO OBJETO, E PODE SER USADA PARA REALIZAR AÇÕES OU MODIFICAR O ESTADO DO OBJETO.


//CONSTRUCTOR :
// É EXECUTADO QUANDO UM OBJETO É CRIADO COM NEW.


//THIS:
//REPRESENTA O OBJETO ATUAL.

//NEW
// CRIA UMA NOVA INSTANCIA DE CLASSE


//ESTADO:
// SAO OS VALORES ATUAIS DOS ATRIBUTOS DO OBJETO


//EXEMPLO CENTRAL:


