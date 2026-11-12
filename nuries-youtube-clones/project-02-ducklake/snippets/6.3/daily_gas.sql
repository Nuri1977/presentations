{{ config(
    materialized='incremental',
    incremental_strategy='merge',
    unique_key='block_date',
    post_hook="call eth_lake.set_commit_message('dbt', 'daily_gas: incremental merge')"
) }}

select
    block_date,
    count(*) as transactions,
    round(sum(fee_eth), 4) as total_fee_eth,
    round(median(fee_eth), 8) as median_fee_eth,
    round(100.0 * avg(succeeded::int), 2) as success_pct
from {{ ref('stg_transactions') }}
{% if is_incremental() %}
where block_date >= (select max(block_date) from {{ this }})
{% endif %}
group by block_date
