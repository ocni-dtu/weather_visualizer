__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import typing
from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np

# Weather imports
from weather_visualizer import visualization

# -------------------------------------------------------------------------------------------------------------------- #
#


class PDF(FPDF):
    def header(self):
        # Logo
        self.image(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                'tests/test_data/report_data/livestock_cow.png'), 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(155)
        # Title
        self.cell(w=30, h=10, txt='Livestock Weather Visualizer', border=0, ln=0, align='C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def simple_report(weather_file: str, output: str):

    visualization.draw_wind_rose(weather_file, size=(110, 110))
    wind_path = os.path.join(output, 'wind.png')
    plt.savefig(wind_path, bbox_inches='tight', dpi=300)

    _, values = visualization.draw_yearly_values(weather_file, 'utci', size=(280, 90))
    utci_path = os.path.join(output, 'utci.png')
    plt.savefig(utci_path, bbox_inches='tight', dpi=300)
    maximum = np.max(values)
    q75 = np.quantile(values, 0.75)
    mean = np.mean(values)
    q25 = np.quantile(values, 0.25)
    minimum = np.min(values)

    pdf = PDF(orientation='L', format='A3')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.image(utci_path, x=12.7, y=54, w=280, h=90)
    pdf.image(wind_path, x=12.7, y=171, w=110, h=110)
    out_path = os.path.join(output, 'report.pdf')

    pdf.set_y(50)
    pdf.cell(290)
    pdf.set_font('Arial', 'B', 15)
    pdf.cell(w=30, h=10, txt=f'UTCI Stats:')
    pdf.ln(15)
    pdf.cell(290)
    pdf.cell(w=30, h=10, txt=f'Max: {maximum:.2f}C')
    pdf.ln(10)
    pdf.cell(290)
    pdf.cell(w=30, h=10, txt=f'Q75: {q75:.2f}C')
    pdf.ln(10)
    pdf.cell(290)
    pdf.cell(w=30, h=10, txt=f'Mean: {mean:.2f}C')
    pdf.ln(10)
    pdf.cell(290)
    pdf.cell(w=30, h=10, txt=f'Q25: {q25:.2f}C')
    pdf.ln(10)
    pdf.cell(290)
    pdf.cell(w=30, h=10, txt=f'Min: {minimum:.2f}C')

    pdf.output(out_path, 'F')
