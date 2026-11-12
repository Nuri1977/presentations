{{ config(materialized='view') }}

select
    number as block_number,
    date as block_date,
    timestamp as block_time,
    fee_recipient,
    transaction_count,
    gas_used,
    gas_limit,
    round(100.0 * gas_used / gas_limit, 2) as gas_used_pct,
    base_fee_per_gas / 1e9 as base_fee_gwei
from {{ source('raw', 'blocks') }}
