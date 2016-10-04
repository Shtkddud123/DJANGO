from django.shortcuts import render
from django.http import HttpResponse ## Standard website response you want
from django.http import HttpResponseNotFound
from django.template import loader
#from django.urls import reverse

# image libraries
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image, StringIO

def showimage(request):
    # Construct the graph
    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)
    plot(t, s, linewidth=1.0)
    
    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('About as simple as it gets, folks')
    grid(True)
    
    # Store image in a string buffer
    buffer = StringIO.StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue())
