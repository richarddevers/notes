- A sub­class can’t reduce the inter­face of the super­class. You have to imple­ment all abstract meth­ods of the par­ent class even if you won’t be using them.

- When over­rid­ing meth­ods you need to make sure that the new behav­ior is com­pat­i­ble with the base one. It’s impor­tant because objects of the sub­class may be passed to any code that expects objects of the super­class and you don’t want that code to break.

- Inher­i­tance breaks encap­su­la­tion of the super­class because the inter­nal details of the par­ent class become avail­able to the sub­class. There might be an oppo­site sit­u­a­tion where a pro­gram­mer makes a super­class aware of some details of sub­class­es for the sake of mak­ing fur­ther exten­sion easier.

- Sub­class­es are tight­ly cou­pled to super­class­es. Any change in a super­class may break the func­tion­al­i­ty of subclasses.

- Try­ing to reuse code through inher­i­tance can lead to cre­at­ing par­al­lel inher­i­tance hier­ar­chies. Inher­i­tance usu­al­ly takes place in a sin­gle dimen­sion. But when­ev­er there are two or more dimen­sions, you have to cre­ate lots of class com­bi­na­tions, bloat­ing the class hier­ar­chy to a ridicu­lous size.
