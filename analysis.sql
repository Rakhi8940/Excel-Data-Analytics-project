-- ============================================================
-- Data Jobs Market Analysis — SQL Queries
-- Author  : Rakhi Yadav
-- Dataset : 2023 Data Science Job Market
-- Dialect : Standard SQL (compatible with SQLite / PostgreSQL)
-- ============================================================
-- Assumed tables after importing Excel data:
--   jobs   (job_id, job_title_short, salary_year_avg,
--            job_country, job_schedule_type, job_posted_date)
--   skills (job_id, skill_name, skill_type)
-- ============================================================


-- ── Q1: Which job titles have the highest median salary? ──────────────────────
--   Business use: benchmark compensation expectations by role.
SELECT
    job_title_short,
    COUNT(*)                                          AS job_count,
    ROUND(AVG(salary_year_avg), 0)                   AS avg_salary,
    ROUND(PERCENTILE_CONT(0.5)
          WITHIN GROUP (ORDER BY salary_year_avg), 0) AS median_salary,
    ROUND(MIN(salary_year_avg), 0)                   AS min_salary,
    ROUND(MAX(salary_year_avg), 0)                   AS max_salary
FROM jobs
WHERE salary_year_avg IS NOT NULL
  AND salary_year_avg > 0
GROUP BY job_title_short
ORDER BY median_salary DESC;


-- ── Q2: How do salaries vary by country? (Top 20 by job volume) ───────────────
--   Business use: guide location decisions and remote-work strategy.
WITH country_volume AS (
    SELECT
        job_country,
        COUNT(*) AS total_jobs
    FROM jobs
    WHERE salary_year_avg IS NOT NULL
    GROUP BY job_country
    ORDER BY total_jobs DESC
    LIMIT 20
)
SELECT
    j.job_country,
    cv.total_jobs,
    ROUND(PERCENTILE_CONT(0.5)
          WITHIN GROUP (ORDER BY j.salary_year_avg), 0) AS median_salary,
    ROUND(AVG(j.salary_year_avg), 0)                    AS avg_salary
FROM jobs j
JOIN country_volume cv ON j.job_country = cv.job_country
WHERE j.salary_year_avg IS NOT NULL
GROUP BY j.job_country, cv.total_jobs
ORDER BY median_salary DESC;


-- ── Q3: Which technical skills appear most in job postings? ───────────────────
--   Business use: identify skills to prioritise when upskilling.
SELECT
    s.skill_name,
    COUNT(DISTINCT s.job_id)                              AS job_count,
    ROUND(100.0 * COUNT(DISTINCT s.job_id)
          / (SELECT COUNT(DISTINCT job_id) FROM jobs), 2) AS pct_of_jobs
FROM skills s
GROUP BY s.skill_name
ORDER BY job_count DESC
LIMIT 20;


-- ── Q4: Which skills are associated with the highest salaries? ────────────────
--   Business use: identify the highest-value skills to learn.
SELECT
    s.skill_name,
    COUNT(DISTINCT s.job_id)                              AS job_count,
    ROUND(PERCENTILE_CONT(0.5)
          WITHIN GROUP (ORDER BY j.salary_year_avg), 0)  AS median_salary
FROM skills s
JOIN jobs j ON s.job_id = j.job_id
WHERE j.salary_year_avg IS NOT NULL
GROUP BY s.skill_name
HAVING COUNT(DISTINCT s.job_id) >= 50          -- filter out rare/noisy skills
ORDER BY median_salary DESC
LIMIT 20;


-- ── Q5: Does requiring more skills correlate with higher pay? ─────────────────
--   Business use: understand whether broader skill sets command premiums.
WITH skill_counts AS (
    SELECT
        job_id,
        COUNT(*) AS num_skills
    FROM skills
    GROUP BY job_id
),
salary_skill AS (
    SELECT
        j.job_title_short,
        j.salary_year_avg,
        sc.num_skills
    FROM jobs j
    JOIN skill_counts sc ON j.job_id = sc.job_id
    WHERE j.salary_year_avg IS NOT NULL
)
SELECT
    job_title_short,
    ROUND(AVG(num_skills), 1)                              AS avg_skills_required,
    ROUND(PERCENTILE_CONT(0.5)
          WITHIN GROUP (ORDER BY salary_year_avg), 0)      AS median_salary,
    COUNT(*)                                               AS job_count
FROM salary_skill
GROUP BY job_title_short
ORDER BY median_salary DESC;


-- ── Q6: How does employment type affect salary? ───────────────────────────────
--   Business use: compare full-time vs contract compensation.
SELECT
    job_schedule_type,
    COUNT(*)                                              AS job_count,
    ROUND(PERCENTILE_CONT(0.5)
          WITHIN GROUP (ORDER BY salary_year_avg), 0)    AS median_salary,
    ROUND(AVG(salary_year_avg), 0)                       AS avg_salary
FROM jobs
WHERE salary_year_avg IS NOT NULL
  AND job_schedule_type IS NOT NULL
GROUP BY job_schedule_type
ORDER BY median_salary DESC;


-- ── Q7: Senior vs. entry-level salary gap ─────────────────────────────────────
--   Business use: quantify the career-progression salary premium.
SELECT
    CASE
        WHEN LOWER(job_title_short) LIKE '%senior%'  THEN 'Senior'
        WHEN LOWER(job_title_short) LIKE '%lead%'    THEN 'Lead'
        WHEN LOWER(job_title_short) LIKE '%manager%' THEN 'Manager'
        WHEN LOWER(job_title_short) LIKE '%junior%'
          OR LOWER(job_title_short) LIKE '%entry%'   THEN 'Entry-Level'
        ELSE 'Mid-Level'
    END                                                      AS seniority,
    COUNT(*)                                                 AS job_count,
    ROUND(PERCENTILE_CONT(0.5)
          WITHIN GROUP (ORDER BY salary_year_avg), 0)        AS median_salary
FROM jobs
WHERE salary_year_avg IS NOT NULL
GROUP BY seniority
ORDER BY median_salary DESC;


-- ── Q8: Month-by-month job posting volume ─────────────────────────────────────
--   Business use: identify hiring cycles and peak recruitment months.
SELECT
    STRFTIME('%Y-%m', job_posted_date) AS posting_month,
    COUNT(*)                           AS total_postings,
    ROUND(AVG(salary_year_avg), 0)     AS avg_salary
FROM jobs
WHERE job_posted_date IS NOT NULL
  AND salary_year_avg IS NOT NULL
GROUP BY posting_month
ORDER BY posting_month;


-- ── Q9: Data Analyst specific — top skills & salaries ─────────────────────────
--   Business use: focus study plan specifically on Data Analyst requirements.
SELECT
    s.skill_name,
    COUNT(DISTINCT s.job_id)                             AS da_job_count,
    ROUND(PERCENTILE_CONT(0.5)
          WITHIN GROUP (ORDER BY j.salary_year_avg), 0) AS median_salary
FROM skills s
JOIN jobs j ON s.job_id = j.job_id
WHERE j.job_title_short = 'Data Analyst'
  AND j.salary_year_avg IS NOT NULL
GROUP BY s.skill_name
HAVING COUNT(DISTINCT s.job_id) >= 20
ORDER BY da_job_count DESC
LIMIT 15;


-- ── Q10: Remote vs. on-site salary comparison ─────────────────────────────────
--   Business use: assess the financial impact of remote-work roles.
SELECT
    CASE
        WHEN LOWER(job_schedule_type) LIKE '%remote%' THEN 'Remote'
        ELSE 'On-Site / Hybrid'
    END                                                      AS work_model,
    COUNT(*)                                                 AS job_count,
    ROUND(PERCENTILE_CONT(0.5)
          WITHIN GROUP (ORDER BY salary_year_avg), 0)        AS median_salary,
    ROUND(AVG(salary_year_avg), 0)                           AS avg_salary
FROM jobs
WHERE salary_year_avg IS NOT NULL
GROUP BY work_model
ORDER BY median_salary DESC;
