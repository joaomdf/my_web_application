import pytest

# """
# return list of predefined names plus name given
# Julia, Alice, Karim is predefined. when they pass the route Eddie gets added to returned string.
# assert response.status_code == 200
# """
# def test_returns_name_added(web_client):
#     response = web_client.get('/names?add=Eddie')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'

# def test_returns_different_name_added(web_client):
#     response = web_client.get('/names?add=Paul')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Paul'

# """
# if no name is added, return predefined list
# assert response.status_code == 200
# """
# def test_added_nothing(web_client):
#     response = web_client.get('/names?add')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Julia, Alice, Karim'

# """
# if no key or value is specified then status_code == 400,
# plus return error message "Bad request!"
# """
# def test_no_request(web_client):
#     response = web_client.get('/names')
#     assert response.status_code == 400
#     assert response.data.decode('utf-8') == 'Bad request!'

"""
return list of predefined names plus name given in alphabetical order
Julia, Alice, Karim is predefined. when they pass the route Eddie and Leo get added to returned string in the correct order.
assert response.status_code == 200
"""
def test_add_one_name_and_alphabetized(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

def test_add_more_than_one_name_and_alphabetized(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'

"""
if no name is added, return predefined alphabetised list
assert response.status_code == 200
"""
def test_no_name_return_alphabetized_preset_list(web_client):
    response = web_client.get('/names?add')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Julia, Karim'


"""
if no key or value is specified then status_code == 400,
plus return error message "Bad request!"
"""
def test_no_request_alphabetized(web_client):
    response = web_client.get('/names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Bad request!'