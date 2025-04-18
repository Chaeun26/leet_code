class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        '''
        mobile moneypot monitor mouse mousepad

        m -> mobile, moneypot, monitor
        mo -> mobile, moneypot, monitor
        mou -> mouse, mousepad
        mous -> mouse, mousepad
        mouse -> mouse, mousepad

        idx=bisect_left(products, m, 0)

        '''
        # Mlog(M)+nlog(M)

        products.sort() # o(Mlog(M))
        start =0
        res=[]
        prefix=""
        for letter in searchWord:#o(N)
            prefix+=letter

            idx=bisect_left(products, prefix, start)#o(log(M))
            tmp=[]
            for i in range(idx, min(idx+3, len(products))):
                if products[i].startswith(prefix):
                    tmp.append(products[i])
                else:
                    break
            res.append(tmp)
            start = idx

        return res

        '''
        mobile moneypot monitor mouse mousepad
        start=3
        mouse idx=3
        tmp=[mouse, mousepad]
        res=[[mobile, moneypot, monitor], [mobile, moneypot, monitor], [mouse, mousepad], [mouse, mousepad], [mouse, mousepad]]


        m - o - b - i - l - e - end
               - n - e- y -p -o - t - end
                   - i - t - o - r - end
              - u - s - e - end
                          - p - a - d - end

        m:{o:{n:{e:{}, i:{}}}}

        '''