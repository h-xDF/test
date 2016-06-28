with open("dataset_24465_4.txt") as date, open("test1.txt","w") as w:
     for line in reversed(date.readlines()):
         w.write(line)
