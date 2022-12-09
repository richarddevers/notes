Note of the specialization "Software Design and Architecture" on Coursera from the university of Alberta

# Design process

## 1 -  gathering requirements through discussion
- functional and non functional requirements
    - functional:
        - what the solutions must provide. Basically what the client want.

    - Non functional:
        - how must it provided the functional requirements in terms of:
            - security
            - quality
            - performance
            - load capability
            - green IT
            - maintability
            - backward compatibility
            - evolutabilty
            ...


## 2 - Conceptual design (WHAT?):

- high lvl representation
- mock object representation
- establish reponsibility
- CRC (class/responsibility/collaborators cards)


## 3 - Technical design (HOW?):
- lower level design
- for each objects, how can you implement it


# CRC (Class Responsibilty Collabortors (or Connections))

- for the designers to break down component (if a card is to big, there's big chances it might need to be break down into smallers cars)
- help design explicitly and physically and reorganize the design
- fast prototyping
- easy to shared and to work with

the CRC cards agencement is reffered as "CRC Models"

# Models

- Entity objects: Products or 'Actors'. Manageable objects type.
- control objects: receive events , coordinate actions and process
- boundary objects: connect the system to the outside worls. Eithers in input or ouput.

Usually expressed in visual notation using UML (unified modelling language)

# Four design principle

- What attributes and behaviors do you need to model in a class through abstraction?
- How are these attributes and behaviors grouped together and accessed through encapsulation?
- Can my classes be simplified into smaller parts using decomposition?
- Are there common things across my objects that can be generalized?



## Abstraction

- simplify a concept to his essential attributes. Remove useless details
- must make sense where the abstraction is used
- rule of least astonishment: no surprises or anything that fall beyond the scope of the current abstraction.
- usually done using a Class to define a concept and his relevant detail (attribute, property, method etc...)
- relative to the context where it's used.

## Encapsulation

- hide unwanted complexity from context. Bundle data, method, attribute, behaviors.
- expose a public interface
    - restrict private detail access. 
    - secure access 
- re-usability. You just need to know the public interface to re-use it.
- maintainability:
    - if the public interface remains the same. the internal behavior can be modify without breaking .
- black box thinking: you want a behavior from the box. You don't care how the box works inside. It's the abstraction barrier.

## Decomposition

- break down problems/objects/concept in smaller class which are easier to deal with
- allow composition by creating top lvl class that can be composed by using smaller part (and not though class inheritancy)
- what are the dynamic/static part of our object?

## Generalization

- in method, avoid code duplication
- in class, avoid class duplication
  - using inheritancy
  - composition


# UML

relation between object:
 - association: loosest relation. Each object can live independently from the others. Simple line
 - aggregation: stronger relation. The whole object may have the other object (part). However both can still exist without the association. Empty diamond on the whole object line.
 - composition: strongest relation. The whole object canno't exist without the part object. black diamond on the whole object line.

 *polymorphism*: description of a behavior is the same for differents objects but the implementation is different. Usually done though interface.

 *interface vs abstract class*:
 interface define behavior and attribute without implementation.
 abstract class can specify an implementation.

 # Coupling and Cohesion

 - cohesion: what's the responsibility of my object?  the fewer the better. high cohesion is good.
 - coupling: depends on external objects. relationship between object can break without modifying or breaking each object. 

 # Conceptual integrity

 It's about implementing the service/software in a consistent manner. The software/service must look like it have been created/designed by one person.
 It does not mean that people in our team don't get to voice their opinion, or their opinions will be ignore. It's about agreeing on design principle and conventions. the goal is to achieve consistency.

 - guidelines (api design, naming convention)
 - communication
 - daily
 - sprint review
 - code review
 - restrict code review to selected core-members who will ensure that the code respect the overall design considerations.


>Conceptual integrity is often quoted as being the most important consideration in
system design.
Fred Brooks, a well known computer architect, states in his book,
The Mythical Man-Month, it is better to have a system omit certain anomalous
features and improvements, but to reflect one set of design ideas,
than to have one that contains many good but independent and uncoordinated ideas.
Simply put, conceptual integrity is about designing and implementing the software in
a consistent manner, as if it were written by one person. '

# Inheritance Issues

Inheritancy is full of corner case and implementation varies from one language to another.
- am I using inheritance to simply share attributes or behavior without further adding anything special in my subclasses?  If yes, it's a missuse.
- by design inheritancy is coupling.z
- Can i achieve the same things using composition? If yes, use composition.
- if you break the Liskov substitution principle: a subclass can replace a superclass if the subclass doesn't change the functionality of the superclass (eg: An overridden method of a subclass needs to accept the same input parameter values as the method of the superclass.)

Ideally, inheritancy must be kept to the minimum which is "add attribute and method" to the subclass. However, doing this would lead to use composition over inheritancy.