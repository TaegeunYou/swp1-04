from cgi import parse_qs
from three import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])

    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    if '' not in [a, b]:
        a, b = int(a), int(b)
        sum = a+b
        multiplication = a*b
    else:
        sum = "None"
        multiplication = "None"
    

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
