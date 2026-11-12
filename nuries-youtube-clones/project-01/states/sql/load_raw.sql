-- Lesson 2.2 loads the parquet files into DuckDB from Studio's SQL Editor; start states after 2.2 repeat it off camera.
create schema if not exists raw;
create or replace table raw.green_trips as
select * from read_parquet('/Users/Shared/academy/learner/projects/nyc_taxi/data/raw/green_tripdata_2025-*.parquet', union_by_name = true);
