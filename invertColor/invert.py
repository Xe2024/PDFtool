# converting the pdf to image
from pdf2image import convert_from_path
# Store Pdf with convert_from_path function
images = convert_from_path('C:/Users/COMPUTER/Downloads/5Matrices-and-Determinants-Notes-English.pdf', poppler_path = r'C:\Program Files\poppler-24.08.0\Library\bin')


for i in range(len(images)):
  
      # Save pages as images in the pdf


    # convert to greyscale
    from PIL import Image
    import PIL.ImageOps  
     # Op
    # print("Successfully made pdf file")
    # Save the grayscale image

    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')en the image
    image = images[i]

    # Convert the image to grayscale
    image = image.convert("L")
    inverted_image = PIL.ImageOps.invert(image)

    # converting back to pdf
    import img2pdf
    import os
    inverted_image.save(f"C:/Users/COMPUTER/Desktop/PDFtools/invertColor/invertedimages/inverted_image{i}.jpg") 
    

    from fpdf import FPDF
    pdf = FPDF()
    # imagelist is the list with all image filenames

    imageList =[]
    for i in range(len(images)):
        imageList.append(f"inverted_image{i}.jpg")
    


    with open(r"C:\Users\COMPUTER\Desktop\PDFtools\invertColor\finalPDF\final.pdf", "wb") as f:
      f.write(img2pdf.convert([open(f"C:/Users/COMPUTER/Desktop/PDFtools/invertColor/invertedimages/{i}", "rb") for i in os.listdir('C:/Users/COMPUTER/Desktop/PDFtools/invertColor/invertedimages/') if i.endswith(".jpg")]))
