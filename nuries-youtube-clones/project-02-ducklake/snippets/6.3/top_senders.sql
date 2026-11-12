{{ config(materialized='table') }}

select
    from_address,
    count(*) as transactions,
    round(sum(fee_eth), 4) as fees_paid_eth
from {{ ref('stg_transactions') }}
group by from_address
order by transactions desc
limit 100
