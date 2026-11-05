**COURSE DEVELOPMENT DRAFT v0.1**

**dbt Fundamentals**

From ETL to ELT with open-source dbt (v1 and v2)

Self-paced LMS course: video scripts, learner text, labs and quizzes

Labs: Rosetta DBT Studio \+ DuckDB

Prepared November 4, 2026\. Content researched against dbt documentation of that date.

**Contents**

# **How to use this document**

This is the working draft of the dbt course: landing page, curriculum, and every lesson written out. It is built for editing. Every lesson separates what the presenter records from what the learner reads in the LMS.

| Block | Who it is for | Where it goes |
| :---- | :---- | :---- |
| **VIDEO SCRIPT** (purple box) | Presenter | Read on camera or as voice-over. Lines in \[brackets\] are on-screen cues, not spoken. |
| **LMS CONTENT** (blue rule) | Learner | Pasted into the LMS lesson page beneath or beside the video. |
| **LAB** (green rule) | Learner | Hands-on exercise in Rosetta DBT Studio with DuckDB. Delivered as LMS pages with downloadable starter files. |
| **KNOWLEDGE CHECK** (amber rule) | LMS quiz engine | Question and answer pairs to load as quiz items. |

### **Open items to verify before recording**

dbt changed substantially in 2026, and the sources do not fully agree with each other. Check these items against the live docs on the day you record, then update the lessons.

* **v2 naming and status.** In 2025 the new Rust engine was called "Fusion". The June 2026 announcement renamed the open-source piece "dbt Core v2.0" (alpha). By October 2026 the docs call the two distributions "dbt v2" and "dbt OSS" (package dbt-oss), and describe v2 as the recommended default. Confirm which names and which release stage (alpha, beta, GA) apply when you record.

* **Latest v1 release.** The docs list v1.12 as current and v1.13 as beta (October 2026). Confirm.

* **Rosetta DBT Studio runs dbt Core v1.** Its README says it embeds dbt Core and a managed Python environment. It does not say which version, and it does not mention v2. This course therefore runs all labs on v1 and treats v2 as a CLI side-lab. Confirm the version bundled in the release you teach with.

* **Studio menu names.** Lab steps describe actions ("open the SQL editor", "run dbt build") rather than exact button labels. Replace with the current UI labels and capture screenshots.

* **v2 and DuckDB.** The v2 docs list gaps in the DuckDB adapter (extension loading needs a separate driver, static analysis can fail on local-file reads). Re-check issue tracker dbt\#14393 before recording Lesson 2.5.

* **Tool-agnostic sections.** Lesson 1.4 names alternative tools. Verify each is still maintained and who owns it. Fivetran and dbt Labs merged in 2026, so vendor ownership claims age quickly.

# **Course landing page (LMS)**

**Course title:** dbt Fundamentals: From ETL to ELT with Open-Source dbt

**Format:** self-paced, about 12 hours. 26 short lessons (video plus reading), 7 labs and a capstone.

## **About this course**

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 1.5 min *\[ON SCREEN: course title card, then a simple before/after diagram: tangled pipeline of scripts on the left, a clean lineage graph on the right\]* Welcome. If your team moves data into a cloud warehouse, someone is writing SQL to clean it up, join it and make it trustworthy. The question is where that SQL lives, who can change it, and how you know it still works. dbt is the most widely adopted answer to that question. You write plain SQL select statements. dbt works out the order, builds the tables and views, tests them, documents them, and gives your team the same workflow software engineers have used for decades: version control, code review, automated tests and deployment. In this course you will learn what dbt is, why it moved the industry from ETL to ELT, where that pattern is the wrong choice, and how to bring it into your own organization. You will build a working project as you go, using DuckDB and Rosetta DBT Studio, so nothing needs a cloud account. We focus on the open-source versions of dbt, version 1 and the new version 2, and we are direct about what is free, what is open source, and what is a paid commercial feature. Let's get started. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

dbt is a framework for transforming data inside your warehouse using SQL and software engineering practices. This course teaches the idea, the tool, and the judgment to know when to use it.

* **Concept first, tool second.** Every module teaches a pattern that applies to any transformation tool, then shows it in dbt.

* **Open source focus.** Labs run on open-source dbt and a free local database. No warehouse account or credit card.

* **Honest about trade-offs.** Dedicated lessons on when not to use dbt, and which alternatives to consider.

* **Version aware.** You learn both dbt v1 (Python) and dbt v2 (Rust), what changed, and how to choose.

## **What you will learn**

**LMS CONTENT  \|  learner reads this on the page**

* Explain what dbt does and does not do, and where it sits in a modern data stack.

* Contrast ETL with ELT and justify why ELT fits cloud data warehouses.

* Recognize situations where dbt is the wrong tool and name better options.

* Build a dbt project: sources, staging models, marts, tests, documentation and lineage.

* Use Jinja, macros, packages and incremental models to keep projects DRY and fast.

* Describe the differences between dbt v1 and v2, and between open-source, free-proprietary and paid platform capabilities.

* Set up version control, environments and CI so analytics code ships like software.

* Make an adoption case for your organization and plan a first project and a migration path.

## **Who it is for**

**LMS CONTENT  \|  learner reads this on the page**

| If you are... | You will get... |
| :---- | :---- |
| A data or analytics engineer new to dbt | A full working foundation and the reasoning behind each convention. |
| An analyst who writes SQL | A path from ad hoc queries to tested, versioned, shared models. |
| A data lead, architect or consultant | A decision framework: when dbt fits, when it does not, and how v1, v2 and the commercial platform compare. |
| A customer success or solutions professional | The vocabulary and arguments to guide a customer through an adoption decision. |

**Prerequisites:** comfortable reading and writing SQL (joins, group by, CTEs). No Python, Git or command-line experience required; the course introduces what you need. **You need:** a laptop (Windows, macOS or Linux) and permission to install a desktop app.

## **Curriculum**

**LMS CONTENT  \|  learner reads this on the page**

| Module | Title | Lessons | Lab |
| :---- | :---- | :---- | :---- |
| 1 | From ETL to ELT: why dbt exists | 1.1 What dbt is; 1.2 ETL vs ELT; 1.3 Why ELT wins on cloud warehouses; 1.4 When not to use dbt | Lab 1: Set up the sandbox and do ELT by hand |
| 2 | dbt versions and the ecosystem | 2.1 Language and engine; 2.2 dbt v1; 2.3 dbt v2 and its distributions; 2.4 The commercial platform; 2.5 Choosing your path | Lab 2: Version readiness check |
| 3 | Building models | 3.1 Anatomy of a project; 3.2 ref() and the DAG; 3.3 Sources and staging; 3.4 Materializations | Lab 3: Staging and marts on DuckDB |
| 4 | Testing, documentation and trust | 4.1 Data tests; 4.2 Unit tests; 4.3 Docs and lineage | Lab 4: Break it, test it, document it |
| 5 | DRY code and performance | 5.1 Jinja and macros; 5.2 Packages; 5.3 Incremental models | Lab 5: Macro and incremental model |
| 6 | Working like a software team | 6.1 Environments; 6.2 Git and CI; 6.3 Orchestration and deployment options | Lab 6: Branch, change, validate |
| 7 | Applying dbt in your organization | 7.1 Benefits and value; 7.2 Project structure and governance; 7.3 Adoption and migration; 7.4 Capstone brief | Capstone |

# **Module 1: From ETL to ELT: why dbt exists**

**Module goal:** the learner can explain dbt, ETL versus ELT, why ELT suits cloud warehouses, and where it does not fit. This module is mostly concept, so it is also the tool-agnostic core of the course.

## **Lesson 1.1: What dbt is (and is not)**

Format: video \+ reading   \|   Time: 15 min

**Learning objectives.** By the end of this lesson the learner can:

* State in one sentence what dbt does.

* Place dbt in the extract, load, transform, serve flow.

* List three things dbt does not do.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3 min *\[ON SCREEN: a simple data flow: Sources \> Extract and Load tool \> Warehouse \> dbt (inside the warehouse) \> BI tools and apps\]* Let's start with the simplest possible definition. dbt is the T in ELT. It transforms data that is already sitting in your warehouse. You write a select statement. That's a model. dbt wraps it in the right create-table or create-view statement, runs it in the right order, and tells you if something breaks. Notice what dbt does not do. It does not extract data from source systems. It does not load data into your warehouse. It is not a database, and it does not run your queries itself. Your warehouse does the work. dbt writes and orders the SQL, and adds the engineering around it. *\[ON SCREEN: three icons for what dbt adds: testing, documentation, version control\]* That engineering is the real value. Tests that run on every build. Documentation generated from the code. Everything in Git, so every change is reviewed. In short, dbt brings software engineering practice to SQL. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

**dbt in one sentence:** dbt compiles SQL select statements and Jinja into runnable code, executes it in dependency order inside your data platform, and adds testing, documentation and lineage.

| dbt does | dbt does not |
| :---- | :---- |
| Transform data already in the warehouse | Extract data from source systems |
| Order models by dependency (the DAG) | Load raw data into the warehouse |
| Test, document and trace lineage | Store or process data itself. Your warehouse or engine does. |
| Work with version control and CI | Schedule itself in the open-source version. You need an orchestrator (Lesson 6.3). |

**Analogy for customers:** dbt is to SQL what a build system is to source code. You describe what each piece should look like; the tool works out the order and builds it.

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Which part of the data flow does dbt own?**

*Answer: Transformation, inside the warehouse (the T in ELT).*

**True or false: dbt stores your data.**

*Answer: False. Your warehouse or database stores and processes it. dbt generates and orders the SQL.*

## **Lesson 1.2: ETL versus ELT**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Define ETL and ELT and give the order of steps in each.

* Explain where transformation runs in each pattern.

* Describe how the shift changes who does the work.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: two horizontal flows. Top: Extract \> Transform (separate server) \> Load. Bottom: Extract \> Load \> Transform (inside warehouse)\]* ETL means extract, transform, load. You pull data out of source systems, transform it on a separate processing server, and only then load the finished result into the warehouse. ELT flips the last two steps. You extract, you load the raw data straight into the warehouse, and you transform it there. It sounds like a small change. It changes almost everything. In ETL, the transformation logic lives in a proprietary tool or custom code, owned by specialist engineers. Raw data is often thrown away after the transform. If the business changes a definition, you may have to go back to the source and run it all again. In ELT, raw data lands untouched and stays there. Transformations are SQL, run on the warehouse's own engine. Analysts can read them, review them and change them. And when a definition changes, you simply rebuild from the raw data you already have. *\[ON SCREEN: highlight the phrase "Raw data is kept"\]* That one idea, keep the raw data and transform it where it lives, is the foundation of everything in this course. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

|  | ETL | ELT |
| :---- | :---- | :---- |
| Order of steps | Extract, transform, load | Extract, load, transform |
| Where transformation runs | A separate processing server or tool | Inside the data warehouse or lakehouse |
| Raw data | Often not stored in the warehouse | Loaded first and retained |
| Transformation language | Tool-specific designer or custom code | SQL (plus Jinja and, where needed, Python) |
| Who can change logic | Specialist ETL developers | Anyone who writes SQL and follows the review process |
| When requirements change | Often rework upstream and re-extract | Edit the model and rebuild from retained raw data |
| Typical tools | Informatica, SSIS, custom Spark or Python jobs | EL: Fivetran, Airbyte, dlt, custom loaders. T: dbt and similar |

| Common point of confusion ELT does not mean "no transformation before load". Light fixes (file format, encoding, dropping a corrupt file) can happen at load. The principle is that business logic is applied after the raw data lands. |
| :---- |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**In ELT, where does business logic run?**

*Answer: Inside the warehouse, after the raw data has been loaded.*

**Name one practical benefit of retaining raw data.**

*Answer: You can rebuild or change any model without re-extracting from the source, and you can audit back to the original record.*

## **Lesson 1.3: Why ELT wins on cloud warehouses**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Explain the historical reason ETL dominated.

* Give three properties of cloud warehouses that favor ELT.

* State the trade-offs of ELT honestly.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: timeline: on-premises warehouse era \> cloud warehouse era\]* Why did ETL come first? Because storage and compute used to be scarce and expensive. On-premises warehouses were sized for a fixed workload. Running heavy transformations inside them competed with reporting, so teams moved the work to separate servers and loaded only what was finished. Cloud warehouses changed the economics in three ways. *\[ON SCREEN: three labels appear: Cheap storage, Elastic compute, Scalable SQL engines\]* First, storage is cheap, so keeping all the raw data is affordable. Second, compute is elastic and, in most platforms, separated from storage, so a big transformation job does not slow down the dashboards. Third, the warehouse engines are built for large-scale SQL, so a separate transformation server is often just an extra hop. Put together, it is usually faster to build, cheaper to run and easier to maintain if you load first and transform in place. I want to be fair about the trade-offs. ELT puts more load on the warehouse, and that shows up on the bill. Raw data may include sensitive fields you need to protect. And SQL is not the right tool for every kind of transformation. We cover those limits in the next lesson. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

### **Why ETL came first**

Legacy warehouses coupled storage and compute and had fixed capacity. Transformations competed with queries from business users, so teams offloaded the work to dedicated ETL servers and loaded only curated output.

### **What cloud platforms changed**

* **Low-cost storage.** Retaining full raw history is practical, which makes reprocessing and audit possible.

* **Elastic, often decoupled compute.** Transformation workloads can be scaled or isolated from reporting workloads.

* **Columnar, massively parallel SQL engines.** Set-based SQL on large tables is what these engines do best.

* **Simpler architecture.** One fewer system to run, secure and monitor between the loader and the warehouse.

### **The organizational benefit (often the bigger one)**

When transformations are SQL in a repository, the people who understand the business can read and contribute to them. Review, testing and documentation become normal parts of the workflow instead of afterthoughts.

### **Trade-offs to be honest about**

| Trade-off | What to do about it |
| :---- | :---- |
| Compute cost can climb as models multiply | Use incremental models, tune materializations, monitor spend per model. |
| Raw sensitive data lands in the warehouse | Apply masking, access controls and column-level security at load or in a protected raw layer. Where regulation forbids landing it, see Lesson 1.4. |
| Warehouse lock-in of SQL dialects | dbt abstracts some differences, but not all. Keep platform-specific SQL isolated. |
| Less suited to non-SQL or streaming logic | Use a better-fit tool for that portion (Lesson 1.4). |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Name two cloud-warehouse properties that make ELT practical.**

*Answer: Any two of: cheap storage, elastic or decoupled compute, scalable SQL engines.*

**What is the main cost-related risk of ELT, and one mitigation?**

*Answer: Warehouse compute can grow with model count. Mitigate with incremental models, right-sized materializations and cost monitoring.*

## **Lesson 1.4: When not to use dbt, and what to consider instead**

Format: video \+ reading   \|   Time: 25 min

**Learning objectives.** By the end of this lesson the learner can:

* Identify five situations where dbt is a poor fit.

* Match each situation to a better-suited alternative.

* Apply a short checklist to a real scenario.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 4 min *\[ON SCREEN: title "Right tool, right job"\]* A good practitioner knows when not to use a tool. dbt is excellent at one thing: batch SQL transformation inside an analytical platform. When your problem is not that, use something else. Here are the main cases. *\[ON SCREEN: list builds one item at a time as you speak\]* One. Streaming and sub-second latency. dbt runs in batches. If you need to transform events as they arrive, look at stream processors such as Flink, Spark Structured Streaming, or the streaming features of your platform. Two. Getting data in. dbt does not extract or load. You need an ingestion tool or your own loaders. Three. Heavy non-SQL work, like machine learning feature pipelines on unstructured data or complex procedural logic. Spark or Python-based frameworks fit better. dbt does support Python models on some platforms, but it is not its strength. Four. Data that must not land raw. If regulation requires masking or tokenizing before data enters the warehouse, you need a transform step before load. That is ETL, or a hybrid, and it is the right choice for that data. Five. Orchestration and operational workflows. dbt can order its own models, but it is not a general scheduler for everything else in your estate. And one more: very small projects. If you have three views and one analyst, dbt may be more ceremony than value. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Situation | Why dbt is a poor fit | Consider instead |
| :---- | :---- | :---- |
| Real-time, event-by-event processing | dbt is batch oriented. Latency is bounded by run frequency. | Stream processors (Flink, Spark Structured Streaming, Kafka Streams) or the platform's native streaming tables. |
| Extracting and loading from sources | Out of scope. dbt starts after data is loaded. | Managed or open-source EL tools (Fivetran, Airbyte, dlt) or custom loaders. Pair them with dbt. |
| Unstructured data, ML features, complex procedural or row-by-row logic | SQL is a poor expression of the work. Python models exist on some adapters but are secondary. | Spark, Python frameworks, notebooks, feature-store tooling. |
| Data that must be masked or tokenized before it reaches the warehouse | ELT lands raw data first. | ETL or ETLT for that pipeline: transform or tokenize in flight, then load. |
| Cross-system orchestration and operational workflows | dbt orders its own DAG only. | Orchestrators (Airflow, Dagster, Prefect) that call dbt as one step. |
| Warehouse with no spare or cost-effective compute (some on-premises systems) | ELT assumes the platform can absorb transformation load. | Transform upstream (ETL) or move the workload to a platform that can. |
| Tiny projects: a handful of views, one author | Overhead may exceed benefit. | Plain SQL views or scheduled queries. Adopt dbt when complexity grows. |
| Teams standardized on a platform-native or competing transformation tool | Switching cost may outweigh gains. | Evaluate the native option (for example BigQuery-native Dataform, Databricks declarative pipelines) or SQLMesh. Compare on your requirements. |

| Hybrid is normal Many mature stacks use several of these together: an EL tool and a streaming path for ingestion, dbt for warehouse transformation, an orchestrator on top, and a tokenization step before load for regulated fields. The question is rarely "dbt or not" but "which part of the stack is dbt's job". |
| :---- |

### **Quick checklist for customers**

1. Is the data already in an analytical platform that can run SQL at scale?

2. Is batch latency (minutes to hours) acceptable?

3. Is the logic naturally expressible as SQL set operations?

4. Can raw data legally and safely land in the platform?

5. Is there enough shared logic or team size to benefit from testing, review and lineage?

If you answered yes to most of these, dbt is likely a good fit. Any "no" tells you where a different tool belongs in the picture.

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**A bank must tokenize card numbers before they reach the cloud warehouse. Is pure ELT with dbt appropriate for that data flow?**

*Answer: No for that flow. Tokenize before load (ETL or ETLT), then use dbt on the tokenized data in the warehouse.*

**You need transformations on events within one second of arrival. Name a better-suited category of tool.**

*Answer: A stream processor such as Flink or Spark Structured Streaming.*

## **Lab 1: Set up the sandbox and do ELT by hand**

**Time:** 45 minutes   \|   **Goal:** install Rosetta DBT Studio, create a DuckDB database, and perform the E, L and T steps manually so the ELT pattern is concrete before dbt automates it.

**LAB 1  \|  LMS lab page**

### **Why this lab**

Before using dbt, you will do its job by hand. You will "load" raw data into a raw schema, then write a transformation in SQL. In Module 3 you will see what dbt adds.

### **Setup**

1. Download the latest Rosetta DBT Studio release for your operating system from its GitHub releases page and install it. The README states that no separate Python or dbt installation is required.

2. Open Rosetta DBT Studio and create a new project named dbt\_course.

3. Create a new connection of type **DuckDB** and point it to a new local file, for example course.duckdb. (If your Studio release does not list DuckDB, use the sample project that ships with a DuckDB database, per the README.)

4. Open the SQL editor and confirm the connection works by running select 1;.

### **Step A: Load raw data (the "EL")**

Open the SQL editor and run the script in **Appendix A: Starter data** to create the raw schema and three tables: raw.customers, raw.orders, raw.payments. This stands in for an extraction and loading tool such as Fivetran or Airbyte.

Check your work:

| select count(\*) from raw.customers;   \-- expect 6 select count(\*) from raw.orders;      \-- expect 10 select count(\*) from raw.payments;    \-- expect 10 |
| :---- |

### **Step B: Transform by hand (the "T")**

Create a table that gives one row per customer with their order count and total paid. Run:

| create schema if not exists analytics;   create or replace table analytics.customer\_summary as select     c.id as customer\_id,     c.first\_name,     c.last\_name,     count(distinct o.id) as order\_count,     coalesce(sum(p.amount\_cents), 0\) / 100.0 as total\_paid from raw.customers c left join raw.orders o   on o.customer\_id \= c.id left join raw.payments p on p.order\_id \= o.id group by 1, 2, 3;   select \* from analytics.customer\_summary order by total\_paid desc; |
| :---- |

### **Step C: Feel the pain**

Answer in the lab notes box:

* If a colleague changed the logic, how would you know what changed and why?

* If raw.orders got a new row tomorrow, what would you have to do to refresh customer\_summary?

* If you had 50 tables like this, how would you know which to rebuild first?

* How would you test that customer\_id is unique and not null?

| What you should notice The raw data stayed untouched in raw. The transformation ran inside the database, not on a separate server. That is ELT. Everything painful in Step C is what dbt automates, starting in Module 3\. |
| :---- |

### **Deliverable**

Screenshot of the customer\_summary result plus your answers to the four Step C questions.

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**After Step A, where does business logic run in your pipeline?**

*Answer: It has not been applied yet. Raw data is loaded unchanged. The logic runs in Step B, inside DuckDB (ELT).*

# **Module 2: dbt versions and the ecosystem**

**Module goal:** the learner can describe the differences between dbt v1 and v2, tell open source from free-proprietary from paid commercial capabilities, and choose a path for a given organization. This is the module most likely to change, so it is isolated from the hands-on modules.

## **Lesson 2.1: The dbt framework: language and engine**

Format: video \+ reading   \|   Time: 15 min

**Learning objectives.** By the end of this lesson the learner can:

* Distinguish the dbt language from the dbt engine.

* Explain why a major version change affects the engine more than your SQL.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 2.5 min *\[ON SCREEN: two stacked layers. Top: "dbt language: SQL, Jinja, YAML, tests". Bottom: "dbt engine: parse, compile, run, metadata"\]* The dbt docs describe dbt as two things. A language and an engine. The language is what you write: SQL select statements, Jinja templating, YAML configuration, tests. The engine is the program that reads your project, compiles it, runs the graph of models against your warehouse, and produces metadata. Why does this matter? Because when people say "dbt version 1" and "dbt version 2", they are mostly talking about the engine. Version 1 is a Python engine. Version 2 is a rewrite in Rust. The goal is that your project, your business logic, carries across, with a stricter definition of the language so mistakes are caught earlier. Keep this model in your head, because in the next lessons we will separate three questions: which engine, which license, and which commercial features. They are different questions, and mixing them up is the most common source of confusion. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Layer | What it is | Who owns the change |
| :---- | :---- | :---- |
| dbt language | The project you write: models (SQL), Jinja, YAML configs, tests, macros, seeds, snapshots | You, guided by the framework spec |
| dbt engine | Parses and compiles the project, executes the DAG, produces artifacts (metadata files) | The dbt maintainers. You choose which distribution to install. |
| Adapters | Connectors that translate dbt to a specific database or warehouse | Platform vendors and the community. In v2 these are bundled. |
| dbt platform (optional) | A hosted commercial product for development, scheduling, CI and more | dbt Labs (now part of Fivetran). Paid tiers plus a free developer tier. |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Is the SQL in your models different between v1 and v2?**

*Answer: The language is shared, but v2 enforces a stricter specification, so previously ignored mistakes (for example a misspelled config) can become errors.*

## **Lesson 2.2: dbt v1: the Python, Apache 2.0 version**

Format: video \+ reading   \|   Time: 15 min

**Learning objectives.** By the end of this lesson the learner can:

* Describe what v1 is, its license and its support status.

* List what v1 gives you and what it leaves to you.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3 min *\[ON SCREEN: "dbt v1.x, Python, Apache 2.0"\]* Version 1 is the original dbt, written in Python. It is released under the Apache 2.0 license, which is a permissive open-source license. You can use it, modify it and redistribute it, including commercially. You install it with pip, along with an adapter for your platform, for example dbt-duckdb or dbt-snowflake. Then you run commands: dbt run, dbt test, dbt build, dbt docs generate. Is it going away? No. dbt Labs has said v1 remains fully supported, the old versions stay on PyPI and GitHub, and they are continuing to release it. Version 1.12 is the current line, with 1.13 in beta as of this recording. But they also say that over time, new capabilities will land in v2 only. In this course, we use v1 for the labs. Rosetta DBT Studio embeds dbt Core, so it works with the Python version out of the box. Everything you build carries over to v2. *\[ON SCREEN: "Labs: v1. Concepts: both."\]* |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Attribute | dbt v1 (dbt Core) |
| :---- | :---- |
| Engine | Python |
| License | Apache 2.0 (OSI-approved open source) |
| Install | Python and pip, plus an adapter package (for example dbt-duckdb) |
| Current line | v1.12 (v1.13 in beta, per October 2026 docs) |
| Support | Fully supported. Old versions remain available. The maintainers state v1 is not going away soon. |
| Strengths | Mature, huge package and adapter ecosystem, widely known, fully open source, runs everywhere Python runs |
| Limits | Slower parsing on very large projects, no built-in SQL comprehension, tooling such as the language server and linter are not part of the open-source package |
| Where used | Self-hosted pipelines, Rosetta DBT Studio, the dbt platform (v1 release tracks) |

| Getting v1 projects ready for v2 v1.12 includes an opt-in flag, dbt parse \--use-v2-parser, that checks whether your project parses under the stricter v2 rules. Earlier releases (v1.10 and v1.11) added deprecation warnings that point out configs that v2 will reject. Fixing those warnings is the best preparation. |
| :---- |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**What license covers dbt v1, and what does that allow?**

*Answer: Apache 2.0, a permissive open-source license: use, modify and redistribute, including commercially.*

## **Lesson 2.3: dbt v2 and its two free distributions**

Format: video \+ reading   \|   Time: 25 min

**Learning objectives.** By the end of this lesson the learner can:

* Describe what changed in v2.

* Distinguish dbt v2 from dbt OSS by license and capability.

* Explain why the naming in older articles differs ("Fusion", "dbt Core 2.0").

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 5 min *\[ON SCREEN: "dbt v2: Rust, one engine, two distributions"\]* Now the new generation. Version 2 is a rewrite of the engine in Rust, built on the same foundations as what dbt Labs first called the Fusion engine in 2025\. What changes for you? Faster parsing, especially on very large projects. A stricter language specification, so a typo in a config key is an error instead of being silently ignored. New metadata files in Parquet format that you can query with DuckDB. A rebuilt documentation experience. A simpler install without Python virtual environments. And adapters built on Arrow-based drivers. *\[ON SCREEN: two boxes: "dbt v2" and "dbt OSS"\]* Here is the part that causes confusion. There are two free ways to get v2. The first is simply called dbt v2. It is the recommended install. It builds on the open-source runtime and adds proprietary capabilities: SQL comprehension that catches errors before your warehouse runs the query, a built-in linter, editor features such as autocomplete, and with the free VS Code extension, column-level lineage. It is free to install and run. Some features unlock with a free login. It is released under the dbt Product Licensing Agreement, so it is not open source. The second is dbt OSS. It is the Apache 2.0 open-source runtime, nothing proprietary. It runs the standard commands: run, build, test, compile, parse. It does not include the SQL comprehension, the linter or the language server. dbt Labs says to choose it only if your organization requires a strictly open-source license, or if you are building something on top of the code. Same framework, same language specification, so your project is portable between them. *\[ON SCREEN: note "Older articles say Fusion or dbt Core 2.0. Same lineage, names changed."\]* If you read older material, you will see the names Fusion and dbt Core 2.0. The naming settled over 2026, so check the docs for the current terms. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

### **What changed in v2**

* **Rust engine** with faster parsing and execution, aimed at very large projects.

* **Strict language specification.** Unknown or misspelled configuration is an error.

* **Parquet metadata artifacts** (instead of very large JSON files) that can be queried directly with DuckDB.

* **New documentation experience** that scales to large projects.

* **Bundled adapters** built on ADBC and Arrow. No separate adapter packages to manage.

* **Simpler installation** without Python virtual environments.

### **The two free v2 distributions**

|  | dbt v2 (recommended) | dbt OSS |
| :---- | :---- | :---- |
| Package | dbt | dbt-oss (install with uv tool install dbt-oss) |
| License | dbt Product Licensing Agreement (proprietary, free to use) | Apache 2.0 (open source) |
| Built on | The open-source runtime plus proprietary extensions | The open-source runtime only |
| Standard commands (run, build, test, compile, parse) | Yes | Yes |
| SQL comprehension, static analysis | Yes | No |
| Built-in linter (dbt lint) | Yes | No |
| Language server and VS Code extension features | Yes | No |
| Column-level lineage | Yes (precise lineage in the "full" docs experience; some features may need a free login) | No |
| Free login unlocks some features | Yes. Optional. | Not applicable |
| Choose it when | Almost always | Your policy requires a strictly open-source license, or you are building on the code |

| How to explain "open source" precisely dbt v1 and dbt OSS are open source (Apache 2.0). dbt v2 is free to use but proprietary: you can run it everywhere, but you cannot treat its source as open source or freely redistribute it. If a customer says "we need open source", ask whether they mean "free" or "OSI-approved license". They get different answers. |
| :---- |

### **Known limits to flag (verify at recording time)**

* In the October 2026 docs, v2 DuckDB support has gaps: loading DuckDB extensions requires installing a separate driver with dbc, and static analysis can fail on models that read local CSV, Parquet or JSON files directly.

* Release stage: the open-source v2 was in alpha in June and beta in August 2026\. Confirm GA status before advising production use.

* v1 to v2 is a major version change. Expect some breaking changes. Helper tools exist (dbt-autofix and an agent skill for migration).

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Which v2 distribution is open source under Apache 2.0?**

*Answer: dbt OSS (\`dbt-oss\`).*

**A customer needs the built-in SQL linter and does not have a paid account. Is that possible?**

*Answer: Yes. The recommended dbt v2 distribution includes the linter and is free to use, though it is proprietary rather than open source.*

## **Lesson 2.4: The commercial layer: what the dbt platform adds**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* List the main capabilities of the paid dbt platform.

* Map each to an open-source substitute.

* Explain why teams choose either route.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: three concentric rings: Open source runtime, dbt v2 free, dbt platform\]* So far we have talked about engines you run yourself. There is also a commercial product, the dbt platform. It is a hosted service. It works with both v1 and v2. What does it add? A browser-based development environment. Job scheduling. Continuous integration, so every pull request builds in a temporary schema. Hosted documentation. Monitoring and alerts. And on selected plans, features like the Semantic Layer for consistent metrics, a data catalog, a discovery API, cost insights, and an AI assistant called dbt Wizard. None of this is required to use dbt. Everything the platform does at the operational level, a team can build with open-source parts: Git, an orchestrator such as Airflow or Dagster, CI in your Git host, and a static site for docs. So the choice is a classic build versus buy. The platform saves you the build and maintenance, and adds features that are hard to replicate. Open source gives you control and no subscription cost, but you own the plumbing. We will give you a table you can use with customers. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Capability | Open-source way (v1 or dbt OSS) | dbt platform (commercial) |
| :---- | :---- | :---- |
| Develop | Any editor, VS Code, Rosetta DBT Studio, the CLI | Browser-based Studio IDE, Canvas (drag and drop), VS Code extension and platform CLI |
| Schedule and run | Cron, Airflow, Dagster, Prefect, GitHub Actions, your orchestrator | Built-in job scheduler and run history |
| CI/CD | Pipelines in your Git host that run dbt build on pull requests | Built-in CI that builds changed models in temporary schemas on each PR |
| Docs hosting | dbt docs generate plus any static web host | Hosted, access-controlled docs |
| Alerting and monitoring | Orchestrator alerts, logs, community observability packages | Job notifications, run and model timing dashboards |
| Metrics layer | Define metrics in SQL or a separate semantic tool | dbt Semantic Layer (selected plans) |
| Catalog and discovery | Generated docs and lineage; your own catalog tool | dbt Catalog, Insights, Discovery API (selected plans) |
| Cost visibility | Warehouse query history and your own reporting | Cost Insights (beta, selected plans) |
| Cross-project governance (Mesh) | Manual conventions and packages | Mesh features on enterprise plans (verify) |
| AI assistance | General-purpose AI tools; open agent skills for dbt | dbt Copilot and dbt Wizard (selected plans) |
| Security and access | Your infrastructure, your IAM | SOC 2 hosted service, RBAC, SSO on higher plans |
| Cost model | No license fee. You pay for infrastructure and engineering time. | Subscription tiers from a free developer plan through enterprise. See current pricing. |

**Rosetta DBT Studio** sits on the open-source side: it is a free, AGPL-3.0 licensed desktop IDE that bundles dbt Core, a SQL editor, Git integration, and AI-assisted model generation. It is a useful teaching tool and a lightweight local development option, not a hosted scheduler or a CI service.

| Do not oversell either side Plans, feature lists and pricing change often. Always confirm tier details on the current pricing page before quoting a feature as "free" or "paid". |
| :---- |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Name two dbt platform capabilities and an open-source way to get the same outcome.**

*Answer: Example: scheduling, via Airflow or cron; CI, via GitHub Actions running \`dbt build\` on pull requests.*

## **Lesson 2.5: Choosing your path: a decision guide**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Use a short decision tree to recommend v1, dbt v2 or dbt OSS, with or without the platform.

* Defend the recommendation with reasons.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: decision tree builds step by step\]* Let's turn this into a decision you can make or help a customer make. First question. Do you have an existing v1 project that works and no pressing need to change? Then stay on v1, and prepare. Fix the deprecation warnings, try the v2 parser flag, and plan the move. v1 is not going away. Second question. Are you starting a new project, or do you want the best local developer experience? Then choose dbt v2. It is free, it is the recommended install, and you get the linter and the language features. Third question. Does your policy require a strictly open-source license, or are you building on the code itself? Then choose dbt OSS, or stay on v1. Both are Apache 2.0. Fourth question. Do you want to run the operational pieces yourself? If you have an orchestrator and CI already, you do not need the platform. If you want one place for development, scheduling, CI and docs, the platform is the fast route. Remember that these choices are independent. You can run v1 or v2 with or without the platform, and moving between them is designed to be possible because the language is shared. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Situation | Recommendation | Reasoning |
| :---- | :---- | :---- |
| Stable production project on v1, no urgent need | Stay on v1 (1.12). Run dbt parse \--use-v2-parser and fix deprecations. | v1 remains supported. Preparing now makes a later upgrade cheap. |
| New project, free tooling, no license restriction | dbt v2 | Recommended install. Includes linter and editor features at no cost. |
| Organization requires OSI-approved open source only | v1 (Apache 2.0) or dbt OSS (Apache 2.0) | dbt v2 is proprietary under the product license, even though it is free. |
| Building a product or tooling on dbt code | dbt OSS or v1 | Apache 2.0 allows modification and redistribution. |
| Very large project with slow parse times | Evaluate v2 | Rust engine is designed for large-project performance. Test on a copy first. |
| Learning dbt, no warehouse account | Rosetta DBT Studio with DuckDB (v1 inside Studio) | Free local sandbox. Concepts transfer to every distribution. |
| Small team that wants one managed place to develop, schedule and review | Consider the dbt platform | Saves building and maintaining the operational plumbing. |
| Existing orchestrator and CI, cost sensitive | Open-source route plus your own orchestration | No subscription. You already own the plumbing. |

### **Questions to ask a customer**

* Does your policy say "open source" or "free"? (They are not the same.)

* How large and how old is the project? Any heavy custom macros or package overrides?

* Who operates scheduling and CI today?

* What warehouse, and is its v2 adapter at parity for your needs?

* What is the cost of owning the plumbing versus subscribing?

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Your customer must use only Apache 2.0 licensed software and wants the fastest engine. Which option?**

*Answer: dbt OSS (the Apache 2.0 Rust runtime). Note it lacks the proprietary linter and SQL comprehension, and confirm its release stage.*

## **Lab 2: Version readiness check**

**Time:** 40 minutes   \|   **Goal:** inspect the dbt version inside Rosetta DBT Studio, check a project for v2 readiness, and (optionally) try the v2 distributions from the command line.

**LAB 2  \|  LMS lab page**

### **Part 1: What version am I running? (required)**

1. In Rosetta DBT Studio, open your dbt\_course project. Open the terminal or command runner and run dbt \--version. Record the dbt version and the adapter version in your notes.

2. Confirm the version begins with 1\.. Studio embeds dbt Core; the lab therefore runs on v1.

3. Open dbt\_project.yml. Note the name, version and profile fields. You will use these in Module 3\.

### **Part 2: Is my project v2-ready? (required, needs v1.12 or later)**

If your embedded dbt is 1.12 or later, run:

| dbt parse \--use-v2-parser |
| :---- |

Record whether it passes. If it fails, note the first error and which config it concerns. (The starter project is tiny, so it should pass. In Lab 4 you will intentionally introduce a misspelled config and re-run this check.) If your version is older than 1.12, note that this flag is not available and what the docs say about upgrading.

### **Part 3: Try v2 from the command line (optional, needs a terminal and internet)**

| Heads up This part runs outside Studio, in your own terminal, because Studio bundles v1. Use a throwaway folder. Check the current install pages first; commands and release stage change. |
| :---- |

1. Install uv from its official page.

2. Install the Apache 2.0 distribution: uv tool install dbt-oss, then dbt \--version. Confirm it starts with 2\..

3. Install the recommended distribution by following the "Install dbt" page in the docs. Compare dbt \--help between the two. Look for lint and login.

4. Point either at a copy of your lab project with a DuckDB profile. Note any warnings. Do not expect everything to work: the v2 DuckDB adapter has documented limits.

### **Deliverable**

A short table: version found, license, and whether the project passed the v2 parser check. Then two sentences: which path would you recommend for this project and why?

# **Module 3: Building models**

**Module goal:** the learner can read and build a dbt project with sources, staging models and marts, and choose the right materialization. Labs run on DuckDB inside Rosetta DBT Studio (dbt v1).

## **Lesson 3.1: Anatomy of a dbt project**

Format: video \+ reading   \|   Time: 15 min

**Learning objectives.** By the end of this lesson the learner can:

* Name the key files and folders of a dbt project and what each does.

* Explain how profiles.yml separates connection settings from project code.

* Run the core commands and say what each does.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3 min *\[ON SCREEN: file tree of a project in Rosetta DBT Studio, with callouts\]* A dbt project is just a folder of text files. That is deliberate, because text files work with Git. The center is dbt\_project.yml. It names the project and sets defaults. The models folder holds your select statements. Seeds are small CSV files dbt can load. Tests holds custom tests. Macros holds reusable Jinja. Snapshots track slowly changing data. Connection details live somewhere else, in a file called profiles.yml, so the same project can point at your laptop, a test environment and production without changing any code. In Rosetta DBT Studio, the connection you created in Lab 1 is managed for you. *\[ON SCREEN: command table builds: compile, run, test, build, docs generate\]* Five commands cover most of your day. Compile turns your models into plain SQL without running them. Run builds the models. Test checks your data. Build does run and test together in dependency order. And docs generate creates your documentation site. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| File or folder | Purpose |
| :---- | :---- |
| dbt\_project.yml | Project name, folder paths, default configs such as materialization by folder |
| profiles.yml | Connection settings (kept outside the project in command-line setups; managed by Studio in this course) |
| models/ | SQL select statements (models) and YAML files describing them |
| seeds/ | Small CSV files loaded into the database (lookup tables, test data) |
| tests/ | Custom "singular" tests written as SQL |
| macros/ | Reusable Jinja functions |
| snapshots/ | Definitions that record how mutable records change over time |
| target/ | Generated output: compiled SQL and metadata. Not committed to Git. |

| Command | What it does |
| :---- | :---- |
| dbt compile | Renders Jinja and ref() into plain SQL. Nothing runs in the database. |
| dbt run | Builds models in dependency order |
| dbt test | Runs data tests and unit tests |
| dbt build | run plus test (plus seeds and snapshots), in order, stopping downstream work when something fails |
| dbt docs generate | Builds the documentation site and lineage graph |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Why is the connection kept out of the models?**

*Answer: So the same code can run against dev, test and production just by changing the target.*

## **Lesson 3.2: Models, ref() and the DAG**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Write a model as a select statement.

* Use ref() to depend on another model.

* Explain what the DAG is and why dbt builds it.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: a .sql file with a single select statement\]* A model is a select statement in a .sql file. The filename becomes the table or view name. You never write create table. dbt does that. *\[ON SCREEN: highlight {{ ref('stg\_orders') }}\]* The second idea is ref. When one model needs another, you do not write the table name. You write double curly braces, ref, and the model name. That does two things. It resolves to the right table in whichever environment you are running in. And it tells dbt that this model depends on that one. *\[ON SCREEN: lineage graph appears as models are added\]* dbt reads every ref in your project and builds a directed acyclic graph, a DAG. It uses the graph to run models in a safe order, run independent ones in parallel, and show you lineage: where each number comes from and what breaks if you change it. That is the pain from Lab 1, solved. You do not manage the order. You declare the dependencies, and dbt does the rest. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| \-- models/marts/fct\_orders.sql with orders as (     select \* from {{ ref('stg\_orders') }} ), payments as (     select order\_id, sum(amount) as amount     from {{ ref('stg\_payments') }}     group by 1 ) select     o.order\_id, o.customer\_id, o.order\_date, o.status,     coalesce(p.amount, 0\) as amount from orders o left join payments p using (order\_id) |
| :---- |

* **Model:** one select statement per file. The file name is the object name.

* **\`ref()\`:** references another model. Resolves to the correct schema and object for the current environment and records the dependency.

* **DAG:** the dependency graph. dbt uses it for ordering, parallelism, selection (dbt build \--select stg\_orders+) and lineage.

* **Idempotent by design:** a model can be rebuilt any number of times and produce the same result from the same inputs.

| Tip for customers The biggest mindset change is declarative thinking. Instead of "run script A then script B", you say "B is built from A" and the tool derives the schedule. |
| :---- |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**What two things does \`ref()\` do?**

*Answer: Resolves to the correct object for the current environment, and declares a dependency so dbt can order and graph the models.*

**What does the acronym DAG stand for?**

*Answer: Directed acyclic graph: dependencies go one direction and there are no cycles.*

## **Lesson 3.3: Sources and the staging layer**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Declare raw tables as sources and read them with source().

* Explain the purpose of staging models.

* Describe the staging, intermediate and marts layering convention.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3 min *\[ON SCREEN: layered diagram: raw \> staging \> intermediate \> marts\]* Raw data is messy: odd column names, cents instead of dollars, text where you want dates. If every report cleans it up its own way, you get five definitions of the same thing. dbt projects solve this with layers. First you declare your raw tables as sources, in YAML. Then you write staging models, one per source table, that do light cleanup only: rename columns, cast types, standardize units. Nothing else. On top of those you build intermediate models for reusable joins and logic, and finally marts: the clean business-facing tables like orders or customers that dashboards and analysts use. Why bother? Because a fix happens once, in staging, and every downstream model benefits. And because the structure is the same in every dbt project, new team members know where to look. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Layer | Contains | Rules of thumb |
| :---- | :---- | :---- |
| Sources | Declarations of raw tables (YAML) | Declare once. Reference with source(). Enables freshness checks and lineage back to raw. |
| Staging (stg\_) | One model per source table | Rename, cast, convert units. No joins, no business logic. Usually views. |
| Intermediate (int\_) | Reusable joins and logic | Break complex logic into named steps. Optional in small projects. |
| Marts (dim\_, fct\_) | Business-ready tables | Business definitions live here. Usually tables. |

| \# models/staging/\_sources.yml version: 2 sources:   \- name: raw     schema: raw     tables:       \- name: customers       \- name: orders       \- name: payments   \-- models/staging/stg\_payments.sql select     id as payment\_id,     order\_id,     method as payment\_method,     amount\_cents / 100.0 as amount from {{ source('raw', 'payments') }} |
| :---- |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**What is the only kind of logic that belongs in a staging model?**

*Answer: Light cleanup: renaming, type casting and unit conversion. No joins or business logic.*

## **Lesson 3.4: Materializations: how a model is built**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Describe view, table, incremental and ephemeral materializations.

* Choose a materialization for a given model.

* Set materialization by folder and per model.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3 min *\[ON SCREEN: four icons: View, Table, Incremental, Ephemeral\]* A materialization is how dbt turns your select statement into something in the database. A view stores only the query. It is always fresh and costs nothing to build, but each read pays the compute. A table stores the result. It is fast to read and costs compute at build time. An incremental model builds the table once, then on later runs only processes new or changed rows. That is how you keep large tables affordable. And an ephemeral model is never created at all: dbt inlines it as a CTE in whatever uses it. A sensible default: staging models as views, marts as tables, and switch big, growing tables to incremental when build time or cost demands it. You set these defaults by folder in dbt\_project.yml and override them in a single model when needed. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Materialization | Build cost | Read cost | Freshness | Use for |
| :---- | :---- | :---- | :---- | :---- |
| view | Very low | Pays query on every read | Always current | Staging, light transforms |
| table | Full rebuild each run | Fast | As of last run | Marts and anything queried often |
| incremental | Only new or changed rows after first run | Fast | As of last run | Large, append-heavy tables (events, orders) |
| ephemeral | None (inlined as a CTE) | Paid by the consumer | Always current | Small helper logic you do not want as an object |

| \# dbt\_project.yml (excerpt) models:   dbt\_course:     staging:       \+materialized: view     marts:       \+materialized: table   \-- override in one model: {{ config(materialized='table') }} |
| :---- |

Some platforms also offer materialized views and other types. The principle is the same: trade build cost against read cost and freshness. Cost mitigation: favor incremental builds for large tables (Lesson 5.3).

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Which materialization would you pick for a 2-billion-row event table that grows daily?**

*Answer: Incremental, so each run processes only new rows.*

## **Lab 3: Staging and marts on DuckDB**

**Time:** 60 minutes   \|   **Goal:** declare sources, build three staging models and two marts, and view the lineage.

**LAB 3  \|  LMS lab page**

### **Before you start**

Complete Lab 1 so raw.customers, raw.orders and raw.payments exist in your DuckDB file. Open the dbt\_course project in Rosetta DBT Studio. Use the file explorer to create folders models/staging and models/marts. If Studio generated example models, delete them.

### **Step 1: Declare sources**

Create models/staging/\_sources.yml with the YAML from Lesson 3.3.

### **Step 2: Staging models**

Create three files in models/staging:

| \-- stg\_customers.sql select     id as customer\_id,     first\_name,     last\_name,     email,     cast(created\_at as date) as created\_at from {{ source('raw', 'customers') }}   \-- stg\_orders.sql select     id as order\_id,     customer\_id,     cast(order\_date as date) as order\_date,     status from {{ source('raw', 'orders') }}   \-- stg\_payments.sql select     id as payment\_id,     order\_id,     method as payment\_method,     amount\_cents / 100.0 as amount from {{ source('raw', 'payments') }} |
| :---- |

Studio also has a staging layer generator that can create these from raw tables. Try it after you have written them by hand, and compare its output with yours.

### **Step 3: Marts**

| \-- models/marts/fct\_orders.sql  (from Lesson 3.2)   \-- models/marts/dim\_customers.sql select     c.customer\_id,     c.first\_name,     c.last\_name,     c.email,     min(o.order\_date) as first\_order\_date,     count(o.order\_id) as order\_count,     coalesce(sum(o.amount), 0\) as lifetime\_value from {{ ref('stg\_customers') }} c left join {{ ref('fct\_orders') }} o using (customer\_id) group by 1, 2, 3, 4 |
| :---- |

### **Step 4: Set materializations**

Add the models: block from Lesson 3.4 to dbt\_project.yml (use your project name).

### **Step 5: Build and inspect**

1. Run dbt compile. Open target/compiled/ and read the compiled fct\_orders.sql. Find what ref() became.

2. Run dbt run (use the Run button or the command runner).

3. In the SQL editor, run select \* from dim\_customers order by lifetime\_value desc;

4. Open the lineage or docs view and find the graph from sources to dim\_customers.

### **Expected result**

| customer\_id | first\_name | order\_count | lifetime\_value |
| :---- | :---- | :---- | :---- |
| 1 | Ava | 3 | 102.00 |
| 4 | Dmitri | 2 | 55.00 |
| 3 | Chloe | 2 | 50.00 |
| 2 | Ben | 2 | 23.00 |
| 5 | Elena | 1 | 12.00 |
| 6 | Farid | 0 | 0.00 |

### **Reflection questions**

* Compare the customer\_summary table from Lab 1 with dim\_customers. What is different about how you would maintain each?

* Which models are views and which are tables? How can you tell?

* Change stg\_orders (for example, rename a column) and run dbt run \--select stg\_orders+. What rebuilt, and why?

### **Troubleshooting**

* **"Source not found" or schema errors:** confirm the schema name in \_sources.yml is raw and Lab 1 created the tables in the same DuckDB file that your dbt connection uses.

* **Compiled SQL looks wrong:** run dbt compile and read the output in target/compiled.

* **Models land in an unexpected schema:** dbt-duckdb uses the schema from your connection (default main). Custom schemas append to it; we skip them in this course.

# **Module 4: Testing, documentation and trust**

**Module goal:** the learner can protect data quality with tests, verify logic with unit tests, and publish documentation and lineage that stakeholders trust.

## **Lesson 4.1: Data tests**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Write generic tests (unique, not\_null, accepted\_values, relationships) in YAML.

* Write a singular test in SQL.

* Interpret a failing test.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: a dashboard number is wrong; an analyst asks "since when?"\]* Every data team has had this moment. A number on a dashboard is wrong, and nobody knows since when. Tests shorten that moment from days to minutes. A data test in dbt is a query that looks for bad rows. If it finds any, the test fails. dbt ships four generic tests you apply in YAML. Unique and not null, which together protect a primary key. Accepted values, which checks a column only contains expected values. And relationships, which checks that every foreign key exists in the parent table. When you need something specific, write a singular test: a SQL file that returns the rows that should not exist. For example, orders with a negative amount. Run dbt build, and dbt tests each model right after building it, and skips downstream models if something upstream fails. Bad data stops at the gate instead of reaching the dashboard. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| \# models/staging/\_staging.yml version: 2 models:   \- name: stg\_customers     columns:       \- name: customer\_id         data\_tests: \[unique, not\_null\]   \- name: stg\_orders     columns:       \- name: order\_id         data\_tests: \[unique, not\_null\]       \- name: customer\_id         data\_tests:           \- relationships:               to: ref('stg\_customers')               field: customer\_id       \- name: status         data\_tests:           \- accepted\_values:               values: \['placed','shipped','completed','returned','return\_pending'\]   \- name: stg\_payments     columns:       \- name: payment\_id         data\_tests: \[unique, not\_null\]       \- name: order\_id         data\_tests:           \- relationships:               to: ref('stg\_orders')               field: order\_id   \-- tests/assert\_no\_negative\_amounts.sql select \* from {{ ref('fct\_orders') }} where amount \< 0 |
| :---- |

| Version note The key is data\_tests in current releases (older material uses tests). In v2, misspelled or misplaced keys are rejected, which is a reason to run the v2 parser check from Lab 2\. |
| :---- |

| Test | Fails when |
| :---- | :---- |
| unique | A value appears more than once |
| not\_null | A value is null |
| accepted\_values | A value is outside the allowed list |
| relationships | A foreign key has no matching parent row |
| Singular (SQL file) | The query returns any rows |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**A singular test passes when its query returns how many rows?**

*Answer: Zero rows. Any returned row is a failure.*

## **Lesson 4.2: Unit tests for transformation logic**

Format: video \+ reading   \|   Time: 15 min

**Learning objectives.** By the end of this lesson the learner can:

* Explain the difference between a data test and a unit test.

* Write a unit test with mocked inputs and expected output.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 2.5 min *\[ON SCREEN: two columns: "Data tests: is the data right?" and "Unit tests: is the logic right?"\]* Data tests check the data. Unit tests check your logic. You give a model a few made-up input rows and say exactly what output you expect. If the logic changes in a way that breaks that expectation, the unit test fails, even if the production data happens to look fine. They are most useful for tricky logic: case statements, date math, edge cases like an order with two payments. And because they use fixed inputs, they run quickly and can run in CI before anything touches real data. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| \# models/marts/\_marts.yml  (unit test excerpt) unit\_tests:   \- name: fct\_orders\_sums\_multiple\_payments     model: fct\_orders     given:       \- input: ref('stg\_orders')         rows:           \- {order\_id: 1, customer\_id: 1, order\_date: '2026-05-03', status: placed}       \- input: ref('stg\_payments')         rows:           \- {payment\_id: 1, order\_id: 1, payment\_method: credit\_card, amount: 32.00}           \- {payment\_id: 2, order\_id: 1, payment\_method: gift\_card, amount: 5.00}     expect:       rows:         \- {order\_id: 1, customer\_id: 1, order\_date: '2026-05-03', status: placed, amount: 37.00} |
| :---- |

Unit tests were introduced in dbt v1.8. Adapter support and type matching (for example dates) can vary; if a test fails on a type mismatch, add explicit casts in the mock rows.

|  | Data test | Unit test |
| :---- | :---- | :---- |
| Checks | Real data in the warehouse | Logic against fixed, mocked inputs |
| Runs | After a model builds | Before the model builds, on mocked data |
| Catches | Bad or unexpected source data, broken assumptions | Regression in transformation logic |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**You changed a join and want to make sure orders with two payments still sum correctly. Which test type?**

*Answer: A unit test with mocked order and payment rows.*

## **Lesson 4.3: Documentation and lineage**

Format: video \+ reading   \|   Time: 15 min

**Learning objectives.** By the end of this lesson the learner can:

* Add descriptions to models and columns.

* Generate and serve the docs site.

* Use lineage for impact analysis.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 2.5 min *\[ON SCREEN: generated docs site with a lineage graph\]* Documentation that lives in a wiki goes stale. Documentation that lives next to the code, and is generated from it, stays close to the truth. You add descriptions in the same YAML where you define tests. Run dbt docs generate, and dbt builds a website with every model, column, test, and a lineage graph. That graph answers two questions teams constantly ask. Where does this number come from? And if I change this model, what breaks? Both answers come straight from the ref statements you already wrote. *\[ON SCREEN: v2 note: "In v2, docs are rebuilt on Parquet metadata; column-level lineage is available in dbt v2 (free), not in dbt OSS or v1"\]* v2 rebuilds the documentation experience for large projects, and the free dbt v2 distribution adds column-level lineage. In v1 and dbt OSS you get model-level lineage. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| models:   \- name: dim\_customers     description: One row per customer with lifetime order metrics.     columns:       \- name: lifetime\_value         description: Sum of payments across all of the customer's orders, in dollars. |
| :---- |

* dbt docs generate builds the site artifacts. dbt docs serve hosts it locally (v1). Studio exposes the same through its docs action.

* **Descriptions can be reused** with doc blocks, so the same definition appears everywhere a column is used.

* **Exposures** let you declare downstream dashboards so lineage extends to the consumer.

* **Impact analysis:** select a model in the graph, follow its descendants. Command-line equivalent: dbt ls \--select dim\_customers+.

* **Hosting:** open source means hosting the static site yourself (any web server or object store). The commercial platform hosts and access-controls it for you.

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Where does the lineage graph come from?**

*Answer: From the \`ref()\` and \`source()\` calls in your models. No separate maintenance needed.*

## **Lab 4: Break it, test it, document it**

**Time:** 60 minutes   \|   **Goal:** add tests, deliberately introduce bad data, watch tests catch it, add a unit test, and generate documentation.

**LAB 4  \|  LMS lab page**

1. Create models/staging/\_staging.yml from Lesson 4.1. Run dbt build. Everything should pass.

2. Create tests/assert\_no\_negative\_amounts.sql. Run dbt test. It should pass.

3. Add the unit test from Lesson 4.2 to models/marts/\_marts.yml. Run dbt test \--select fct\_orders. It should pass.

4. **Break it.** In the SQL editor, run the "bad rows" script in Appendix A. It adds an order with status lost and a payment that references an order that does not exist.

5. Run dbt build. Which tests fail? Which models were skipped because of a failure upstream? Record the failing test names.

6. **Investigate.** Use the compiled SQL of a failing test (in target/) to find the offending rows in DuckDB.

7. **Decide.** For lost, decide whether the source is wrong or your accepted list is incomplete. Add lost to the list or fix the data, and explain your choice in the notes.

8. Add descriptions to dim\_customers and its columns. Run dbt docs generate and open the docs. Find dim\_customers and its lineage.

9. Optional v2 check: add a misspelled key (for example desciption:) under a column and run dbt parse \--use-v2-parser if you have v1.12 or later. Note what happens, then remove the typo.

### **Deliverable**

A screenshot of the failing build output and a screenshot of the lineage graph, plus your written decision about the lost status.

| What you should notice The bad data was caught at the staging layer, and downstream marts were skipped rather than built on bad inputs. That is the safety mechanism the manual script in Lab 1 did not have. |
| :---- |

# **Module 5: DRY code and performance**

**Module goal:** the learner can remove repetition with Jinja macros and packages and keep large tables affordable with incremental models.

## **Lesson 5.1: Jinja and macros**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Distinguish {{ }} expressions from {% %} statements.

* Write and call a macro.

* Use if and for to generate SQL.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: the same cents-to-dollars expression copy-pasted into five models\]* Look at this. Every model that handles money divides cents by one hundred and rounds. Copy it five times, and when finance changes the rule, you change it in five places and miss one. dbt uses Jinja, a templating language, to fix this. Double curly braces insert a value or call a function. Curly brace percent signs run logic, like if statements, for loops, and macro definitions. *\[ON SCREEN: macro definition, then the call in a model\]* A macro is a reusable function that returns SQL text. Define it once in the macros folder, call it anywhere. dbt renders the Jinja first, and what reaches your warehouse is plain SQL. You can always see the result with dbt compile. One piece of advice. Jinja is powerful and easy to overuse. If a macro makes the SQL harder to read than the repetition it removed, keep the repetition. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| \-- macros/cents\_to\_dollars.sql {% macro cents\_to\_dollars(column\_name, scale=2) %}     round({{ column\_name }} / 100.0, {{ scale }}) {% endmacro %}   \-- usage in a model select {{ cents\_to\_dollars('amount\_cents') }} as amount from {{ source('raw', 'payments') }}   \-- a loop to pivot payment methods select     order\_id,     {% for m in \['credit\_card', 'bank\_transfer', 'gift\_card'\] %}     sum(case when payment\_method \= '{{ m }}' then amount else 0 end) as {{ m }}\_amount     {% if not loop.last %},{% endif %}     {% endfor %} from {{ ref('stg\_payments') }} group by 1 |
| :---- |

| Syntax | Meaning |
| :---- | :---- |
| {{ ... }} | Expression: print a value or call a function or macro |
| {% ... %} | Statement: control flow, macro or variable definition |
| {\# ... \#} | Comment (not sent to the warehouse) |

| Readability rule Always check what the macro compiles to. If a reviewer cannot read the compiled SQL and understand the intent, simplify. |
| :---- |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**What reaches the warehouse after Jinja is rendered?**

*Answer: Plain SQL. You can inspect it with \`dbt compile\`.*

## **Lesson 5.2: Packages**

Format: video \+ reading   \|   Time: 15 min

**Learning objectives.** By the end of this lesson the learner can:

* Install a package with packages.yml and dbt deps.

* Describe what packages commonly provide.

* Name the risks of third-party code.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 2.5 min *\[ON SCREEN: packages.yml with one entry, then terminal output of dbt deps\]* You do not have to write everything yourself. dbt packages are shared projects you install into yours, like libraries in other languages. You list a package in packages.yml, run dbt deps, and its macros and models become available. The best known is dbt\_utils, with ready-made helpers: generating surrogate keys, pivoting, date spines, and extra tests. There are packages for common source systems too, and for project quality checks. Two cautions. Pin versions, so an upstream change does not break your build on a Tuesday. And review what you install. A package is code that runs against your warehouse. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| \# packages.yml packages:   \- package: dbt-labs/dbt\_utils     version: \["\>=1.0.0", "\<2.0.0"\]   \# pin a range; check the package hub for the current release   \# then dbt deps |
| :---- |

* **Where to find them:** the dbt Package Hub and GitHub. Packages can also be private Git repositories inside your company.

* **Typical content:** utility macros, extra tests, source-specific staging models, observability and quality checks.

* **Risks:** breaking changes, abandoned packages, and compatibility with your dbt version. Check compatibility with v2 before adopting a package, especially one with heavy Jinja.

* **Internal packages** are the standard way to share conventions across several dbt projects.

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Why pin a package version?**

*Answer: To prevent upstream changes from silently breaking your builds.*

## **Lesson 5.3: Incremental models**

Format: video \+ reading   \|   Time: 25 min

**Learning objectives.** By the end of this lesson the learner can:

* Explain how an incremental model differs from a table.

* Write an incremental model with is\_incremental() and unique\_key.

* Identify the late-arriving data trap and mitigations.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 4 min *\[ON SCREEN: a table rebuilt in full each night: 3 hours. Then incremental: 5 minutes\]* Rebuilding a large table from scratch every run is simple, and it gets expensive. An incremental model builds the table in full the first time, and after that processes only new or changed rows. *\[ON SCREEN: the incremental model with is\_incremental block highlighted\]* You write the model as usual, then add a filter that only applies on incremental runs, using the is\_incremental check. You also tell dbt a unique key, so rows that already exist are updated rather than duplicated. Here is the trap that catches almost every team. If a source row from last week gets corrected today, and your filter only looks for rows newer than the latest one you have, you will never pick up the correction. Your table is quietly wrong. There are fixes. Use a lookback window. Filter on an updated-at column instead of the event date. And schedule an occasional full refresh as a safety net. In the lab you will cause this problem on purpose and fix it. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| \-- models/marts/fct\_orders.sql {{ config(materialized='incremental', unique\_key='order\_id') }}   with orders as (     select \* from {{ ref('stg\_orders') }}     {% if is\_incremental() %}     where order\_date \>= (select max(order\_date) from {{ this }})     {% endif %} ), payments as (     select order\_id, sum(amount) as amount     from {{ ref('stg\_payments') }}     group by 1 ) select o.order\_id, o.customer\_id, o.order\_date, o.status,        coalesce(p.amount, 0\) as amount from orders o left join payments p using (order\_id) |
| :---- |

| Concept | Notes |
| :---- | :---- |
| is\_incremental() | True only when the model already exists and the run is not a full refresh |
| {{ this }} | The existing target table |
| unique\_key | Lets dbt update rows that already exist. Behavior depends on the incremental strategy the adapter supports (merge, delete+insert, and others). |
| \--full-refresh | Rebuilds the table from scratch. Use after logic changes or to repair drift. |
| Late-arriving data | Rows changed after the high-water mark are missed. Mitigate with a lookback window, an updated\_at filter, and periodic full refresh. |

**When not to go incremental:** small tables, or logic that depends on the whole history (for example window functions over all rows). Incremental adds complexity; use it when build time or cost justifies it.

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Why might an incremental model silently miss a corrected historic row?**

*Answer: The incremental filter only selects rows newer than the latest loaded row, so a correction to an older row is never reprocessed unless you use a lookback window, an updated-at filter or a full refresh.*

## **Lab 5: Macro and incremental model**

**Time:** 60 minutes   \|   **Goal:** replace repeated logic with a macro, convert a mart to incremental, trigger the late-arriving data problem and repair it.

**LAB 5  \|  LMS lab page**

### **Part 1: Macro**

1. Create macros/cents\_to\_dollars.sql from Lesson 5.1.

2. Edit stg\_payments.sql to use {{ cents\_to\_dollars('amount\_cents') }} as amount.

3. Run dbt compile, open the compiled file and confirm it contains round(amount\_cents / 100.0, 2\). Run dbt build. Everything should still pass.

### **Part 2: Incremental model**

1. Replace fct\_orders.sql with the incremental version in Lesson 5.3. Run dbt run \--select fct\_orders \--full-refresh, then dbt run \--select fct\_orders. The second run should process very few rows (check the run log).

2. In the SQL editor, run the "new order" script in Appendix A. Run dbt build. Confirm order 20 appears in fct\_orders and that dim\_customers for customer 5 now shows two orders.

### **Part 3: Trigger the trap**

1. In the SQL editor run update raw.orders set status \= 'returned' where id \= 9; (order 9 is dated 2026-05-01, older than the newest order).

2. Run dbt build. Check select status from fct\_orders where order\_id \= 9; What status do you see? Why?

3. Fix 1: run dbt run \--select fct\_orders \--full-refresh and check again.

4. Fix 2 (design): change the filter to a lookback window, for example where order\_date \>= (select max(order\_date) \- interval 30 day from {{ this }}). Run update raw.orders set status \= 'shipped' where id \= 10;, rebuild, and confirm the change is captured. (DuckDB interval syntax shown; other platforms differ.)

### **Deliverable**

Notes answering: (1) why the first fix works but is not a good routine, and (2) when a 30-day lookback would still fail.

# **Module 6: Working like a software team**

**Module goal:** the learner can set up environments, version control and CI for a dbt project and choose a deployment and orchestration approach, open source or commercial.

## **Lesson 6.1: Environments and targets**

Format: video \+ reading   \|   Time: 15 min

**Learning objectives.** By the end of this lesson the learner can:

* Explain dev, CI and prod environments and why they are separated.

* Describe targets and per-developer schemas.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 2.5 min *\[ON SCREEN: three boxes: Dev (each developer), CI (temporary), Prod (scheduled)\]* You never want to test a change on the tables your CFO is looking at. dbt handles this with targets. The same code can run against different connections or schemas depending on which target you choose. A typical setup has three environments. Development, where each person builds into their own schema, so they cannot collide. CI, where every pull request builds into a temporary schema. And production, where a scheduled job builds the real tables from the main branch. Because you used ref and source instead of hard-coded table names, nothing in the code changes between them. Only the target does. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| \# profiles.yml (command-line setups) dbt\_course:   target: dev   outputs:     dev:       type: duckdb       path: ./dev.duckdb     prod:       type: duckdb       path: ./prod.duckdb   \# run against a specific target dbt build \--target prod |
| :---- |

| Environment | Who builds it | Typical data | Trigger |
| :---- | :---- | :---- | :---- |
| Dev | Each developer | Own schema, often a sample or limited dataset | Manual |
| CI | Automation | Temporary schema, changed models only | Each pull request |
| Prod | Scheduler | Production schema, full data | Schedule or merge to main |

Secrets such as passwords belong in environment variables (env\_var() in profiles), never in Git.

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Why use a separate schema per developer?**

*Answer: So concurrent development does not overwrite each other's tables or production data.*

## **Lesson 6.2: Git and continuous integration**

Format: video \+ reading   \|   Time: 25 min

**Learning objectives.** By the end of this lesson the learner can:

* Describe a branch, pull request and review workflow for dbt.

* Explain state-based "slim CI" (state:modified+ and \--defer).

* Recognize what a CI pipeline for dbt contains.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: git branch diagram: main, feature branch, pull request, merge\]* Your dbt project is a folder of text files, so you get the full power of Git. Every change happens on a branch. A teammate reviews it in a pull request. Automated checks run. Only then does it merge to main. Those automated checks are continuous integration. A simple CI job runs dbt build on the pull request, so broken SQL or failing tests never reach main. Rebuilding the entire project on every pull request gets slow and expensive. So dbt can compare your branch with the last production run using its saved metadata, build only what you changed and everything downstream of it, and read unchanged models from production using the defer option. That is state-based, or slim, CI. In the open-source world, you set this up in your Git host, such as GitHub Actions or GitLab CI. The commercial platform offers it as a built-in feature. Either route gets you the same outcome. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| \# .github/workflows/dbt\_ci.yml  (illustrative; adapt to your warehouse and secrets) name: dbt CI on: pull\_request jobs:   build:     runs-on: ubuntu-latest     steps:       \- uses: actions/checkout@v4       \- uses: actions/setup-python@v5         with: { python-version: '3.12' }       \- run: pip install dbt-duckdb       \- run: dbt deps       \# prod-artifacts/ holds manifest.json from the last production run       \- run: dbt build \--select state:modified+ \--defer \--state prod-artifacts \--target ci |
| :---- |

| Practice | Why |
| :---- | :---- |
| Branch per change, pull request review | Every logic change is visible, discussed and reversible |
| dbt build on every PR | Broken SQL and failing tests are caught before merge |
| state:modified+ with \--defer | Builds only what changed and its descendants. Reads the rest from production. |
| Lint SQL in CI | Consistent style. Open-source option: SQLFluff. dbt v2 includes a built-in dbt lint. |
| Protect main, require passing checks | Production only receives reviewed, tested code |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**What does \`--select state:modified+\` do?**

*Answer: Selects models that changed compared with a saved state (the manifest of a previous run), plus all their downstream models.*

## **Lesson 6.3: Orchestration and deployment options**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Compare scheduling options for open-source dbt.

* Choose between self-managed orchestration and the dbt platform.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3 min *\[ON SCREEN: comparison grid: cron, GitHub Actions schedule, Airflow, Dagster, dbt platform\]* Once your project is merged and tested, something has to run it on schedule. dbt itself does not schedule jobs. The simplest option is cron or a scheduled GitHub Action that calls dbt build. It is fine for a small team with a few jobs. When your dbt run needs to happen after an ingestion job finishes, or trigger something afterwards, you reach for an orchestrator such as Airflow, Dagster or Prefect, which have integrations that treat each dbt model as a task you can retry and monitor. Or you use the dbt platform, where scheduling, CI, alerts and docs hosting come built in. The decision comes down to what you already run. If you have an orchestrator, add dbt to it. If you do not want to build and maintain any of this, the platform is the faster path. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Option | Best when | Watch for |
| :---- | :---- | :---- |
| Cron or CI scheduled job | Small project, simple daily build | Limited retries, alerting and dependency awareness |
| Airflow | Existing Airflow estate, cross-system dependencies | Operational overhead. dbt integration choices vary (whole-project task vs model-level). |
| Dagster | Asset-oriented teams, wants model-level lineage in the orchestrator | Learning curve |
| Prefect or similar | Python-heavy teams wanting lightweight flows | Smaller dbt-specific ecosystem |
| dbt platform jobs | Want scheduling, CI, alerts and hosted docs in one place | Subscription cost, platform dependency |

### **Deployment checklist (any option)**

* Production runs from the main branch only.

* Failures alert a human, with logs and the failing test name.

* Run artifacts (manifest.json, run\_results.json) are saved. They power slim CI and observability.

* Secrets are injected from a secret manager or CI variables.

* Docs are regenerated and published on each production run.

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**dbt does not schedule itself in open source. Name two ways to schedule it.**

*Answer: Any two of: cron, a scheduled CI workflow, Airflow, Dagster, Prefect, or the dbt platform scheduler.*

## **Lab 6: Branch, change, validate**

**Time:** 60 minutes   \|   **Goal:** use Git in Studio, make a change on a branch, build only what changed, and read a CI definition.

**LAB 6  \|  LMS lab page**

1. In Rosetta DBT Studio, open the Git explorer and initialize a repository for dbt\_course if it is not one. Create a .gitignore that excludes target/, dbt\_packages/, logs/ and \*.duckdb. Commit everything on main with message "Initial dbt project".

2. **Save the production state.** Run dbt build. Copy target/manifest.json into a new folder prod\_artifacts/ in the project (do not commit it).

3. Create a branch feature/customer-segment.

4. Add a column to dim\_customers: case when coalesce(sum(o.amount), 0\) \>= 100 then 'gold' when coalesce(sum(o.amount), 0\) \>= 40 then 'silver' else 'bronze' end as customer\_segment.

5. Run only what changed: dbt build \--select state:modified+ \--state prod\_artifacts. Confirm only dim\_customers (and any descendants) was built.

6. Check the result: Ava is gold; Dmitri and Chloe are silver; Ben, Elena and Farid are bronze.

7. Review the diff in the Git explorer, then commit with a clear message.

8. Create .github/workflows/dbt\_ci.yml from Lesson 6.2. You do not need to run it. In your notes, answer: what would you need to add for a real warehouse (secrets, a target, where prod-artifacts comes from)?

### **Deliverable**

Screenshot of the diff and the selective build log, plus your answer about the CI file.

# **Module 7: Applying dbt in your organization**

**Module goal:** the learner can build the business case for dbt, set conventions and governance, plan an adoption or migration, and avoid common failure modes. This module is conversational and decision-oriented.

## **Lesson 7.1: Benefits and how to make the case**

Format: video \+ reading   \|   Time: 20 min

**Learning objectives.** By the end of this lesson the learner can:

* Connect dbt capabilities to business outcomes.

* Define measurable success criteria for a pilot.

* Present an honest cost side.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: two columns: "Capability" and "Business outcome"\]* When you take dbt to your leadership, do not lead with the tool. Lead with the outcomes. Version control and code review mean changes are visible and reversible, so fewer surprises. Tests mean data problems are caught before the business sees them, so more trust. Documentation and lineage mean new team members and stakeholders find answers themselves, so less time spent on questions. Modular models and macros mean logic is defined once, so one definition of revenue instead of five. And because the work is SQL, more of the team can contribute, so less of a bottleneck on specialist engineers. Be honest about the costs, too. Warehouse compute grows as you build more. Your team needs time to learn the workflow. And you need to decide who owns the plumbing, scheduling, CI, docs, because open source leaves that with you. The strongest case is a pilot with measures you pick up front. We will show you which. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| dbt capability | Business outcome | How to measure it in a pilot |
| :---- | :---- | :---- |
| Version control, review, CI | Fewer production surprises, auditable change history | Count incidents caused by code changes before and after. Time from request to deploy. |
| Automated tests | Higher trust in numbers | Data-quality incidents found by tests vs. by users |
| Docs and lineage | Faster onboarding, self-service answers | Time for a new analyst to ship a first change. Number of "where does this come from" questions. |
| Modular, DRY logic | One definition per metric | Number of conflicting definitions found and retired |
| SQL-first workflow | Wider contribution base | Number of contributors who ship a change in the first quarter |
| ELT with retained raw data | Faster response to changing requirements | Time to implement a changed business rule and backfill |

| Avoid unsupported numbers Do not quote productivity percentages from vendor material to a customer. Measure their own baseline in the pilot and report that. It is more credible and it is what leadership will check. |
| :---- |

### **Cost side**

* Warehouse compute (control with incremental models, right-sized materializations, scheduling).

* Engineering time to set up CI, orchestration and docs hosting, or the platform subscription instead.

* Training and the shift to a review-based way of working.

* Ongoing maintenance of conventions, packages and upgrades (including the v1 to v2 move).

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Name two measurable pilot outcomes and the baseline needed for each.**

*Answer: Example: time from request to deploy (baseline current cycle time); data incidents found by users (baseline current count per month).*

## **Lesson 7.2: Project structure, conventions and governance**

Format: video \+ reading   \|   Time: 25 min

**Learning objectives.** By the end of this lesson the learner can:

* Define naming and layering conventions.

* Assign ownership and review rules.

* Describe contracts, model versions and access controls, and when to use them.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 3.5 min *\[ON SCREEN: a project tree with conventions highlighted\]* Tools do not make a good project. Conventions do. Agree early on a small set: layer names, file naming, where logic goes, how tests and descriptions are required, and who reviews what. A few rules that pay for themselves. Every model in a mart has a description and a primary-key test. Every pull request needs one reviewer. Business logic lives in marts, not staging. And every important model has an owner who is responsible when it breaks. As projects grow, dbt gives you stronger tools. Contracts, which declare a model's columns and types so a breaking change fails the build. Model versions, so consumers can migrate on their own timeline. And access modifiers, which mark models as public or private. For very large organizations, you split into multiple projects with clear interfaces, sometimes called a mesh. That last part is the point where the commercial platform adds the most. Start small. Add structure when you feel the pain it solves, not before. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Convention | Starter rule |
| :---- | :---- |
| Layers | staging (stg\_), intermediate (int\_), marts (dim\_, fct\_) |
| Naming | snake\_case. Plural entities. Verb-free model names. |
| Logic placement | Cleanup in staging. Joins in intermediate. Business definitions in marts. |
| Required in marts | Description, primary key unique and not\_null, an owner |
| Reviews | One approving reviewer. CI must pass. CODEOWNERS for critical areas. |
| Materializations | Staging views, marts tables, incremental when justified |
| SQL style | A linter in CI (SQLFluff, or dbt lint in dbt v2) |

| Advanced feature | Use when |
| :---- | :---- |
| Contracts | Other teams or dashboards depend on exact column names and types |
| Model versions | You must make a breaking change and give consumers time to migrate |
| Access (public / private) | You want to restrict which models other teams may reference |
| Multiple projects (mesh) | Several teams own separate domains. Cross-project references need governance. |
| Semantic layer / metrics | Many tools query the same business metrics and must agree. Native option is on the commercial platform. Alternatives exist. |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**What problem do contracts solve?**

*Answer: They make breaking changes to a model's shape (columns or types) fail the build instead of surprising downstream consumers.*

## **Lesson 7.3: Adoption, migration and common pitfalls**

Format: video \+ reading   \|   Time: 25 min

**Learning objectives.** By the end of this lesson the learner can:

* Plan a phased adoption starting with a pilot.

* Describe a safe migration from legacy ETL or stored procedures.

* List common failure modes and their remedies.

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 4 min *\[ON SCREEN: roadmap: Pilot \> Prove \> Expand \> Standardize\]* Do not try to move everything at once. Pick one domain with a clear sponsor, real pain and a manageable size. Build it in dbt, run it alongside the old process, and compare outputs until they reconcile. That parallel run is how you build trust. For migration from legacy ETL or stored procedures, work outward from the outputs that matter. Rebuild a report's data in dbt, reconcile, switch consumers, then retire the old job. This is sometimes called the strangler pattern. *\[ON SCREEN: pitfalls list\]* Watch for the common failure modes. Treating dbt as a drop-in for ingestion. Putting business logic in staging. Skipping tests because it is faster this week. Building one giant model nobody understands. Ignoring warehouse cost until the bill arrives. And not deciding who owns scheduling and CI. If you are already on v1, add one more item to the plan: prepare for v2. Fix the deprecation warnings, try the v2 parser flag, and schedule the upgrade when the team has room. |
| :---- |

**LMS CONTENT  \|  learner reads this on the page**

| Phase | Activities | Exit criteria |
| :---- | :---- | :---- |
| Pilot (4 to 8 weeks) | One domain, 5 to 15 models, tests on keys, docs, Git workflow, CI | Outputs reconcile with the legacy process. Success measures captured. |
| Prove | Parallel run, stakeholder review, cost review | Sponsor signs off. Cost per run understood. |
| Expand | Add domains, adopt conventions, set up orchestration and docs hosting (or the platform) | Two or more teams contributing through pull requests |
| Standardize | Governance, contracts where needed, training, upgrade policy (v1 to v2) | Documented conventions. Owners per model. |

### **Legacy migration pattern**

1. Inventory outputs and consumers. Prioritize by value and risk.

2. Load the needed raw data into the warehouse (EL).

3. Rebuild the logic in staging then marts. Add tests that encode known rules.

4. Run in parallel. Reconcile row counts and key totals daily. Document and resolve differences.

5. Switch consumers. Keep the legacy job on standby for a defined period. Retire it.

### **Pitfalls and remedies**

| Pitfall | Remedy |
| :---- | :---- |
| Using dbt for ingestion or streaming | Pair with EL tools or stream processors (Lesson 1.4) |
| Business logic in staging | Enforce layer rules in review |
| No tests ("we will add them later") | Require key tests on every mart as a merge criterion |
| Monolithic models | Split into intermediate steps with clear names |
| Runaway cost | Incremental models, scheduling review, query cost monitoring |
| No owner for scheduling, CI, docs | Decide at the start: own it (open source) or buy it (platform) |
| Skipping version planning | Track v1.x deprecations. Test the v2 parser. Plan the upgrade. |

**KNOWLEDGE CHECK  \|  LMS quiz items (answer in italics)**

**Why run the new dbt output in parallel with the legacy output?**

*Answer: To reconcile results, find logic differences and build stakeholder trust before switching consumers.*

## **7.4 Capstone brief**

**CAPSTONE  \|  LMS assignment page**

**Time:** 2 hours. Choose Track A (technical) or Track B (advisory). Both require applying the module concepts.

### **Track A: Extend the project**

1. Add a new mart fct\_payments\_by\_method summarizing amount and count per payment method and month. Source the logic from staging models.

2. Add tests: primary-key tests, an accepted\_values test on method, and one unit test.

3. Add descriptions for every column and generate the docs.

4. Make one model incremental, with a lookback window, and explain your choice.

5. Commit on a branch with a pull request description that includes lineage and test results.

6. Write a half-page "v2 readiness note": run dbt parse \--use-v2-parser if available, list findings, and recommend a v1, dbt v2 or dbt OSS path.

### **Track B: Adoption plan**

Pick a real or fictional organization (or one from your customer work). Write a 2-page plan that includes:

* Current state and the problem to solve.

* Where dbt fits and where it does not (use the Lesson 1.4 checklist and name the alternative for each gap).

* Recommendation on v1, dbt v2 or dbt OSS, and open source versus the dbt platform, with reasoning.

* A phased roadmap with pilot scope and success measures.

* Risks and mitigations, including cost, skills and upgrade path.

### **Rubric (both tracks)**

| Criterion | Meets expectations |
| :---- | :---- |
| Concept accuracy | ELT, versions and licensing described correctly |
| Reasoning | Each recommendation is justified with trade-offs |
| Fit and limits | Names where dbt should not be used and the alternative |
| Quality (Track A) | Tests pass, docs generated, clear PR |
| Actionability (Track B) | Roadmap, measures and owners are specific |

### **Course wrap-up (LMS closing page)**

| VIDEO SCRIPT  \|  presenter records this  \|  approx. 1.5 min *\[ON SCREEN: course map with all modules checked\]* You started with a question: where should transformation logic live? You now have a clear answer for cloud warehouses: load the raw data first, transform it where it lives, in SQL, under version control, with tests and documentation. You also know where that answer stops applying, and what to use instead. You have seen the two generations of dbt, which parts are open source, which are free but proprietary, and which are paid, and how to choose between them. And you built a working project end to end. Take the capstone to your own team. Start small, measure it, and let the results make the case. Thank you for learning with us. |
| :---- |

**Next steps:** official dbt docs and quickstarts, the dbt community forum and Slack, and the dbt Package Hub. Apply the pilot template from Lesson 7.3 to a real project in the next 30 days.

# **Appendix A: Lab starter data and scripts**

Provide these as downloadable .sql files on the LMS lab pages. All scripts use plain values lists so they run anywhere DuckDB runs, with no file paths.

### **A1. Starter data (Lab 1\)**

| create schema if not exists raw;   create or replace table raw.customers as select \* from (values   (1, 'Ava',    'Nguyen',  'ava@example.com',    '2026-01-05'),   (2, 'Ben',    'Ortiz',   'ben@example.com',    '2026-01-12'),   (3, 'Chloe',  'Patel',   'chloe@example.com',  '2026-02-03'),   (4, 'Dmitri', 'Ivanov',  'dmitri@example.com', '2026-02-20'),   (5, 'Elena',  'Rossi',   'elena@example.com',  '2026-03-08'),   (6, 'Farid',  'Haddad',  'farid@example.com',  '2026-03-15') ) as t(id, first\_name, last\_name, email, created\_at);   create or replace table raw.orders as select \* from (values   (1,  1, '2026-03-01', 'completed'),   (2,  1, '2026-03-20', 'completed'),   (3,  2, '2026-03-05', 'completed'),   (4,  3, '2026-03-10', 'returned'),   (5,  3, '2026-04-02', 'completed'),   (6,  4, '2026-04-05', 'shipped'),   (7,  4, '2026-04-18', 'placed'),   (8,  5, '2026-04-20', 'completed'),   (9,  2, '2026-05-01', 'return\_pending'),   (10, 1, '2026-05-03', 'placed') ) as t(id, customer\_id, order\_date, status);   create or replace table raw.payments as select \* from (values   (1,  1,  'credit\_card',   2500),   (2,  2,  'credit\_card',   4000),   (3,  3,  'bank\_transfer', 1500),   (4,  4,  'gift\_card',     3000),   (5,  5,  'credit\_card',   2000),   (6,  6,  'credit\_card',   5500),   (7,  8,  'bank\_transfer', 1200),   (8,  9,  'gift\_card',      800),   (9,  10, 'credit\_card',   3200),   (10, 10, 'gift\_card',      500\) ) as t(id, order\_id, method, amount\_cents); |
| :---- |

### **A2. Bad rows (Lab 4\)**

| insert into raw.orders   values (11, 6, '2026-05-10', 'lost'); insert into raw.payments values (11, 99, 'credit\_card', 700);  \-- order 99 does not exist |
| :---- |

### **A3. New order (Lab 5\)**

| insert into raw.orders   values (20, 5, '2026-05-12', 'placed'); insert into raw.payments values (20, 20, 'credit\_card', 2500); |
| :---- |

If you fixed the bad rows in Lab 4 by deleting them, the scripts in A3 still work. If you instead extended the accepted values list, order 11 and payment 11 remain and the orphan payment test will still fail; delete payment 11 to continue (delete from raw.payments where id \= 11;).

# **Appendix B: Command cheat sheet**

| Task | Command |
| :---- | :---- |
| Show version | dbt \--version |
| Install packages | dbt deps |
| Load seed CSVs | dbt seed |
| Render SQL without running | dbt compile |
| Build models | dbt run (add \--select model\_name) |
| Run tests | dbt test |
| Models, tests, seeds, in order | dbt build |
| A model and everything downstream | dbt build \--select model\_name+ |
| Only what changed vs. saved state | dbt build \--select state:modified+ \--state path/ |
| Rebuild an incremental model from scratch | dbt run \--select model\_name \--full-refresh |
| List nodes in a selection | dbt ls \--select model\_name+ |
| Docs | dbt docs generate, then dbt docs serve (v1) |
| Check v2 parse readiness (v1.12+) | dbt parse \--use-v2-parser |
| Install dbt OSS (v2, Apache 2.0) | uv tool install dbt-oss |

# **Appendix C: Production notes for the LMS build**

### **Assets to create**

* **Diagrams:** ETL vs ELT flow; dbt in the data stack; language vs engine layers; v1 / dbt v2 / dbt OSS / platform decision tree; layered project (raw, staging, intermediate, marts); environments (dev, CI, prod).

* **Screenshots:** Rosetta DBT Studio install, connection setup, SQL editor, file explorer, run and test output, lineage view, Git explorer.

* **Downloads:** starter\_data.sql, bad\_rows.sql, new\_order.sql, a completed reference project for each lab (zip), the command cheat sheet, the Lesson 1.4 checklist and the Lesson 2.5 decision table as PDFs.

* **Quiz bank:** the Knowledge Check items per lesson (about 45 items). Add a 20-question end-of-course quiz drawn from them.

### **Recording guidance**

* Target 2 to 5 minutes per lesson video. Total video is about 90 minutes.

* Record Module 2 last, immediately after re-checking the open items on page 1\. It is the most likely to date.

* Show lab steps live in Studio for Labs 1, 3 and 5 as optional walkthrough videos (5 to 8 minutes each).

* Say "dbt v2" and "dbt OSS" consistently, and mention once that older material says "Fusion".

### **Estimated learner time**

| Component | Time |
| :---- | :---- |
| Video (26 lessons) | about 1.5 hours |
| Reading and knowledge checks | about 3 hours |
| Labs 1 to 6 | about 5.5 hours |
| Capstone | about 2 hours |
| **Total** | **about 12 hours** |

# **Appendix D: Sources**

Research for this draft was done on November 4, 2026\. Re-verify before recording.

* dbt Developer Hub, What is dbt? https\://docs.getdbt.com/docs/introduction

* dbt Core v2 is here: still open source, now rebuilt for what is next (June 1, 2026), https\://docs.getdbt.com/blog/dbt-core-v2-is-here

* dbt roadmap, Announcing v2.0 (June 2026), https\://github.com/dbt-labs/dbt/blob/main/docs/roadmap/2026-06-announcing-v2.md

* dbt licensing, https\://docs.getdbt.com/docs/dbt-licensing

* Install dbt OSS, https\://docs.getdbt.com/docs/local/install-dbt-v2

* Install dbt Core 2.0 (earlier beta page), https\://docs.getdbt.com/docs/local/install-dbt-core-v2

* v2 feature availability, https\://docs.getdbt.com/docs/dbt/dbt-availability

* dbt platform features, https\://docs.getdbt.com/docs/platform/about-platform/dbt-platform-features

* DuckDB setup for dbt v2, https\://docs.getdbt.com/docs/local/connect-data-platform/duckdb-setup

* dbt-duckdb adapter (v1), https\://github.com/duckdb/dbt-duckdb

* Rosetta DBT Studio, https\://github.com/rosettadb/dbt-studio

* dbt Licensing FAQ, https\://www\.getdbt.com/licenses-faq