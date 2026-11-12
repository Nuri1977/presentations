"""Shared pieces for lesson.yaml files: the commit beat and indentation of a snippet."""
def ind(t, n=14):
    return '\n'.join(' ' * n + l for l in t.rstrip('\n').split('\n'))
def commit_beat(bid, n, fname, sql, msg, say):
    return f'''      - id: {bid}
        say: "{say}"
        zoom: git-panel
        actions:
          - nav: DBT Studio
          - new_file: {{ folder: sql, name: {fname} }}
          - paste: |
{ind(sql)}
          - click_save
          - expect_file: {{ path: sql/{fname}, snippet: ../snippets/{n}/{fname} }}
          - close_tab: sql/{fname}
          - git_tab
          - git_stage_all
          - git_message: "{msg}"
          - git_commit
          - git_push
'''
