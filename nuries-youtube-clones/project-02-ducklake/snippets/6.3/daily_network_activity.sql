{{ config(materialized='table') }}

select
    block_date,
    count(*) as blocks,
    sum(transaction_count) as transactions,
    round(avg(gas_used_pct), 1) as avg_gas_used_pct,
    round(avg(base_fee_gwei), 3) as avg_base_fee_gwei
from {{ ref('stg_blocks') }}
group by block_date
