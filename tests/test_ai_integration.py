import unittest.mock as mock
from app.services.ai_service import generate_response

def test_ai_mock_call():
    payload = {'prompt': 'Hello'}
    mock_response = mock.MagicMock()
    mock_response.json.return_value = {'result': 'Hi there'}
    
    with mock.patch('requests.post', return_value=mock_response) as m:
        res = generate_response(payload)
        m.assert_called_once()
        assert res == 'Hi there'

def test_ai_failure_handling():
    with mock.patch('requests.post', side_effect=Exception('Network Error')):
        res = generate_response({'prompt': 'fail'})
        assert res is None
