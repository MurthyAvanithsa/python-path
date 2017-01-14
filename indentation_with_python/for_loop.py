
# using range in for loop
for num in range(1, 10):
    '''
    block starts here
    everything under this indent level is the body of for loop
    '''
    print num

# inner blocks
# using range in for loop
for num in range(1, 10):
    '''
    block starts here
    everything under this indent level is the body of for loop
    '''
    if num%2==0:
        # this is a inner if block with in for loop
        print "even:{}".format(num)

# iterating through list
my_accounts = ["twitter.com/murthya",
               "facebook.com/murthya",
               "linkedin.com/murthya"]

for account in my_accounts:
    print account
