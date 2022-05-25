<https://github.com/Sairyss/domain-driven-hexagon>

## Scalar types

A scalar type can be considered any type that's unknown to the Domain Model. This includes primitive types and types that don't belong to the Domain.

source: <https://github.com/Sairyss/domain-driven-hexagon#application-services>

## Pros vs Cons

Pros:

- easyly testable and scalable
- more secure
- multi teams compatible
- easier to make evolution
- easy to split, convert it in micro service

cons:

- complex
- lots of boilerplate
- may be overkill for simple app with only crud

## In short

- DTO are transmited to cli/api/event. It stimulates the system though these "primary" adapter
- Controller parse it, map it to a command/query object (create a 'command' object) and pass it to an application.
In the example, created command are send to a bus.
- Application service handle the command/query. It executes **domain logic** using **domain service** and **infrastructure layer**
Use mapper (a.k.a 'parser') to convert data to Domain Model (business model).
Use adapter (infrastructure layer) to communicate with external (a.k.a "secondary adapter", the one needed by your system)
- Job finish, it return the data back, eventually converted using mapper
- controller return it

Each layer is in charge of is own logic (single responsibility principle)

### Modules

a.k.a "components". Reflet an important concept from the domain
It encapsulate parts of a highly cohesive business domain.

- expose public (stable) api (a.k.a "mediator" or "facade"). Do not access private attr of a domain from another one, only use the public one (to avoid tight coupling and on the other hand enable loose coupling)
- no dependencies between modules. move shared logic into a third one.
- alternatively, modules can communicate using a bus message

<https://www.culttt.com/2014/12/10/modules-domain-driven-design/>

modules vs bound context? In short: Modules represent important concepts inside of Bounded Contexts. (<https://www.culttt.com/2014/11/19/bounded-contexts-context-maps-domain-driven-design>)

# Application Core

Core of the system, build using DDD building blocks

Domain layer:

- Entities
- Aggregates
- Domain Services
- Value Objects
- Domain Errors

Application layer:

- Application Services
- Commands and Queries
- Ports

## Application Services

A.k.a:

- workflow services
- use cases
- interactors
- ...

In short:

- Basically, handle the command/query.
- call outside world using adapter implementing ports
- if command or query need to call other command, query, use bus
- operate on scalar type, map them into domain TYpes, using ports if needed.
- should not depend on other app service (cyclic dependencies)
- no domain specific business logic (???????)

One service per use case is considered a good practice.
Use cases are, simply said, list of actions required from an application.

## Command and Query

basically comand modify data and query retrieves it.

command = write
query = read

By enforcing Command and Query separation, the code becomes simpler to understand. One changes something, another just retrieves data.

Also, following CQS from the start will facilitate separating write and read models into different databases if someday in the future the need for it arises.

Similarly to Commands, Queries can use a Query Bus if needed. This way you can query anything from anywhere without importing repositories directly and avoid coupling.

## Ports

interfaces (abstrac class in python) to define contracts to be implemented by adapters.
adapter perform (private) action related to tech details but exposed a public "business" api based on ports.

- It abstract tech details from the domain
- allow different implementation (polymorphism)
- Mocking and test are easier
- can delay the tech choice and the dev can still continue (mocking the interface)

# Domain Layer

This layer contains the application's business rules.

## Entities

Core. Encapsulate enterprise business rules and attr.
Can be object with properties and methods or just function or just data structures.

- entities must protect their invariant (usually the id or something that make sense, for eg, a price of an article can't be negative.).
- contain domain business logic. Avoid having bl (business logici) in service.
- strong and consistent identity
- equality is determined by comparing their identificators
