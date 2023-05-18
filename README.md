<br />
  <h1 align="center">Assignment 5: Emotion classification of psychedelic trip reports</h1> 
  <h2 align="center">Cultural Data Science, 2023</h2> 
  <h3 align="center">
  Author: Aleksander Moeslund Wael <br>
  Student no. 202005192
  </h3>
</p>

---

## About the project
This repo contains code for conducting emotion classification on a large text dataset. The goal of this project is to analyze the emotion of retrospectively written psychedelic trip reports to further understand the subjective experience of psychedelic states. Emotion classification is performed on all reports using a pretrained language model. The overall emotion present in the corpus and the differences between psychedelic substances is analyzed and discussed.

### Data
The dataset used for this project was originally obtained for use in the author's bachelor project, *Comparing subjective psychedelic experiences across substances using the BERTopic model* (Wael, 2023). It consists of reports obtained from the [Erowid Experience Vaults](https://erowid.org/experiences/), which collects and publishes people's experiences with psychoactive plants and chemicals. There are approximately 39,000 reports in the vaults, covering experiences with about 950 substances. Each report includes a title, author, substance type, and the writer's experience. Some reports provide additional information such as dose, body weight, route of administration, year of experience, gender, and age. Reports must be approved by at least two members of the Erowid Reviewing Crew to be included. The data was collected by scraping the report site, focusing on the title, substance, and report. Combination substances were excluded, and pseudonymous handles and personal information were not collected to comply with GDPR regulations. The final dataset includes 4,219 reports describing experiences with LSD, psilocybin, mescaline, Ayahuasca, DMT, and 2C-B.

### Model
The model used for the emotion classification task is the `j-hartmann/emotion-english-distilroberta-base` transformer model from the HuggingFace platform (Jochen Hartmann, "Emotion English DistilRoBERTa-base". [HuggingFace link](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/), 2022). The model is a finetuned version of the `distilroberta-base` model. It predicts Ekman's 6 basic emotions plus a neutral class: `anger`, `disgust`, `fear`, `joy`, `neutral`, `sadness` and `surprise`.

### Pipeline
1. Imports necessary packages
2. Set up a text classification pipeline
3. Load data
4. Classify emotions in reports
5. Save classifications in the `df_python_emotion.csv` file
5. Create a plot showing the distribution of emotions in all reports
6. Create plots for each substance's reports
7. Save plots to `plots` folder

## Requirements

The code is tested on Python 3.11.2. Futhermore, if your OS is not UNIX-based, a bash-compatible terminal is required for running shell scripts (such as Git for Windows).

## Usage

The repo was setup to work with Windows (the WIN_ files), MacOS and Linux (the MACL_ files).

### 1. Clone repository to desired directory

```bash
git clone https://github.com/alekswael/assignment-5---self-assigned-project
cd assignment-5---self-assigned-project
```
### 2. Run setup script 
**NOTE:** Depending on your OS, run either `WIN_setup.sh` or `MACL_setup.sh`.

The setup script does the following:
1. Creates a virtual environment for the project
2. Activates the virtual environment
3. Installs the correct versions of the packages required
5. Deactivates the virtual environment

```bash
bash WIN_setup.sh
```

### 3. Run pipeline
**NOTE:** Depending on your OS, run either `WIN_run.sh` or `MACL_run.sh`.

Run the `*run.sh` script. The script does the following:
1. Activates the virtual environment
2. Runs `emotion_classification.py` located in the `src` folder
3. Deactivates the virtual environment

```bash
bash WIN_run.sh
```

## Repository structure
This repository has the following structure:
```
│   .gitignore
│   MACL_run.sh
│   MACL_setup.sh
│   README.md
│   requirements.txt
│   WIN_run.sh
│   WIN_setup.sh
│   
├───data
│       df_python.csv
│       df_python_emotion.csv # WITH EMOTION CLASSIFICATIONS
│
├───plots
│       all_data_plot.png 
│       multi_plot.png
│
└───src
        psych_classification.py
```

## Remark on findings

![all](plots/all_data_plot.png)



![2c-b](plots/multi_plot.png)

