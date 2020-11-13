# Cap. 7: Command pattern

## Introdução

- O padrão Comando encapsula todas as informações necessárias para executar uma ação ou acionar um evento. Essas informações são: o nome do método, o proprietário do método e os parãmetros necessários para executar esse método.
- Um exemplo simples é um assistente de instalação que contém multiplas telas que capturam as preferencias do usuário. Usa-se um objeto Command para carregar as escolhas e preferências do usuário. Quando o usuário clica em Install, o objeto Command executa um método `execute()` que considera todas as escolhas armazenadas e executa o procedimento de instalação apropriada.
- Todas as informações referentes as escolhas dos usuário são encapsulados no objeto Command que pode ser usado mais tarde para tomar uma ação.
 
## Entendendo o padrão Command

O padrão Command trabalha com os seguintes termos:

- Um objeto **Command** que sabe sobre os objetos **Receiver** e invocam o método do objeto Receiver.
- Valores para parâmetros do método do receptor(**Receiver**) são carregados no objeto Command. O Receiver sabe como realizar as operações associadas à realização da solicitação.
- O **Invoker** sabe como executar a commando.
- O cliente cria um objeto **Command** e define seu **Receiver**. 

![alt text](https://www.carloscaballero.io/content/images/2019/05/uml.png)

As principais intenções do padrão Command são as seguintes:

- Encapsula uma requisição como objeto.
- Permite parametrização dos clientes com diferentes requisições.
- Permite salvar requisições em uma fila.

O padrão Command pode ser usado nos seguintes cenários:

- Parametrizar objetos dependendo da ação ser executada.
- Adicionar ações para a fila e executar requisições em diferentes pontos.
- Criar uma estrutura para operações em alto nível que são baseadas em pequenas operações.

## Vantagens e Desvantagens

Vantagens:

- Desacopla as classes que invocam a operação do objeto que sabe como executar a operação.
- Permite criar uma sequencia de comandos providenciado por um sistema de fila.
- Extensões para adicionar um novo comando é fácil e pode ser feito sem mudar o código existente.
- Pode definir um sistema de rollback com o padrão Command em um instalador, por exemplo.

Desvantagens:

- Vai existir um número alto de classes e objetos trabalhando juntos para atingir um objetivo. Deve-se tomar cuidado para desenvolver essas classes corretamente.
- Cada comando individual é uma classe *ConcreteCommand* que aumenta o volume de classes que devem ser implementadas e mantidas.
