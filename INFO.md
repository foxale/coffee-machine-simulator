### Notes:
__95%__ of the effort was put into creating scalable, modular coffee machine models with basic functionalities.   
The model and view are completely __separated__, connected only by the controller class.   
Most of the __PEP 8__ coding conventions were applied during development process along with the maxim _'A Foolish Consistency is the Hobgoblin of Little Minds'_.   
   
I treat every task as a new challenge, and every new challenge as an opportunity to improve myself. 
That's why I decided to try __TDD__ for the first time. 
All of the code in _models_ was developed only after a proper test function had been created.
It slowed the development process dramatically, but eventually I was positively surprised. 
Writing tests first saved loads of time at the end, when combining models with view and controller.
Of course, some sacrifices had to be made because of my choice. And so, the Coffee object magically appears out of nowhere, instead of coming out as the result of the (non-existing) Brewer component doing some real brewing. 

Among the features, design patterns and frameworks I rejected or postponed, were:
 - __Flask__ - the task did not require neither creating web app, nor storing data in the database; dropped to reduce complexity
 - __Django__ - an absolute overkill
 - __asyncio__ (or some other async lib) - user could change machine settings while waiting for coffee; The task clearly did not indicate this as a requirement, and so I picked simplicity over functionality
 - __producer-consumer pattern__ - so we could order multiple coffees for all our coworkers and go play some table football in the meantime; tempting, but an overkill for now 
 - __Tkinter__ (or some other GUI lib) - as clearly stated in the task description, there was absolutely no reason to waste more than 15 minutes for GUI 
 - __Docker__ - there was no indication that the code is meant for production; the dependencies are also extremely simple - just pytest and click  
 
The last commit and pull request are dated on Monday. However, the last commit containing code __did not exceed the Sunday, 11:59 PM deadline__.

__My biggest regret:__ I did not manage to write all the code using TDD. In fact, both view and controller are still untested and undocumented. I decided to meet the deadline to provide a working MVP and fill in the missing parts as soon as possible. 

