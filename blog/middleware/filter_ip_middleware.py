class FilterIPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
    # Check if client IP is allowed

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        # Authorized ip's
        allowed_ips = ['192.168.1.1', '123.123.123.123',
                       '127.0.0.1', '192.168.233.251']
        ip = request.META.get('REMOTE_ADDR')  # Get client IP
        if ip not in allowed_ips:
            raise Http403  # If user is not allowed raise Error

       # If IP is allowed we don't do anything
        return None
