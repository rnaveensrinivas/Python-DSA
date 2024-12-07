class Fraction: 
	def __init__(self,top,bottom):

		if not isinstance(top, int):
			raise TypeError(f"Numerator must be an integer. Provided {type(top)}")
		if not isinstance(bottom, int):
			raise TypeError(f"Denominator must be an integer. Provided {type(bottom)}")
		
		# we don't want negative denominators.
		if bottom < 0:
			if top < 0:
				top, bottom = abs(top), abs(bottom)
			else:
				top *= -1
		
		common = self.gcd(top, bottom)
		self.num = top // common
		self.den = bottom // common
        
	def show(self) -> None:
		print(self.num, '/', self.den)

	def __str__(self) -> str:
		return f"{self.num}/{self.den}"
	
	def gcd(self, a, b):
		while b:
			a, b = b, a%b
		return a
	
	def __add__(self, other):
		new_num = self.num * other.den + other.num * self.den
		new_den = self.den * other.den
		return Fraction(new_num, new_den)
	
	def __sub__(self, other):
		new_num = self.num * other.den - other.num * self.den
		new_den = self.den * other.den
		return Fraction(new_num, new_den)
	
	def __mul__(self, other):
		new_num = self.num * other.num
		new_den = self.den * other.den
		common = self.gcd(new_num, new_den)
		return Fraction(new_num, new_den)
	
	def __truediv__(self, other):
		new_num = self.num * other.den
		new_den = self.den * other.num
		common = self.gcd(new_num, new_den)
		return Fraction(new_num, new_den)
	
	def __eq__(self, other: object) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num == second_num
	
	def __ne__(self, other: object) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num != second_num
	
	def __lt__(self, other) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num < second_num
		
	def __gt__(self, other) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num > second_num
	
	def __le__(self, other) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num <= second_num
		
	def __ge__(self, other) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num >= second_num
	
	def get_num(self) -> int:
		return self.num
    
	def get_den(self) -> int:
		return self.den
        
f1 = Fraction(1,4)
f2 = Fraction(2,4)
print(f"{f1} + {f2}: {f1+f2}")
print(f"{f1} - {f2}: {f1-f2}")
print(f"{f1} / {f2}: {f1/f2}")
print(f"{f1} * {f2}: {f1*f2}")
print(f"{f1} == {f2}: {f1==f2}")
print(f"{f1} >= {f2}: {f1>=f2}")
print(f"{f1} <= {f2}: {f1<=f2}")
print(f"{f1} < {f2}: {f1<f2}")
print(f"{f1} > {f2}: {f1>f2}")