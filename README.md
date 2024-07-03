# Chat Multicast
Este é um simples aplicativo de chat multicast em Python que permite que múltiplos usuários se comuniquem em uma rede local. Este projeto faz parte de uma atividade da disciplina de Redes e Sistemas Distribuídos do curso de Análise e Desenvolvimento de Sistemas (ADS) da Universidade Federal do Cariri (UFCA).

## PDF de Referência
Para mais detalhes sobre o desenvolvimento da atividade, consulte o documento PDF fornecido no diretório do repositório.

## Como Usar

### Requisitos

- Python 3.x
- Biblioteca `socket`
- Biblioteca `json`
- Biblioteca `struct`

### Instruções

1. Clone este repositório:

    ```sh
    git clone https://github.com/seu-usuario/chat-multicast.git
    cd chat-multicast
    ```

2. Execute o script em diferentes terminais como `receptor` e `emissor`:

    ```sh
    python script.py receptor NomeDoReceptor1
    python script.py receptor NomeDoReceptor2
    python script.py emissor NomeDoEmissor1
    python script.py emissor NomeDoEmissor2
    ```

Cada terminal de receptor exibirá as mensagens enviadas pelos emissores. O chat funcionará até que um emissor envie a mensagem "sair", encerrando a comunicação.

### Estrutura do Projeto

- `chat_multicast.py`: Contém o código principal do chat multicast.
- `README.md`: Documentação do projeto.

## Navegação
* [Repositório de Atividades - Análise e Desenvolvimento de Sistemas (UFCA)](https://github.com/devitruvius/college-repository)
    * [Rede e Sistemas Distribuídos](https://github.com/devitruvius/ADS-distributed-networks-systems)

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
