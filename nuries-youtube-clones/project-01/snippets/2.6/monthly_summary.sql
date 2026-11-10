-- one row per month: total trips and the share paid by card
with totals as (
    select month, sum(trips) as total_trips
    from {{ ref('trips_per_month') }}
    group by month
),
card as (
    select date_trunc('month', pickup_at) as month, count(*) as card_trips
    from {{ ref('trips') }}
    where payment_type = 1   -- credit card
    group by month
)
select
    month,
    total_trips,
    card_trips,
    round(100.0 * card_trips / total_trips, 1) as pct_card
from totals
join card using (month)
order by month
