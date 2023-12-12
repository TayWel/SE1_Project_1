def Process_Image():
    #Import neccessary tools and libraries
    from PIL import Image
    from pytesseract import pytesseract
    import enum


    T="hi"
    class OS(enum.Enum):
        if T == "hi":
            print('Works')


    class ImageReader:
        def __init__(self, os:OS):
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            pytesseract.tesseract_cmd = windows_path
        
        def extract_text(self, image: str,) -> str:
            img = Image.open(image)
            extracted_text = pytesseract.image_to_string(img)
            return extracted_text


    ir = ImageReader(OS)
    text = ir.extract_text('C:\\Users\\Daniel\\Desktop\\Project_Code\\Test_Image0.png')
    processed_text = ' '.join(text.split())
    print(processed_text)

#Call Function
Process_Image()