from sys import stdin
import pandas as pd
from utility import bank
from utility import credit_card

# print('Reading Bank Statements...')
# bank_transactions_df = bank.read_bank_statement('files/transactions.csv')
# print(
#     'Done Reading!\n'
#     f"Size: {len(bank_transactions_df)}"
# )
# # print(bank_transactions_df.columns)
# summary_df = bank.create_bank_pivot(
#     transactions_df=bank_transactions_df
# )

# print(summary_df)

# cc_pdf = credit_card.read_cc_statement(
#     'files/Statement_102024_5607.pdf'
# )

# print(cc_pdf.pages)

# page_1 = cc_pdf.pages[0]

# test_char = page_1.chars[3]

# print(page_1)
# print(test_char)

def main():
    try:
        cc_transactions_df = credit_card.read_cc_statement(
            'files/Statement_102024_5607.pdf'
        )

        # # Print extracted information
        # print("Full Text Preview:")
        # # First 500 characters
        # print(pdf_content['full_text'][:500])

        # Print tables if exists
        if not cc_transactions_df.empty:
            print(
                "SIZE OF DF: ",
                len(cc_transactions_df)
            )
            print("COLUMNS: ")
            for col in cc_transactions_df.columns:
                print(col)

            print(cc_transactions_df)

        # # Print image information
        # print(
        #     "\n\n\nImages Found:",
        #     len(pdf_content['images'])
        # )
        # for img in pdf_content['images']:
        #     print(
        #         f"Image on page {img['page']}: {img['width']}x{img['height']} pixels"
        #     )

    except FileNotFoundError:
        print(
            "PDF file not found.",
            "Please check the file path."
        )
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
