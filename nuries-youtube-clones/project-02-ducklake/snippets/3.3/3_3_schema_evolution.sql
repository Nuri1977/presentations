alter table raw.blocks add column gas_used_pct double;
update raw.blocks set gas_used_pct = round(100.0 * gas_used / gas_limit, 2) where date = date '2026-11-02';
alter table raw.blocks rename miner to fee_recipient;
alter table raw.blocks alter number set not null;
select number, fee_recipient, gas_used_pct from raw.blocks where date = date '2026-11-02' limit 3;
select number, miner from raw.blocks at (version => 11) limit 3;
