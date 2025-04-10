import random
from prometheus_client import start_http_server, Counter, Gauge
import time

REQUEST_COUNTER = Counter('http_requests_total', 'Total HTTP Requests')
TEMPERATURE_GAUGE = Gauge('temperature_celsius', 'Current Temperature')

if __name__ == '__main__':
    start_http_server(9091)
    print("Сервер метрик запущено на порту 9091")

    while True:
        REQUEST_COUNTER.inc()
        TEMPERATURE_GAUGE.set(round(random.uniform(10, 40), 1))
        time.sleep(1)