"""
Data Jobs Market Analysis — Python EDA Script
Author : Rakhi Yadav
Dataset: 2023 Data Science Job Market (data_jobs_salary_all.xlsx)

Business Questions Answered:
  1. Which job titles command the highest median salaries?
  2. How do salaries vary by country?
  3. Which technical skills are most in demand?
  4. Which skills are associated with higher salaries?
  5. Does requiring more skills correlate with higher pay?
  6. How does employment type (full-time vs contract) affect salary?
"""

import sys
import warnings

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import seaborn as sns

warnings.filterwarnings("ignore")

# ── Configuration ─────────────────────────────────────────────────────────────
DATA_FILE = "data_jobs_salary_all.xlsx"
SHEET_JOBS = "data_jobs_all"          # adjust if sheet name differs
SHEET_SKILLS = "data_jobs_skills"     # adjust if sheet name differs
PALETTE = "Blues_r"
FIG_SIZE = (12, 6)

# ── 1. Load Data ───────────────────────────────────────────────────────────────
def load_data(filepath: str) -> tuple[pd.DataFrame, pd.DataFrame | None]:
    """Load jobs and (optionally) skills sheets from the Excel workbook."""
    xl = pd.ExcelFile(filepath)
    print(f"Available sheets: {xl.sheet_names}")

    # Load the jobs sheet — fall back to first sheet if name is different
    jobs_sheet = SHEET_JOBS if SHEET_JOBS in xl.sheet_names else xl.sheet_names[0]
    df_jobs = xl.parse(jobs_sheet)
    print(f"\nJobs sheet '{jobs_sheet}': {df_jobs.shape[0]:,} rows × {df_jobs.shape[1]} columns")

    # Load skills sheet if present
    df_skills = None
    if SHEET_SKILLS in xl.sheet_names:
        df_skills = xl.parse(SHEET_SKILLS)
        print(f"Skills sheet '{SHEET_SKILLS}': {df_skills.shape[0]:,} rows × {df_skills.shape[1]} columns")

    return df_jobs, df_skills


# ── 2. Clean Data ──────────────────────────────────────────────────────────────
def clean_jobs(df: pd.DataFrame) -> pd.DataFrame:
    """Standardise columns, remove blanks, fix dtypes."""
    # Normalise column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Drop rows with no salary information
    salary_col = next((c for c in df.columns if "salary" in c and "year" in c), None)
    if salary_col is None:
        raise ValueError(
            f"Could not find a yearly salary column. Columns present: {list(df.columns)}"
        )
    df = df.rename(columns={salary_col: "salary_year_avg"})

    before = len(df)
    df = df[df["salary_year_avg"].notna() & (df["salary_year_avg"] > 0)].copy()
    print(f"\nData Cleaning: removed {before - len(df):,} rows with missing/zero salary "
          f"({before:,} → {len(df):,} rows retained)")

    # Remove extreme outliers (below 1st or above 99th percentile) per title
    low, high = df["salary_year_avg"].quantile([0.01, 0.99])
    df = df[(df["salary_year_avg"] >= low) & (df["salary_year_avg"] <= high)].copy()

    # Standardise title / country / schedule columns
    for col in ["job_title_short", "job_country", "job_schedule_type"]:
        if col in df.columns:
            df[col] = df[col].str.strip()

    # Deduplicate on job_id if column exists
    if "job_id" in df.columns:
        before_dedup = len(df)
        df = df.drop_duplicates(subset="job_id")
        print(f"Deduplication: {before_dedup - len(df):,} duplicate job IDs removed")

    return df


# ── 3. Analysis Functions ─────────────────────────────────────────────────────
def median_salary_by_title(df: pd.DataFrame) -> pd.DataFrame:
    """Return median salary and job count for each job title, sorted descending."""
    result = (
        df.groupby("job_title_short", as_index=False)
        .agg(median_salary=("salary_year_avg", "median"),
             job_count=("salary_year_avg", "count"))
        .sort_values("median_salary", ascending=False)
    )
    return result


def median_salary_by_country(df: pd.DataFrame, top_n: int = 15) -> pd.DataFrame:
    """Return median salary for the top N countries by job count."""
    country_counts = df["job_country"].value_counts()
    top_countries = country_counts.head(top_n).index
    result = (
        df[df["job_country"].isin(top_countries)]
        .groupby("job_country", as_index=False)
        .agg(median_salary=("salary_year_avg", "median"),
             job_count=("salary_year_avg", "count"))
        .sort_values("median_salary", ascending=False)
    )
    return result


def salary_by_employment_type(df: pd.DataFrame) -> pd.DataFrame:
    """Median salary and count by employment / schedule type."""
    if "job_schedule_type" not in df.columns:
        return pd.DataFrame()
    result = (
        df.groupby("job_schedule_type", as_index=False)
        .agg(median_salary=("salary_year_avg", "median"),
             job_count=("salary_year_avg", "count"))
        .sort_values("median_salary", ascending=False)
    )
    return result


def top_skills(df_skills: pd.DataFrame, top_n: int = 15) -> pd.DataFrame:
    """Return the most frequently listed technical skills."""
    if df_skills is None or df_skills.empty:
        return pd.DataFrame()
    df_skills.columns = df_skills.columns.str.strip().str.lower().str.replace(" ", "_")
    skill_col = next((c for c in df_skills.columns if "skill" in c and "name" in c), None)
    if skill_col is None:
        skill_col = next((c for c in df_skills.columns if "skill" in c), None)
    if skill_col is None:
        return pd.DataFrame()
    counts = df_skills[skill_col].value_counts().head(top_n).reset_index()
    counts.columns = ["skill", "count"]
    return counts


def skill_count_vs_salary(df: pd.DataFrame, df_skills: pd.DataFrame) -> pd.DataFrame:
    """Average skill count per job vs median salary by job title."""
    if df_skills is None or df_skills.empty:
        return pd.DataFrame()
    df_skills.columns = df_skills.columns.str.strip().str.lower().str.replace(" ", "_")
    id_col = next((c for c in df_skills.columns if "job_id" in c), None)
    if id_col is None or "job_id" not in df.columns:
        return pd.DataFrame()
    skill_counts = df_skills.groupby(id_col).size().reset_index(name="skill_count")
    merged = df.merge(skill_counts, left_on="job_id", right_on=id_col, how="inner")
    result = (
        merged.groupby("job_title_short", as_index=False)
        .agg(median_salary=("salary_year_avg", "median"),
             avg_skill_count=("skill_count", "mean"))
        .sort_values("median_salary", ascending=False)
    )
    return result


# ── 4. Visualisations ─────────────────────────────────────────────────────────
def _fmt_salary(ax, axis: str = "x") -> None:
    """Format salary axis ticks as $K."""
    fmt = mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K")
    if axis == "x":
        ax.xaxis.set_major_formatter(fmt)
    else:
        ax.yaxis.set_major_formatter(fmt)


def plot_salary_by_title(df_agg: pd.DataFrame) -> None:
    """Horizontal bar chart: median salary by job title."""
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    colors = sns.color_palette(PALETTE, len(df_agg))
    ax.barh(df_agg["job_title_short"], df_agg["median_salary"], color=colors)
    _fmt_salary(ax, "x")
    ax.set_xlabel("Median Annual Salary (USD)")
    ax.set_title("Median Annual Salary by Job Title — 2023 Data Market", fontweight="bold")
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig("salary_by_title.png", dpi=150)
    plt.show()
    print("Saved: salary_by_title.png")


def plot_salary_by_country(df_agg: pd.DataFrame) -> None:
    """Horizontal bar chart: median salary by country."""
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    colors = sns.color_palette(PALETTE, len(df_agg))
    ax.barh(df_agg["job_country"], df_agg["median_salary"], color=colors)
    _fmt_salary(ax, "x")
    ax.set_xlabel("Median Annual Salary (USD)")
    ax.set_title("Median Annual Salary by Country (Top 15) — 2023", fontweight="bold")
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig("salary_by_country.png", dpi=150)
    plt.show()
    print("Saved: salary_by_country.png")


def plot_top_skills(df_agg: pd.DataFrame) -> None:
    """Horizontal bar chart: most in-demand technical skills."""
    if df_agg.empty:
        print("Skills data not available — skipping skills chart.")
        return
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    colors = sns.color_palette("Greens_r", len(df_agg))
    ax.barh(df_agg["skill"], df_agg["count"], color=colors)
    ax.set_xlabel("Number of Job Postings")
    ax.set_title("Top 15 Most In-Demand Technical Skills — 2023 Data Market", fontweight="bold")
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig("top_skills.png", dpi=150)
    plt.show()
    print("Saved: top_skills.png")


def plot_skill_count_vs_salary(df_agg: pd.DataFrame) -> None:
    """Scatter plot: average skill count vs median salary by job title."""
    if df_agg.empty:
        print("Skill-salary correlation data not available — skipping scatter.")
        return
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df_agg, x="avg_skill_count", y="median_salary",
                    s=120, color="steelblue", ax=ax)
    for _, row in df_agg.iterrows():
        ax.annotate(row["job_title_short"],
                    xy=(row["avg_skill_count"], row["median_salary"]),
                    xytext=(6, 0), textcoords="offset points",
                    fontsize=8, va="center")
    _fmt_salary(ax, "y")
    ax.set_xlabel("Average Number of Skills Required")
    ax.set_ylabel("Median Annual Salary (USD)")
    ax.set_title("Do More Skills = Higher Salary? (by Job Title)", fontweight="bold")
    plt.tight_layout()
    plt.savefig("skill_count_vs_salary.png", dpi=150)
    plt.show()
    print("Saved: skill_count_vs_salary.png")


def plot_salary_by_employment_type(df_agg: pd.DataFrame) -> None:
    """Bar chart: median salary by employment type."""
    if df_agg.empty:
        print("Employment type data not available — skipping chart.")
        return
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = sns.color_palette("Oranges_r", len(df_agg))
    ax.bar(df_agg["job_schedule_type"], df_agg["median_salary"], color=colors)
    _fmt_salary(ax, "y")
    ax.set_xlabel("Employment Type")
    ax.set_ylabel("Median Annual Salary (USD)")
    ax.set_title("Median Salary by Employment Type — 2023", fontweight="bold")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig("salary_by_employment_type.png", dpi=150)
    plt.show()
    print("Saved: salary_by_employment_type.png")


# ── 5. KPI Summary ─────────────────────────────────────────────────────────────
def print_kpis(df: pd.DataFrame) -> None:
    """Print a concise KPI summary to the console."""
    print("\n" + "=" * 60)
    print("  KEY PERFORMANCE INDICATORS — 2023 DATA JOBS MARKET")
    print("=" * 60)
    print(f"  Total job postings analysed : {len(df):>10,}")
    print(f"  Unique job titles           : {df['job_title_short'].nunique():>10,}")
    print(f"  Countries represented       : {df['job_country'].nunique():>10,}")
    print(f"  Overall median salary (USD) : ${df['salary_year_avg'].median():>9,.0f}")
    print(f"  Overall mean salary (USD)   : ${df['salary_year_avg'].mean():>9,.0f}")
    print(f"  Salary range (USD)          : ${df['salary_year_avg'].min():,.0f} – ${df['salary_year_avg'].max():,.0f}")

    top_title = df.groupby("job_title_short")["salary_year_avg"].median().idxmax()
    top_salary = df.groupby("job_title_short")["salary_year_avg"].median().max()
    print(f"  Highest-paying title        : {top_title} (${top_salary:,.0f})")

    top_country = df.groupby("job_country")["salary_year_avg"].median().idxmax()
    top_country_sal = df.groupby("job_country")["salary_year_avg"].median().max()
    print(f"  Highest-paying country      : {top_country} (${top_country_sal:,.0f})")
    print("=" * 60 + "\n")


# ── 6. Main ────────────────────────────────────────────────────────────────────
def main() -> None:
    print("Loading data …")
    df_jobs, df_skills = load_data(DATA_FILE)

    print("\nCleaning data …")
    df_jobs = clean_jobs(df_jobs)

    print_kpis(df_jobs)

    # --- Analysis ---
    df_title_salary = median_salary_by_title(df_jobs)
    df_country_salary = median_salary_by_country(df_jobs)
    df_emp_salary = salary_by_employment_type(df_jobs)
    df_skills_demand = top_skills(df_skills)
    df_skill_corr = skill_count_vs_salary(df_jobs, df_skills)

    # --- Console output ---
    print("Median Salary by Job Title:")
    print(df_title_salary.to_string(index=False))

    print("\nMedian Salary by Country (Top 15):")
    print(df_country_salary.to_string(index=False))

    # --- Visualisations ---
    plot_salary_by_title(df_title_salary)
    plot_salary_by_country(df_country_salary)
    plot_top_skills(df_skills_demand)
    plot_skill_count_vs_salary(df_skill_corr)
    plot_salary_by_employment_type(df_emp_salary)

    print("\nAnalysis complete. All charts saved as PNG files.")


if __name__ == "__main__":
    main()
