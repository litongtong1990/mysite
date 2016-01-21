from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import qrcode
from cStringIO import StringIO
 
 
def generate_qrcode(request, product_name):
    

    url="http://10.140.41.190:8000/polls/"+product_name
    print "====="
    print url
    print "====="
    img = qrcode.make(url)
    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()
 
    response = HttpResponse(image_stream, content_type="image/png")
    response['Last-Modified'] = 'Mon, 27 Apr 2015 02:05:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response
