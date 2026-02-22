import math

W = 168
H = 64

W1 = 15
H1 = 20


W2 = 50
H2 = 50


W3 = 17
H3 = 29


W4 = 1000000000
H4 = 500000000


side_lenght = math.gcd(W,H)
side_lenght1 = math.gcd(W1,H1)
side_lenght2 = math.gcd(W2,H2)
side_lenght3 = math.gcd(W3,H3)
side_lenght4 = math.gcd(W4,H4)


number_of_squares = (W // side_lenght) * (H // side_lenght)
number_of_squares1 = (W1 // side_lenght1) * (H1 // side_lenght1)
number_of_squares2 = (W2 // side_lenght2) * (H2 // side_lenght2)
number_of_squares3 = (W3 // side_lenght3) * (H3 // side_lenght3)
number_of_squares4 = (W4 // side_lenght4) * (H4 // side_lenght4)


print("side_lenght =", side_lenght, "number_of_squares=", number_of_squares)
print("side_lenght1 =", side_lenght1, "number_of_squares1=", number_of_squares1)
print("side_lenght2 =", side_lenght2, "number_of_squares2=", number_of_squares2)
print("side_lenght3 =", side_lenght3, "number_of_squares3=", number_of_squares3)
print("side_lenght4 =", side_lenght4, "number_of_squares4=", number_of_squares4)
