import sys
import logging

logging.basicConfig(filename='sample.log',
                    level=logging.DEBUG,
                    format="%(asctime)s %(levelname)-10s  %(filename)6s  %(message)s",
                    )


crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)


# Создать регистратор верхнего уровня с именем 'app'
app_log = logging.getLogger('app')
app_log.setLevel(logging.INFO)
app_log.addHandler(crit_hand)


# app_log.debug(' This is DEBUG msg ')
# app_log.info(' This is INFO msg ')
# # app_log.warning(' This is WARNING msg ')
# # app_log.error(' This is ERROR msg ')
# app_log.critical(' This is CRITICAL msg ')
