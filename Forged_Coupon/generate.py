from zmq.utils import z85
from datetime import datetime

PERCENT = "99"

now = datetime.now()
unencoded = now.strftime('%B')[:3].upper()
year = now.year
unencoded += str(year)[2:] + "-" + PERCENT
encoded = z85.encode(unencoded.encode()).decode()
print("Generated key: " + encoded)
