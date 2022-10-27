def convert_pdf_to_image(pdf_object):
    """
    Utility helper that converts pdf object into image object
    :params pdf_object: pdf in binary
    :returns image binary
    """
    import traceback
    try:
        startmark = b"\xff\xd8"
        startfix = 0
        endmark = b"\xff\xd9"
        endfix = 2
        i = 0

        njpg = 0
        while True:
            istream = pdf_object.find(b"stream", i)
            if istream < 0:
                break
            istart = pdf_object.find(startmark, istream, istream + 20)
            if istart < 0:
                i = istream + 20
                continue
            iend = pdf_object.find(b"endstream", istart)
            if iend < 0:
                raise Exception("Didn't find end of stream!")
            iend = pdf_object.find(endmark, iend - 20)
            if iend < 0:
                raise Exception("Didn't find end of JPG!")

            istart += startfix
            iend += endfix
            jpg = pdf_object[istart:iend]
            
            njpg += 1
            i = iend

            return jpg
    except Exception as e:
        xprint('Excepton in convert_pdf_to_image | {} | {}'.format(e, traceback.format_exc()))
