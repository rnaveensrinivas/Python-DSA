class Fraction: 
    
	def __init__(self, top, bottom):

		# Programming Exercies
		# Question 5. Modify the constructor for the fraction class so that it 
  		# checks to make sure that the numerator and denominator are both 
    	# integers. If either is not an integer the constructor  should raise 
     	# an exception.
		if not isinstance(top, int):
			raise TypeError(f"Numerator must be an integer." + 
                   "Provided {type(top)}")
		if not isinstance(bottom, int):
			raise TypeError(f"Denominator must be an integer." + 
                   "Provided {type(bottom)}")
		

		# Programming Exercises
		# Question 6. In the definition of fractions we assumed that negative 
  		# fractions have a negative numerator and a positive denominator. 
    	# Using a negative denominator would cause some of the relational 
     	# operators to give incorrect results. In general, this is an 
      	# unnecessary constraint. Modify the constructor to allow the user to 
       	# pass a negative denominator so that all of the operators continue 
        # to work properly. 
		if bottom < 0:
			if top < 0:
				top, bottom = abs(top), abs(bottom)
			else:
				top *= -1
		# Question 6. ----
		
		# Programming Exercises
		# Question 2. In many ways it would be better if all fractions were 
  		# maintained in lowest terms right from the start. Modify the 
    	# constructor for the Fraction class so that GCD is used to  reduce 
     	# fractions immediately. Notice that this means the __add__ function 
      	# no longer  needs to reduce. Make the necessary modifications.
		common = self.gcd(top, bottom)
		self.num = top // common
		self.den = bottom // common
		# Question 2. ----
        
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
	
	# Programming Exercise
	# Question 3. Implement the remaining simple arithmetic operators 
 	# (__sub__, __mul__, and __truediv__).
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
	# Question 3. ----
	
	def __eq__(self, other: object) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num == second_num
	
	# Programming Exercises
	# Question 4.  Implement the remaining relational operators 
 	# (__gt__, __ge__, __lt__, __le__, and __ne__)
	def __gt__(self, other) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num > second_num

	def __ge__(self, other) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num >= second_num

	def __lt__(self, other) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num < second_num
	
	def __le__(self, other) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num <= second_num

	def __ne__(self, other: object) -> bool:
		first_num = self.num * other.den
		second_num = other.num * self.den
		return first_num != second_num
	# Question 4. ---- 
	
	# Programming Exercises
	# Question 1. Implement the simple methods get_num and get_den that will 
 	# return the numerator and denominator of a fraction.
	def get_num(self) -> int:
		return self.num
    
	def get_den(self) -> int:
		return self.den
	# Question 1. ----
 
	# Programming Exercies
	# Question 7. Research the __radd__ method. How does it differ from 
 	# __add__? When is it used? Implement __radd__.
	def __radd__(self, other):
		return self.__add__(other)
	# Question 7. ----

	# Question 8. Repeat the last question but this time consider 
 	# the __iadd__ method.
	def __iadd__(self, other):
		return self.__add__(other)
	# Question 8. ----
 
	def __isub__(self, other):
		return self.__sub__(other)

	def __mul__(self, other):
		return self.__mul__(other)
	
	def __truediv__(self, other):
		return self.__truediv__(other)

	# Question 9. Research the __repr__ method. How does it differ from 
 	# __str__? When is it used?  Implement __repr__.
	def __repr__(self):
		return f"Fraction(num='{self.num}', den='{self.den}')"
	# Question 9. ----
        
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
f1 += f2
print(f"{f1} += {f2}: {f1}")
