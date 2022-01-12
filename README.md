# padpdf-ocr
PaddleOCR for Chinese pdf
## Rationale: 
中文pdf的识别日常中要么用Adobe Acrobat, 精度尚可但是是付费软件，要么用tesseract但是只在极高清晰度时才有效果。
结合pymupdf与paddleocr, 完成对中文扫描pdf的识别，并进行简单排版。
## TODO
利用PPstructure获得简单排版，图片截图插入
为没有目录的pdf文件增加识别的目录。
## Usage
`python pdf-ocr.py <pdf file path>`
## Example Results
!(Example)[https://github.com/nmusik/padpdf-ocr/blob/main/docs/examples/SapF.png?raw=true]
