from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Curve:
    """
    Elliptic Curve over the field of integers modulo a prime.
    Points on the curve satisfy y^2 = x^3 + a*x + b (mod p).
    """
    p: int
    a: int
    b: int

@dataclass
class Point:
    """ An integer point (x,y) on a Curve """
    curve: Curve
    x: int
    y: int

@dataclass
class Generator:
    """
    A generator over a curve: an inial point and the (pre-computed) order
    """
    G: Point
    n: int

bitcoin_curve = Curve(
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    a = 0x0000000000000000000000000000000000000000000000000000000000000000, # a = 0
    b = 0x0000000000000000000000000000000000000000000000000000000000000007, # b = 7
)

#楕円曲線上に開始地点としてGenerator pointを設定し、secp256k1ではGenerator pointは公開されている。このgenerator pointからランダムウォークを行い。
G = Point(
    bitcoin_curve,
    x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    y = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
)

bitcoin_gen = Generator(
    G = G,
    # the order of G is known and can be mathematically derived
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,
)


# pで割った余りが0になっている
print("Generator IS on the Curve: ", (G.y**2 - G.x**3 - 7) % bitcoin_curve.p == 0)

import random
random.seed(1337)
x = random.randrange(0, bitcoin_curve.p)
y = random.randrange(0, bitcoin_curve.p)
print("Totally random point is not: ", (y**2 - x**3 - 7) % bitcoin_curve.p == 0)

secret_key = int.from_bytes(b'Andrej is cool :P', 'big')
assert 1 <= secret_key < bitcoin_gen.n
print(secret_key)