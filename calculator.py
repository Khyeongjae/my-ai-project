#!/usr/bin/env python3
"""
간단한 계산기 모듈
버전: 1.1.0
"""

import statistics

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


class StatisticalCalculator(Calculator):
    """통계 기능이 추가된 고급 계산기 클래스"""
    
    def mean(self, numbers):
        """숫자 리스트의 평균을 계산한다"""
        if not numbers:
            raise ValueError("빈 리스트의 평균은 계산할 수 없습니다")
        return statistics.mean(numbers)
    
    def median(self, numbers):
        """숫자 리스트의 중앙값을 계산한다"""
        if not numbers:
            raise ValueError("빈 리스트의 중앙값은 계산할 수 없습니다")
        return statistics.median(numbers)
    
    def stdev(self, numbers):
        """숫자 리스트의 표준편차를 계산한다"""
        if len(numbers) < 2:
            raise ValueError("표준편차 계산에는 최소 2개의 값이 필요합니다")
        return statistics.stdev(numbers)
    
    def variance(self, numbers):
        """숫자 리스트의 분산을 계산한다"""
        if len(numbers) < 2:
            raise ValueError("분산 계산에는 최소 2개의 값이 필요합니다")
        return statistics.variance(numbers)

if __name__ == "__main__":
    calc = Calculator()
    print("=== 기본 계산기 기능 ===")
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 2 = {calc.subtract(5, 2)}")
    print(f"4 * 3 = {calc.multiply(4, 3)}")
    print(f"10 / 2 = {calc.divide(10, 2)}")
    
    stat_calc = StatisticalCalculator()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n=== 통계 계산기 기능 ===")
    print(f"평균: {stat_calc.mean(numbers)}")
    print(f"중앙값: {stat_calc.median(numbers)}")
    print(f"표준편차: {stat_calc.stdev(numbers):.2f}")
    print(f"분산: {stat_calc.variance(numbers):.2f}")