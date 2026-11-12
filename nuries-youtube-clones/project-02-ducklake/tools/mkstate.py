"""Write states/<name>/recipe.yaml: the project as the previous lesson pushed it + the lake rebuilt from snippets.
  python3 tools/mkstate.py lesson-2-3-end 2.2/2_2_load_blocks.sql 2.3/2_3_look_inside.sql ..."""
import sys, pathlib
name, sn = sys.argv[1], sys.argv[2:]
d = pathlib.Path(__file__).resolve().parents[1] / 'states' / name
d.mkdir(parents=True, exist_ok=True)
lst = ', '.join(f'../../snippets/{s}' for s in sn)
(d / 'recipe.yaml').write_text(f'''# {name}: project as pushed by GitHub (clone), lake rebuilt from the lesson scripts (S3 reads come from the cache).
name: {name}
project_name: ethereum_lake
clone: https://github.com/Nuri1977/ethereum-ducklake-dbt.git
dirs: [analysis, macros, models, rosetta, seeds, snapshots, tests, lake/data]
database_file: ../ethereum_lake_dev.duckdb
sql: []
connection_name: ethereum_lake_dev
git:
  user: Rosetta Academy
  email: academy@users.noreply.github.com
lake:
  name: eth_lake
  dir: lake
  catalog: eth_catalog.duckdb
  sql: [{lst}]
'''+('  dirs: [landing]\n' if any(x.startswith('4.5/') for x in sn) else ''))
print('wrote', d / 'recipe.yaml')
