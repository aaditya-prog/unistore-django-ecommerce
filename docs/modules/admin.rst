Admin/Staff
===========

`/staff <http://127.0.0.1:8000/staff/>`_

* An admin/staff who is usually the owner of the store can perform CRUD operations on dynamic contents such as blogs, products, and manage users.


The different requests, actions and responses carried out on hitting specific urls have been described on the basis of the urls.

Add User
********

1. `/staff/add-user <http://127.0.0.1:8000/staff/add-user>`_

* When this url gets hit, the respective view "useradd" is called. A "GET" request is sent to the server by default.

**Method: GET**

* When the "GET" request is sent to the server, the view returns a user add form.

.. list-table:: **User add form**
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
   * - Staff
     - Checkbox
     - Optional


**Method: POST**

* The values entered in the fields are submitted to the server via POST request. Validation of the inputs is carried out. And, if the input passes the validation, the data is saved in the database using save() function. Now, the credentials can be used to login. Also, when the "register as staff" checkbox is checked, the new user will be the admin and can perform CRUD operations.

**Response**

* Based on the input data, the server sends different responses. Using the django messages framework, a success message is displayed if the data is valid whereas an error message is displayed if the data is invalid.

View User
********

2. `/staff/view-user <http://127.0.0.1:8000/staff/view-user>`_

**Request**

* When this url gets hit, the respective view "view-users" is called. A "GET" request is sent to the server by default.

**Response**

* When the "GET" request is sent to the server, the view returns the list of the users using queryset.

Delete User
********

3. `/staff/delete-user/<user-id> <http://127.0.0.1:8000/staff/delete-user/100>`_

**Request**

* When this url gets hit, the respective view "delete-user" is called.

**Method: POST**
The specific <user-id> is sent in the url from the form of `/staff/view-user <http://127.0.0.1:8000/staff/view-user>`_ and passed onto the view. And, the record of the specific Id is deleted from the database using delete() method.

**Response**
Using the django messages framework, a success message stating that the data has been deleted is returned to the template.

Update User
********

4. `/staff/update-user/<user-id> <http://127.0.0.1:8000/staff/update-user/100>`_

**Request**

* When the url along with the <user-id> gets hit, the view returns the user add form with the populated data of the same ID using queryset.

.. list-table:: **User add form**
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
   * - Staff
     - Checkbox
     - Optional

**Method: POST**
The specific <user-id> is sent in the url from the form of `/staff/view-user <http://127.0.0.1:8000/staff/view-user>`_ and passed onto the view. And, the record of the specific Id is deleted from the database using delete() method.

**Response**
Using the django messages framework, a success message stating that the data has been deleted is returned to the template.

Add Category
********

5. `/staff/add-category <http://127.0.0.1:8000/staff/add-category>`_

* When this url gets hit, the respective view "categoryAdd" is called. A "GET" request is sent to the server by default.

**Method: GET**

* When the "GET" request is sent to the server, the view returns a category add form.

.. list-table:: **Category add form**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Name
     - Text
     - Required

**Method: POST**

* The values entered in the fields are submitted to the server via POST request. Validation of the inputs is carried out. And, if the input passes the validation, the data is saved in the "Category" model using save() method.

**Response**

* Based on the input data, the server sends different responses. Using the django messages framework, a success message is displayed if the data is valid whereas an error message is displayed if the data is invalid.

View Category
********

6. `/staff/view-category <http://127.0.0.1:8000/staff/view-category>`_

**Request**

* When this url gets hit, the respective view "caregoryRead" is called. A "GET" request is sent to the server by default.

**Response**

* When the "GET" request is sent to the server, the view returns the list of the categories using queryset.

Delete Category
********

7. `/staff/delete-category/<category-id> <http://127.0.0.1:8000/staff/delete-category/100>`_

**Request**

* When this url gets hit, the respective view "delete-category" is called.

**Method: POST**
The specific <category-id> is sent in the url from the form of `/staff/view-category <http://127.0.0.1:8000/staff/view-category>`_ and passed onto the view. And, the record of the specific Id is deleted from the "Category" model using delete() method.

**Response**
Using the django messages framework, a success message stating that the data has been deleted is returned to the template.

Update Category
********

8. `/staff/update-category/<category-id> <http://127.0.0.1:8000/staff/update-category/100>`_

**Request**

* When the url along with the <category-id> gets hit, the view returns the user add form with the populated data of the same ID using queryset.

. list-table:: **Category update form**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Name
     - Text
     - Required

**Method: POST**
The specific <category-id> is sent in the url from the form of `/staff/view-category <http://127.0.0.1:8000/staff/view-category>`_ and passed onto the view. And, the record of the specific Id is deleted from the "Category" model using delete() method.

**Response**
Using the django messages framework, a success message stating that the data has been deleted is returned to the template.

Add Product
********

9. `/staff/add-product <http://127.0.0.1:8000/staff/add-product>`_

* When this url gets hit, the respective view "productAdd" is called. A "GET" request is sent to the server by default.

**Method: GET**

* When the "GET" request is sent to the server, the view returns a product add form.

.. list-table:: **Product add form**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Name
     - Text
     - Required
   * - Price
     - Number
     - Required
   * - Image
     - File
     - Required
   * - Category
     - Select
     - Required

**Method: POST**

* The values entered in the fields are submitted to the server via POST request. Validation of the inputs is carried out. And, if the input passes the validation, the data is saved in the "Product" model using save() method.

**Response**

* Based on the input data, the server sends different responses. Using the django messages framework, a success message is displayed if the data is valid whereas an error message is displayed if the data is invalid.

View Product
********

10. `/staff/view-product <http://127.0.0.1:8000/staff/view-product>`_

**Request**

* When this url gets hit, the respective view "productAdd" is called. A "GET" request is sent to the server by default.

**Response**

* When the "GET" request is sent to the server, the view returns the list of the the products from the "Product" model using queryset.

Delete Product
********

11. `/staff/delete-product/<product-id> <http://127.0.0.1:8000/staff/update-product/100>`_

**Request**

* When this url gets hit, the respective view "delete-product" is called.

**Method: POST**
The specific <product-id> is sent in the url from the form of `/staff/view-product <http://127.0.0.1:8000/staff/view-product>`_ and passed onto the view. And, the record of the specific Id is deleted from the "Product" model using delete() method.

**Response**
Using the django messages framework, a success message stating that the data has been deleted is returned to the template.

Update Product
********

12. `/staff/update-product/<product-id> <http://127.0.0.1:8000/staff/update-product/100>`_

**Request**

* When the url along with the <product-id> gets hit, the view returns the product add form with the populated data of the same ID using queryset.

. list-table:: **Product update form**
   :widths: 25 25 25
   :header-rows: 1

    * - Fields
     - Input Type
     - Attribute
   * - Name
     - Text
     - Required
   * - Price
     - Number
     - Required
   * - Image
     - File
     - Required
   * - Category
     - Select
     - Required

**Method: POST**
The specific <product-id> is sent in the url from the form of `/staff/view-product <http://127.0.0.1:8000/staff/view-product>`_ and passed onto the view. And, the record of the specific Id is deleted from the "Product" model using delete() method.

**Response**
Using the django messages framework, a success message stating that the data has been deleted is returned to the template.


Add BLog
********

13. `/staff/add-blog <http://127.0.0.1:8000/staff/add-blog>`_

* When this url gets hit, the respective view "BlogAdd" is called. A "GET" request is sent to the server by default.

**Method: GET**

* When the "GET" request is sent to the server, the view returns a blog add form.

.. list-table:: **Blog add form**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Title
     - Text
     - Required
   * - Description
     - TinyMCE
     - Required
   * - Date
     - File
     - Required
   * - Image
     - File
     - Required
   * - Url
     - Text
     - Required


**Method: POST**

* The values entered in the fields are submitted to the server via POST request. Validation of the inputs is carried out. And, if the input passes the validation, the data is saved in the "BLog" model using save() method.

**Response**

* Based on the input data, the server sends different responses. Using the django messages framework, a success message is displayed if the data is valid whereas an error message is displayed if the data is invalid.

View Blog
********

14. `/staff/view-blog <http://127.0.0.1:8000/staff/view-blog>`_

**Request**

* When this url gets hit, the respective view "BlogView" is called. A "GET" request is sent to the server by default.

**Response**

* When the "GET" request is sent to the server, the view returns the list of the the blogs from the "Blog" model using queryset.

Delete Blog
********

15. `/staff/delete-blog/<blog-id> <http://127.0.0.1:8000/staff/delete-blog/100>`_

**Request**

* When this url gets hit, the respective view "delete-blog" is called.

**Method: POST**
The specific <blog-id> is sent in the url from the form of `/staff/view-blog <http://127.0.0.1:8000/staff/view-blog>`_ and passed onto the view. And, the record of the specific Id is deleted from the "Blog" model using delete() method.

**Response**
Using the django messages framework, a success message stating that the data has been deleted is returned to the template.

Update Blog
********

16. `/staff/update-blog/<product-id> <http://127.0.0.1:8000/staff/update-blog/100>`_

**Request**

* When the url along with the <blog-id> gets hit, the view returns the product add form with the populated data of the same ID using queryset.

.. list-table:: **Blog update form**
   :widths: 25 25 25
   :header-rows: 1

   * - Fields
     - Input Type
     - Attribute
   * - Title
     - Text
     - Required
   * - Description
     - TinyMCE
     - Required
   * - Date
     - File
     - Required
   * - Image
     - File
     - Required
   * - Url
     - Text
     - Required

**Method: POST**
The specific <blog-id> is sent in the url from the form of `/staff/view-blog <http://127.0.0.1:8000/staff/view-vlog>`_ and passed onto the view. And, the record of the specific Id is deleted from the "Product" model using delete() method.

**Response**
Using the django messages framework, a success message stating that the data has been deleted is returned to the template.
