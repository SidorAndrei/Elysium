drop table if exists  orders;
drop table if exists user_cart;
drop table if exists carts;
drop table if exists products;
drop table if exists categories;
drop table if exists supermarket;
drop table if exists users;
drop table if exists user_status;


create table supermarket
(
    supermarket_id serial
        constraint supermarket_pk
            primary key,
    name           text not null,
    address        text
);


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



create table carts
(
    cart_id    serial
        constraint carts_pk
            primary key,
    product_id integer not null
        constraint carts_products_product_id_fk
            references products,
    quantity   integer not null
);



create table user_cart
(
    cart_id integer not null
        constraint user_cart_carts_cart_id_fk
            references carts,
    user_id integer not null
        constraint user_cart_users_user_id_fk
            references users
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
            references carts
);


insert into  user_status(name) values ('provider'), ('organisation');
insert into categories(name) values  ('dulciuri'), ('produse de baza'), ('condimente'),
         ('lactate'), ('legume'), ('fructe'), ('carne'), ('bauturi'), ('panificatie'),
         ('conserve si borcane'), ('gustari sarate'), ('semipreparate'), ('preparate');



