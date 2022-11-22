# Moduuli 13. {"Number":31, "isPrime":true}

from flask import Flask, request

app = Flask(__name__)


@app.route("/summa")
def primenumber():
    args = request.args
    luku = int(args.get("luku1"))
    isPrime = False

    if luku > 1:
        for i in range(2, luku):
            if (luku % i) == 0:
                isPrime = True
            else:
                isPrime = True

    vastaus = {
        "Number": luku,
        "isPrime": isPrime
    }
    return vastaus


app.run(use_reloader=True, host="127.0.0.1", port=3000)

# http://127.0.0.1:3000/summa?luku1=13&luku2=28 -> Toimii
# http://127.0.0.1:3000/summa (???????????????) -> Ei toimi???

"""
def test_prime(n):
    if (n==1):
    return False

    elif (n==2): # Ei tarvii
    return True; # Ei tarvii

    else:
    for x in range(2,n):
    if(n % x==0):

    return False
    return True

    print(test_prime(9))
"""