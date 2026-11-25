# Assignment 2 – PostgreSQL as SQL + NoSQL using JSONB

## Objective

The objective of this assignment was to understand how PostgreSQL can store both structured relational data and flexible document-style data using the `jsonb` data type. The implementation was also compared with MongoDB.

## Part A – Conceptual Understanding

### 1. JSONB vs JSON

PostgreSQL provides both `json` and `jsonb` for storing JSON data. The `json` type stores the original JSON as text, whereas `jsonb` stores it in a processed binary format.

Plain JSON can be slightly faster while inserting because less processing is required. JSONB is generally better for querying because PostgreSQL does not need to repeatedly parse the original JSON text. JSONB also supports indexing, including GIN indexes, which can improve searches within JSON documents.

For example, a value can be extracted from JSONB using:

`SELECT attributes ->> 'author' FROM products;`

Therefore, JSONB is generally preferred when JSON data needs to be frequently searched, filtered, or indexed.

### 2. PostgreSQL as SQL + NoSQL

PostgreSQL can combine fixed relational columns with a flexible JSONB column in the same table.

For the product catalog, `id`, `name`, `category`, and `price` were stored as normal typed SQL columns, while `attributes` was stored as JSONB.

This allowed different products to contain different attributes. Books stored properties such as `author` and `pages`, laptops stored `ram_gb`, `cpu`, and `storage_gb`, while accessories stored `color` and `wireless`.

This provides the schema enforcement and relational capabilities of SQL while also providing document-style flexibility.

#### PostgreSQL Table Structure

![PostgreSQL Table Structure](./screenshots/postgresql-table.png)

### 3. JSONB Operators

Several PostgreSQL JSONB operators were tested.

`->` extracts a value while retaining its JSON representation, whereas `->>` extracts the value as SQL text.

The `@>` operator checks whether one JSONB document contains a specified key/value pair. The `?` operator checks whether a particular key exists.

For example:

`attributes @> '{"wireless": true}'`

was used to locate products that contained `wireless: true`.

#### JSONB Query Results

![JSONB Query Results](./screenshots/jsonb-queries.png)

### 4. GIN Index

A GIN index was created on the `attributes` JSONB column to study JSONB query performance.

GIN indexes are useful for operations such as JSONB containment and key-existence searches. They do not improve unrelated queries on columns such as `price`.

`EXPLAIN ANALYZE` was executed before and after creating the index. Since the experiment contained only five products, PostgreSQL could still prefer a sequential scan because scanning such a small table is inexpensive.

#### Before Creating the GIN Index

![GIN Index Before](./screenshots/gin-index-before.png)

#### After Creating the GIN Index

![GIN Index After](./screenshots/gin-index-after.png)

### 5. PostgreSQL JSONB vs MongoDB

PostgreSQL JSONB is useful when an application requires flexible attributes together with relational features such as transactions, joins, constraints, and schema enforcement.

MongoDB is naturally document-oriented and provides simpler syntax for querying nested properties. It is also designed with document-based horizontal scaling in mind.

For example, PostgreSQL accesses RAM using `attributes ->> 'ram_gb'`, whereas MongoDB can directly query `attributes.ram_gb`.

Therefore, PostgreSQL JSONB is suitable when both relational and document-style data are required, while MongoDB can be more convenient for applications primarily based on flexible documents.

## Part B – Product Catalog Implementation

A `products` table was created in PostgreSQL containing fixed columns for ID, name, category, and price along with a JSONB `attributes` column.

Five products across three categories were inserted:

- Clean Code
- Atomic Habits
- Gaming Laptop
- Work Laptop
- Wireless Mouse

#### Inserted Products

![Inserted Products](./screenshots/inserted-products.png)

Category-specific JSONB queries were then performed for books based on page count, laptops based on RAM, and accessories based on the wireless property.

#### Category-Specific Query Results

![JSONB Queries](./screenshots/jsonb-queries.png)

A new `discount_pct` attribute was added to the Wireless Mouse using JSONB without altering the table structure.

#### JSONB Update

![JSONB Update](./screenshots/jsonb-update.png)

A GIN index was then created and the query execution was compared using `EXPLAIN ANALYZE`.

#### Query Performance Before Index

![Before GIN Index](./screenshots/gin-index-before.png)

#### Query Performance After Index

![After GIN Index](./screenshots/gin-index-after.png)

## MongoDB Comparison

The same five products were recreated as documents in a MongoDB `products` collection.

#### MongoDB Products

![MongoDB Products](./screenshots/mongodb-products.png)

Equivalent category-specific queries were performed using MongoDB's nested field syntax.

#### MongoDB Query Results

![MongoDB Queries](./screenshots/mongodb-queries.png)

An index was also created on the nested `attributes.ram_gb` field.

#### MongoDB Index

![MongoDB Index](./screenshots/mongodb-index.png)

The MongoDB implementation demonstrated simpler document-oriented syntax, while PostgreSQL demonstrated the advantage of combining flexible JSONB data with relational database functionality.

## Conclusion

This assignment demonstrated how PostgreSQL JSONB can provide document-style flexibility within a relational database. JSONB attributes were queried, updated, and indexed without changing the table schema. Comparing the same product catalog with MongoDB showed that both systems support flexible data, but PostgreSQL combines this flexibility with traditional SQL features such as relational schemas, joins, constraints, and transactions.