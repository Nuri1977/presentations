-- Appendix A1: starter data (Lab 1). Runs anywhere DuckDB runs.
create schema if not exists raw;

create or replace table raw.customers as
select * from (values
  (1, 'Ava',    'Nguyen',  'ava@example.com',    '2026-01-05'),
  (2, 'Ben',    'Ortiz',   'ben@example.com',    '2026-01-12'),
  (3, 'Chloe',  'Patel',   'chloe@example.com',  '2026-02-03'),
  (4, 'Dmitri', 'Ivanov',  'dmitri@example.com', '2026-02-20'),
  (5, 'Elena',  'Rossi',   'elena@example.com',  '2026-03-08'),
  (6, 'Farid',  'Haddad',  'farid@example.com',  '2026-03-15')
) as t(id, first_name, last_name, email, created_at);

create or replace table raw.orders as
select * from (values
  (1,  1, '2026-03-01', 'completed'),
  (2,  1, '2026-03-20', 'completed'),
  (3,  2, '2026-03-05', 'completed'),
  (4,  3, '2026-03-10', 'returned'),
  (5,  3, '2026-04-02', 'completed'),
  (6,  4, '2026-04-05', 'shipped'),
  (7,  4, '2026-04-18', 'placed'),
  (8,  5, '2026-04-20', 'completed'),
  (9,  2, '2026-05-01', 'return_pending'),
  (10, 1, '2026-05-03', 'placed')
) as t(id, customer_id, order_date, status);

create or replace table raw.payments as
select * from (values
  (1,  1,  'credit_card',   2500),
  (2,  2,  'credit_card',   4000),
  (3,  3,  'bank_transfer', 1500),
  (4,  4,  'gift_card',     3000),
  (5,  5,  'credit_card',   2000),
  (6,  6,  'credit_card',   5500),
  (7,  8,  'bank_transfer', 1200),
  (8,  9,  'gift_card',      800),
  (9,  10, 'credit_card',   3200),
  (10, 10, 'gift_card',      500)
) as t(id, order_id, method, amount_cents);
