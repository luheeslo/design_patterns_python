# Facade Pattern

## Structural Patterns

- Structural patterns describe how objects and classes can be combined to form larger structures.
- Structural patterns can be thought of as design patterns that ease the design by identifying 
simpler ways to realize or demonstrate relationships between entities. Entities mean objects or 
classes in the object-oriented world.
- While the Class patterns describe abstraction with the help of inheritance
and provide a more useful program interface Object patterns describe how
objects can be associated and composed to form larger objects. Structural
patterns are a combination of Class and Object patterns.

## Understanding the Façade design pattern

- Façade hides the complexities of the internal system and provides an interface to the client that can 
access the system in a very simplified way.
- It provides a unified interface to a set of interfaces in a subsystem and defines
a high-level interface that helps the client use the subsystem in an easy way.
- Façade discusses representing a complex subsystem with a single interface
object. It doesn't encapsulate the subsystem but actually combines the
underlying subsystems.
- It promotes the decoupling of the implementation with multiple clients.
- **Façade**: The main responsibility of a façade is to wrap up a complex group of
subsystems so that it can provide a pleasing look to the outside world.
- **System**: This represents a set of varied subsystems that make the whole
system compound and difficult to view or work with.
- **Client**: The client interacts with the Façade so that it can easily communicate
with the subsystem and get the work completed. It doesn't have to bother
about the complex nature of the system.

## The principle of least knowledge

- The design principle that is employed behind the Façade pattern is the principle of least knowledge.
- The principle of least knowledge guides us to reduce the interactions between
objects to just a few friends that are close enough to you.
- When designing a system, for every object created, one should look
at the number of classes that it interacts with and the way in which the
interaction happens.
- Following the principle, make sure that we avoid situations where there are
many classes created that are tightly coupled to each other.
- If there are a lot of dependencies between classes, the system becomes hard
to maintain. Any changes in one part of the system can lead to unintentional
changes to other parts of the system, which means that the system is exposed
to regressions and this should be avoided.
- The disadvantages of the principle of the least knowledge is that the Façade provides
a simplified interface for the clients to interact with subsystems. In the spirit of providing 
a simplified interface, an application can have multiple unnecessary interfaces that add to 
the complexity of the system and reduce runtime perfomance.
