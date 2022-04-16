drop table if exists  orders;
drop table if exists cart_products;
drop table if exists user_cart;
drop table if exists products;
drop table if exists categories;
drop table if exists supermarket;
drop table if exists users;
drop table if exists requests;
drop table if exists user_status;




create table user_status
(
    user_status_id serial
        constraint user_status_pk
            primary key,
    name           text
);




create table users
(
    user_id        serial
        constraint users_pk
            primary key,
    username       text    not null,
    password       text    not null,
    user_status_id integer not null
        constraint users_user_status_user_status_id_fk
            references user_status,
    name           text    not null,
    email          text    not null,
    phone_number   text    not null,
    cui_number     text
);

create table supermarket
(
    supermarket_id serial
        constraint supermarket_pk
            primary key,
    name           text not null,
    address        text,
    user_id        integer
        constraint supermarket_users_user_id_fk
            references users
);



create table categories
(
    category_id serial
        constraint categories_pk
            primary key,
    name        text not null
);



create table products
(
    product_id     serial
        constraint products_pk
            primary key,
    supermarket_id integer not null
        constraint products_supermarket_supermarket_id_fk
            references supermarket,
    category_id    integer not null
        constraint products_categories_category_id_fk
            references categories,
    name           text    not null,
    quantity       integer not null,
    price          integer not null,
    expire_date    date,
    product_date   date
);



create table user_cart
(
    cart_id serial
        constraint user_cart_pk
            primary key,
    user_id integer not null
        constraint user_cart_users_user_id_fk
            references users
);



create table cart_products
(
    cart_id   integer not null
        constraint cart_products_user_cart_id_fk
            references user_cart,
    product_id integer not null
        constraint carts_products_product_id_fk
            references products,
    quantity   integer not null
);


create table orders
(
    order_id serial
        constraint orders_pk
            primary key,
    user_id  integer not null
        constraint orders_users_user_id_fk
            references users,
    cart_id  integer not null
        constraint orders_carts_cart_id_fk
            references user_cart
);

create table requests
(
    request_id     serial
        constraint requests_pk
            primary key,
    username       text,
    password       text,
    user_status_id integer
        constraint requests_user_status_user_status_id_fk
            references user_status,
    name           text,
    email          text,
    phone_number   text,
    cui_number     text,
    address        text
);


insert into  user_status(name) values ('provider'), ('organisation'), ('admin');
insert into categories(name) values  ('dulciuri'), ('produse de baza'), ('condimente'),
         ('lactate'), ('legume'), ('fructe'), ('carne'), ('bauturi'), ('panificatie'),
         ('conserve si borcane'), ('gustari sarate'), ('semipreparate'), ('preparate');



