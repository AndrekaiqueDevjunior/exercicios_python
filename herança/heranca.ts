// herança 

//voce ja viu a ideia mas falt  a praticar:

class Usuario {
    constructor(
        public nome: string,
        public email: stringtring
    ) { }
}


class Tecnico extends Usuario {
    constructor(
        nome: string,
        email: string,
        public especialidade: string
    ) {
        super(nome, email);
    }
}

//precisamos estudar com atencao:
//extends;
//super;
//metodos herdados;
//sobrescritas de metodos
//quando usar herança;

//quando nao usar herança

//herança  mal utilizada pode deixar o sistema muito acoplado e dificil de alterar



//polimmorfismo na pratica

//o polimorfismo fica mais claro usando pagando ou notificacoes;

