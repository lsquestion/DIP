import imageio
import xlsxwriter


image_color=imageio.imread('Sekuai.jpg')
"""
WB=xlsxwriter.Workbook('imgdata.xlsx')
WB_S1=WB.add_worksheet()

WB_S1.write(image_color[0][0][0])
WB.close()
"""

print(image_color[0])