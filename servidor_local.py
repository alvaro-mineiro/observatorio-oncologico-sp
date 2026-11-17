# Abre o painel no computador: um servidor só desta máquina (127.0.0.1), nesta pasta. Feche a janela para parar.
import functools, http.server, os, socket, threading, time, webbrowser
pasta = os.path.dirname(os.path.abspath(__file__))
with socket.socket() as s:
    s.bind(("127.0.0.1", 0)); porta = s.getsockname()[1]
srv = http.server.ThreadingHTTPServer(("127.0.0.1", porta),
    functools.partial(http.server.SimpleHTTPRequestHandler, directory=pasta))
url = f"http://127.0.0.1:{porta}/index.html"
print("Painel em", url, "- deixe esta janela aberta enquanto usa; feche para encerrar.", flush=True)
threading.Thread(target=srv.serve_forever, daemon=True).start()   # o servidor já responde antes de abrir o navegador
webbrowser.open(url)
try:
    while True: time.sleep(3600)
except KeyboardInterrupt: pass
