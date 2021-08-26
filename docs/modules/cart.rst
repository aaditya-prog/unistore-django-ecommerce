Cart
======

`/store/cart <http://127.0.0.1:8000/store/cart>`_

* This URL gets hit when the user submits a form from `/store/cart <http://127.0.0.1:8000/store/cart>`_. A POST request is sent, and the forms consists of the following inputs.

.. list-table:: **Add to cart form**
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

**Response**

* Based on the input data, the server sends different responses. Using the django messages framework, a success message is displayed if the data is valid whereas an error message is displayed if the data is invalid. The product, quantity, and user are saved to the "Cart" model using the save() function.
