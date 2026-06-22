import certifi
from pymongo import MongoClient
from flask import Flask, jsonify, request
from bson.objectid import ObjectId

app = Flask(__name__)

# =========================
# CONEXÃO COM MONGODB ATLAS
# =========================

uri = "mongodb+srv://thiagogosantossilva_db_user:Kg8meUxZ4exHONbN @cluster0.awbdpgu.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(
        uri,
        tls=True,
        tlsCAFile=certifi.where()
    )

    db = client['ecommerce']
    produtos_collection = db['produtos']

    # Teste de conexão
    client.admin.command('ping')

    print("Conectado com sucesso ao MongoDB Atlas!")

except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")

# =========================
# ROTA INICIAL
# =========================

@app.route('/')
def home():
    return "API de E-commerce rodando no MongoDB Atlas!"

# =========================
# CREATE - Adicionar produto
# =========================

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    try:
        novo_produto = request.get_json()

        produto_id = produtos_collection.insert_one(
            novo_produto
        ).inserted_id

        return jsonify({
            "mensagem": "Produto adicionado com sucesso!",
            "id": str(produto_id)
        }), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# =========================
# READ - Listar produtos
# =========================

@app.route('/produtos', methods=['GET'])
def listar_produtos():

    produtos = list(produtos_collection.find())

    for produto in produtos:
        produto['_id'] = str(produto['_id'])

    return jsonify(produtos)

# =========================
# READ - Buscar produto por ID
# =========================

@app.route('/produtos/<id>', methods=['GET'])
def obter_produto(id):

    try:
        produto = produtos_collection.find_one({
            "_id": ObjectId(id)
        })

        if produto:
            produto['_id'] = str(produto['_id'])
            return jsonify(produto)

        return jsonify({
            "erro": "Produto não encontrado"
        }), 404

    except:
        return jsonify({
            "erro": "ID inválido"
        }), 400

# =========================
# UPDATE - Atualizar produto
# =========================

@app.route('/produtos/<id>', methods=['PUT'])
def atualizar_produto(id):

    try:
        dados_atualizados = request.get_json()

        resultado = produtos_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": dados_atualizados}
        )

        if resultado.matched_count > 0:
            return jsonify({
                "mensagem": "Produto atualizado com sucesso!"
            })

        return jsonify({
            "erro": "Produto não encontrado"
        }), 404

    except:
        return jsonify({
            "erro": "ID inválido"
        }), 400

# =========================
# DELETE - Remover produto
# =========================

@app.route('/produtos/<id>', methods=['DELETE'])
def remover_produto(id):

    try:
        resultado = produtos_collection.delete_one({
            "_id": ObjectId(id)
        })

        if resultado.deleted_count > 0:
            return jsonify({
                "mensagem": "Produto removido com sucesso!"
            })

        return jsonify({
            "erro": "Produto não encontrado"
        }), 404

    except:
        return jsonify({
            "erro": "ID inválido"
        }), 400

# =========================
# INICIAR SERVIDOR
# =========================

if __name__ == '__main__':
    app.run(debug=True)