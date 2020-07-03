## Proxy

### O que é um proxy?

- O proxy é um sistema que intermedia entre um seeker e um provider. Seeker é
aquele que faz a requisição e o provider é aquele que entrega recursos em res-
posta a requisição Ex.: Servidor Proxy.
- No contexto de design patterns, Proxy é uma classe que age como uma interface para objetos reais.
- Proxy é um wrapper ou objeto agente que envolve o real objeto servido, até podendo
providenciar alguma funcionalidade adicional sem mudar o código do objeto real.
- Ele fornece um substituto para outro objeto, para que você possa controlar o acesso ao objeto original.
- É usado como uma camada ou interface para suporta acesso distribuído.
- Acrescente delegação e protege o componente real contra impactos indesejados.

### Scenarios

- It represents a complex system in a simpler way. For example, a system that
involves multiple complex calculations or procedures should have a simpler
interface that can act as a proxy for the benefit of the client.
- It adds security to the existing real objects. In many cases, the client is not
allowed to access the real object directly. This is because the real object can
get compromised with malicious activities. This way proxies act as a shield
against malicious intentions and protect the real object.
- It provides a local interface for remote objects on different servers. A clear
example of this is with the distributed systems where the client wants to run
certain commands on the remote system, but the client may not have direct
permissions to make this happen. So it contacts a local object (proxy) with the
request, which is then executed by the proxy on the remote machine.
- It provides a light handle for a higher memory-consuming object. Sometimes,
you may not want to load the main objects unless they're really necessary.
This is because real objects are really heavy and may need high resource
utilization. A classic example is that of profile pictures of users on a website.
You're much better off showing smaller profile images in the list view, but of
course, you'll need to load the actual image to show the detailed view of the
user profile.

### UML

::uml::
class Client

interface Subject {
    + request()
}

class RealSubject {
    + request()
}

class Proxy {
    + request()
}

hide empty members

Subject <|-- RealSubject
Subject <|-- Proxy
RealSubject <- Proxy : represents
Client --> Subject

note as N1
    <b><color:royalBlue>Proxy</color></b>
    <b>Type:</b> Structural
    Provide a surrogate or placeholder for
    another object to control access to it.
end note
::end-uml::

- **Proxy**: Providencia uma interface identica ao do **Subject**, para que o Proxy possa substituir o objeto real(RealSubject). Claramente a classe Proxy manterá uma referencia ao objeto real. Manipula as requisições do cliente e é responsável por criar e deletar RealSubject.
- **Subject**: Interface do proxy e do objeto real. Como Proxy e RealSubject implementam Subject, Proxy pode ser usado sempre que o RealSubject é experado.
- **RealSubject**: Isso define o objeto real que o proxy representa e providencia as reais funcionalidades que é usado pelo cliente.
- **Client**: Acessa a classe Proxy que controla o acesso ao **RealSubject** que contém as funcionalidades reais.

### Tipos de Proxies


- **Virtual proxy**: É um placeholder para objetos que são muito pesados para instanciar. Por exemplo, seu site pode carregar várias imagens grandes. Mas ás vezes só precisa de um ícone de cada imagem em vez da versão maior. Nesse caso, os desenvolvedores criam um ícone placeholder sugerida na página web. Quando o usuário clicar no ícone, a imagem irá ser renderizado na página economizando o custo de carregar uma imagem pesada na memória. Portanto, com proxy virtuais o objeto real só é criado quando o cliente requisita ou acessa um objeto.

- **Remote proxy**: Providência uma representação local do objeto real que reside em um servidor remoto ou diferente espaço de endereço. Por exemplo, se nos queremos monitorar a CPU e a utilização de disco desses servidores nós necessitamos de um objeto que está disponível no contexto onde a aplicação de monitoramento executa mas possa executar comandos remotos para pegar os valores de parâmetros. Nesse caso, temos um objeto proxy remoto que é uma representação local do objeto remoto.

- **Protective proxy**: Esse proxy controla acesso ao objeto de matéria sensível do objeto real. Um exemplo é em sistemas web que tem um serviço de autenticação que age como um servidor proxy de proteção responsável pela autenticação e autorização. Nesse caso, o proxy ajuda a proteger a funcionalidade core do sistema web de agentes não autorizados.

- **Smart proxy**: Proxies inteligentes interpõem ações adicionais quando um objeto é acessado. Considere que existe um componente principal no sistema que armazena estados em um local centralizado. Esse componente é chamado por vários serviços diferentes para concluir suas tarefas e pode resultar em problemas com recursos compartilhados. Em vez de os serviços invocarem diretamente o componente principal, um proxy inteligente é incorporado e verifica se o objeto real está bloqueado antes de ser acessado para garantir que nenhum outro objeto possa alterá-lo.

### Vantagens do Proxy

- Proxies podem ajudar a melhorar a performance de uma aplicação fazendo caching dos objetos maiores ou, tipicamente, objetos de acessos frequente.
- Proxies também autoriza o acesso ao objeto real. Assim, esse padrão ajuda em delegar apenas se as permissões estiverem corretas.
- Proxies remotos também facilitam a interação com servidores remotos que podem funcionar como conexões de rede e conexões de banco de dados e pode ser usado para monitorar sistemas.

### Comparando os padrões Façade e Proxy

- Ambos os padrões são padrões de projeto estruturais.
- São similares no sentido que ambos tem um objeto proxy/façade na frente dos objetos reais.

|Proxy|Façade|
|-----|------|
|Providencia um substituto para outro objeto para controle de acesso desse objeto|Providencia uma interface para um largo subsistemas de classes|
|Um objeto Proxy tem a mesma interface do objeto real e tem uma referencia para esse objeto|Minimiza a comunicação e dependencia entre os sistemas|
|Isso age como um intermediário entre o cliente e o objeto|Providencia uma interface simplificada|
