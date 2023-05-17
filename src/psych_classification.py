# Importing packages
from transformers import pipeline
import pandas as pd
import numpy as np
import os
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

def pipeline_setup():
    classifier = pipeline("text-classification", 
                        model="j-hartmann/emotion-english-distilroberta-base", 
                        return_all_scores=False,
                        padding=True,
                        truncation=True # Some reports are too long, so we truncate them
                        ) # Only return the most likely label
    return classifier

def load_data():
    filename = os.path.join(os.getcwd(), "data", "df_python.csv") # load the data
    data = pd.read_csv(filename, encoding="ISO-8859-1")
    data = data.sample(n=3, random_state=42) ### TESTING ONLY, REMOVE THIS LINE
    return data

def perform_emotion_classification(data, classifier):
    emotion_classification = []
    count = 0
    
    print("[INFO]: Starting emotion classification of reports...")

    for report in data["report"]:
        report_data = classifier(report)
        report_emotion = report_data[0]["label"]
        emotion_classification.append(report_emotion)
        count += 1
        print("[INFO]: Done with report " + str(count) + " of " + str(len(data["title"])))
    
    # Add the emotion classification to the data
    data["emotion"] = emotion_classification
    
    # Save the new data as csv
    data.to_csv(os.path.join(os.getcwd(), "data", "df_python_emotion.csv"))

def plot_data(data):
    # Define list of emotions for ordering
    emotions = data["emotion"].unique().tolist()

    # Making plot with all data
    all_data_plot = sns.countplot(x="emotion", data=data, order = emotions)
    all_data_plot.set_title("Distribution of emotions in all psychedelic reports")
    all_data_plot.set_xlabel("Emotion")
    all_data_plot.set_ylabel("Count")
    all_data_fig = all_data_plot.get_figure()
    all_data_fig.savefig(os.path.join(os.getcwd(), "plots", "all_data_plot.png"))
    all_data_fig.clf()

def plot_individual_substances(data):
    # Define list of emotions for ordering
    emotions = data["emotion"].unique().tolist()
    substance_core = data["substance_core"].unique().tolist()
    
    # Plot with real news only
    for i in substance_core:
        data_subset = data[data["substance_core"] == i]
        separated_plot = sns.countplot(x="emotion", data=data_subset, order = emotions)
        separated_plot.set_title("Distribution of emotions in " + i + " reports")
        separated_plot.set_xlabel("Emotion")
        separated_plot.set_ylabel("Count")
        separated_fig = separated_plot.get_figure()
        separated_fig.savefig(os.path.join(os.getcwd(), "plots", i + "_plot.png"))
        separated_fig.clf()


def main(): # This is the main function that runs the program.
    classifier = pipeline_setup()
    data = load_data()
    perform_emotion_classification(data, classifier)
    print("[INFO]: Done with emotion classification of reports.")
    plot_data(data)
    plot_individual_substances(data)
    print("[INFO]: Plots saved to folder.")

if __name__ == "__main__":
    main()