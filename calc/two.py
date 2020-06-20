from cgi import parse_qs
from three import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])

    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    q = 0
    if '' not in [a, b]:
        a, b = int(a), int(b)
        for i in range(b):
            q = q+a
    sum = a+b
    multiplication = q


    response_body = html % {
        'a':a,
        'b':b,
        'sum':sum,
        'multiplication':multiplication,
    }


    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
