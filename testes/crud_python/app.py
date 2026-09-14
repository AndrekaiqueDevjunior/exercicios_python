from http.server import BaseHTTPRequestHandler, HTTPServer
import json


produtos = [
    {
        "id": 1,
        "nome": "Teclado",
        "preco": 100
    },
    {
        "id": 2,
        "nome": "Mouse",
        "preco": 50
    }
]


class Servidor(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/produtos":

            resposta = json.dumps(produtos)

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                resposta.encode()
            )


servidor = HTTPServer(
    ("localhost", 8000),
    Servidor
)

print("Servidor rodando em http://localhost:8000")

servidor.serve_forever()