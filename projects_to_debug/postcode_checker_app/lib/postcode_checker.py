import re

class PostcodeChecker():
    def check(self, postcode):
        if re.match(r"^[a-z]{1,2}\d[a-z\d]?\s*\d[a-z]{2}$",postcode, re.IGNORECASE) is not None:
            return True
        else:
            return False