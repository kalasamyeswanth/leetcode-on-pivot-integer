#the pivot integer number logic
#enter a number n= 4
#sum of integers of (1-4) is 10 and (1-8) is 36
# square root of 10 is unkown number in floot and squar root of 36 is 6
# answer of 4 is -1 ans answer of 8 is 6
num = int(input('enter the number : '))
if(num>1):
    num1 = num//2
    for i in range(num1,num):
        if(sum(list(n for n in range(1,i+1)))) == (sum(list(n for n in range(i+1,num)))):
            print(i)
    else:
        print(-1)
elif num == 1:
    print('num is one ')
else:
    print('num is less than one ')




if(num > 1):
    num1 = num//2
    for i in range(num1,num):
        l1 = list(n for n in range(1,i+1))
        l2 = list(n for n in range(i,num))
        print(l1)
        print('sum of l1 first list is :',l1,'--->',sum(l1))
        print('l2')
        print('sum of l2 second list is : ',l2,'--->',sum(l2))
        print('-----------'*5)






#logic three
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        if(n > 1):
            n1 = n//2
            for i in range(n1,n):
                if(sum(list(n for n in range(1,i+1)))==sum(list(n for n in range(i,n+1)))):
                    return i
        elif(n == 1):
            return 1
        
        return -1
                




#logic one
sum_of_numbers = n * (n + 1) // 2
        square_root = int(sqrt(sum_of_numbers))
        return square_root if square_root * square_root == sum_of_numbers else -1




#logic two
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        
        for x in range(n):
            p=0
            k=0
            for i in range(x+1):
                p=p+i
            for j in range(x,n+1):
                k=k+j
            if p==k:
               return x
        return -1
