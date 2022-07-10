ciphertext_bytes=bytes.fromhex('bdaf6ce0')

# ascii range: 0 - 126

key_candidates=[]

def result_reqs(result_tuple):
    """
        check for common requirements of english text
    """

    key_bytes, pl = result_tuple

    if pl[0] < 65 or pl[1] < 65:
        return False

    if pl[0] > 122 or pl[1] > 122:
        return False

    return True

def is_special_char(c):

    if c < 65 or c > 122 or (90 <  c < 97):
        return True
    else:
        return False


for i in range(256):
    c1=i ^ ciphertext_bytes[0]
    if not is_special_char(c1):
        for j in range(256):
            c2=j ^ ciphertext_bytes[1]
            if not is_special_char(c2):
                for n in range(256):
                    c3=n ^ ciphertext_bytes[2]
                    if not is_special_char(c3):
                        for m in range(256):
                            c4=m ^ ciphertext_bytes[3]
                            if not is_special_char(c4):
                                res=([hex(i),hex(j),hex(n),hex(m)], [c1,c2,c3,c4])

                                if result_reqs(res):
                                    key_candidates.append(res)
                                    print(str([hex(i),hex(j),hex(n),hex(m)]) + "| -->  " + ''.join([chr(s) for s in [c1,c2,c3,c4]]))



