import argparse

parser = argparse.ArgumentParser()

# define your arguments
parser.add_argument("-n1",
                    help="Provide number one",
                    default=10,
                    type=int,
                    dest="n1")

parser.add_argument("-n2",
                    help="Provide number two",
                    default=20,
                    type=int,
                    dest="n2")

parser.add_argument('-nvalues',
                    nargs='+',
                    type=int,
                    help="send email to only these emails",
                    dest="nvalues",
                    default=[])

arguments = parser.parse_args()

print "N1 is : {}".format(arguments.n1)

print "N2 is : {}".format(arguments.n2)

print "emails is : {}".format(arguments.nvalues)


total_sum = arguments.n1+arguments.n2
for num in arguments.nvalues:
    total_sum += num

print "Added:{}".format(total_sum)




