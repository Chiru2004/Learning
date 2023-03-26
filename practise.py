def nroot(n,m):
    if n>0:
     return n**(1/m)
    else:
     return (-n)**(1/m)
import cryptography.fernet    
from cryptography.fernet import Fernet   
def sym_encrypt(str):
  key=Fernet.generate_key()
  fernet=Fernet(key)
  code=fernet.encrypt(str.encode())
  print(f"Ercrypted message {code}")
  comb=[key,code]
  return comb
def sym_decrypt(str,key):
  fernet=Fernet(key)
  code=fernet.decrypt(str)
  print(f"The decoded string is {code}")  