# Joseph Mitchell: 1/31/2025
# Code Generate Memory Initialization Statements for UART Debugging projects
#  I started this project because FPGA debugging was no longer feasible with logic analyzer
#  since the logic analyzer that I am using maxes out at 48 MHz and the niquist rate should be ~2x the frequency
# My goal is to use this for my current SD Memory project since it is taking off very fast
#  and requires an insightful aesthetically pleasing debug log for which commands succeeded and which ones failed
#  based off of the open source SD Memory specification document available.
# The goal of this python script is to take care of this repetitive task


# Step 1: Create a text document with the Title of the UART Debug log I wish to have sent to USB COM port
# Step 2: Open text file for reading

f = open("UARTmessageLog.txt","r")#UART Message Log text file for debug messages

# Step 3: Open another text file for case statement generation, since BRAM does not exist for Tang Primer 20K

f2 = open("UARTcaseStatementGen.txt","w")#UART case statement generation


# After completing these steps I should have a list of Memory Instatiations that I can access to write
#  any message I want to write through UART robustly

# ASCII Index Key from Verilog Module:
# [32,126] decimal range for printable characters ~80-90 so 7 bits for pointer...
# 41 still 6 bits now! Messages will be capital alphas, decimal digits, spaces, colons, underscores, square brackets
# I care about the decimal digits, space, and colon
# 0 ->  032 8'h20 -> ' '
# 1 ->  045 8'h2D -> _        Underscore is 2D, not 5F
# 2 ->  048 8'h30 -> 0
# 3 ->  049 8'h31 -> 1
# 4 ->  050 8'h32 -> 2
# 5 ->  051 8'h33 -> 3
# 6 ->  052 8'h34 -> 4
# 7 ->  053 8'h35 -> 5
# 8 ->  054 8'h36 -> 6
# 9 ->  055 8'h37 -> 7
# 10 -> 056 8'h38 -> 8
# 11 -> 057 8'h39 -> 9
# 12 -> 058 8'h3A -> :

# I care about the upper case alphas, square brackets, underscore
# 13 -> 065 8'h41 -> A
# 14 -> 066 8'h42 -> B
# 15 -> 067 8'h43 -> C
# 16 -> 068 8'h44 -> D
# 17 -> 069 8'h45 -> E
# 18 -> 070 8'h46 -> F
# 19 -> 071 8'h47 -> G
# 20 -> 072 8'h48 -> H
# 21 -> 073 8'h49 -> I
# 22 -> 074 8'h4A -> J
# 23 -> 075 8'h4B -> K
# 24 -> 076 8'h4C -> L
# 25 -> 077 8'h4D -> M
# 26 -> 078 8'h4E -> N
# 27 -> 079 8'h4F -> O
# 28 -> 080 8'h50 -> P
# 29 -> 081 8'h51 -> Q
# 30 -> 082 8'h52 -> R
# 31 -> 083 8'h53 -> S
# 32 -> 084 8'h54 -> T
# 33 -> 085 8'h55 -> U
# 34 -> 086 8'h56 -> V
# 35 -> 087 8'h57 -> W
# 36 -> 088 8'h58 -> X
# 37 -> 089 8'h59 -> Y
# 38 -> 090 8'h5A -> Z
# 39 -> 091 8'h5B -> [
# 40 -> 093 8'h5D -> ]

index = 0


lines = f.readlines()

string = ""

for line in lines:
 for char in line:
  if char == ' ':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"20") # SPACE
  elif char == '0':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"30") # Binary Digit 0
  elif char == '1':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"31") # Binary Digit 1
  elif char == '2':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"32") # Decimal Digits
  elif char == '3':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"33")
  elif char == '4':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"34")
  elif char == '5':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"35")
  elif char == '6':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"36") 
  elif char == '7':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"37")
  elif char == '8':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"38")
  elif char == '9':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"39")
  elif char == ':':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"3A")
  elif char == 'A':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"41")
  elif char == 'B':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"42")
  elif char == 'C':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"43")
  elif char == 'D':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"44")
  elif char == 'E':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"45")
  elif char == 'F':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"46")
  elif char == 'G':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"47")
  elif char == 'H':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"48")
  elif char == 'I':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"49")
  elif char == 'J':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"4A")
  elif char == 'K':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"4B")
  elif char == 'L':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"4C")
  elif char == 'M':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"4D")
  elif char == 'N':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"4E")
  elif char == 'O':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"4F")
  elif char == 'P':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"50")
  elif char == 'Q':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"51")
  elif char == 'R':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"52")
  elif char == 'S':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"53")
  elif char == 'T':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"54")
  elif char == 'U':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"55")
  elif char == 'V':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"56")
  elif char == 'W':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"57")
  elif char == 'X':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"58")
  elif char == 'Y':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"59")
  elif char == 'Z':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"5A")
  elif char == '[':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"5B")
  elif char == ']':
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"5D")
  else:# Must be an underscore
   string = "16'd%d: tx_str <= 8'h%s;\n" % (index,"2D")
  if char != '\n':
   f2.write(string)#Write the case statement entry to text file
  index = index + 1 #Point to next address

f.close()
f2.close()
