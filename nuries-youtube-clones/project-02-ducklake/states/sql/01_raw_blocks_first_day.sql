-- Lesson 2.2: the raw schema and the first day of blocks
create schema raw;
create table raw.blocks as select * from read_parquet('{{cache}}/data/eth/blocks/blocks_2026-08-01.parquet');
