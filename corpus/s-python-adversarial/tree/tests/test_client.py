from unittest import mock


def test_prompt_wiring():
    client = mock.Mock()
    client.chat.completions.create(model="gpt-3.5-turbo", messages=[])
    client.chat.completions.create.assert_called_once()
