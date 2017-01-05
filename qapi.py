
import requests
from ireport import report
import _settings


class QuizletAPI(object):

    def __init__(self, token=_settings.QUIZLET_ACCESS_TOKEN):
        report("init quizletapi")
        self.access_token = token
        self.endpoint = "https://api.quizlet.com/2.0/"
        report("finished initialization")

    def create_set(self, title, terms, terms_language, definitions, definition_language):
        report("init create set")
        response = requests.post(self.endpoint + "sets", {
            "title": title,
            "terms[]": terms,
            "definitions[]": definitions,
            "lang_terms": terms_language,
            "lang_definitions": definition_language
        }, headers={
            'Authorization': 'Bearer ' + self.access_token
        })
        report(response.content)

    def retrieve_set_list(self, username):
        return requests.get(self.endpoint + username + "/sets").content