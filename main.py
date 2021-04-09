from xlsx2html import xlsx2html
import pdfkit

WKHTML2PDF_VERSION='0.12.4'


xlsx2html('path/example.xlsx', 'path/output.html')
pdfkit.from_url('path/output.html', 'path/out.pdf')
