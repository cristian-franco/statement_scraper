import pandas as pd
import pdfplumber

def read_cc_statement(
    file_path: str
):
    '''
    First page of transactions will say TRANSACTIONS
    when extract_tables is called
    Subsequent pages will say TRANSACTIONS (Continued)
    '''
    df = pd.DataFrame()
    with pdfplumber.open(
        file_path
    ) as pdf:
        print(
            "Total number of pages:",
            len(pdf.pages)
        )

        third_page = pdf.pages[2]

        tables = third_page.crop((
            third_page.width * 0.08,  # left
            third_page.height * 0.15,  # top
            third_page.width * 0.97,   # right
            third_page.height * 0.9   # bottom
        )).extract_tables()

        print(len(tables))

        if tables:
            df = pd.DataFrame(
                tables[0][1:],
                columns=tables[0][0]
            )

        df[

        ]

    return df


def extract_pdf_content(
    pdf_path: str
):
    # Open the PDF
    with pdfplumber.open(
        pdf_path
    ) as pdf:
        # Basic text extraction
        print(
            "Total number of pages:",
            len(pdf.pages)
        )

        # Extract text from entire document
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n\n"

        # Extract text from first page
        first_page_text = pdf.pages[0].extract_text()

        # Extract tables from first page
        tables = pdf.pages[0].extract_tables()

        # Convert first table to pandas DataFrame
        if tables:
            df = pd.DataFrame(
                tables[0][1:],
                columns=tables[0][0]
            )

        # Extract specific regions (if the PDF has a structured layout)
        first_page = pdf.pages[0]

        # Example of extracting text from a specific bounding box
        extracted_region = first_page.crop((
            first_page.width * 0.1,  # left
            first_page.height * 0.1,  # top
            first_page.width * 0.9,   # right
            first_page.height * 0.5   # bottom
        )).extract_text()

        # Extract images (if any)
        images = []
        for page_num, page in enumerate(pdf.pages):
            page_images = page.images
            for img in page_images:
                images.append({
                    'page': page_num,
                    'x0': img['x0'],
                    'top': img['top'],
                    'width': img['width'],
                    'height': img['height']
                })

        return {
            'total_pages': len(pdf.pages),
            'full_text': full_text,
            'first_page_text': first_page_text,
            'tables': tables,
            'extracted_region': extracted_region,
            'images': images
        }
