def KaratsubaMultiplication(a , b):
    
    n = max(len(str(a)),len(str(b)))
    if n <= 1:
        return a * b 
    else:
        
        half = n // 2
        
        x = a // (10 ** (half))
        y = a %  (10 ** (half))
        c = b // (10 ** (half))
        d = b %  (10 ** (half))
        
        xc = KaratsubaMultiplication(x, c)
        yd = KaratsubaMultiplication(y,d)
        xy = KaratsubaMultiplication(x+y, c+d) - xc - yd
        print(xy)
        
        summ =(xc * (10 ** (2*half)))+ (xy * (10 ** half)) + yd
        return (summ)

def Multiply_string(a, b):
	len1 = len(a)
	len2 = len(b)
	if len1 == 0 or len2 == 0:
		return "0"
    
	result = [0] * (len1 + len2)
	num1 = int(a.copy); num2 = int(b.copy)
    
	pos_n1 = 0
	pos_n2 = 0

	for i in range(len1 - 1, -1, -1): # This is to move from right to left
		carry = 0
		n1 = ord(num1[i]) - 48 #python doesnt support ascii so ord is used to generate number
		pos_n2 = 0
		for j in range(len2 - 1, -1, -1):
			n2 = ord(num2[j]) - 48
			summ = n1 * n2 + result[pos_n1 + pos_n2] + carry
			# Carry for next iteration
			carry = summ // 10
			result[pos_n1 + pos_n2] = summ % 10
			pos_n2 += 1
		if carry > 0:
			result[pos_n1 + pos_n2] += carry	
		pos_n1 += 1
	
	i = len(result) - 1
	while i >= 0 and result[i] == 0:
		i -= 1
	if i == -1:
		return "0"
	s = ""
	while (i >= 0):
		s += chr(result[i] + 48)
		i -= 1
	return s


def Multiply_integer(a,b):
 
    len1 = len(str(a))
    len2 = len(str(b))
    exponential  = 0
    counter  = 0
    result = [0] * (len1+len2)
    for i in range(len1- 1 , -1 , -1):
        carry = 0
        inner_exponential = 1
        sum_inner = 0
        n1 = (a % pow(10,exponential + 1))
        n1 = n1 % pow(10,counter)
        
        for j in range(len2 - 1, -1, -1):
            n2 = b % pow(10,inner_exponential)
            
            n2 = n2 % pow(10,exponential + 1)
            summ = (n1 * n2) + carry
            if summ < 10:
                sum_inner = sum_inner + summ * pow(10,inner_exponential)
                
                result.append(sum_inner)
                inner_exponential += 1
            else:
                carry = summ // 10
                sum_inner = sum_inner + summ * pow(10,inner_exponential)
                result.append(sum_inner)
                
                inner_exponential += 1
        
        exponential += 1
        counter += 1
    
    return str((sum(result) //10))

def Multiply_recursive(a , b):
    
    n = max(len(str(a)),len(str(b)))
    if n <= 1:
        return a * b 
    else:
        
        half = n // 2
        
        x = a // (10 ** (half))
        y= a %  (10 ** (half))
        c = b // (10 ** (half))
        d = b %  (10 ** (half))
        
        xc = Multiply_recursive(x, c)
        yd = Multiply_recursive(y,d)
        xd = Multiply_recursive(x,d)
        yc = Multiply_recursive(y,c)
        
        summ =( xc * (10 ** (2*half)) )+ ((xd+yc) * (10 ** half)) + yd
        return summ

#print(Multiply_recursive(142123, 353620))
def is_hex(num):
    
    for i in num:
       
        if ((i < '0' or i > '9') and (i < 'A' or i > 'F')):
            #is_check = False
            return False
        
    return True

def is_binary(num):
    for i in num:
        if i !='0' and i != '1':
            return False
    return True


def binary_mul(bin_one,bin_two):
    
    idx = 0
    summ = []
    bin_prod = 0
    remainder = 0
    
    while bin_one != 0 or bin_two != 0:
        #iterative_prod = ((bin_one % 10) + (bin_two % 10)) / 2
        iterative_prod = ((bin_one % 10) + (bin_two % 10) + remainder)% 2
        #summ.insert(idx + 1,iterative_prod)
        #print(summ.insert(idx + 1,iterative_prod))
        summ.insert(idx,iterative_prod)
        remainder = int( ((bin_one % 10) + (bin_two % 10) + remainder) / 2)
        #remainder = int( ((bin_one % 10) + (bin_two % 10) + remainder) % 2)
        bin_one = int(bin_one / 10)
        bin_two = int(bin_two / 10)
        idx +=1
    
    if remainder != 0:
        summ.insert(idx,remainder)
        idx += 1
    idx -= 1
    
    while idx >= 0:
        bin_prod = (bin_prod * 10) + summ[idx]
        idx -= 1
    
    return bin_prod


def Multiply2(x,y):
    if is_binary((x))==False or is_binary((y)) == False :
        return
    
    x = int(x)
    y = int(y)
    bin_sum = 0
    fcr = 1
    while y != 0:
        dig = y % 10
        
        if dig == 1:
            x = x * fcr
            #print(x)
            bin_sum = binary_mul(x, bin_sum)
            #print(bin_sum)
        else:
            x = x * fcr
        
        y = int(y / 10)
        fcr = 10
    return str(bin_sum)


    
def Multiply16(x,y): #5B1
    if is_hex(x) == False or is_hex(y) == False:
        return
    
    len1 = len(x)
    len2 = len(y)
    
    pos_n1 = 0
    pos_n2 = 0
    
    x = int(x,16)
    y = int(y,16)
    
    x = str(x)
    y = str(y)
    
    final = [0] * (len1+len2)
         
    for i in range(len1 - 1, -1, -1):
        carry = 0
        #positional_arg = 0
        #sum_inner = 0
        n1 = ord(x[i]) - 48
        pos_n2 = 0
        
        for j in range(len2 - 1, -1,-1):
            n2 = ord(y[j]) - 48
            summ = (n1 * n2) + final[pos_n1 + pos_n2] + carry
            carry = summ // 16
            final[pos_n1 + pos_n2] = summ % 16
            pos_n2 += 1
        if carry > 0:
            final[pos_n1 + pos_n2] = carry
        pos_n1 += 1
    for i in range(0,len(final)):
        if final[i] >= 0:
            final[i] = hex(final[i])
    
    
    return str(final)

if __name__=='__main__':
    
    x = int(input('Enter Number 1: '))
    y = int(input('Enter Number 2: '))
    print(KaratsubaMultiplication(x,y))