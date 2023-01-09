
euros = int(input('What do you have left in euro? '))
corona_danesa = int(input('What do you have left in corona? '))
won = int(input('What do you have left in won? '))

total = euros * 1.07 + corona_danesa * 0.14 + won * 0.00080

print(total)