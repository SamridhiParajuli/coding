"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

"""

Month : dict[str,int] = {
    "january": 2200,
    "february": 2350,
    "march": 2600,
    "April": 2130,
    "may": 2190
} 

# how much extra spent on feb compared to jan

print(f'the amount spent more on february is:{Month["february"]-Month["january"]}');


# expense on first 3 months of year 

print(Month["january"]+Month["february"]+Month["march"])



for i,j in Month.items():
    if j in Month ==[2000]:
        print("yes");

print("no");

month = [2200,2350,2600,2130,2190]


for i in month:
    if(i==2000):
        print("true")

print("no")


#  June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

Month["June"] = 1980

print(Month)


# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

Month["April"] = Month["April"] - 200
print(Month)


    