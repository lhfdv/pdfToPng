from wand.image import Image as local

PDFfile = local(filename="base.pdf", resolution=400)

Images = PDFfile.convert('png')

ImageSequence = 1

for img in PDFfile.sequence:
    Image = local(image = img)
    Image.save(filename = "img" + str(ImageSequence) + ".png")
    ImageSequence += 1