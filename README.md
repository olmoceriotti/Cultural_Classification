# BERT&ERNIE MNLP Homework 1
For a better understanding of the project scope, refer to the [report](BERT_ERNIE_report.pdf).  

The directory contains the following files:

- NoLM_method.ipynb
- LM_method.ipynb
- Bert&Ernie_output_model_NoLM.csv
- Bert&Ernie_output_model_LM.csv
- BERT_ERNIE_report.pdf

The two .csv files contain the test dataset with our added labels, generated directly by the code present in the two notebooks.
The folders present in this directory contain all the data needed to run the two notebooks. 
In the data folder, we stored all the complete wikipedia texts for all the entry in the dataset, divided in train, validation and test, all the features extracted from wikidata for the NoLM method, in a .pkl file, and the unlabeled test set needed to rerun the results generation. We also include the script used to fetch the wikipedia files in the additional_files folder.
To run the tests, both notebooks provide two separate ways:
The first one, is to rerun all the code until the Standalone Evaluation chapter, re-training all models and using the newly trained model to make the predictions and label the test set.
The second one it to run the Setup, Dataset and Standalone Evaluation Chapter resulting in setting up the environment and dataset and using the models we pretrained on our own.
As present in the report file, we used Colab Pro with its A100 GPU and T4 GPU, yielding slighlty different results, in favor of the former.
In regards of the style of our code, we tried to keep the structure as readable and clear as possible. To avoid using comments, not practical while running the code, we used a fair amount of printing statements, to keep the developer running the code informed on the status of the process.

## Important notes
-  For the LM based method, the T4 GPU can't be used to perform training since it's not powerful enough. To run the notebooks without re-training the embeddings model is sufficient to skip the section with title: "Embedding model fine-tuning" and simply run the next block, that will load the model from drive.
-  To properly see the folder mounted in the "MyDrive" directory, is necessary to create a shortcut from the MyShared folder and give all the authorizations when drive is mounted in the script.
-  The warnings when pip install is ran are not to be listened to.
