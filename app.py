from flask import Flask, jsonify, request
from generic import generic_query_ext, vector_db
from langchain.chains import LLMChain
import os

app = Flask(__name__)

'''
Multi input chain with memory for external chat & doc qna app e.g. UiPath
'''
@app.route('/api/create_vectordb', methods=['POST'])
def create_vectordb():
    data = request.get_json()
    source = data.get('source')
    source_type = data.get('source_type')
    source_name = data.get('source_name')
    vdb = vector_db.create_db_from(source,source_type)
    # save vector db to local file
    vector_db.save_db(vdb, source_name)
    return jsonify({'result': source_name})

@app.route('/api/ask_question', methods=['POST'])
def ask_question():
    data = request.get_json()
    # load vector db from local file
    db_name = data.get('source_name')
    vdb = vector_db.load_db(db_name)
    # create chain with or without existing memory from local file
    memory_file = data.get('memory_file')
    if not os.path.isfile(memory_file):
        open(memory_file, 'w').close()
    chat, prompt, memory = generic_query_ext.init_llm_prompt_memory(memory_file, 0.0)
    chain = LLMChain(llm=chat, prompt=prompt, memory=memory) 
    query = data.get('query')    
    response = generic_query_ext.get_response_from_query(chain, vdb, 
                                                    query, k=10)
    print(response)
    vector_db.save_memory(chain, memory_file)
    return jsonify({'result': response, 'memory_file': memory_file})


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
