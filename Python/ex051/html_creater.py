


def create(data, device = 1):
    p, t, w = data
    h = "<html><head></head><body>"

    h+='<p>Temperature: {}</p>'.format(t)
    h+='<p>Wind speed: {}</p>'.format(w)
    h+='<p>Pressure: {}</p>'.format(p)

    with open('index.html', 'w') as page:
        page.write(h)
  
    return h
