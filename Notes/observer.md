# Cap. 6: Observer design pattern

1. Entender o que são os padrões de projetos comportamentais.
2. Entender o básico do padrão Observer e como isso é efetivamente usado na arquitetura de software.
3. Entender como o Observer é notificado das mudanças que acontecem no Subject.
4. Implementar o padrão baseado no diagrama UML do padrão.
5. Implementar o padrão através de um caso de uso.
5. Entender os dois modelos de implementação do padrão: push e pull.
6. Entender o princípio do baixo acoplamento no projeto de software e como esse princípio é aplicado no padrão Observer.

## Padrões de projeto comportamentais

- Os padrões comportamentais lidam com as responsabilidades e interações dos objetos entre si com o objetivo de manter o baixo acoplamento entre eles.

## Padrão Observer e casos de uso na arquitetura do software

- No padrão Observer, um objeto(**Subject**) mantém uma lista de dependentes(**Observers**) que podem ser notificados se houver alguma mudança de estado usando algum método definido pelo Observer.

- Um dos principais objetivos desse padrão é definir uma relação um-para-muitos entre objetos então qualquer mudança em um objeto será notificado para outro objeto dessa relação.

- Outro objetivo é encapsular o componente core do **Subject**.

O padrão Observer é usado nos seguintes cenários:

- Implementar o um serviço de evento em sistemas distribuídos.
- Um framework para agência de notícias.
- Múltiplos seviços podem interagir um com o outro para executar grandes operações, mas a operação que eles executam é diretamente ou fortemente dependente do estado dos objetos do serviço com os quais interagem.
- Considere um caso de um registro do usuário em que o serviço do usuário é responsável pelas operações do usuário no site. Vamos dizer que temos outro serviço chamado serviço de e-mail que observa o estado do usuário e envia e-mails para o usuário. Por exemplo, se o usuário acabou de se cadastrar, então o serviço de usuário chamará um método do serviço de e-mail que enviará um email ao usuário para verificação da conta. Se a conta for confirmada e tiver poucos créditos, o serviço de e-mail irá monitorar o serviço de usuário e enviar um alerta de e-mailpara créditos baixos ao usuário.
- Se existe um serviço core na aplicação onde muitos outros serviços são dependentes, o serviço core se torna o Subject que tem que ser observado/monitorado pelos Observer para mudanças. O Observer deve fazer mudanças no estado do seu próprios objetos ou fazer certas ações baseado nas mudanças no **Subject**.
- Considerando um blog como exemplo, você pode querer ficar atualizado com os últimos posts desse blog. Você fazer isso fazendo um subscribe nesse blog. Então qualquer atualização que acontecer no blog, você é notificado por e-mail, por exemplo. Nesse caso, o blog é o **Subject** e você é o **Observer**.

## Diagrama UML do padrão Observer

Em um diagrama UML, existe três principais participantes desse padrão:

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Observer.svg/500px-Observer.svg.png)

- **Subject**: A classe **Subject** é consciente do Observer. Essa classe tem métodos como `register` e `deregister` que são usados pelos **Observers** para registrar a si mesmos com o objeto Subject.
- **Observer**: Define uma interface para objetos que são observados pelo Subject. Isso define métodos que necessitam ser implementados pelo **Observer** para ser notificado as mudanças do **Subject**.
- **ConcreteObserver**: Esse objeto ou objetos tem estados que devem ser consistentes com o estado do **Subject**.
