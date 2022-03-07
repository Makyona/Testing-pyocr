import pytesseract as pyt
import glob
import pdf2image as p2i
path = 'PDFs/'
for file in glob.iglob(f'{path}/*'):
    txtname = file[:-4] + ".txt"
    fp = open(txtname, 'w')
    [fp.write(str(pyt.image_to_string(p))) for p in p2i.convert_from_path(file, 300)]
    fp.close()