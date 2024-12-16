# 4. win32com
# The win32com module is used for working with COM (Component Object Model) objects, which are an
#  integral part of Windows applications like Microsoft Office, Internet Explorer, etc.

# Key Features:
# Automating applications like Excel, Word, or Outlook.
# Creating and interacting with COM objects.
# Advanced scripting and control of Windows components.



# Automating Microsoft Word:
import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.Visible = True
doc = word.Documents.Add()
doc.Content.Text = "Hello, Word!"
doc.SaveAs("example.docx")
word.Quit()


# Automating Microsoft excel
# import win32com.client

# excel = win32com.client.Dispatch("Excel.Application")
# excel.Visible = True
# workbook = excel.Workbooks.Add()
# sheet = workbook.Sheets(1)
# sheet.Cells(1, 1).Value = "Hello, Excel!"
# workbook.SaveAs("example.xlsx")
# excel.Quit()


# text to speech
