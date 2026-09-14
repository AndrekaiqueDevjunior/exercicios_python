//## o que significa implements?

//implements significa:

// esta classe promete cumprir o contrato definido pela interface.


//exemplo:

interface Pagamento{
    processar(valor: number) : void;
}

class PagamentoPix implements Pagamento {
    processar(valor: number): void {
        console.log(`Processando PIX de R$ ${valor}`);
    }
}

//podemos ler assim:
// a classe PagamentoPix implementa o contrato Pagamento.

//como a interface exige:

processar(valor: number): void;

// a classe é obrigado a criar esse método

// ## O QUE ACONTECE QUANDO CUMPRIMOS O CONTRATO ?

interface Pagamento{
    processar(valor: number) : void;
}

class PagamentoPix implements Pagamento {
}

// o typescript mostrará um erro.

// isso acontece porque a classe declarou:

implements Pagamento 

// mas nao criou o metodo obrigátorio:

processar(valor: number): void


// a implementação correta seria:

class PagamentoPix implements Pagamento{
    processar(valor: number): void {
        console.log(`PIX de R$ ${valor} processado`)
    }
}


//analogia simples

//imagina uma vaga de emprego para técnico:
//contrato técnico:

// -deve saber executar manutencao
// -deve saber gerar relatorio

// na programação

interface Tecnico {
    executarManutencao() : void;
    gerarRelatorio(): string;

}

//agora uma classe promete cumprir esse contrato:

class TecnicoInformatica implements Tecnico {
    executarManutencao(): void{
        console.log("Executando manutencao no computador")
    }


    gerarRelatorio(): string {
        return "Manutenção concluida"
    }
}

//a interface diz o que deve existir

// a classe diz como será feito


//exemplo com Ordem de Serviço

//vamos definir um contrato para objetos que podem ser finalizados

interface Finalizavel {
    finalizar(): void;
}

//agora a classe OrdemServico implementa esse contrato:

class OrdemServico implements Finalizavel {
    constructor(
        public id: number,
        public status: string = "ABERTA"
    ) {}

    finalizar(): void {
        this.status = "FINALIZADA";
    }
}

//uso: 

const ordem = new OrdemServico(1);

ordem.finalizar();

console.log(ordem.status);

//resultado

FINALIZADA

// A INTERFACE OBRIGOU A CLASSE A POSSUIR:

finalizar(): void


//uma interface pode exigir atributos
//uma interface nao serve apenas para metodos

//ela tambem pode exigir propriedades;

interface Cliente{
    id: number;
    nome: string;
    email: string;
}

// agora podemos  criar um objeto que respeita essa interface:


const cliente: Cliente = {
    id: 1,
    nome: "André",
    email: "andre@email.com"
}

//este objeto esta correto porque possui tudo o que a interface exige.

//ele estaria errado:

const cliente: Cliente = {
    id: 1,
    nome: "André"
};

//esta faltando:
email  

//interface usada diretamente em objetos

//nem sempre uma interface precisa ser implementada por uma classe.

// ela também pode definir o formato de um objeto:

interface CriarOrdemServicoDTO {
    clienteID: number;
    descricao: string;
    valor: number;
}
//uso:

const dados: CriarOrdemServicoDTO = {
    clienteId: 10,
    descricao: "Formatação do computador",
    valor: 250
};

// isso é muito comum em:

// payloads de API;
// formularios;
// respostas do backend;
// propriedades de componentes react;
// dados enviados para funcoes;

//interface com método e atributos

interface Notificador {
    canal: string;

    enviar(mensagem: string): void;
}

//a classe precisa implementar os dois:

class NotificadorWhatsapp implements Notificador{
    canal: string = "Whatsapp";

    enviar(mensagem: string): void {
        console.log(`Enviando Pelo Whatsapp: ${mensagem}`);
    }
}

// se faltar o atributo canal, haverá erro.

// se faltar o metodo enviar, tambem havera erro

//por que utilizar interfaces ?

//imagina que nosso sistema pode enviar notificacoes por:
// whatsapp;
// email;
// sms.

//criamos um contrato comum:

interface Notificador{
    enviar(mensagem: string): void;
}

//implementacao por whatsapp:

class NotificadorWhatsapp implements Notificador{ // class notificadorWhatsapp 
    enviar(mensagem: string): void{
        console.log(`Whatsapp: ${mensagem}`) // isso significa que 
    }
}

//implementacao por email: 

class NotificadorEmail implements Notificador{ //  classe NotificadorEmail 
    enviar(mensagem: string): void{
        console.log(`Email: ${mensagem}`);
    }
} 

//implementacao por SMS:

class NotificadorSms implements Notificador {
    enviar(mensagem: string): void {
        console.log(`SMS: ${mensagem}`)
    }
}


//todas cumprem o mesmo contrato:

enviar(mensagem: string): void


//por isso, podemos criar uma funcao que aceita qualquer notificador:

function notificarCliente(
    notificador: Notificador,
    mensagem: string
): void {
    notificador.enviar(mensagem);
}

//uso:

const whatsapp = new NotificadorWhatsapp();
const email = new NotificadorEmail();

    NotificarCliente( // significa que: 
        whatsapp,
        "Sua ordem de serviço foi criada"
    );

    notificarCliente(
        email,
        "Sua Ordem de servico foi finalizada"

    );

//# a funcao nao precisa saber exatamenter qual classe recebeu.

// ela sabe apenas que o objeto cumpre o contrato Notificador.

// esse é um exemplo de polimorfismo



//interface versus Class 
// uma interface define um contrato:

interface Pagamento { // interface significa que pagamento é um contrato que define o que uma classe ou objeto precisa possuir
    processar(valor: number): void; // processar e um metodo que recebe um valor number
}

//uma classe poissui implementacao:

class PagamentoPix{ // a classe pagamentoPix implementa o contrato Pagamento
    processar(valor: number): void{ // aqui ele esta implementando o metodo processar com valor number, e o void significa que ele nao retorna nenhum valor
        console.log("Processando PIX ") // console.log significa que ele vai imprimir uma mensagem no console
    }
}

// podemos resumir assim:

// interface = define o que deve existir
//class = define dasdos e comportamentos
// implements = obriga a classe a cumnprir a interface


//implements versus extends

//extends = heranca
//implements = polimorfismo

//essa diferença é importante

//implements = obrigatorio
//extends = opcional    

//implements 
// uma classe cumpre o contrato de uma inferface:

interface Notificador { // interface significa que pagamento é um contrato que define o que uma classe ou objeto precisa possuir
    enviar(): void; // interface significa que pagamento é um contrato que define o que uma classe ou objeto precisa possuir
}

class Email implements Notificador { // a classe email implementa o contrato Notificador
    enviar(): void {
        console.log("enviando e-mail");
    }
}

// a classe nao recebe uma implementacao pronta. ela precisa escrever o método 


//extends

//uma classe herda atributos e metodos de outra classe:

class Usuario{
    constructor( // aqui criamos um constructor que recebe public nome string  que é acessivel por outras classes ou objetos fora da classe 
        public nome: string
    ) {} // esse simbolo significa que: public significa que o atributo nome da classe Usuario eh publico, 
    // ou seja, pode ser acessado por outras classes ou objetos fora da classe Usuario.

    autenticar(): void {
        console.log("Usuario autenticado")
    } 
}


class Administrador extends Usuario { // a classe administrador herda os atributos e metodos da classe usuario 
// e tambem pode adicionar seus proprios atributos e metodos


    excluirUsuario(): void { // void significa que nao retorna nenhum valor apenas o  feedback de usuario 
        console.log("Usuário excluído");
    }
    AdicionarUsuario(): void {
        console.log("Usuário adicionado");
    }
    AtualizarUsuario(): void {
        console.log("Usuário atualizado");
    }

}

// o admionistrador herda:

nome
autenticar()
excluirUsuario()
AdicionarUsuario()
AtualizarUsuario()


//uso:

const admin = new Administrador("André"); // admin eh uma instancia da classe Administrador que recebe o nome "André"

// admin const é uma instancia da classe Administrador
// por que estamos fazendo isso ? porque estamos criando um objeto da classe Administrador
// o que é um objeto eh uma instancia de uma classe

admin.autenticar(); //
admin.excluirUsuario(); 
admin.AdicionarUsuario();
admin.AtualizarUsuario();
//portanto:

// implements = cumprir um contrato de uma interface que podem ser atributos e metodos 
//exemplo: interface Notificador { enviar(): void; }      
//   class Email implements Notificador { enviar(): void { console.log("enviando e-mail"); } }
// extends = herdar de uma classe

//uma classe pode implementar várias interfacers


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