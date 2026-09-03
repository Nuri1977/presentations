# The most comprehensive "step-by-step" tutorial about using Apache Iceberg.  

If you're like me, when you think about analytics or big data, the first thing that comes to mind is a massive pile of files
0:12
Sitting somewhere in a data lake, probably an S3.
0:16
For years, data lakes were really simple.
0:18
They were parquet files organized into directories, and those directories corresponded to
0:23
partitions.
0:24
If you don't know Parquet, it's a columnar storage format that is really efficient to scan.
0:30
And why scan?
0:31
Well, that is the most common operation in OLAP or analytics type queries.
0:38
You've got a bunch of records, and you have to read all those records as quickly as possible,
0:43
and usually compute some aggregate over some value in those records.
0:46
So, it's efficient to scan, and scanning is very important in analytics.
0:50
So, anyway, you dump these Parquet files into S3 at hard-coded paths.
0:56
Then you would write in the bad old days: MapReduce programs in Java to process them.
1:03
These were not really fun times.
1:05
You filtered partitions by hand and just hope nobody else was writing to the
1:09
same location at the same time as you were reading. There were no transactions.
1:14
Schema changes broke pipelines all the time, and figuring out what data was current was a nightmare.
Hive
1:21
It kind of worked, you know, but it was fragile, error-prone, and you could never really guarantee correctness.
1:28
In 2008, Hive changed the game.
1:32
It brought table formats to data lakes, adding schemas, partitions, and the best thing, a SQL interface.
1:39
Suddenly, you could just write select star from sales instead of some weird
1:44
200-line Java program jammed into a function called map
1:47
and a function called reduce in ways that were really not pleasant to think about.
1:53
But it didn't take long for new problems to surface.
1:58
Schema evolution was limited.
2:00
You want to add a column?
2:01
Well, okay.
2:02
But rename or drop a column, you had to rewrite the whole table, actually copy it from one place over to another.
2:09
Partitions were hard-coded into the directory structure.
2:12
If you pick wrong at the time you create the table, you're stuck.
2:16
Slow queries or a full rewrite and no transactions for years.
Limitations of Hive
2:21
So concurrent writes would corrupt data.
2:23
ACID finally arrived in 2014, but only with orc files, files in that format.
2:30
And it created delta files needing constant compaction to keep queries fast.
2:36
And this was all built for Hive.
2:37
Other engines could connect to the data lake, but it was never really seamless.
Introducing Apache Iceberg
2:42
In 2017, engineers at Netflix looked at this mess and decided to start over.
2:47
Design it right from the ground up.
2:50
They built Iceberg, an open table format that treats data lake files like actual database tables,
2:56
with all the guarantees that you've come to expect from a transactional database.
3:01
Like Hive, you get SQL tables with schemas and partitions.
3:06
But unlike Hive, you also get real ACID transactions, schema evolution that actually works, time travel.
3:13
Hidden partitioning that adapts as your queries change, and the ability to change the partitioning scheme over time.
3:20
And here's another difference: Hive stored its metadata outside the data lake.
3:26
Iceberg stores metadata right alongside the data.
3:29
Everything lives in the lake.
Inside Iceberg
3:31
Let's look at how Iceberg actually organizes a table.
3:34
An Iceberg table starts with a data layer. At the bottom, there, the actual files that hold your data.
3:39
And we call those famously the data files.
3:42
The files are immutable.
3:44
Once they're written, they can't be changed.
3:46
If you want to update a row, Iceberg writes a new file, and we'll talk about how later.
3:51
But that's a typical thing in data lakes and in analytic systems.
3:54
We normally think of analytics as backward looking at events, at things that have happened in the past.
4:00
Which are, as we know, immutable.
4:02
That's not always the case, and we'll talk about upserts later on.
4:06
The format of those data files is usually parquet.
4:09
That's probably what you're going to find in the wild. But it doesn't have to be.
4:12
They can be orc, they can be avro, you know, whatever you like.
4:16
But again, typically parquet.
4:18
Next up is the metadata layer.
4:20
There's a lot of complexity in here. And this is where iceberg really starts to get interesting.
4:24
The metadata layer tracks everything about your table: schema, partitions, which files contain which data,
4:30
even statistics like min, max values per column, and things like that that will help with scanning later on.
4:37
This is all the data about the data.
4:39
Iceberg's metadata is organized into kind of a tree here, and the names can be a little tricky the first time through.
4:44
Sometimes you can get them mixed up.
4:47
Follow closely.
4:48
At the bottom, these are the manifest files.
4:51
Each manifest tracks a set of data files along with
4:56
Stats, again, things like row count, min, max values for numeric columns, partitioning information, things like that.
5:03
This is what lets query engines skip entire files without even opening them.
5:09
You know, if you want sales from January and you know that these 47 files have nothing from January, you can skip them.
5:16
And you could tell that possibly just by looking at the metadata.
5:19
Like data files, manifests are immutable.
5:22
They never change once they're written.
5:24
One level up, we have manifest lists.
5:28
These are lists of manifest files.
5:31
Each one points to a bunch of manifests and tracks their combined stats.
5:37
How many files in that list of manifests?
5:40
Which partitions are covered?
5:41
What ranges?
5:43
Those stats are kind of rolled up into the manifest list.
5:46
And this adds another level of pruning.
5:48
You have a query filtering on January 2025.
5:51
Iceberg can skip an entire manifest list if it knows it only covers dates in 2024 and never needs to open a single data file.
6:00
And again, manifest lists, immutable.
6:03
At the top is the metadata file.
6:05
This is the single source of truth for a table.
6:08
It's got the schema, it's got the partitioning strategy.
6:12
Table properties, and most importantly, a thing called the snapshot history.
6:17
Snapshot, you say?
6:18
Well, yes, a snapshot is a version of the table at a specific point in time.
6:24
Think of it like a Git commit.
6:25
If you know how Git works, that's going to help you a lot with thinking about time travel, branching,
6:30
tagging, snapshotting, all of these things.
6:33
In Iceberg, the snapshot captures the state of the table, and once it's created, it's frozen.
6:39
That's it.
6:39
That snapshot is frozen for all time.
6:42
Here we have snapshot S0 pointing to our manifest list.
6:47
Each snapshot has an ID and a timestamp and points to a manifest list.
6:52
And I sure hope you see this coming.
6:54
Metadata files are immutable too.
6:57
Everything in iceberg is right once and never changed.
7:00
So, if everything's immutable, how do you add data? Well, simple.
7:03
You write new files at every level.
7:06
New data comes in, Iceberg writes new data files.
7:09
Then, what's it going to do?
7:10
It's got to create a new manifest pointing to those files.
7:14
And that new manifest, a new manifest list gets created too, referencing the old manifests and the new one.
7:23
So, this is data being added to a table.
7:25
So, we'll just point to all those manifest files and add our new manifest file to this manifest list.
7:31
And of course, we're going to need a new metadata file with a fresh snapshot.
7:36
That snapshot is going to point to the new manifest list.
7:39
All those old files are still there, unchanged.
7:42
And that's going to support time travel later on.
7:45
And if you look closely here, you'll see that that old snapshot is available too.
7:49
So that state of the database, we still know about that, even though we've mutated it
7:54
and added data to the table in the current snapshot. So, how does a query engine know where this metadata file is located?
How catalogs track Iceberg tables
8:01
You think about that, that's some path in an S3 bucket.
8:04
That's a horrible name.
8:05
Some big long thing.
8:06
You don't want to be copying and pasting that and managing that everywhere.
8:10
You want a nice table with a name like sales or meetups or something like that.
8:15
That's where the catalog comes in.
8:18
And we're going to cover this catalog in depth next.
8:21
So that is the basic iceberg architecture, data files at the bottom.
8:26
Manifests track the data files, manifest lists organize the manifests, and then metadata files tie it all together.
8:35
The catalog, kind of on the outside, points to the current metadata file with a
8:40
nice friendly name that a human can deal with. Everything in there is immutable.
8:46
That's what makes time travel, transactions, and schema evolution all possible.
8:50
Next up, like I said, the magic of:
8:53
the catalog.

-----

https://www.youtube.com/watch?v=b02Y1UMFv2k&list=PLf38f5LhQthcLN84xP6JgQ-pEbAc8SbSi&index=3

Iceberg Data vs Metadata Layers
0:05
We've seen that Iceberg splits files into two layers, the data layer that holds your actual records.
0:10
Parquet or ORC or Avro or whatever.
0:12
Then the metadata layer, that's the manifests, the manifest lists,
0:17
and the metadata files that track what's in the data and where the data is.
0:22
So you want to query that sales table.
0:24
How does Spark or Trino or Dremio or whatever know where to find the metadata file?
0:31
You're not going to hard code that S3 path into every query.
0:34
That would be ridiculous and painful, and nobody wants that life.
0:38
And anyway, it changes with every single snapshot.
Why Iceberg Needs a Catalog
0:42
No, you're just going to write select star from sales.
0:46
Hopefully, you're not literally going to write select star from sales against your data lake, but you know what I mean.
0:51
This is where the catalog comes in.
0:53
It maintains a simple mapping, table name to metadata file location in your blob store.
1:02
Here's what happens.
1:03
The query engine says, hey, catalog, where sales?
1:07
The catalog says, oh, the metadata file.
1:11
Is S3 colon slash slash blah blah blah slash something slash blah blah blah.
1:15
The engine reads the metadata, follows the tree down through the manifest list and manifests and actual data files,
1:15
and there you go.
1:16
Every commit, whether it's new data, schema change, partition update, whatever, the catalog gets atomically updated
1:29
to point to the latest metadata file.
1:33
Keeping a pointer to the current metadata file for each table is the first responsibility of the catalog.
1:40
New data means new metadata file, which means a new pointer.
1:44
But that seems a little too simple.
Atomic Commits & Concurrent Writers
1:46
That's not all the catalogue is willing to do for us.
1:49
It also ensures atomicity.
1:52
When that pointer swaps from old to new, it's one atomic operation.
1:57
This is what gives you consistent reads and safe concurrent rights.
2:01
If two writers try to commit at once, only one of them wins.
2:05
The other sees the conflict and retries with the latest state.
2:10
Third, and this is important, the catalog coordinates.
2:13
It doesn't write anything.
2:14
It doesn't write data files, doesn't write manifests, manifest lists, metadata files.
2:18
Your engine does that: Spark, Flink, whatever it is you're using.
2:22
The catalog just tracks which version is current and makes sure commits don't step on each other.
2:28
You might be wondering, is there a standard way for catalogs to work?
2:32
Like a common API.
2:33
Ah, good news.
2:34
There is.
Iceberg REST Catalogs & Governance
2:35
It's called the Iceberg REST Catalog specification.
2:38
It is just a spec, it is not itself an executable thing.
2:42
Iceberg provides a reference implementation, of course, but it's a spec and anyone can implement it.
2:49
The main open source implementations are Apache Polaris.
2:53
Unity Catalog, Apache Lakekeeper, and Apache Gravatino.
2:57
Let it never be said that Apache doesn't care about your catalog needs.
3:02
Some of them really stick to the basics: track tables, point to the metadata, get out of the way.
3:07
Others implement the full spec and add governance features on top, like access control, lineage, that kind of stuff.
3:13
The spec also gives you portability.
3:15
You can switch catalog implementations without changing your table format
3:19
or rewriting queries or rewriting any data or anything like that.
3:23
Of course, if one catalog provides a feature that you really like, you're going to stick with that catalog.
3:28
but the underlying mass of the data lake is compatible between them.
3:33
Here's another trend: multi-format catalogs.
3:37
Right now, you probably have separate catalogs: one for iceberg tables, one for Delta, maybe another for raw parquet files.
3:46
That's a pain.
3:47
The new generation of catalogs handles all of it.
3:51
And catalogs are adding more advanced features.
3:54
Some are implementing Git like versioning for metadata.
3:57
So you could branch and merge table schemas like they were code.
3:59
Some are adding cross region replication, real time metadata sync, even automatic table maintenance.
4:05
To keep files compacted and snapshots pruned.
4:08
Catalogs are evolving from simple name-to-location mappers into kind of little control planes for your entire data lake,
4:15
a portion of your whole data platform. If you're a Confluent Cloud user and
Cloud, Legacy Options & How to Choose
4:20
you're using Tableflow, which we're going to cover in this course, Tableflow itself provides a fully compliant iceberg.
4:27
REST catalog, and it works on all of the clouds.
4:31
If you prefer to stick with your own service provider, each one has their own product, there's AWS Glue.
4:36
Microsoft Purview, Google Dataplex, and they can work along with Iceberg,
4:40
but none of them fully implements the REST Catalog API as of the time of this.
4:45
recording.
4:45
Now, if you already have data infrastructure of some kind, and well, who doesn't, Iceberg can work with that too.
4:52
Hive Metastore
4:53
GDBC databases, even Hadoop, they can all act as iceberg catalogs.
4:59
They weren't built for icebergs, so you might lose some features, but you could get an integration win.
5:04
Hive Metastore, for example, doesn't support atomic commits with multiple concurrent writers, again,
5:10
as of the time of this recording in late 2025.
5:13
It's okay for batch ETL type things, but streaming, you're probably going to have some struggle.
5:18
In any case, catalogs aren't optional.
5:20
That's a necessary part of what it means to be iceberg.
5:23
Every iceberg data lake needs one.
5:26
The good news is you have the options.
5:28
REST catalogs for flexibility, cloud-native ones for convenience if you're all in on your provider,
5:34
Hive Metastore if you're already still running Hive.
5:37
And pick based on what you need.
5:40
If you need concurrent writers, well, then you're going to need atomic commits.
5:43
Multi-region, you're going to need replication support.
5:46
It's the same thing as always.
5:47
You need to look at the feature matrix current as of the moment you're making the decision.
5:52
Evaluate what you need and make trade-offs from there.
5:55
The catalog you choose, though, shapes what's possible, so it is an important decision.
6:00
Next up, we've got ACID Transactions, how Iceberg handles multiple writers without the whole world blowing up.
