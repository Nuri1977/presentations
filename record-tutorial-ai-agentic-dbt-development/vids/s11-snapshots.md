# S11 · Snapshots: Google Vids script

**Import:** `s11-snapshots.pptx` (speaker notes = the scripts below). **Voiceover:** 412 words, about 2.7 min at 150 wpm. **Demo recording budget:** about 6.8 min (Vids videos max 10 min).

**Scene order in Vids:** scenes 1 to 12 (slides) → your demo recording → scene 13 (recap). Drag the recap scene to the end after you add the recording.

## Voiceover, scene by scene

**Scene 1 · Snapshots**

Section eleven: snapshots. Trips never change once they happen. But some data is updated in place, and when that happens, the old value is gone. Snapshots keep it.

**Scene 2 · When a row is updated, the old value is gone.**

Think of an address, a price, or a vendor name. The source system overwrites it, and yesterday's value is lost, unless we keep one row per version, with the dates each version was valid. That is a slowly changing dimension, type two.

**Scene 3 · This really happened to the taxi data**

This really happened in our data. Older versions of the taxi data dictionary say vendor two is VeriFone. The current one says Curb Mobility. And two new vendors appeared, Myle and Helix.

**Scene 4 · Snapshots**

The snapshots page, version one. Since dbt one point nine, a snapshot is a YAML file pointing at a source or model. It needs a unique key and a strategy. dbt adds valid from and valid to columns, and snapshots ignore full refresh, so history is never wiped.

**Scene 5 · Two strategies**

Two strategies. Timestamp compares an updated at column, when the source has a reliable one. Check compares the actual values of the columns you list. Our vendor list has no timestamp, so we check the vendor name.

**Scene 6 · Prompt card**

First we need a source system that changes. In the demo, the agent creates a small vendor registry table with the old list: Creative Mobile Technologies, and VeriFone.

**Scene 7 · Prompt card**

Then the agent adds the table to our source, creates the snapshot in YAML with the check strategy, and runs dbt snapshot. Many examples online use an older syntax. Our skill says YAML.

**Scene 8 · The snapshot**

Seven lines: a name, the source it reads, a unique key, the check strategy, and the column to check. If the agent writes the old syntax, we discard it, and add the rule to the skill.

**Scene 9 · After the first snapshot**

After the first snapshot, both vendors are current, and their valid to column is empty.

**Scene 10 · The registry changes**

Then someone updates the vendor system. Vendor two becomes Curb Mobility, and vendors six and seven are added, exactly as in the real dictionary. We run dbt snapshot again.

**Scene 11 · History, kept**

History, kept. Vendor two now has two rows: VeriFone, valid until the second run, and Curb Mobility, valid from then on. Any report can now ask what a vendor was called at the time of a trip.

**Scene 12 · Snapshot and current dimension**

On the graph: the new source, the snapshot, and a vendor dimension built from the current rows of the snapshot.

**Scene 13 · Section 11 done**

That is section eleven. Snapshots keep history, and we used one on a real change from the taxi data dictionary. Next: documentation, lineage, and a real answer.

## Demo recording: prompting and changing files

**Set up before you hit record**

- Section 10 end state.

**Steps**

1. SQL Editor → AI panel → **Code** mode. Paste prompt 1. **Allow** at the approval gate.

   > Create raw.vendor_registry (vendor_id, vendor_name) with two rows: 1 = Creative Mobile Technologies, LLC and 2 = VeriFone Inc.

2. New chat, **Code** mode. Paste prompt 2. Check it wrote YAML (not a `{% snapshot %}` block). **Keep**. **Allow** `dbt snapshot`. *File:* `snapshots/snap_tlc__vendors.yml, _tlc__sources.yml`

   > Add vendor_registry to the tlc source. Create snapshots/snap_tlc__vendors.yml on source('tlc', 'vendor_registry') with the check strategy on vendor_name and unique_key vendor_id, using the YAML snapshot syntax for my dbt version. Run dbt snapshot.

3. SQL editor: query the snapshot (2 current rows).
4. SQL editor (approval gate): update vendor 2 to "Curb Mobility, LLC"; insert 6 "Myle Technologies Inc" and 7 "Helix".
5. Run `dbt snapshot` again (agent or terminal).
6. Query the snapshot ordered by vendor_id, dbt_valid_from: vendor 2 has two rows.
7. Code mode: "Create dim_vendors from snap_tlc__vendors, current rows only, with YAML and a primary-key test." **Keep**, build. *File:* `models/marts/dim_vendors.sql`

**Optional lines to say over the recording**

- "VeriFone, then Curb Mobility: history kept."

**All prompts in this section, ready to paste**

1. Create raw.vendor_registry (vendor_id, vendor_name) with two rows: 1 = Creative Mobile Technologies, LLC and 2 = VeriFone Inc.

2. Add vendor_registry to the tlc source. Create snapshots/snap_tlc__vendors.yml on source('tlc', 'vendor_registry') with the check strategy on vendor_name and unique_key vendor_id, using the YAML snapshot syntax for my dbt version. Run dbt snapshot.
