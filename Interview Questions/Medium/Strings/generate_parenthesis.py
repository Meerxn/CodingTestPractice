class Solution:

    '''
    This is Nick White's solution implmentation but i did it in Python as I was unable to see how to work with this
    ''' 
    def gpHelp(self,mx,posA,posB,OPT,curr):

        if (len(curr) == mx*2):
            OPT.append(curr)
            return
        else:
            if (posA < mx):
                self.gpHelp(mx,posA+1,posB,OPT,curr+"(")
            if (posB < posA):
                self.gpHelp(mx,posA,posB+1,OPT,curr+")")

        '''

        Main understanding:
        You start with a bottom approach and then we have choices 

        you either start a bracket here 
        ((( and keep starting until you can 

        or you either close if there is a valid open placed already 

        




        We are using a recurrence + memoization approach for this case 

        Subproblem: 
        OPT[i] = number of parenthesis combination for i
        OPT[3*2] is where we will have our answer 
        Recurrence
        GP(len,posA,posB,OPT) = { 
            Base Case: 

            if posA = 0 
            OPT[i] = "" + ( posA<max

            return currString // if stringLen = n*2



            Recursive Case: 

            We build our string by using an open
            OPT[i] = OPT[i-1] + "(" iff posA < maxpos
            or 
            OPT[i] = OPT[i-1] + ")" iff posB < posA




        }

        '''

    def generateParenthesis(self, n: int) -> List[str]:
        OPT = []
        mx = n
        posA = 0 
        posB = 0 
        curr=""
        self.gpHelp(mx,posA,posB,OPT,curr)
        return OPT





