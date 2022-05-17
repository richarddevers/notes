<https://github.com/Sairyss/domain-driven-hexagon>

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

- DTO (data transfert object <https://martinfowler.com/eaaCatalog/dataTransferObject.html> ) are transmit to cli/api/event. It stimulates the system though these "primary" adapter

- Controller parse it, map it to a command/query object and pass it to an application
- Application service handle it. It executes **business logic**.
Use mapper (a.k.a 'parser') to convert data to Domain Model (business model).
Use adapter to communicate with external (a.k.a "secondary adapter", the one needed by your system)
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
