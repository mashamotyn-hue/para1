import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="para8_3_logs.log",
                    filemode="w",
                    format="we a\hame logging massafgrg: %(asctime)s%(levelname)s - %(message)s"
                    )
try:
    print(10/0)
except Exception:
    logging.exception("Exception")
    