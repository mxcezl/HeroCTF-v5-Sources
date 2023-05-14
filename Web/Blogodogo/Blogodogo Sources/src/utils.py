from datetime import datetime
from random import seed, randbytes

epoch_secret_post_created = 1683946380
timestamp_list = [1683946380 + n for n in range(60)]

def generate_hash(timestamp=None):
    """Generate hash for post preview."""
    if timestamp:
        seed(timestamp)
    else:
        #print(int(datetime.now().timestamp()))
        seed(int(datetime.now().timestamp()))

    return randbytes(32).hex()

#generate_hash()

for timestamp in timestamp_list:
    print(generate_hash(timestamp))
    pass