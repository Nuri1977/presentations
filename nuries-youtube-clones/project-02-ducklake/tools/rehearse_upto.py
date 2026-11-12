"""Rebuild a scratch lake from the given snippet scripts and print the result of the last one.
  python tools/rehearse_upto.py <scratch> 2.2/2_2_load_blocks.sql ... 3.4/3_4_change_feed.sql"""
import duckdb, sys, pathlib, shutil
sys.path.insert(0, str(pathlib.Path(__file__).parent)); from s3cache import to_cache
R = pathlib.Path(sys.argv[1]); shutil.rmtree(R, ignore_errors=True); (R / 'data').mkdir(parents=True); (R / 'landing').mkdir(parents=True)
c = duckdb.connect(); c.execute(f"attach 'ducklake:{R}/c.duckdb' as eth_lake (data_path '{R}/data/')"); c.execute('use eth_lake')
P = '/Users/Shared/academy/learner/projects/ethereum_lake'
files = sys.argv[2:]
for f in files:
    t = to_cache((pathlib.Path(__file__).parents[1] / 'snippets' / f).read_text()).replace(P + '/lake/data', str(R / 'data')).replace(P + '/lake', str(R)).replace(P, str(R))
    for st in [x.strip() for x in t.split(';') if x.strip()]:
        try:
            r = c.execute(st)
            if f == files[-1]: print(st[:90], '->', r.fetchall()[:8] if r.description else '')
        except Exception as e:
            print('ERROR', st[:90], str(e)[:300])
print('max snapshot', c.execute('select max(snapshot_id) from eth_lake.snapshots()').fetchone())
