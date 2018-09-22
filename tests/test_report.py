__author__ = "Christian Kongsgaard"
__license__ = "GNU GPLv3"

# -------------------------------------------------------------------------------------------------------------------- #
# Imports


# Module imports
import os
import typing
import subprocess

# Weather imports
from weather_visualizer import report

# -------------------------------------------------------------------------------------------------------------------- #
#


def test_report_simple(tmpdir):
    pdf = report.PDF(orientation='L', format='A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in range(1, 10):
        pdf.cell(0, 10, 'Printing line number ' + str(i), 0, 1)

    out_path = os.path.join(tmpdir, 'test.pdf')
    pdf.output(out_path, 'F')

    subprocess.Popen(out_path, shell=True)


def test_simple_report(tmpdir, test_data):
    epw = os.path.join(test_data, 'weather_data', 'CPH_DRY_2013CST.epw')

    report.simple_report(epw, tmpdir)

    out_path = os.path.join(tmpdir, 'report.pdf')
    subprocess.Popen(out_path, shell=True)
