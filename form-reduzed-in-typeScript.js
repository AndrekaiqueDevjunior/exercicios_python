//forma reduzida no TypeScript

//no typescript, podemos reduzir o codigo do constructor usando public
//  ou private na frente dos parametros do constructor, assim nao precisamos declarar os atributos da classe 
// e nem inicializa-los dentro do constructor, o TypeScript faz isso automaticamente para nos.

class OrdemServico{
    public status: string = "ABERTA";// o que isso significa aqui ? significa que o atributo status da 
    //classe OrdemServico é do tipo string e seu valor inicial é "ABERTA".
    //logo ela inicia como o status INICIAL COMO ABERTA, e depois pode ser finalizada, que é um dos status que estamos trabalhando.


    constructor(
        public cliente: string,
        public descricao: string,
        public valor: number
    ) {}

    finalizar(): void {
        this.status = "FINALIZADA";
    }
}

//isso

constructor( // isso é um metodo especial chamado constructor, que é chamado automaticamente quando criamos um objeto da classe OrdemServico.
    public descricao: string, // isso significa que o atributo descricao da classe OrdemServico é do tipo string e é publico, ou seja, pode ser acessado por outras classes ou objetos fora da classe OrdemServico.
    public cliente: string, // isso significa que o atributo cliente da classe OrdemServico é do tipo string e é publico, ou seja, pode ser acessado por outras classes ou objetos fora da classe OrdemServico.
    public valor: number // isso significa que o atributo valor da classe OrdemServico é do tipo number e é publico, ou seja, pode ser acessado por outras classes ou objetos fora da classe OrdemServico.

    //logo descricao, cliente, valor sao atributos da classe OrdemServico, e sao inicializados com os valores passados como parametros do constructor.
    
) {}  // o que significa {} ? significa que o constructor nao tem nenhum corpo, ou seja, ele nao faz nada alem de inicializar 
// os atributos da classe com os valores passados como parametros.
// ou seja esta publicando os atributos da classe que sao cliente, descricao e valor, e inicializando eles com os valores passados como parametros do constructor.
//por que usamos construtor ? porque o constructor é um metodo especial que é chamado automaticamente quando criamos um objeto da classe.
//ou seja, quando criamos um objeto da classe OrdemServico, o constructor é chamado automaticamente e inicializa os atributos da classe com os valores passados como 
//parametros do constructor. e o que significa public ? significa que os atributos da classe sao publicos, ou seja, podem ser acessados por outras classes ou objetos 
// fora da classe OrdemServico.
