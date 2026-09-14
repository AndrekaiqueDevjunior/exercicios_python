//Classe versus objeto.


//veja a diferença entre classe e objeto.

//classe é um molde, um modelo, uma estrutura que define as características e comportamentos de um objeto. 
//Ela é como uma planta de uma casa, que define como a casa será construída, mas não é a casa em si.

//objeto é uma instância de uma classe, ou seja, é uma entidade concreta que possui as características e comportamentos definidos pela classe. 
//Ele é como a casa construída a partir da planta, que possui todas as características definidas na planta, mas é uma entidade concreta e real.


class OrdemServico{
    //molde da classe, definindo os atributos e metodos que os objetos dessa classe terão.
    //exemplo como:
    //atributos da classe, que são as caracteristicas que os objetos dessa classe terão. 
}

//isso é uma classe.

const ordem1 = new OrdemServico( //isso é um objeto, uma instancia da classe OrdemServico.
    "André",
    "Manutenção",
    250
);


//isso é um objeto criado a partir da classe.

//podemos criar vários  objetos:

const ordem1 = new OrdemServico(
    "André",
    "Manutenção",
    250
);

const ordem2 = new OrdemServico(
    "Kaique",
    "Formatação",
    400
);

const ordem3 = new OrdemServico(
    "Carlos",
    "Troca de memória",
    180
);


//cada objeto possui seu proprio estado.

console.log(ordem1.cliente); //André
console.log(ordem2.cliente); //Kaique
console.log(ordem3.cliente); //Carlos   


///se finalizarmos somente a primeira:
ordem1.finalizar();

//Teremos:


console.log(ordem1.status); //FINALIZADA
console.log(ordem2.status); //ABERTA
console.log(ordem3.status); //ABERTA

// uma instancia nao altera automaticamente as outras.


