select min(block_number) as first_block, max(block_number) as last_block from raw.transactions;
explain analyze select count(*) from raw.transactions where block_number between 26100000 and 26100100;
alter table raw.transactions set sorted by (block_number asc);
select option_name, value from eth_lake.options();
