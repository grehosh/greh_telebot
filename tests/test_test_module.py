from sheldon import SheldonTest
from time import time

message = {
    "text": '!test',
    "time": time(),
    "sender_id": 1,
    "sender_type": None,
    "user_id": 1
}
bot = SheldonTest('en')
bot.load_modules()


def test_module_in_loaded_modules():
    assert 'test' in bot.loaded_modules


def test_getting_answer():
    bot.parse_message(message)
    assert bot.sent_messages[-1]['message_text'] == "Test completed. Message: '!test'"


def test_getting_answer_with_wrong_cmd():
    message['text'] = '!table'
    bot.parse_message(message)
    assert bot.sent_messages[-1]['message_text'] != "Test completed. Message: '!table'"
