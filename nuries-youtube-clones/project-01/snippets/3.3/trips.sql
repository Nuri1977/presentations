-- one row per 2025 green taxi trip, obviously broken rows removed
select
    VendorID              as vendor_id,
    lpep_pickup_datetime  as pickup_at,
    lpep_dropoff_datetime as dropoff_at,
    PULocationID          as pickup_zone_id,
    DOLocationID          as dropoff_zone_id,
    passenger_count,
    trip_distance,
    payment_type,
    fare_amount,
    tip_amount,
    total_amount
from {{ source('raw', 'green_trips') }}
where lpep_pickup_datetime >= '2025-01-01'
  and lpep_pickup_datetime <  '2026-01-01'
  and trip_distance > 0
  and total_amount > 0
