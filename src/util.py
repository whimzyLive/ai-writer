import os


def create_prompt(system_message, messages):
    prompt = system_message
    message_template = "\n<|im_start|>{}\n{}\n<|im_end|>"
    for message in messages:
        prompt += message_template.format(message['sender'], message['text'])
    prompt += "\n<|im_start|>assistant\n"
    return prompt


def read_topic_and_content(input_file):
    topic_title = os.path.splitext(input_file)[0]

    input_file_stream = open(input_file, 'r')
    topic_content = input_file_stream.read()

    print("....file read successful....")
    return {'topic_title': topic_title.replace('/', ' '), 'topic_content': topic_content}
