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


### Data


### Model
The model used for the emotion classification task is the `j-hartmann/emotion-english-distilroberta-base` transformer model from the HuggingFace platform (Jochen Hartmann, "Emotion English DistilRoBERTa-base". [HuggingFace link](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/), 2022). The model is a finetuned version of the `distilroberta-base` model. It predicts Ekman's 6 basic emotions plus a neutral class: `anger`, `disgust`, `fear`, `joy`, `neutral`, `sadness` and `surprise`.

### Pipeline


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

```

## Remark on findings

