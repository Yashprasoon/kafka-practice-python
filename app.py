from flask import Flask, jsonify, request
import consumer
import producer

app = Flask(__name__)

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    topic = data.get('topic')
    message = data.get('message')
    
    if topic and message:
        producer.send_message(topic, message)
        return jsonify({'status': 'Message sent successfully'})
    else:
        return jsonify({'error': 'Invalid request. Please provide topic and message.'}), 400

@app.route('/consume-messages', methods=['POST'])
def consume_message():
    data = request.get_json()
    topic = data.get('topic')
    
    if topic:
        consumer.consume_messages(topic)
        return jsonify({'status': 'Consuming messages'})
    else:
        return jsonify({'error': 'Invalid request. Please provide a topic.'}), 400

if __name__ == '__main__':
    app.run(debug=True)