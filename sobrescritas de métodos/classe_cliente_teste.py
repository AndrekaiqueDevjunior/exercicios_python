


class Cliente:

    def __init__(self, 
        Nome, ##string
        cpf_cnpj, ##string
        Telefone, ##int
        WhatsApp, ##int
        Email, ##string
        Tipo_cliente, ##string
        Proprietario, ##string
        Comprador, ##string
        Locador, ##string
        Locatário, ##string
        Investidor, ##string
        Corretor_responsavel, ##string
        Data_do_cadastro, #int
        ultimo_contato, #int
        Próximo_contato, ##int
        Observacoes ##string
                 )

        self.Nome = Nome
        self.cpf_cnpj = cpf_cnpj
        self.Telefone = Telefone
        self.WhatsApp = WhatsApp
        self.Email = Email
        self.Tipo_cliente = Tipo_cliente
        self.Proprietario = Proprietario
        self.Comprador = Comprador
        self.Locador = Locador
        self.Locatário = Locatário
        self.Investidor = Investidor
        self.Corretor_responsavel = Corretor_responsavel
        self.Data_do_cadastro = Data_do_cadastro
        self.ultimo_contato = ultimo_contato
        self.Próximo_contato = Próximo_contato
        self.Observacoes = Observacoes