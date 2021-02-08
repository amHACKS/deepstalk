## SmartScrapes
Predicting the personality of the user based on their social activity. This project uses 6 parameters for measuring the personality of a user.
- EXT - Extraversion
- OPN - Openness
- NEU - Neuorticism
- CON - Conscientiousness
- AGR - Agreeableness

## Setup ##
1. Clone the project
```
git clone https://github.com/Mainakdeb/e_summit.git
```
2. Go to specific Directory 
```
cd e_summit
```
3. Install the requirements from / requirements.txt file
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
   Link for collab


## Demos ##
### 1. Providing input through names.txt ###
![Screenshot from 2021-02-08 15-23-23](https://user-images.githubusercontent.com/53506835/107203684-bc447480-6a21-11eb-9655-0bb4d9e4d5f1.png)

### 2. Output of Personality predictions ###
![Screenshot from 2021-02-08 15-25-51](https://user-images.githubusercontent.com/53506835/107203908-075e8780-6a22-11eb-9934-cbc9054de2e4.png)

### 3. An insight into prediction (in the colab notebook)###
![Screenshot from 2021-02-08 15-29-07](https://user-images.githubusercontent.com/53506835/107204242-6fad6900-6a22-11eb-8f95-dc1a209bc1e5.png)


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
