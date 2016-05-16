
from django.shortcuts import render
from django.template.loader import get_template 
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from django.conf import settings

from django.conf import settings

class Resume(View):

	def get(self,request):
		return render(request,'resume.html')

	def post(self,request):
		return HttpResponse('Resume post')

class Download(View):

	def get(self,request):
		# template = get_template("pdf_resume.html")
		# context = Context()  # data is the context data that is sent to the html file to render the output. 
		# html = template.render(context)  # Renders the template with the context data.
		# pdfkit.from_string(html, 'out.pdf')
		# pdf = open("out.pdf")
		# response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
		# response['Content-Disposition'] = 'attachment; filename=output.pdf'
		# pdf.close()
		
		# return response

		# html  = render_to_string('resume.html', { 'pagesize' : 'A4', }, context_instance=RequestContext(request))
		# result = StringIO.StringIO()
		# pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), dest=result, link_callback=fetch_resources )
		# if not pdf.err:
		#     return HttpResponse(result.getvalue(), content_type='application/pdf')
		# return HttpResponse('Gremlins ate your pdf! %s' % cgi.escape(html))

		# templates_dir = settings.BASE_DIR+'/res/templates'
		# print templates_dir
		# print os.path.abspath(__file__)
		# print os.path.dirname('templates')

		# input_filename = settings.BASE_DIR+'/res/templates/resume.html'
		# output_filename = 'README.pdf'
	
		# #pdf = pdfkit.from_file('resume.html', 'micro.pdf')
		# with open(input_filename, 'r') as f:
		# 	#f.decode('utf-8')
		# 	html_text = markdown(f.read().decode('utf-8'), output_format='html4')
 
		# options = {
		#     'page-size': 'Letter',
		#     'margin-top': '0.25in',
		#     'margin-right': '0.25in',
		#     'margin-bottom': '0.25in',
		#     'margin-left': '0.25in',
		#     'encoding': "UTF-8",
		#     'no-outline': None
		# }
		 
		# css = settings.BASE_DIR+'/res/static/css/style.css'
		
		with open(settings.BASE_DIR+'/res/static/assets/resume.pdf') as pdf:
			response = HttpResponse(pdf.read(), content_type='application/pdf') 
			response['Content-Disposition'] = 'attachment; filename=resume.pdf'
			pdf.closed	
	
		return response

	def post(self,request):
		return HttpResponse('Download post')

def fetch_resources(uri, rel):
	    # use short variable names
	    sUrl = settings.STATIC_URL      # Typically /static/
	    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
	    mUrl = settings.MEDIA_URL       # Typically /static/media/
	    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

	    # convert URIs to absolute system paths
	    if uri.startswith(mUrl):
	        path = os.path.join(mRoot, uri.replace(mUrl, ""))
	    elif uri.startswith(sUrl):
	        path = os.path.join(sRoot, uri.replace(sUrl, ""))
	    else:
	        return uri  # handle absolute uri (ie: http://some.tld/foo.png)