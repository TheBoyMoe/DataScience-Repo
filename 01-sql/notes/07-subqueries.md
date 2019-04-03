# Subqueries

**SEMI and ANTI JOIN**

Use the right table to determine which rows in the left table to keep, e.g. it removes rows from the table. The semi and anti join are used in a way similar to a `WHERE` clause, dependent on the values of the right table.

Anti-join  is particularly useful in identifying which records are causing an incorrect number of records to appear in join queries.

NOTE: All other joins (inner, left, right, full, self and cross) are additive, they add columns to the left table. 

`WHERE` clause is used to create a sub query to join the two table queries:

```sql
SELECT president, country, continent
FROM presidents
WHERE country IN
    (SELECT name
    FROM states
    WHERE indep_year < 1800);
```

* the first displays the president, country and continent from the presidents (left) table, dependent upon, 
* the condition to check in the `WHERE` clause which  queries the right table.

```sql
-- identify languages spoken in the Middle East
SELECT DISTINCT name -- same languages appear multiple times
  FROM languages
WHERE code IN
  (SELECT code
   FROM countries
   WHERE region = 'Middle East')
ORDER BY name;

-- the same result can be obtained with the following inner join
SELECT DISTINCT languages.name AS language
FROM languages
INNER JOIN countries
ON languages.code = countries.code
WHERE region = 'Middle East'
ORDER BY language;

-- identify the currencies used in Oceanian countries
SELECT code, name
  FROM countries
  WHERE continent = 'Oceania'
  	-- 1. And code not in
  	AND code NOT IN
  	-- 2. Subquery
  	(SELECT code
  	 FROM currencies);

-- Identify the country codes that are included in either economies or currencies but not in populations.
-- Use that result to determine the names of cities in the countries that match the specification
-- Select the city name
SELECT name 
  -- Alias the table where city name resides
  FROM cities
  -- Choose only records matching the result of multiple set theory clauses
  WHERE country_code IN
(
    -- Select appropriate field from economies AS e
    SELECT e.code
    FROM economies AS e
    -- Get all additional (unique) values of the field from currencies AS c2  
    UNION
    SELECT c2.code
    FROM currencies AS c2
    -- Exclude those appearing in populations AS p
    EXCEPT
    SELECT p.country_code
    FROM populations AS p
);

-- Select all fields from populations with records corresponding to larger than 1.15 times the average life expectancy for 2015
SELECT *
  -- From populations
  FROM populations
-- Where life_expectancy is greater than
WHERE life_expectancy >
  -- 1.15 * subquery
  1.15 * (SELECT AVG(life_expectancy)
    FROM populations
    WHERE year = 2015) 
  AND year = 2015;

-- get the urban area population for only capital cities.
SELECT name, country_code, urbanarea_pop
  -- 3. From cities
  FROM cities
-- 4. Where city name in the field of capital cities
WHERE name IN
  -- 1. Subquery
  (SELECT capital
   FROM countries)
ORDER BY urbanarea_pop DESC;

-- selects the top nine countries in terms of number of cities appearing in the cities table. 
SELECT name AS country,
  (SELECT COUNT(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;

-- Alternative
SELECT countries.name AS country, COUNT(*) AS cities_num
  FROM cities
    INNER JOIN countries
    ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;

--  determine the number of languages spoken for each country, identified by the country's local name
SELECT local_name, subquery.lang_num
  FROM countries,
  	(SELECT code, COUNT(*) AS lang_num
  	 FROM languages
  	 GROUP BY code) AS subquery
  WHERE countries.code = subquery.code
ORDER BY lang_num DESC;

-- Determine the maximum inflation rate for each continent in 2015
SELECT name, continent, inflation_rate
  -- From countries
  FROM countries
	-- Join to economies
	INNER JOIN economies
	-- Match on code
	ON countries.code = economies.code
  -- Where year is 2015
  WHERE year = 2015
    -- And inflation rate in subquery (alias as subquery)
    AND inflation_rate IN (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
             SELECT name, continent, inflation_rate
             FROM countries
             INNER JOIN economies
             ON countries.code = economies.code
             WHERE year = 2015) AS subquery
        GROUP BY continent);

-- Use a subquery to get 2015 economic data for countries that do not have
-- 'gov_form' of 'Constitutional Monarchy' or
-- 'Republic' in their gov_form.
SELECT economies.code, unemployment_rate, inflation_rate
  -- From economies
  FROM economies
  -- Where year is 2015 and code is not in
  WHERE year = 2015 AND code NOT IN
  	-- Subquery
  	(SELECT code
  	 FROM countries
  	 WHERE (gov_form = 'Constitutional Monarchy' OR gov_form LIKE '%Republic%'))
-- Order by inflation rate
ORDER BY inflation_rate;

-- get the country names and other 2015 data in the economies table and the countries table for Central American countries with an official language.
SELECT DISTINCT name, total_investment, imports
  -- From table (with alias)
  FROM countries AS c
    -- Join with table (with alias)
    LEFT JOIN economies AS e
      -- Match on code
      ON (c.code = e.code
      -- and code in Subquery
        AND c.code IN (
          SELECT l.code
          FROM languages AS l
          WHERE official = 'true'
        ) )
  -- Where region and year are correct
  WHERE region = 'Central America' AND year = 2015
-- Order by field
ORDER BY name;

--  calculate the average fertility rate for each region in 2015.
SELECT region, continent, AVG(fertility_rate) AS avg_fert_rate
  -- From left table
  FROM countries AS c
    -- Join to right table
    INNER JOIN populations AS p
      -- Match on join condition
      ON c.code = p.country_code
  -- Where specific records matching some condition
  WHERE p.year = 2015
-- Group appropriately
GROUP BY region, continent
-- Order appropriately
ORDER BY avg_fert_rate;

-- determining the top 10 capital cities in Europe and the Americas in terms of a calculated percentage using city_proper_pop and metroarea_pop in cities
SELECT name, country_code, city_proper_pop, metroarea_pop,  
      -- Calculate city_perc
      city_proper_pop / metroarea_pop * 100 AS city_perc
  -- From appropriate table
  FROM cities
  -- Where 
  WHERE name IN
    -- Subquery
    (SELECT capital
     FROM countries
     WHERE (continent = 'Europe'
        OR continent LIKE '%America'))
       AND metroarea_pop IS NOT NULL
-- Order appropriately
ORDER BY city_perc DESC
-- Limit amount
LIMIT 10;
```