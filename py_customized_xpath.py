"""
Customize Xpath

XPath is defined as XML path. It is a syntax or language for finding any element on the web page using XML path expression

Syntax for XPath:

Xpath=//tagname[@attribute='value']

// 		 : Select current node.
Tagname  : Tagname of the particular node.
@		 : Select attribute.
Attribute: Attribute name of the node.
Value  	 : Value of the attribute.


Types of X-path:

*******************************************************************************************************************
Absolute XPath:

It is the direct way to find the element, but the disadvantage of the absolute XPath is that if there are any changes 
made in the path of the element then that XPath gets failed.

The key characteristic of XPath is that it begins with the single forward slash(/),
which means you can select the element from the root node.

E.g.,: html/body/div[1]/section/div[1]/div/div/div/div[1]/div/div/div/div/div[3]/div[1]/div/h4[1]/b

*****************************************************************************************************************8
Relative xpath:

For Relative Xpath the path starts from the middle of the HTML DOM structure. It starts with the double forward slash (//), which means it can search the element anywhere at the webpage.

You can start from the middle of the HTML DOM structure and no need to write long xpath.

E.g.,: //*[@class='featured-box']//*[text()='Testing']

********************************************************************************************************************

Customized Xapth(s):

1. Basic XPath

	//input[@name='uid']

2. Contains()
	
	//*[contains(@type,'sub')]
	//*[contains(@name,'btn')]
	//*[contains(@id,'message')]
	//*[contains(text(),'here')]
	//*[contains(@href,'guru99.com')]

3. Using OR & AND

	//*[@type='submit' or @name='btnReset']
	//input[@type='submit' and @name='btnLogin']

4. Start-with function
	
	//label[starts-with(@id,'message')]


5. Text()
	
	//td[text()='UserID']

6. XPath axes methods:
	a. Following
	
		//*[@type='text']//following::input
		//*[@type='text']//following::input[1]

	b. Ancestor

		//*[text()='Enterprise Testing']//ancestor::div
		//*[text()='Enterprise Testing']//ancestor::div[1]

	c. Child

		//*[@id='java_technologies']/child::li
		//*[@id='java_technologies']/child::li[1]

	d. Preceding

		//*[@type='submit']//preceding::input
		//*[@type='submit']//preceding::input[1]

	e. Following-sibling

		//*[@type='submit']//following-sibling::input

	f. Parent

		//*[@id='rt-feature']//parent::div
		//*[@id='rt-feature']//parent::div[1]

	g. Self

		//*[@type='password']//self::input

	h. Descendant

		//*[@id='rt-feature']//descendant::a

"""



