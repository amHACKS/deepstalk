## SmartScrapes
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mainakdeb/e_summit/blob/main/predict_personality.ipynb)
[![Binder](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/Mainakdeb/e_summit/blob/main/predict_personality.ipynb)

This project aims to predict the psychological traits of a person on the basis of his/her social media posts. It predicts the following traits:
- EXT - Extraversion
- OPN - Openness
- NEU - Neuorticism
- CON - Conscientiousness
- AGR - Agreeableness

## Setup ##
1. Clone the repository
```
git clone https://github.com/Mainakdeb/e_summit.git
```
2. Navigate to specific Directory 
```
cd e_summit
```
3. Install the requirements from requirements.txt file
``` python
pip install -r requirements.txt
```
## Usage ##
### 1.  Via Command line: ###  

   Add desired names in names.txt along with some keywords(Already some have been included).
   
   Run the command down below  
   
   ```
   python3 predict_type.py --testcase 7 --inputfile "names.txt"
   ```
   See the output using:
   ```
   cat predictions.txt
   ```
### 2. Run on Google Colab ###
   [Link to colab notebook](https://colab.research.google.com/github/Mainakdeb/e_summit/blob/main/predict_personality.ipynb)
   This notebook demostrates how our script works.

## Props! ##
1. Python
2. Socialreaper
3. SkLearn
4. MatplotLib
5. Pandas
6. GSearch Library

## Demos ##
### 1. Providing input through names.txt ###
![Screenshot from 2021-02-08 15-23-23](https://user-images.githubusercontent.com/53506835/107203684-bc447480-6a21-11eb-9655-0bb4d9e4d5f1.png)

### 2. Output of Personality predictions ###
![Screenshot from 2021-02-08 15-25-51](https://user-images.githubusercontent.com/53506835/107203908-075e8780-6a22-11eb-9934-cbc9054de2e4.png)

### 3. Visualized Report (in the colab notebook) ###
![Screenshot from 2021-02-08 15-29-07](https://github.com/Mainakdeb/e_summit/blob/main/images/chetan_bhagat_report_non_transparent.png)


## Tasks completed ##
|Done | Set Of Tasks   
| --|:---------------------------------------------------------------------------:|
| :heavy_check_mark: | Main file and/or other header files if used | 
| :heavy_check_mark: | The trained model |                                             
| :heavy_check_mark: | A Readme with instructions on how to run the code | 
| :heavy_check_mark: | A brief one page description of the methods used with proper citations |
| :heavy_check_mark: | Outcome Report |

## What's next? ##
- Completing personality prediction for linkedin profiles
- Providing a GUI for the project 
