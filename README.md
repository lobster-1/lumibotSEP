Report for Assignment 1 

Members: 

Abhigya Anand 
_Ishaan Iyer
 

1) 

Name: LumiBot 

 

URL: Lumiwealth/lumibot: Backtesting and Trading Bots Made Easy for Crypto, Stocks, Options, Futures, FOREX and more (github.com) 

 

Number of lines of code and the tool used to count it: 357,561 

 

Programming language: Python 

 

2) Coverage measurement 

 

Inform the name of the existing tool that was executed and how it was executed: 

We use Coverage.py.  Following 3 commands were used coverage run; coverage report; and coverage html 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Show the coverage results provided by the existing tool with a screenshot 

 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/3b5ftucq.png)
 

 

 

3) 

Our own coverage tool 

 

 

<Group member name> 

Abhigya Anand 


 



Function 1 name 

def check_positive(input, type, custom_message="", strict=False): 

Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements 

Update types.py to analyse checkquantity and checkpositive · lobster-1/lumibotSEP@4222cdd (github.com) 

 

Provide a screenshot of the coverage results output by the instrumentation 

 
 ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/2pgnmd1k.png)
 

![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/d34ma13a.png)
 

 

The function was called with different parameters to make sure all of the branches are hit. If we only call it once only some of the branches will be hit 

 

Function 2 name: check_price(price, custom_message="", nullable=True): 

 

Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements 

Update types.py hidden branches added (else) · lobster-1/lumibotSEP@8250d37 (github.com) 

 

 

 

Provide a screenshot of the coverage results output by the instrumentation 
 
  ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/2pgnmd1k.png)
 ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/2pgnmd1k.png)
 

The function was called with different parameters to make sure all of the branches are hit. If we only call it once only some of the branches will be hit 

Member name: 
Ishaan Iyer 

Function 1 name 

Check_numerical() 

Commit: 
Update types.py added analyses for check_numerical and check_price · lobster-1/lumibotSEP@6ab6eb8 (github.com) 

Screenshot: 

  ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/2pgnmd1k.png)
   ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/2pgnmd1k.png)

Function 2 

Check_price() 

Commit: Update types.py added analyses for check_numerical and check_price · lobster-1/lumibotSEP@6ab6eb8 (github.com) 

  ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/2pgnmd1k.png)
 ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/2pgnmd1k.png)
Note that all the 4 functions were in lumibot/tools/types.py so have the same image for branch analysis 

 

4)Coverage improvement 

         

Group member name: Abhigya Anand 

 

 

 

Test 1 

Check_quantity() 

 

Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test 

Create test_numerical_check,py · lobster-1/lumibotSEP@857126c (github.com) 

 

Provide a screenshot of the old coverage results (the same as you already showed above): 

 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/htbtk0fy.png)
 

 

 

Provide a screenshot of the new coverage results 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/gaubqlii.png)
 

 

State the coverage improvement with a number and elaborate on why the coverage is improved: As we can see in the old coverage html report the lines in the red indicate the uncovered statements. By adding the new tests we were able to cover all the statements/branches of the function and also the hidden else branch. Since none of the branches were fully covered earlier, the improvement is of 100% 

 

 

Test 2 

Check_positive() 

Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test 

https://github.com/lobster-1/lumibotSEP/commit/857126cbb0c37c533571549cd0334375452f4f9c 

 

Provide a screenshot of the old coverage results  

 ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/qlcstpvn.png)

 

 

Screenshot of the new coverage results: 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/fptigixu.png)


 
Improvement: 

Out of the 4 branches in check_positive(including the hidden else) only 2 of them are covered by original tests. By adding our test we were able to cover all the 4 branches.  

Total branch coverage for that function now is 100% and improvement is 2x (from 2 to 4) 

 

Group member: Ishaan Iyer 

Test for check_price 

Commit: https://github.com/lobster-1/lumibotSEP/commit/857126cbb0c37c533571549cd0334375452f4f9c 

 

Old Screenshot 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/551qrqiq.png)
 

New coverage screenshot: 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/qhq535hb.png)
Improvement: Old tests only covered 50% of the branches while our added tests cover 100% of the branches. This puts the improvement at 2 times. 

Test for check_numerical() 

Commit: https://github.com/lobster-1/lumibotSEP/commit/857126cbb0c37c533571549cd0334375452f4f9c 

 

Old screenshot: 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/3qck5qm3.png)

New screenshot: 
 ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/irtkklm2.png)

Improvement: 

We were able to cover 5/6 branches with our new tests putting the new coverage at 83.33. Compared to only 3/6 branches covered with the original tests. This puts the improvement at 1.66 times 

 

5) Overall 

 

Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above) 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/fbkx0w53.png)
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/y41hj5rc.png)
 

Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group 

 

 
![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/ziyu2xup.png)

 ![image](https://github.com/lobster-1/lumibotSEP/blob/dev/Report%20for%20Assignment%201.md/ztnfznxy.png)
Improvement; 

It improved the overall statement coverage from 42.08% to 42.36% across all the files and more importantly from 52.7 % to 94.21% for the file in which our functions were chosen from 

 Statement of individual contributions 

 

Write what each group member did 

Abhigya found the repository even though both Ishaan and Abhigya searched for several ones before finding the chosen one. Ishaan counted the lines of code via the Tokei tool. Abhigya analysed 2 functions and wrote the tests for them and Ishaan also did the same for the other 2 functions. Abhigya did the coverage report and inital coverage while Ishaan analysed the html to search for appropriate functions to analyze. 

Overall it was a team effort by Ishaan and Abhigya as there were only 2 students working and 1 student was removed. 

 
