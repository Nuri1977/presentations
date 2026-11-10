-- the busiest pickup zones of 2025
{% set top_n = 10 %}

select
    t.pickup_zone_id as zone_id,
    z.Zone           as zone,
    z.Borough        as borough,
    count(*)         as trips
from {{ ref('trips') }} as t
join {{ ref('taxi_zone_lookup') }} as z
    on t.pickup_zone_id = z.LocationID
group by all
order by trips desc
limit {{ top_n }}
