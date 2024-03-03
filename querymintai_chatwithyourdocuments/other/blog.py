
# import flask
# from flask import request, jsonify
# from flask import render_template
# import transformers

# model = transformers.pipeline('question-answering', model='distilbert-base-cased-distilled-squad', tokenizer='bert-base-cased')

# app = flask.Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/answer') 
# def answer():
#     question = request.args['question']    
#     answers = get_answer(question)
    
#     return render_template('index.html', answer=answers['answer'])


# def get_answer(question):
#     with open('blog.txt', encoding="utf8") as f:
#         context = f.read()
#     answers = model(question=question, context=context)
#     return jsonify(answers)


# if __name__ == "__main__":
#     app.run()



import flask
from flask import request, jsonify, render_template
import transformers

model = transformers.pipeline('question-answering', model='distilbert-base-cased-distilled-squad', tokenizer='bert-base-cased')

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/answer') 
def answer():
    try:
        question = request.args['question']    
        answers = get_answer(question)
        return render_template('index.html', answer=answers['answer'])
    except Exception as e:
        return jsonify({'error': str(e)})


def get_answer(question):
    try:
        with open('blog.txt', encoding="utf8") as f:
            context = f.read()
        answers = model(question=question, context=context)

        # Accessing the 'answer' field from the dictionary-like object
        answer_text = answers['answer'] if 'answer' in answers else 'No answer found.'

        return jsonify({'answer': answer_text})
    except Exception as e:
        return jsonify({'error': str(e)})




if __name__ == "__main__":
    app.run()
