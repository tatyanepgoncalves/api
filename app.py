from flask import Flask, request, jsonify, render_template
import sqlite3


app = Flask(__name__)

def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL, 
            category TEXT NOT NULL,
            author TEXT NOT NULL,
            image_url TEXT NOT NULL 
        )""")
        print("Banco de dados inicializado com sucesso!")


init_db()


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/doar", methods=["POST"])
def doar():
    dados = request.get_json()

    title = dados.get("title")
    category = dados.get("category")
    author = dados.get("author")
    image_url = dados.get("image_url")

    if not all([title, category, author, image_url]):
        return jsonify({'erro': "Todos os campos são obrigatórios."}), 400

    with sqlite3.connect('database.db') as conn:
        conn.execute(
            """INSERT INTO livros (title, category, author, image_url) VALUES (?, ?, ?, ?)""",
            (title, category, author, image_url)
        )
        conn.commit()

    return jsonify({"Mensagem": "Livro cadastrado com sucesso"}), 201

@app.route("/list-livros", methods=["GET"])
def listar_livros():
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM livros""")
        livros = [dict(row) for row in cursor.fetchall()]

    return jsonify(livros), 200

@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livros(id):

    data = request.json
    title = data.get("title")
    category = data.get("category")
    author = data.get("author")
    image_url = data.get("image_url")

    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(""" UPDATE livros SET title = ?, category = ?, author = ?, image_url = ? WHERE id = ?""", (title, category, author, image_url, id, ))
        conn.commit()

    return jsonify({ "Mensagem": "Livro atualizado com sucesso."}), 200

@app.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livros(id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute(""" SELECT * FROM livros WHERE id = ?""", (id,))
        livro = cursor.fetchone()

        if not livro:
            return jsonify({ "erro" : "Livro não encontrado."}), 404

        cursor.execute(""" DELETE FROM livros WHERE id = ?""", (id,))
        conn.commit()
    return jsonify({ "mensagem": f"Livro com ID {id} deletado com sucesso."}), 200

if __name__ == "__main__":
    app.run(debug=True)
