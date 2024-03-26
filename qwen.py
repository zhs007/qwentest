from http import HTTPStatus
import dashscope


def call_with_messages():
    plugins = {'pdf_extracter': {}}  # choose the desired plugin(s).
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': [
                    {'text': '总结文档'},
                    {'file': 'https://chatbot2.oss-cn-beijing.aliyuncs.com/slotcraft.pdf'}]
                 }]
    response = dashscope.Generation.call(
        model='qwen-plus',
        messages=messages,
        result_format='message',  # set the result to be 'message' format.
        plugins=plugins,
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    call_with_messages()