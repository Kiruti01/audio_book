import PyPDF2
from gtts import gTTS

# Open the PDF file
pdf_file = open('book.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from all pages of the PDF
text = ''
for page in pdf_reader.pages:
    text += page.extract_text()

# Initialize gTTS with the text and language
language = 'en'
audio = gTTS(text=text, lang=language, slow=False)

# Save the audio file
audio.save('book.mp3')

