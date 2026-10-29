-- Outdoor store demo database for the Python notebooks short.
-- A made-up outdoor gear store, orders from Jan 2025 to Sep 2026.
-- Revenue grows over time with a holiday peak, so charts look like a real business.
--
-- Run (drops and recreates the outdoor_store database):
--   psql -h localhost -p 5433 -U postgres -f outdoor_store.sql

drop database if exists outdoor_store;
create database outdoor_store;
\connect outdoor_store

select setseed(0.42);

create table customers (
  customer_id serial primary key,
  first_name  text not null,
  last_name   text not null,
  country     text not null,
  signup_date date
);

create table products (
  product_id   serial primary key,
  product_name text not null,
  category     text not null,
  unit_price   numeric(10, 2) not null
);

create table orders (
  order_id    serial primary key,
  customer_id int not null references customers,
  order_date  date not null,
  channel     text not null,
  status      text not null,
  amount      numeric(12, 2) not null default 0
);

create table order_items (
  order_item_id serial primary key,
  order_id      int not null references orders,
  product_id    int not null references products,
  quantity      int not null,
  unit_price    numeric(10, 2) not null
);

insert into products (product_name, category, unit_price) values
  ('Trail Tent 2P',        'Camping',  249.00),
  ('Summit Tent 4P',       'Camping',  429.00),
  ('Down Sleeping Bag',    'Camping',  189.00),
  ('Camp Stove',           'Camping',   79.00),
  ('Headlamp',             'Camping',   35.00),
  ('Trail Runner Shoes',   'Hiking',   139.00),
  ('Hiking Boots',         'Hiking',   179.00),
  ('Daypack 25L',          'Hiking',    89.00),
  ('Trekking Poles',       'Hiking',    69.00),
  ('Water Filter',         'Hiking',    45.00),
  ('Rain Jacket',          'Apparel',  159.00),
  ('Fleece Hoodie',        'Apparel',   79.00),
  ('Merino Base Layer',    'Apparel',   69.00),
  ('Hiking Socks 3-Pack',  'Apparel',   24.00),
  ('Sun Hat',              'Apparel',   29.00),
  ('Climbing Harness',     'Climbing',  85.00),
  ('Chalk Bag',            'Climbing',  22.00),
  ('Climbing Shoes',       'Climbing', 129.00),
  ('Belay Device',         'Climbing',  35.00),
  ('Dynamic Rope 60m',     'Climbing', 219.00);

-- 1,500 customers with made-up names
insert into customers (first_name, last_name, country)
select
  (array['Ava','Liam','Noah','Emma','Mia','Lucas','Sofia','Leo','Nora','Ethan',
         'Zoe','Omar','Lena','Hugo','Ines','Kai','Maya','Theo','Elif','Jonas'])[1 + floor(random() * 20)::int],
  (array['Berg','Novak','Ortiz','Hayes','Lind','Moreau','Sato','Keller','Reyes','Walsh',
         'Costa','Brandt','Quinn','Ferreira','Holm','Adler','Silva','Park','Vance','Rossi'])[1 + floor(random() * 20)::int],
  (array['United States','United States','United States','Canada','Canada','United Kingdom',
         'Germany','France','Australia','Netherlands','Sweden'])[1 + floor(random() * 11)::int]
from generate_series(1, 1500);

-- Orders per day: steady growth, holiday peak in Nov/Dec, summer bump, busier weekends
insert into orders (customer_id, order_date, channel, status)
select
  -- lower ids order more often, so a few customers stand out as top spenders
  1 + floor(1500 * power(random(), 1.8))::int,
  d::date,
  case when random() < 0.55 then 'web' when random() < 0.67 then 'mobile' else 'store' end,
  case when random() < 0.96 then 'completed' else 'refunded' end
from generate_series(date '2025-01-01', date '2026-09-30', interval '1 day') as d,
     generate_series(1, round(
       (14 + 12 * ((extract(year from d) - 2025) * 12 + extract(month from d) - 1) / 20.0)
       * case extract(month from d)
           when 11 then 1.35 when 12 then 1.6
           when 6 then 1.2 when 7 then 1.2
           when 1 then 0.85 when 2 then 0.85
           else 1.0 end
       * case when extract(isodow from d) >= 6 then 1.25 else 1.0 end
       * (0.85 + random() * 0.3)
     )::int) as n;

-- 1 to 3 products per order
insert into order_items (order_id, product_id, quantity, unit_price)
select i.order_id, p.product_id, i.quantity, p.unit_price
from (
  select o.order_id,
         1 + floor(random() * 20)::int as product_id,
         1 + (random() < 0.2)::int as quantity
  from orders o,
       generate_series(1, 1 + floor(random() * 3)::int + 0 * o.order_id) as g
  offset 0  -- keeps random() picked once per item row
) i
join products p on p.product_id = i.product_id;

update orders o
set amount = t.total
from (
  select order_id, sum(quantity * unit_price) as total
  from order_items
  group by order_id
) t
where t.order_id = o.order_id;

-- Customers signed up shortly before their first order
update customers c
set signup_date = f.first_order - (floor(random() * 60)::int + 0 * c.customer_id)
from (select customer_id, min(order_date) as first_order from orders group by customer_id) f
where f.customer_id = c.customer_id;

update customers
set signup_date = date '2026-09-30' - (floor(random() * 300)::int + 0 * customer_id)
where signup_date is null;

analyze;
