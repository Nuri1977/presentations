create table raw.watchlist (address varchar, label varchar);
call eth_lake.set_option('data_inlining_row_limit', 100, schema => 'raw', table_name => 'watchlist');
insert into raw.watchlist values ('0x00000000219ab540356cbb839cbe05303d7705fa', 'staking deposit'), ('0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 'wrapped ether');
select * from raw.watchlist;
select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');
call ducklake_flush_inlined_data('eth_lake', schema_name => 'raw', table_name => 'watchlist');
select count(*) as files from ducklake_list_files('eth_lake', 'watchlist', schema => 'raw');
