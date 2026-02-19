import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

def interactive_anova():
    file_path = input("Enter the path to your file: ").strip().replace('"', '')
    try:
        df = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    print("\nColumns:", ", ".join(df.columns))
    dep_var = input("\nDependent Variable (Numeric): ").strip()
    factors = [f.strip() for f in input("Enter 3 Factors (separated by commas): ").split(',')]

    try:
        # The Q() wrapper handles spaces and special characters in column names
        formula = f"Q('{dep_var}') ~ C(Q('{factors[0]}')) * C(Q('{factors[1]}')) * C(Q('{factors[2]}'))"
        
        model = ols(formula, data=df).fit()
        anova_table = sm.stats.anova_lm(model, typ=2)
        
        print("\n--- ANOVA RESULTS ---")
        print(anova_table)
    except Exception as e:
        print(f"\nMathematical Error: {e}")
        print("Tip: Check that your Dependent Variable column has only numbers and no empty cells.")

interactive_anova()