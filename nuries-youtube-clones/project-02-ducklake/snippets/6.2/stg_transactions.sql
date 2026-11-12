{{ config(materialized='view') }}

select
    hash as transaction_hash,
    block_number,
    date as block_date,
    from_address,
    to_address,
    value / 1e18 as value_eth,
    receipt_gas_used * receipt_effective_gas_price / 1e18 as fee_eth,
    receipt_status = 1 as succeeded
from {{ source('raw', 'transactions') }}
