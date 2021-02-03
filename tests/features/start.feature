#language:pt
Funcionalidade: Como usuário do Sistema de Transaçoes gostaria de iniciar
    as funcionalidades com o processamento de transações em formato json
    no modelo bulk data

    Cenário: Iniciar o sistema informando o nome de um arquivo nos argumentos do sistema
        Dado Aplicação é iniciada para o arquivo operations.txt
        Quando Configura a classe InitializeProgram._parser
        Então Verifica se existe o arquivo
        Então Inicia o processamento das Transaçoes do arquivo

