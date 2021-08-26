Register
======

.. automodule:: accounts.views
   :members:
   :undoc-members:

`/register <http://127.0.0.1:8000/register/>`_

* When this url gets hit, the respective view "register" is called. A "GET" request is sent to the server by default.

**Method: GET**

* When the "GET" request is sent to the server, the view returns a register form.

.. list-table:: **Register form**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Full Name
     - Text
     - Required
   * - Email
     - Email
     - Required
   * - Password
     - Password
     - Required


**Method: POST**

* The values entered in the fields are submitted to the server via POST request. Validation of the inputs is carried out. And, if the input passes the validation, the data is saved in the database using save() function. And, an activation mail is sent to the user's email.

**Response**

* Based on the input data, the server sends different responses. Using the django messages framework, a success message is displayed if the data is valid whereas an error message is displayed if the data is invalid.
