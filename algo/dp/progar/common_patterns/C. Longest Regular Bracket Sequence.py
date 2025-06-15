s = input()
st = [-1]  # Store indices instead of "("
highest_till_now = 0
count = 0

for index, i in enumerate(s):
    if i == "(":
        st.append(index)  # Store index of '('
    else:
        if st:
            st.pop()  # Pop last '(' index
            if st:
                present = index - st[-1]  # Length of valid substring
                if present > highest_till_now:
                    highest_till_now = present
                    count = 1  # Reset count
                elif present == highest_till_now:
                    count += 1
            else:
                st.append(index)  # Mark invalid position
        else:
            st.append(index)  # Mark invalid position

if highest_till_now == 0:
    count = 1  # If no valid sequence found, return (0,1)

print(highest_till_now, count)
