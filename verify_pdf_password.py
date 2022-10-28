SUCCESSFUL_PASSWORD_VERIFICATION_RESPONSE_FROM_BANK_LENDEN = 'Read Successful'

def verify_pdf_password(pdf_document, password):
    """
    Verify that the password provided for pdf document
    is correct or incorrect
    
    returns boolean, boolean
    
    the first boolean implies whether the document has a password or not
    the second boolean implies whether the password is correct or incorrect
    """ 
    import PyPDF2
    try:
        pypdf_obj = PyPDF2.PdfFileReader(pdf_document)
        if not pypdf_obj.isEncrypted:
            return False, True
        url = settings.BANK_API_URL
        payload = {"password":password}           
        files=[
            ('pdf_document', pdf_document)
        ]
        pdf_document.seek(0)
        response = requests.request("POST", url,data=payload, files=files)
        content = ast.literal_eval(response.content)
        message = content.get('message')
        if not message == SUCCESSFUL_PASSWORD_VERIFICATION_RESPONSE_FROM_BANK_LENDEN:
            return True, False
        return True, True
    except Exception as e:
        xprint(e, traceback.format_exc())
        return False, False
