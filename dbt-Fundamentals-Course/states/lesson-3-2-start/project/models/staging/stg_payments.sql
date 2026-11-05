select
    id as payment_id,
    order_id,
    method as payment_method,
    amount_cents / 100.0 as amount
from {{ source('raw', 'payments') }}
