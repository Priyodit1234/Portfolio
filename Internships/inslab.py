from tinyec import registry
import secrets
curve=registry.get_curve('brainpoolP256r1')

def comp_points(point):
    return hex(point.x)+hex(point.y%2)[2:]


def ecc_encryption_key(pubkey):
    ciphertext_privkey=secrets.randbelow(curve.field.n)
    ciphertext_pubkey=ciphertext_privkey*curve.g
    shared_key=pubkey*ciphertext_privkey
    return (shared_key,ciphertext_pubkey)

def ecc_decryption_key(privkey,ciphertext_pubkey):

    shared_key=ciphertext_pubkey*privkey
    return shared_key

privkey=secrets.randbelow(curve.field.n)
pubkey=privkey*curve.g
print("Private key:",hex(privkey))
print("Public key:",comp_points(pubkey))

(enck,ciphertext_pubkey)=ecc_decryption_key(pubkey)
print("Ciphertext Public Key:",comp_points(ciphertext_pubkey))
print("Encrypted key:",comp_points(enck))

deck=ecc_decryption_key(privkey,ciphertext_pubkey)
print("Decrypted text is:",comp_points(deck))