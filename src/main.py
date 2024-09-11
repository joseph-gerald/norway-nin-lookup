import capsolver as capsolver
import norid as norid
import yaml
import logging
import coloredlogs

with open("config.yaml", "r") as f: config = yaml.safe_load(f)

coloredlogs.install(level='INFO', fmt='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)


CAPSOLVER_KEY = config["CAPSOLVER_KEY"]
SITE_KEY = "6LfV4cESAAAAACtmONOTo1ImuFurAFvAqHhflUhx"

capsolver = capsolver.Capsolver(CAPSOLVER_KEY)

def lookup_persons(first_name, middle_name, last_name, national_ids):
    recap_token = capsolver.solve_recap_v2(SITE_KEY, "https://pid.norid.no")["gRecaptchaResponse"]
    norid_session = norid.PIDNoridSession(token=recap_token)

    for national_id in national_ids:
        res = norid_session.lookup_person(first_name, middle_name, last_name, national_id)
        logging.info(national_id, res[0])

lookup_persons("Ola", "Nordmann", "Nordmannsen", ["01010112345", "01010112346", "01010112347"])
 