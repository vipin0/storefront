# storefront API
An e-commerce store api created using django, django-rest-framework.

## Installation
Clone the repository and navigate to the main directory.

**Install the requirements**
```
pip install -r requirements.txt
```

**Run Migrations**
```python
python manage.py makemigrations
    
python manage.py migrate
```

**Start Development Server**
```
python manage.py runserver
```

## API Root
- ```/auth ``` user api root
- ```/store  ```  store api root

## View live demo
- [Swagger UI](https://storefront-ecom.herokuapp.com/)
- [DRF Browsable API](https://storefront-ecom.herokuapp.com/store/)

## Working Endpoints

### Store Endpoints (https://storefront-ecom.herokuapp.com/store) :

```POST /store​/carts​/```  store_carts_create

```GET /store​/carts​/{cart_pk}​/items​/``` store_carts_items_list

```POST ​/store​/carts​/{cart_pk}​/items​/```
store_carts_items_create

```GET ​/store​/carts​/{cart_pk}​/items​/{id}​/```
store_carts_items_read

```PATCH ​/store​/carts​/{cart_pk}​/items​/{id}​/```
store_carts_items_partial_update

```DELETE ​/store​/carts​/{cart_pk}​/items​/{id}​/```
store_carts_items_delete

```GET ​/store​/carts​/{id}​/```
store_carts_read

```DELETE ​/store​/carts​/{id}​/```
store_carts_delete

```GET ​/store​/collections​/```
store_collections_list

```POST ​/store​/collections​/```
store_collections_create

```GET ​/store​/collections​/{id}​/```
store_collections_read

```PUT ​/store​/collections​/{id}​/```
store_collections_update

```PATCH ​/store​/collections​/{id}​/```
store_collections_partial_update

```DELETE ​/store​/collections​/{id}​/```
store_collections_delete

```GET ​/store​/customers​/```
store_customers_list

```POST ​/store​/customers​/```
store_customers_create

```GET ​/store​/customers​/me​/```
store_customers_me_read

```PUT ​/store​/customers​/me​/```
store_customers_me_update

```GET ​/store​/customers​/{id}​/```
store_customers_read

```PUT ​/store​/customers​/{id}​/```
store_customers_update

```PATCH ​/store​/customers​/{id}​/```
store_customers_partial_update

```DELETE ​/store​/customers​/{id}​/```
store_customers_delete

```GET ​/store​/customers​/{id}​/history​/```
store_customers_history

```GET ​/store​/orders​/```
store_orders_list

```POST ​/store​/orders​/```
store_orders_create

```GET ​/store​/orders​/{id}​/```
store_orders_read

```PATCH ​/store​/orders​/{id}​/```
store_orders_partial_update

```DELETE ​/store​/orders​/{id}​/```
store_orders_delete

```GET ​/store​/products​/```
store_products_list

```POST ​/store​/products​/```
store_products_create

```GET ​/store​/products​/{id}​/```
store_products_read

```PUT ​/store​/products​/{id}​/```
store_products_update

```PATCH ​/store​/products​/{id}​/```
store_products_partial_update

```DELETE ​/store​/products​/{id}​/```
store_products_delete

```GET ​/store​/products​/{product_pk}​/reviews​/```
store_products_reviews_list

```POST ​/store​/products​/{product_pk}​/reviews​/```
store_products_reviews_create

```GET ​/store​/products​/{product_pk}​/reviews​/{id}​/```
store_products_reviews_read

```PUT ​/store​/products​/{product_pk}​/reviews​/{id}​/```
store_products_reviews_update

```PATCH ​/store​/products​/{product_pk}​/reviews​/{id}​/```
store_products_reviews_partial_update

```DELETE ​/store​/products​/{product_pk}​/reviews​/{id}​/```
store_products_reviews_delete
<hr>

### User Endpoints : (https://storefront-ecom.herokuapp.com/users/)

```POST ​/auth​/jwt​/create​/```
auth_jwt_create_create

```POST ​/auth​/jwt​/refresh​/```
auth_jwt_refresh_create

```POST ​/auth​/jwt​/verify​/```
auth_jwt_verify_create

```GET ​/auth​/users​/```
auth_users_list

```POST ​/auth​/users​/```
auth_users_create

```POST ​/auth​/users​/activation​/```
auth_users_activation

```GET ​/auth​/users​/me​/```
auth_users_me_read

```PUT ​/auth​/users​/me​/```
auth_users_me_update

```PATCH ​/auth​/users​/me​/```
auth_users_me_partial_update

```DELETE ​/auth​/users​/me​/```
auth_users_me_delete

```POST ​/auth​/users​/resend_activation​/```
auth_users_resend_activation

```POST ​/auth​/users​/reset_email​/```
auth_users_reset_username

```POST ​/auth​/users​/reset_email_confirm​/```
auth_users_reset_username_confirm

```POST ​/auth​/users​/reset_password​/```
auth_users_reset_password

```POST ​/auth​/users​/reset_password_confirm​/```
auth_users_reset_password_confirm

```POST ​/auth​/users​/set_email​/```
auth_users_set_username

```POST ​/auth​/users​/set_password​/```
auth_users_set_password

```GET ​/auth​/users​/{id}​/```
auth_users_read

```PUT ​/auth​/users​/{id}​/```
auth_users_update

```PATCH ​/auth​/users​/{id}​/```
auth_users_partial_update

```DELETE ​/auth​/users​/{id}​/```
auth_users_delete




