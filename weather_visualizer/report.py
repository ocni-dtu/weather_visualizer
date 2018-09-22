__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import typing
from fpdf import FPDF
import matplotlib.pyplot as plt

# Weather imports
from weather_visualizer import visualization

# -------------------------------------------------------------------------------------------------------------------- #
#

class PDF(FPDF):
    def header(self):
        # Logo
        self.image(r'C:\Users\Christian\PycharmProjects\weather_visualizer\tests\test_data\report_data\livestock_cow.png', 10, 8, 33)
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
    plt.savefig(wind_path, bbox_inches='tight')

    visualization.draw_yearly_values(weather_file, 'utci', size=(280, 90))
    utci_path = os.path.join(output, 'utci.png')
    plt.savefig(utci_path, bbox_inches='tight')

    pdf = PDF(orientation='L', format='A3')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.image(utci_path, x=12.7, y=54, w=280, h=90)
    pdf.image(wind_path, x=12.7, y=171, w=110, h=110)
    out_path = os.path.join(output, 'report.pdf')
    pdf.output(out_path, 'F')
