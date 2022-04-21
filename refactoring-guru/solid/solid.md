# Single responsibility principle

One class =  One responsibility entirely encapsulated

From one class that do everything to multiple class with one responsibility.
Every class consume other based on his interface.

How? Identify behavior. Move it into antoher class. If data from origin class is needed, use composition to have it as parameters.

# Open/Closes principle

Classes shoulb be open for extension but closes for modification

Main idea -> keep existing code for breaking when you implement new features

Open for extension, close for modification.

Instead of modify it, you can create a subclass or a new one with composition to have the new behavior

# Liskov subtitution

a.k.a genericity

When extending a class, you should be able to pass object to the subclass in place of object of the parent class

Subclass should remain compatible with the behavior of the superclass

- param type in a method of subclass should match or be more abstract than the one in the superclass
- return type in a method of subclass should match or be more abstract than the one in the superclass
- in a subclass , thrown exceptions must be part of the one the superclass can throw
- a subclass shouldn't strenghten pre-conditions
- a subclass shouldn't weaken post-conditions (ex: connection closing)
- invariant of superclass must be preserved
- a subclass shouldn't change values of private fields of the superclass

# Interface segregation principle

clients shouldn't be forced to depends on methods they do not use
Do no hesitate to create smaller interface and implement them depending of the subclass need.

A class should not implement method interface that they do not use

If it does, you may have to split your interface

# Dependency inversion principle

low-lvl class: basic operation, technical detail (adapter in ddd)
high-lvl class: business logic. Use low-lvl class to do things (manager in ddd)

Usually, low-lvl classes are done first to understand what is possible or not.
Business logic tend to become dependant on primitive low level

To adress that:

- describe interfaces for low-lvl operations high-lvl classes rely on
- then high-lvl consume the low-lvl classes based on the interface.
- low-lvl are now dependant of the implemented interface

Basically, the low-lvl classes have a 'upper' dependency (the interface they implement).
The interface is a compatibility layer between high and low level interface
