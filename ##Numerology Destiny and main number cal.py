##Numerology Destiny and main number calculator
numerology_map = {
    1: ["a","A","j","J","s","S"],
    2: ["b","B","k","K","t","T"],
    3: ["c","C","l","L","u","U"],
    4: ["d","D","m","M","v","V"],
    5: ["e","E","n","N","w","W"],
    6: ["f","F","o","O","x","X"],
    7: ["g","G","p","P","y","Y"],
    8: ["h","H","q","Q","z","Z"],
    9: ["i","I","r","R"],

}



class Calculate:
    

    def name_number_sum(self,name_number_list):
        total_sum = 0
        for j in name_number_list:
            total_sum = total_sum + j
        #print("NAME Number sum is ",total_sum)
        return total_sum

    def calculations(self,integer_number):    
        num = integer_number
        sum = 0
        sum_n = 0
        des = 0
        while(num>0):
            rem = num%10
            num = num- rem
            num = num/10
            sum = sum + rem
        
        if sum>10:
            sum_n=sum
            #print("Total cal is more than 10")
                    
            while (sum_n>0):
                r =sum_n%10
                sum_n = sum_n - r
                sum_n = sum_n/10
                des = des+r
                #print("DES")
                #print(des)
                #print("Sum_N = %f",sum_n)
                return des
        else:
            #print(sum)
            return sum
        pass
    def __init__(self, date, month, year,full_name):
        self.date = date
        self.month = month
        self.year = year
        self.radical_number = self.calculations(self.date)
        self.destiny_number = self.date + self.month + self.year
        self.full_name = full_name
        self.run()

    def Name_Number (self,full_name ):
        chars = [c for c in full_name if c!=" "]
        name_number_array = []
        #print(chars)

        for i in chars:
            #print("Crosschecking with map:", i)
            for number, letter in numerology_map.items():
                if i in letter:
                    #print("FOUND LETTER: ",i, "Its number is: ",number)
                    name_number_array.append(number)

        #print(name_number_array)
        name_sum = self.name_number_sum(name_number_array)
        name_sum = self.calculations(name_sum)
        #print("Sum of full name numbers are: ", name_sum)
        return name_sum

    def run(self):
        print("Your Name number by Numerology is: ",self.Name_Number(self.full_name))
        print("Your Destiny Number is: ",self.calculations(self.destiny_number))
        print("Your Radical Number is: ",self.radical_number)
        pass
def main():
    print("**********************Welcome to Numerology Calculator***********************\n")

    Candidate_Name = input("What is your full name? ")
    DOB_year = int(input("\nWhat year were you born? "))
    DOB_month = int(input("\nMonth? "))
    DOB_date = int(input("\nDate? "))

    a = Calculate(DOB_date,DOB_month,DOB_year,Candidate_Name)
    print("\n********************Thanks for using Numerology Calculator******************\n")


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\n⚡ Interrupted by user—shutting down.")