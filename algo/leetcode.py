import webbrowser
import random
head='https://leetcode.com/problems/'
with open('ratings.txt','r') as file:
    q=[]
    for index,line in enumerate(file):
        if index==0:
            continue
        temp= line.strip().split("\t")
        temp[0]=float(temp[0])
        #store all questions whose rating is from 2000 to 2050

        if 2000<=temp[0]<=2200:
            q.append((temp[2],temp[0]))
#q=[('Minimum Number of Days to Eat N Oranges', 2048.0976546787), ('Make Lexicographically Smallest Array by Swapping Elements', 2047.3919190727), ('Find the Number of Subarrays Where Boundary Elements Are Maximum', 2046.2618466463), ('Collecting Chocolates', 2043.1015779104), ('Put Marbles in Bags', 2042.4005521254), ('Maximum Number of Events That Can Be Attended II', 2040.5621123027), ('Find the Longest Substring Containing Vowels in Even Counts', 2040.539289037), ('Ugly Number III', 2039.110874689), ('Make Sum Divisible by P', 2038.8592725467), ('Check if a Parentheses String Can Be Valid', 2037.6527962599), ('Maximum Trailing Zeros in a Cornered Path', 2036.7410194704), ('Tweet Counts Per Frequency', 2036.7206020719), ('Stone Game II', 2034.9740902393), ('Minimum Difficulty of a Job Schedule', 2034.9420578559), ('Most Stones Removed with Same Row or Column', 2034.6759416871), ('Count Unique Characters of All Substrings of a Given String', 2034.4067304341), ('Earliest Possible Day of Full Bloom', 2033.4597721985), ('Total Appeal of A String', 2033.1699277531), ('Constrained Subsequence Sum', 2032.4773038683), ('Minimum Increment Operations to Make Array Beautiful', 2030.922770301), ('Number of Pairs Satisfying Inequality', 2030.1021023033), ('Apply Operations to Make All Array Elements Equal to Zero', 2029.4024513478), ('Divide Chocolate', 2029.1301557536), ('Maximum Frequency Stack', 2027.8772739639), ('Minimum Distance to Type a Word Using Two Fingers', 2027.7304121046), ('Best Team With No Conflicts', 2027.3839266711), ('Stone Game III', 2026.8957817007), ('Digit Count in Range', 2025.1529365814), ('IP to CIDR', 2025.0377429311), ('Decode XORed Permutation', 2024.3797833173), ('The Number of Beautiful Subsets', 2023.4303440211), ('Maximum Profit in Job Scheduling', 2022.8520613737), ('Minimum Moves to Reach Target with Rotations', 2022.4752963768), ('Number of Flowers in Full Bloom', 2022.3137128296), ('Maximum White Tiles Covered by a Carpet', 2021.7790710467), ('Special Permutations', 2020.7095306378), ('Maximum Tastiness of Candy Basket', 2020.6775180586), ('Find the Number of Ways to Place People II', 2020.1846215023), ('Minimum Cost to Split an Array', 2019.9859462755), ('Snakes and Ladders', 2019.5399647546), ('Find Beautiful Indices in the Given Array II', 2016.2085876254), ('Maximum Number of Events That Can Be Attended', 2015.7291888336), ('Construct Target Array With Multiple Sums', 2014.7655493665), ('Filling Bookcase Shelves', 2014.2979320644), ('Maximum Number of Non-overlapping Palindrome Substrings', 2013.4354344791), ('Minimum Amount of Damage Dealt to Bob', 2012.8694334235), ('Minimum Fuel Cost to Report to the Capital', 2011.9703133514), ('Path With Maximum Minimum Value', 2011.3542735398), ('Minimum Sum of Squared Difference', 2011.0496162515), ('Decoded String at Index', 2010.5524756946), ('Minimize the Difference Between Target and Chosen Elements', 2009.7322365973), ('Dice Roll Simulation', 2008.40650791), ('Minimum Number of Flips to Make the Binary String Alternating', 2005.5862669078), ('Minimum Cost to Make Array Equal', 2005.3737929084), ('Minimum Degree of a Connected Trio in a Graph', 2005.2755755378), ('Sum Game', 2004.5346526204), ('Find All People With Secret', 2003.5794613668), ('Minimum Moves to Spread Stones Over Grid', 2001.4515854273), ('Number of Increasing Paths in a Grid', 2001.2074132383), ('Stone Game VI', 2000.8441804448), ('Online Election', 2000.8021428612)]

print(len(q))
r=random.randint(0, len(q) - 1)
x=''
for i in q[r][0].split():
    x+=i
    x+='-'
webbrowser.open(head+x[:-1])
print(q[r][1])


