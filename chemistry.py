class MassFraction:

    def __init__(self, wi=float(0), mi=float(0), mtot=float(0)):
        """This class allows you to calculate the values related to the mass fraction of an object.
        - wi = mass fraction
        - mi = mass
        - mtot = total mass
        """

        self.wi = float(wi) #mass fraction
        self.mi = float(mi) #mass
        self.mtot = float(mtot) #total mass


    #Formula for Fraction Mass: wi = mi/mtot

    def calculate(self):
        massfraction = self.mi/self.mtot
        return massfraction
    
    def cmass(self):
        mass = self.wi * self.mtot
        return mass
    
    def ctmass(self):
        totalmass = self.mi / self.wi
        return totalmass
    


class MolarMass:

    def __init__(self, M=float(0), m=float(0), n=float(0)):
        """This class allows you to calculate the values related to the molar mass of a substance.
        - M = molar mass
        - m = mass
        - n = number of moles
        """

        self.M = float(M) #molar mass
        self.m = float(m) #mass
        self.n = float(n) #number of moles


    #Formula for Molar Mass: M = m/n

    def calculate(self):
        molarmass = self.m / self.n
        return molarmass
    
    def cmass(self):
        mass = self.M * self.n
        return mass
    
    def cn(self):
        number_of_moles = self.m / self.M
        return number_of_moles
    

class MassIP:
        
    def welcome_message(self):
            
            print("")
            print("Chemistry Interaction Program!")
            print("")
            print("This program allows you to calculate")
            print("Mass Fraction and Molar Mass.")
            print("1 for Mass Fraction calculations. ")
            print("2 for Molar Mass calculations.")


    def run(self):
            
            choice = int(input("(1 or 2): "))

            if choice == 1:
                print("")
                print("Mass Fraction Calculations")
                print("Select the variable you want to calculate:")
                print("0. To understand the variables!")
                print("1. Mass Fraction (wi)")
                print("2. Mass (mi)")
                print("3. Total Mass (mtot)")

                mf_choice = int(input("(0, 1, 2, or 3): "))
                if mf_choice == 0:
                    print("")
                    print("Variable explanations:")
                    print("Mass Fraction: In chemistry, the mass fraction of a substance within a mixture is the ratio of the mass of that substance to the total mass.")
                    print("Mass: Mass is a measure of the amount of matter in a substance or an object. The basic SI unit for mass is the kilogram (kg), but smaller masses may be measured in grams (g).")
                    print("Total Mass: Total mass refers to the combined mass of all components in a system or mixture.")
                    print("The formulas used are as follows:")
                    print("Mass Fraction: wi = mi/mtot")

                    
                elif mf_choice == 1:
                    print("Enter the mass")
                    mi = float(input("(mi): "))
                    print("Enter the total mass")
                    mtot = float(input("(mtot): "))
                    mf = MassFraction(mi=mi, mtot=mtot)
                    print("Mass Fraction (wi) =", mf.calculate()) ##

                elif mf_choice == 2:
                    print("Enter the mass fraction")
                    wi = float(input("(wi): "))
                    print("Enter the total mass")
                    mtot = float(input("(mtot): "))
                    mf = MassFraction(wi=wi, mtot=mtot)
                    print("Mass (mi) =", mf.cmass()) ##

                elif mf_choice == 3:
                    print("Enter the mass fraction")
                    wi = float(input("(wi): "))
                    print("Enter the mass")
                    mi = float(input("(mi): "))
                    mf = MassFraction(wi=wi, mi=mi)
                    print("Total Mass (mtot) =", mf.ctmass())

                else:
                    print("Invalid choice.")
            
            elif choice == 2:
                print("")
                print("Molar Mass Calculations")
                print("Select the variable you want to calculate:")
                print("0. To understand the variables!")
                print("1. Molar Mass (M)")
                print("2. Mass (m)")
                print("3. Number of Moles (n)")

                mm_choice = int(input("(0, 1, 2, or 3): "))
                if mm_choice == 0:
                    print("")
                    print("Variable explanations:")
                    print("Mole: One mole of a substance is equal to 6.022 * 10^23 units of that substance (such as atoms, molecules, or ions).")
                    print("Molar Mass: Molar mass can be defined as 'mass per mole. ' In other words, molar mass is the sum of the mass of all the atoms found in one mole's worth of a substance. g/mol")
                    print("Mass: Mass is a measure of the amount of matter in a substance or an object. The basic SI unit for mass is the kilogram (kg), but smaller masses may be measured in grams (g).")
                    print("Number of Moles: The number of moles of a substance equals the ratio of its given mass in a chemical reaction to the mass of one mole of that substance.")
                    print("The formulas used are as follows:")
                    print("Molar Mass: M = m/n")

                elif mm_choice == 1:
                    print("Enter the mass")
                    m = float(input("(m): "))
                    print("Enter the number of moles")
                    n = float(input("(n): "))
                    mm = MolarMass(m=m, n=n)
                    print("Molar Mass (M) =", mm.calculate())

                elif mm_choice == 2:
                    print("Enter the molar mass")
                    M = float(input("(M): "))
                    print("Enter the number of moles")
                    n = float(input("(n): "))
                    mm = MolarMass(M=M, n=n)
                    print("Mass (m) =", mm.cmass())

                elif mm_choice == 3:
                    print("Enter the molar mass")
                    M = float(input("(M): "))
                    print("Enter the mass")
                    m = float(input("(m): "))
                    mm = MolarMass(M=M, m=m)
                    print("Number of Moles (n) =", mm.cn())
                else:
                    print("Invalid choice.")



def run_interaction_program():

    
    program = MassIP()
    program.welcome_message()
    program.run()
    print("Thank you for using the Chemistry Interaction Program. Goodbye!")
           
run_interaction_program()