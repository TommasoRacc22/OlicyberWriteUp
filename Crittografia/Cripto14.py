from Crypto.Hash import SHA3_384, SHA224, HMAC
from Crypto.PublicKey import DSA
import binascii


a = "hash_me_pls"

h = SHA3_384.new()
h.update(a.encode())
print("Prima domanda: " , h.hexdigest())



mess = "La mia integrità è importante!"
mess = mess.encode() 
chiave = bytes.fromhex('fb07694ab62941553efff9b0f92f9c8a153997eaa851483f09f44b3863b8ff23')

h = HMAC.new(chiave, digestmod=SHA224)
h.update(mess)

print(f"HMAC (Hex): {h.hexdigest()}")



hex_key = '3082025d0201003082023606072a8648ce380401308202290282010100f102d97fb367d4edcea2a54786bd096e41bd13b77f035c525afb49d7350416e9217008e2ee3445de58c6eb53a46ccf5f6f50404ffd3168bfbbe762925bcf3313a3effa11f33d2c1fb6cc1968c6bf06c4ca7ab5f63c6aace22b403846ca4313857a7f485c7ed97021e65294447054df672ea986810463eb7aeb3618118ca6cb63473239c4d025b212cccd5be4bc0af48e4196694be1503489646978b1b46f13f4942761a05b6d4896d4b96a525ce1f93b77e9a71de1327fdb8d01b5b382757ed41d285914af0fe05dc09f0271f80ac81a0fa7c6a775f241bd259e9397c689344c71775e9bb451047148300326a6c601b188859f91cd8eea8f25def63ff42b714d021d00f17ab6be52515f2211a57b716d55d495a81b487d70bd55664be81daf028201010080010b64d116ea7a3f11bc620df1068384a85a6bb18c23b35f1ac638a6011474ac86f02a07ccb0543975270a1b18666be87b885be04eef8ad0e0d4cfcd5be58975d1e973f4b47a426c03fb87a1314325ff72bbceb7a3fd6461423f2f4070ab4e245fd38ee6a3e3e414bb5913a63849369692dfeaf0c40335784f96eac7cce74ebac9a96a14c795e0892f6b0156d50cd0644565254cd84d5d9876b2516111f7df580e20e5ca835d754d16ba26cc39a4df34b3eaafa186fde1b2b4e8bfac5122a6c925b2d06ba7a7d83ba8f8ee9770593b89ba81f234eac26c709a880eb52975bee346201f951df70f998eb09f46b115e410ed4ae8ad8e3ae42cf382915e41b71a041e021c4d3f7430273b3ae73f9a2bfcbe631eec11f378da4bef9562621e465a'

key_bytes = binascii.unhexlify(hex_key)

dsa_key = DSA.import_key(key_bytes)

p_valore = dsa_key.p

print(f"Il valore di p è:\n{p_valore}")
print(f"Valore x (Chiave Privata): {dsa_key.x}")
print(f"Valore y (Chiave Pubblica): {dsa_key.y}")
print(f"Valore di q: ", dsa_key.q)
print(f"Valore di g: ", dsa_key.g)




from Crypto.Util import number

# Specifichiamo la lunghezza in bit
bit_length = 1230

# Genera un numero primo forte di quella lunghezza
primo = number.getPrime(bit_length)

print(f"Bit length: {primo.bit_length()}")
print(f"Valore: {primo}")