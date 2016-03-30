data_earlier.txt is made suitable for further processing by fixing some omissions which creped in when the reviews were earlier classified into positive and negative 
and a new file named data.txt is created sorting out these flaws.

For example take a review in data_earlier.txt and we will look at the omissions:
+Great phone It is a wonderful phone. I recently upgraded>> from 4S to 5S. The difference has been "immense". First of all, it  is a larger> display compared to 4S 
and secondly the Memory is 16GB. Touch support is pretty awesome. It is quite fast  also. So happy with the upgrade.

In order to remove the stop words and unnecessary punctuation (which include full stops) from the above reviews, all symbols and words in each of the review must 
be separated by at least one space to be treated as seperated entitied to enable the removal of stop words.But in the above review,this condition doesn't hold.

So at least a gap of one space should be maintained between all the words which includes all possible punctuation.

The above review after sorting out looks like this:

+ Great phone It is a wonderful phone . I recently upgraded  >  >  from 4S to 5S . The difference has been " immense " . First of all , it  is a larger > display compared to 4S and secondly the Memory is 16GB . Touch support is pretty awesome . It is quite fast  also . So happy with the upgrade .

In a similar way all the reviews are updated with the help of microsoft word,searching for punctuation and replacing them appropriately and a new text file named
data.txt is created









