#!/usr/bin/env python3
"""
간단한 계산기 모듈
버전: 1.0.0
"""

class Calculator:
    """기본 산술 연산을 수행하는 계산기 클래스"""
    
    def add(self, a, b):
        """두 수를 더한다"""
        return a + b
    
    def subtract(self, a, b):
        """첫 번째 수에서 두 번째 수를 뺀다"""
        return a - b
    
    def multiply(self, a, b):
        """두 수를 곱한다"""
        return a * b
    
    def divide(self, a, b):
        """첫 번째 수를 두 번째 수로 나눈다"""
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다")
        return a / b
    
    def power(self, a, b):
        """a의 b제곱을 계산한다"""
        return a ** b
    
    def square_root(self, a):
        """제곱근을 계산한다"""
        if a < 0:
            raise ValueError("음수의 제곱근은 계산할 수 없습니다")
        return a ** 0.5
    
    def modulo(self, a, b):
        """a를 b로 나눈 나머지를 반환한다"""
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다")
        return a % b

if __name__ == "__main__":
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 2 = {calc.subtract(5, 2)}")
    print(f"4 * 3 = {calc.multiply(4, 3)}")
    print(f"10 / 2 = {calc.divide(10, 2)}")