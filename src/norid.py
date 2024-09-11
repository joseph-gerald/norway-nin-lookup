import tls_client

# Not even sure if all of these headers are necessary, but it works so I'm not changign it

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/jxl,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://pid.norid.no/personid/lookup',
    'Origin': 'https://pid.norid.no',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
}

class PIDNoridSession:
    def __init__(self, initiate_by_default = True, token = None) -> None:
        self.session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)
        self.session.headers = HEADERS

        if initiate_by_default:
            if token is None:
                raise ValueError("Token must be provided if initiate_by_default is True")
            self.initiate_session(token)

    def initiate_session(self, token):
        self.session.get("https://pid.norid.no/personid/lookup")

        self.session.post(
            'https://pid.norid.no/personid/check_terms',
            data={
            'accept_terms': '1',
            'command': 'Lag person-ID',
            }
        )
        
        self.session.post(
            'https://pid.norid.no/personid/check_captcha',
            data={
                'g-recaptcha-response': token,
            }
        )

    def lookup_person(self, first_name, middle_name, last_name, birth_number):
        response = self.session.post(
            'https://pid.norid.no/personid/lookup_do',
            data={
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'birth_number': birth_number,
                'command': 'Neste',
            }
        )

        response_text = response.text

        invalid = "Ugyldig fødselsnummer" in response_text

        return (not invalid, response.text)
