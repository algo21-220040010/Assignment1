# Assignment1
This paper introduce different ways to decide the direction of trade and design a specify way for chinese market. In this assignment, i replicate the traditional mehtod mentioned in this paper. The chinese version method is not yet finished.
traditional method:1.Tick rule 2.quote rule
# Tick rule
By comparing the current midpoint of the quoted price with the closing price, a transaction that trades above the quoted price is considered a buy, otherwise a sell
# Quote rule
The quote rule compares the transaction price of the last transaction. If the transaction price is greater than the last transaction price, it is regarded as a buy; if the transaction price is less than the last transaction, it is regarded as a sell; if the transaction price is flat with the last transaction, it will continue the trading direction of the last transaction.

# code
This code is dealing with the 2015IF data and the trade direction is assign as a column in dataset. In the following assignment i will use this dataset to replicate other high frequent trade paper.
