class Matrix:
    def __init__(self,lst):
        self.elements=lst

    def isMatrix(self):
        """"This method returns True or False on the basis of
          the given object """
        if all(isinstance(x, (int, str)) for x in self.elements):
            for element in self.elements:
                gaps=0
                if element!='/n':
                    gaps+=1
                return True
            for i in range(len(0,len(self.elements),gaps)):
                count=0
                if self.elements[i]=='/n':
                    count+=1
            #improve the logic...

        else:
            return False
        

    def Order(self):
        """This method returns the order of the matrix in a form of a string and
             Hits none when the given object is not a matrix"""
        proceed=self.isMatrix()
        if proceed:
            coulumns=0
            row=0
            flag='GREEN'
            for element in self.elements:
                if element!='/n' and flag=='GREEN':
                    coulumns+=1
                elif element=='/n':
                    flag='RED'
                    row+=1
                order=f"{row}x{coulumns}"
            return order
        else:
           return None
                

matrix1 = Matrix([29,23,'/n',23,53,'/n',34,64,'/n'])
order=matrix1.Order()
print("Order of the matrix is: ",order)