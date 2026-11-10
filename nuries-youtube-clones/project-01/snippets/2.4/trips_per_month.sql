-- trips per month and pickup borough
select
    date_trunc('month', t.pickup_at) as month,
    z.Borough                        as borough,
    count(*)                         as trips,
    round(avg(t.fare_amount), 2)     as avg_fare
from {{ ref('trips') }} as t
left join {{ ref('taxi_zone_lookup') }} as z
    on t.pickup_zone_id = z.LocationID
group by all
order by month, borough
