Home
======

http://127.0.0.1:8000

* When this url gets hit, the respective view "index" is called. A "GET" request is sent to the server by default.

**Response**

* When the "GET" request is sent to the server, the view returns the latest blogs and featured products i.e. desktops, laptops, and tablets using queryset.
* Filters and slices are used in order to return only the newly added products and blogs.
