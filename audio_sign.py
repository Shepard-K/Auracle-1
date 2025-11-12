# pip install pydub eth-account
from pydub import AudioSegment
from eth_account import Account
import hashlib, time, json, sys

SAMPLE_MS = 1000
acct      = Account.create()   # demo key – new each run

def slice_hash(path):
    audio = AudioSegment.from_file(path)
    chunks = [audio[i:i+SAMPLE_MS] for i in range(0, len(audio), SAMPLE_MS)]
    out = []
    for n, chunk in enumerate(chunks):
        raw = chunk.raw_data
        h   = hashlib.sha256(raw).hexdigest()
        msg = f"{n}:{h}:{int(time.time())}"
        sig = acct.sign_message(msg).signature.hex()
        out.append({"chunk":n,"hash":h,"ts":int(time.time()),"sig":sig,"addr":acct.address})
    return out

if __name__ == "__main__":
    data = slice_hash(sys.argv[1])
    print(json.dumps(data, indent=2))
