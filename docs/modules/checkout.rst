Checkout
========

`/store/checkout <http://127.0.0.1:8000/store/checkout>`_

* When this url gets hit, the respective view "checkout" is called. A "GET" request is sent to the server by default.

**Method: GET**

* When the "GET" request is sent to the server, the view renders the template and all the cart from the "Cart" model using queryset.
* The user must be authenticated to access this template


.. list-table:: **Order Form**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Receiver
     - Text
     - Required
   * - Phone
     - Text
     - Required
   * - Email
     - Email
     - Required
   * - City
     - Text
     - Required
   * - Street
     - Text
     - Required
   * - Building
     - Text
     - Required
   * - Payment
     - Select
     - Required
