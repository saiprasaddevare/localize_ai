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

@app.route('/translate', methods=['POST'])
def bulk_translate():
    # Get text and languages from query parameters
    translate_data = request.json
    translate_data_duplicate = dict(translate_data)
    source_lang = request.args.get('source_lang', 'en')  # Default to English if not specified
    target_lang = request.args.get('target_lang', 'en')  # Default to English if not specified

    # Perform translation
    if translate_data:
        try:
            source = getattr(dlt.lang, source_lang.upper())
            target = getattr(dlt.lang, target_lang.upper())
            to_translate = list(translate_data.values())
            translate_keys = translate_data.keys()
            translated_data = mt.translate(to_translate, source=source, target=target)
            for key, translated_data in zip(translate_keys, translated_data):
                translate_data[key] = translated_data
            return jsonify({
                "source_lang": source_lang,
                "target_lang": target_lang,
                "original_data": translate_data_duplicate,
                "translated_data": translate_data
            })
        except AttributeError:
            return jsonify({"error": "Invalid source or target language"}), 400
    else:
        return jsonify({"error": "Text parameter is required"}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
