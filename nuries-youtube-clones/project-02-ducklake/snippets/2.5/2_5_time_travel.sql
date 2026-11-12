select count(*) as blocks from raw.blocks;
select count(*) as blocks from raw.blocks at (version => 2);
select strftime(date, '%Y-%m') as month, count(*) as blocks from raw.blocks at (version => 3) group by all order by 1;
create table raw.blocks_october as select * from raw.blocks at (version => 4) where date >= date '2026-10-01';
select count(*) as blocks from raw.blocks_october;
drop table raw.blocks_october;
