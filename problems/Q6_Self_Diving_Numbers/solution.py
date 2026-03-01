class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sdv = []
        for num in range(left,right+1):
            divisible = True
            num_str = str(num)
            if '0' not in num_str:
                if len(num_str)==1:
                    sdv +=[num]
                else:
                    for elm in num_str:
                        if num%int(elm)==0:
                            divisible = divisible & True
                        else:
                            divisible = divisible & False
                    if divisible:
                        sdv+=[num]
        return sdv

