![SmishingTool](/img1.png)
# SmishingTool
A tool to do phishing over SMS. This uses free API from fast2sms to send SMS having ngrok tunnel which leads to phishing pages over flask. 

## Execution 
![installing](/execution.gif)
* The scenario is picked from the `scenario.txt` file; you can add any other scenario but to keep the name of the victim include `[NAME]` in the proper location. 
* The victim details are put in the `targets.xlsx` file. Do not need to add country code it is automatically picked by fast2sms api.
* The targets.xlsx contains two columns Name and Number(without the column names), edit it as per your target details. Do not add country code. The api will take care of it.
* The flask application is runing on the `port-5000` in a seperate thread and the ngrok tunnel run directly as a child process. If you have a paid version of ngrok then use it to get a White CNAME to make the URL more authentic. 


## How to Install
1. Make a free account in fast2sms
2. get the api token and put in the token variable
3. install python3
4. run the following commands 
>cd <path_to_folder>/SmishingTool
>
>pip3 install -r requirements.txt
>
>In the smishingTool.py, change the value opf token to your fast2sms api key.
![installing](/install.gif)



