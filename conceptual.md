### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python can be used in data science, machine learning, web development, and computing. Whereas Javascript is primarily used for web development. Python is more readable and uses indentation, whereas Javascript typically uses curly braces. Python typically runs on a server, whereas javascript can run on browsers.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

One is using the get method to get a value of a specific key. The other is using KeyError to catch an error

- What is a unit test?

When individual units are tested separate from the rest of the units in the app.

- What is an integration test?

When units are tested together

- What is the role of web application framework, like Flask?

Flask has an easy to use interface, you can define URL patterns, you can validate form inputs, and can be integrated with SQL. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  Route parameters are best for specific request. Querys are more for filters or categories rather than a specific resource. 

- How do you collect data from a URL placeholder parameter using Flask?

Define a route in URL using brackets <>, and then make an argument

- How do you collect data from the query string using Flask?

You use request object from Flask's flask module.

- How do you collect data from the body of the request using Flask?

Using POST or PUT requests

- What is a cookie and what kinds of things are they commonly used for?

A piece of data sent to a browser to store. They are used for managing sessions, personalizing settings and preferences, tracking user across internet, to authorize logging in, and to advertise based off of tracking.

- What is the session object in Flask?

USed to store information from one request to the next. 

- What does Flask's `jsonify()` do?

It converts Python data into JSON format
