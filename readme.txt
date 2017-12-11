COMS 4705 HW4

To train the model, just using the script below:
python src/parser.py
The default version is for part3. To disable the dropout, we should add a second parameter (False) to the build_graph() function in the train() function defined in network.py
All other parameters could be changed from the parser option.

Part1:
Unlabeled attachment score 84.33
Labeled attachment score 81.12

Part2:
Unlabeled attachment score 83.75
Labeled attachment score 80.65

Reason for the changes:
I have discussed with TA Mohammad, and he said it was possible for the accuracy to be lower for part2 than part1. From my point of view, the reason why the accuracy drops a little may be that there is a overfitting problem when training the model.

Part3:
Variations:
I use dropout with probability 0.5 after hidden layer1 and hidden layer2. Also, I change the dimension of POS embedding and Dependency embedding to 64 for both.
The result for Part3:
Unlabeled attachment score 85.18
Labeled attachment score 82.05
There is a significant improvement for Part3 compared to Part1 and Part2. The reason why I change the model in this way is that as the model may have the overfitting problem, dropout is a way to avoid it. What's more, increasing the dimension of the embedding means that the embedding will contain more information from the original label, so the result may be more accurate.