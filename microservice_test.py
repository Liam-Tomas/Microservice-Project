from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/installed_programs', methods=['GET'])
def get_installed_programs():
    acknowledgment = {'message': "Microservice 'install programs' reached successfully"}
    return jsonify(acknowledgment)


@app.route('/uninstall_programs', methods=['POST'])
def uninstall_programs():
    programs_to_uninstall = request.json['programs_to_uninstall']
    acknowledgment = {'message': 'Microservice reached successfully'}
    return jsonify(acknowledgment)


if __name__ == '__main__':
    app.run(debug=True)
