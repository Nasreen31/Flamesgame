# Flamesgame

# Introduction 

1. This flames calculator assesses and predicts the outcome of a relationship based on an algorithm of two given names using Python.

2. It is a fun filled love calculator to test the status of your love relationship between him/her based on the FLAMES game.

3. FLAMES stands for - Friends, Lover, Affection, Marriage, Enemy, Siblings.

![flames page](https://user-images.githubusercontent.com/117984168/225402598-f392e175-5fab-4a27-a32f-8cb870eba5df.jpeg)

# Flow Chart
[flow chart.docx](https://github.com/Nasreen31/Flamesgame/files/10984177/flow.chart.docx)



# How to play

The flames calculator is based on quite a simple algorithm in which FLAMES stands for:

■ Friendship;

■ Love;

■ Affection;

■ Marriage;

■ Enemy;

■ Siblings.

# Example:

1. Enter your Name : John

![flames page1](https://user-images.githubusercontent.com/117984168/225430124-c685962e-a1e7-4c45-b246-5a2fdde72df6.jpeg)

2. Enter your Crush Name : Sophie

![flames page2](https://user-images.githubusercontent.com/117984168/225430287-a90d0d80-c38c-4232-8791-06eba957ab7a.jpeg)

3. Press Enter 

4. Result will be John and Sophie, You both are cute couples

![flames page3](https://user-images.githubusercontent.com/117984168/225430360-1d614167-802a-4783-a35c-10efc17cada7.jpeg)

5. Play Again.

# Logic Formula

flames = ["F", "L", "A", "M", "E", "S"]

while len(flames) > 1:
formula = d % len(flames) - 1
if formula >= 0:
before = flames[formula + 1:]
after = flames[:formula]
flames = before + after
else:
flames = flames[:len(flames) - 1]




