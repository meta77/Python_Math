import math # 円周率をつかうため
import random

def gcd(a, b):
    """
    2つの整数 a, b の最大公約数 (GCD) をユークリッドの互除法で求める関数

    :param a: 整数
    :param b: 整数
    :return: a と b の最大公約数
    """
    while b != 0:  # b が 0 になるまで繰り返す
        a, b = b, a % b  # a を b に、b を a を b で割った余りに更新する
    return a  # b が 0 になったときの a が最大公約数

s = 0
num = 1

while num <= 10000000:
  a = random.randint(1,10000000)
  b = random.randint(1,10000000)
  if gcd(a,b) == 1: # 最大公約数が1のとき互いに素であると判定
    s += 1
  num += 1


print(s / num) # 実験値
print(6 / math.pi**2) # 理論値

