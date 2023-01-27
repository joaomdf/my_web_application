# User story
This route should return a list of pre-defined names (Julia, Alice, Karim) plus the names given.

# Route signature
GET /names?add=<string of names>
    method - GET
    function - get_add_name()
    add - parameter - string of text with names


# Test examples
"""
return list of predefined names plus name given
Julia, Alice, Karim is predefined. when they pass the route Eddie gets added to returned string.
assert response.status_code == 200
"""

"""
if no name is added, return predefined list
assert response.status_code == 200
"""

"""
return list of predefined names plus name given in alphabetical order
Julia, Alice, Karim is predefined. when they pass the route Eddie and Leo get added to returned string in the correct order.
assert response.status_code == 200
"""

"""
if no name is added, return predefined alphabetised list
assert response.status_code == 200
"""