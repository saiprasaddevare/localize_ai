from flask import Flask, request, jsonify
import dl_translate as dlt

# Initialize Flask app
app = Flask(__name__)

# Initialize the translation model
mt = dlt.TranslationModel()  # Slow when you load it for the first time

@app.route('/translate', methods=['GET'])
def translate_text():
    # Get text and languages from query parameters
    text = request.args.get('text')
    source_lang = request.args.get('source_lang', 'en')  # Default to English if not specified
    target_lang = request.args.get('target_lang', 'en')  # Default to English if not specified

    # Perform translation
    if text:
        try:
            source = getattr(dlt.lang, source_lang.upper())
            target = getattr(dlt.lang, target_lang.upper())
            translated_text = mt.translate(text, source=source, target=target)
            return jsonify({"translated_text": translated_text})
        except AttributeError:
            return jsonify({"error": "Invalid source or target language"}), 400
    else:
        return jsonify({"error": "Text parameter is required"}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
