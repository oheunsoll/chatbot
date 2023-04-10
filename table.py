# Import the required Module
import tabula
import pandas as pd

# Read a PDF File
df = tabula.read_pdf("C:\ll.pdf", pages='all')

# convert PDF into CSV
tabula.convert_into("output.csv", encoding='utf-8')