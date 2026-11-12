"""Rewrite the course's S3 reads to the local cache (same data, no network), for start states and rehearsal."""
import re, pathlib
CACHE = pathlib.Path(__file__).resolve().parents[1] / '.cache' / 'data' / 'eth'
def to_cache(sql):
    sql = re.sub(r"read_parquet\('s3://aws-public-blockchain/v1\.0/eth/(blocks|transactions)/date=([^/']+)/\*\.parquet'\)",
                 lambda m: f"read_parquet('{CACHE}/{m.group(1)}/{m.group(1)}_{m.group(2)}.parquet')", sql)
    sql = re.sub(r"\*\s+exclude\s*\(logs_bloom,\s*last_modified\)", "*", sql, flags=re.I)
    return re.sub(r"\*\s+exclude\s*\(logs_bloom,\s*last_modified,\s*", "* exclude (", sql, flags=re.I)
