# Design Process

It's an iterative process :X

## 1 - Requirements

Gathering requirements through discussion with the client
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
   - define attributes and behavior


# Design techniques: CRC

CRC (Class Responsibilty Collabortors (or Connections))
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