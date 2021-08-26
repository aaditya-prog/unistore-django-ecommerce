Store
======

`/store <http://127.0.0.1:8000/store/>`_

* When this url gets hit, the respective view "index" is called. A "GET" request is sent to the server by default.

**Method: GET**

* When the "GET" request is sent to the server, the view renders the template and all the products from the "Products" model using queryset. Products can also be sorted on the basis of their categories.
* To improve the user experience, django paginator has been used to filter only few products at a single page.
* To order, add items to the cart, or see the cart, the user must be authenticated.


.. list-table:: **Add to cart Form**, Action: **store:cart**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Product ID
     - Hidden
     - Required
   * - User ID
     - Hidden
     - Required
   * - Quantity
     - Hidden
     - Required


.. list-table:: **Direct Order Form**, Action: **store:order-now**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Product ID
     - Hidden
     - Required
   * - User ID
     - Hidden
     - Required
   * - Quantity
     - Hidden
     - Required
