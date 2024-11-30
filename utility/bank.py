import pandas as pd


def read_bank_statement(
    file_path: str
) -> pd.DataFrame:
    '''
    Read bank statement from website provided csv.
    '''
    df = pd.read_csv(
        file_path
    )

    df.columns = df.columns.str.strip()

    df.columns = [
        col.lower().replace(' ', '_').replace('-', '_')
        for col in df.columns
    ]

    return df


def create_bank_pivot(
    transactions_df: pd.DataFrame
) -> pd.DataFrame:
    pivot_df = transactions_df.pivot_table(
        values='amount',
        index='type',
        aggfunc='sum'
    )

    return pivot_df
