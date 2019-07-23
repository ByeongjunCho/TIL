import webbrowser

def make_url(token, method):
    return f'https://api.telgram.com/bot{token}/{method}'

def docs():
    webbrowser.open('https://telegram.com')
    return True