ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
        "nineteen"]
tens = [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def english_number(n):
    if n < 20:
        return ones[n]
    elif 20 <= n < 100 and n % 10 == 0:
        return tens[n//10]
    elif 20 < n < 100:
        return tens[n//10] + "-" + ones[n % 10]
    elif 100 <= n <= 900 and n % 100 == 0:
        return ones[n//100] + " hundred"
    elif 100 < n < 1000:
        return ones[n//100] + " hundred and" + english_number(n % 100)
    elif n == 1000:
        return "one thousand"
    
i = 1000
count = 0
for j in range(i):
    words = english_number(j+1).replace(" ", "").replace("-","")
    count += len(words)

print(count)