# 

# **Module 10 \- Advanced Python Tools**

---

**Assignment 1 \- Working with NumPy**

**Objective** Understand the basics of NumPy, array creation, and manipulation.

**Instructions** 

**Step 1** Install NumPy using  
**pip install numpy**

**Step 2 Create a new Python script numpy\_assignment.ipynb.** Import NumPy and follow these steps:  

1\. Create a 1D NumPy array with integers from 1 to 20\. Perform the following operations:    
  a. Calculate the sum, mean, median, and standard deviation of the elements in the array.    
  b. Find the indices of elements greater than 10 in the array.  

2\. Create a 2D NumPy array of shape 4 X 4 with numbers ranging from 1 to 16\.    
  a. Print the array.    
  b. Find the transpose of the array.    
  c. Calculate the row-wise and column-wise sums of the array.  

3\. Create two 3 X 3 arrays filled with random integers between 1 and 20\.    
  a. Perform element-wise addition, subtraction, and multiplication.    
  b. Compute the dot product of the two arrays.  

4\. Reshape a 1D array of size 12 into a 3 X 4 2D array and slice the first two rows and last two columns.  

---

**Assignment 2 \- Working with Pandas**

**Objective** Learn to create and manipulate dataframes for data analysis.  

**Instructions**

**Step 1** Install Pandas using**:**  
**pip install pandas**

**Step 2** Create a new Python script **pandas\_assignment.ipynb.** Import Pandas and follow these steps:  

**1\.** Create a DataFrame with the following data:    
  

  **data \= {**  
      **'Name': \['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'\],**  
      **'Age': \[24, 27, 22, 32, 29\],**  
      **'Department': \['HR', 'Finance', 'IT', 'Marketing', 'HR'\],**  
      **'Salary': \[45000, 54000, 50000, 62000, 47000\]**  
  **}**  
  a. Print the first five rows of the DataFrame.    
  b. Get the summary statistics of the 'Age' and 'Salary' columns.    
  c. Calculate the average salary of employees in the 'HR' department.  

2\. Add a new column, 'Bonus', which is 10% of the salary.  

3\. Filter the DataFrame to show employees aged between 25 and 30\.  

4\. Group the data by 'Department' and calculate the average salary for each department.  

5\. Sort the DataFrame by 'Salary' in ascending order and save the result to a new CSV file.  

---

**Assignment 3 \- Working with Matplotlib**

**Objective** Practice data visualization techniques for better data representation.  

**Instructions** 

**Step 1** Install Matplotlib using:  
**pip install matplotlib**

**Step 2 Create a new Python script matplotlib\_assignment.ipynb. Import Matplotlib and follow these steps:**  

**1\. Create a simple line plot for the following data:**  
    
  **x \= \[1, 2, 3, 4, 5\]**  
  **y \= \[10, 15, 25, 30, 50\]**  
    
  **a. Plot the data.**    
  **b. Customize the plot by adding a title, axis labels, and a grid.**  

**2\. Create a bar graph to represent the marks scored by students in a subject:**    
    
  **students \= \['John', 'Jane', 'Alice', 'Bob'\]**  
  **marks \= \[75, 85, 60, 90\]**  
    
  **a. Plot the data as a bar graph.**    
  **b. Customize the colors and add a title.**  

**3\. Create a pie chart to represent the percentage distribution of a company’s revenue from different regions:**    
    
  **regions \= \['North America', 'Europe', 'Asia', 'Others'\]**  
  **revenue \= \[45, 25, 20, 10\]**  
    
  **a. Create a pie chart with the region names as labels.**    
  **b. Highlight the region with the highest revenue.**  

**4\. Generate a histogram to show the frequency distribution of randomly generated integers between 1 and 100 (sample size \= 1000).**  

---

**Note: For each assignment, provide explanations in markdown cells describing the steps and purpose of each part of the code. Submit the assignments as .ipynb files with visualization outputs.**

---

