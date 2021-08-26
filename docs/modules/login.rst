Login
======

.. automodule:: accounts.views
   :members:
   :undoc-members:

`/login <http://127.0.0.1:8000/login/>`_

* When this url gets hit, the respective view "user_login" is called. A "GET" request is sent to the server by default.


**Method: GET**

* When the "GET" request is sent to the server, the view returns a login form.

.. list-table:: **Login form**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Email
     - Email
     - Required
   * - Password
     - Password
     - Required

**Method: POST**

* The values entered in the fields (email and password) are submitted to the server via POST request. If the email and password gets matched, the user is authenticated to the website.


**Response**

* Based on the input data, the server sends different responses. Using the django messages framework, a success message is displayed if the data is valid whereas an error message is displayed if the data is invalid.

* If the user is an admin, the user is redirected to the admin page at http://127.0.0.1:8000/staff/view-user. Whereas, if the user is a normal user, he/she is redirected to the home page at http://127.0.0.1:8000
