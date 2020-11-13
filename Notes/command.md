# Cap. 7: Command pattern

## Introdução

- O padrão Comando encapsula todas as informações necessárias para executar uma ação ou acionar um evento. Essas informações são: o nome do método, o proprietário do método e os parãmetros necessários para executar esse método.
- Um exemplo simples é um assistente de instalação que contém multiplas telas que capturam as preferencias do usuário. Usa-se um objeto Command para carregar as escolhas e preferências do usuário. Quando o usuário clica em Install, o objeto Command executa um método `execute()` que considera todas as escolhas armazenadas e executa o procedimento de instalação apropriada.
- Todas as informações referentes as escolhas dos usuário são encapsulados no objeto Command que pode ser usado mais tarde para tomar uma ação.
 
## Entendendo o padrão Command

O padrão Command trabalha com os seguintes termos:

- Um objeto **Command** que sabe sobre os objetos **Receiver** e invocam o método do objeto Receiver.
- Valores para parâmetros do método do receptor(**Receiver**) são carregados no objeto Command.
- O **Invoker** sabe como executar a commando.
- O cliente cria um objeto **Command** e define seu **Receiver**. 
