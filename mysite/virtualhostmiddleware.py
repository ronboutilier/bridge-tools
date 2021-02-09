virtual_hosts = {
    "www.bridgetoolsonline.com":"main.urls",
    "www.ronboutilier.com":"ronboutilier.urls",
}



class VirtualHostMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		host = request.get_host()
		request.urlconf = virtual_hosts.get(host)
		response = self.get_response(request)
		return response
