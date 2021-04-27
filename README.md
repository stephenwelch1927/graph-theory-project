# graph-theory-project

## Project Brief 

As our end of year project, we are to research and design a Python program that will allow the user to input a regular expression and will then return the string that was found by the program.
___
## Research

As I was looking to get started with the project I realised, that my understanding of the algorithms was very minimal so I needed to grasp the concepts and what is actually going on before proceeding any further. 

### Shunting Yard Algorithm

First of my research was to get a better understanding of the Shunting Yard algorithm, after watching this YouTube video https://www.youtube.com/watch?v=HJOnJU77EUs it gave me a far better understanding of why this is used.  So to understand that at the start we need to see if an expression is balanced, so firstly check if the parenthesis is an ( and we keep popping them on to the stack until we find a corresponding ) then we pop them off the stack we continue this through until the stack is empty. If the stack is empty its balanced, if it is not empty it is not balanced then the second part is the postfix where this time you are putting an integer to a stack then once you hit an operator you must check to see there at least two or more integers on the stack otherwise the expression is invalid. Once there are two or more the first integer is put to the left and then an operator in the middle and the second integer to the right, they are then evaluate and put to the stack we continue doing this until there is one element on the stack and if there is not then the expression is invalid. Then we are ready to do postfix which is place all integers on the stack, if we come across and operator pop the two elements off the stack instead of evaluating we put parenthesis around the two numbers. The expression you have at the end of the string is the result, now we have to convert from infix to postfix which is a little more complex we have to firstly give precedence to our operators. So you could have 2 as high precedence for * / % , 1 as low for + -, 0 for ( [{ this basically means any operator can go after these and finally 3 immediate )]}. You can only then place operators on the stack if its empty or have an opening bracket there, you can only put a high precedence there if there is precedence below it we can place it on the stack. We then continue until we reach an operator of equal or less precedence and then we pop from the stack we keep popping until we can add the next operator to the stack then we pop everything off and that is the result.

### Thompson's Construction Algorithm

The next algorithm to look at which we were shown in class is the Thompson’s construction, this is another method of transforming a regular expression into a nondeterministic finite automaton(NFA). This NFA can be used to match strings against regular expressions, it’s a popular algorithm as it can compile regular expressions into NFA’s.
The algorithm works recursively by splitting and expression into its constituent subexpressions, from which the NFA will be constructed using a set of rules. More precisely, from a regular expression E, the obtained automaton A with the transition function Δ[clarification needed] respects the following properties:
•	A has exactly one initial state q0, which is not accessible from any other state. That is, for any state q and any letter a,   does not contain q0.
•	A has exactly one final state qf, which is not co-accessible from any other state. That is, for any letter a,  .
•	Let c be the number of concatenation of the regular expression E and let s be the number of symbols apart from parentheses — that is, |, *, a and ε. Then, the number of states of A is 2s − c (linear in the size of E).
•	The number of transitions leaving any state is at most two.
•	Since an NFA of m states and at most e transitions from each state can match a string of length n in time O(emn), a Thompson NFA can do pattern matching in linear time, assuming a fixed-size alphabet.[4]
Taken from https://en.wikipedia.org/wiki/Thompson%27s_construction

### Understanding the difference between NFA and DFA

As I was getting to understand Automaton it was quite confusing as to what is a DFA(Deterministic Finite Automaton) and what is a NFA(Nondeterministic Finite Automaton), so again with previous algorithms I set out to understand more about this if foun that https://www.geeksforgeeks.org/difference-between-dfa-and-nfa/ was really good at explainig the differences.

So a DFA is set to deterministic If corresponding to an input symbol, there is a single resultant state i.e. there is only one transition. A deterministic finite automata is set to five tuples and represented as,  M = {Q, Σ, δ, q0, F}.

Q: A non empty finite set of states present in the finite control(qo, q1, q2, …). 
Σ: A non empty finite set of input symbols. 
δ: It is a transition function that takes two arguments, a state and an input symbol, it returns a single state. 
qo: It is starting state, one of the state in Q. 
F: It is non-empty set of final states/ accepting states from the set belonging to Q.  

Now an NFA is set to be nondeterministic, this means that there is more than one possible transition from one state on the same input symbol. A nondeterministic finite automata also is set to five tuples and represented as M = {Q, Σ, δ, q0, F}.
Q: A set of non empty finite states. 
Σ: A set of non empty finite input symbols. 
δ: It is a transition function that takes a state from Q and an input symbol from and returns a subset of Q. 
qo: Initial state of NFA and member of Q. 
F: A non-empty set of final states and member of Q. 

#### DFA Diagram Example
![DFA](https://user-images.githubusercontent.com/48323994/116069426-46949000-a683-11eb-97b7-c21bf1e19b00.PNG)

#### NFA Diagram Example
![NFA](https://user-images.githubusercontent.com/48323994/116071192-7fcdff80-a685-11eb-8807-f0089c42a63e.PNG)


___
## Issues Encountered

As I was initially setting up my environment for working using Debian I had a lot of issues, I tried to resolve this so instead of using Debian I reverted to Ubuntu.

As I’m beginning to use python, I’m experiencing some issues with actually how it behaves different compared to say Java. So I looked up a small video just to understand how classes work and how functions work https://www.youtube.com/watch?v=I2wURDqiXdM
___

## Aditional Material Studied

Well working on this README file I was limited in my knowledge of Markdown syntax, so I went off and read up some more additional material. I found that GitHub cheat sheet extremely useful with using Markdown syntax. https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf

___

## What Is A Regular Expression

A regular expression which is also known as regex or regexp is a sequence of characters that specifies a particular search pattern. Usually these patterns are used by string-searching-algorithms for find or find and replace operations on a strings, or for input validation. It is a theoretical computer and formal language theory.
Regular expressions are used in search engines, search and replace dialogs of word processors and text editors. Many programming languages provide Regex capabilities wither built-in or via libraries. You can find a complete detailed explanation here https://www.princeton.edu/~mlovett/reference/Regular-Expressions.pdf.
Regex’s is often used to mean the specific, standard textual syntax for representing patterns for matching text. Each character in a regular expression (that is describing its pattern) is either a  metacharacter which has a special meaning or a regular character that has a literal meaning. For an example of this is the letter s. ‘s’ is a literal character and ‘.’ Is a metacharacter that matches every character except a newline. For example this b. regex could match for an example ‘b%’, ‘b6’ or ‘ba’, a simple case of a regular expression is to locate a word that is spelt two different ways like the regular expression seriali[sz]e will match both “serialize” and “serialise”. Wildcard characters also achieve this but are more limited in what they can pattern, as they have fewer metacharacters and a simple language base.
The usual context of wildcard characters is in gobbing similar names in a list of files, where as regexes are usually employed in applications that pattern-match text strings in general.
Some examples of a regular expressions and their form take from https://en.wikipedia.org/wiki/Regular_expression :

•	.at matches any three-character string ending with "at", including "hat", "cat", and "bat".
•	[hc]at matches "hat" and "cat".
•	[^b]at matches all strings matched by .at except "bat".
•	[^hc]at matches all strings matched by .at other than "hat" and "cat".
•	^[hc]at matches "hat" and "cat", but only at the beginning of the string or line.
•	[hc]at$ matches "hat" and "cat", but only at the end of the string or line.
•	\[.\] matches any single character surrounded by "[" and "]" since the brackets are escaped, for example: "[a]" and "[b]".
•	s.* matches s followed by zero or more characters, for example: "s" and "saw" and "seed".

Metacharacters and their description:

?	Matches the preceding element zero or one time. For example, ab?c matches only "ac" or "abc".
+	Matches the preceding element one or more times. For example, ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac".
|	The choice (also known as alternation or set union) operator matches either the expression before or the expression after the operator. For example, abc|def matches "abc" or "def".

## How do regular expressions differ across implementations

Regular expressions have many different implementations depending on what language you use, there are various different libraries that you will have available to you.
For example in python you will have the re library that will enable you to use all the regular expressions within that library once you import it, the re library has many different expressions that the user can use. For example in the re library we can use the re.match() function this allows the user to return a matched object on success will return none on failure. The re.search will allow the user to search with three different parameters re.search(pattern, string, flags), the pattern is the regular expression to be matched, the string field is the string that will be matched to the pattern in the string. Flags you can specify using operators like && ||. Taken from https://www.tutorialspoint.com/python/python_reg_expressions.htm.
As above in the python language Java does also have a library called  java.util.regex, Java regular expressions are very similar to the Perl programming language and are very easy to learn. The java.util.regex class primarily consists of three different classes Pattern class, Matcher class and a PatternSyntaxException class https://www.tutorialspoint.com/java/java_regular_expressions.htm The Pattern class is a pattern object that is a compiled representation of a regular expression, to create a pattern you must first invoke one of its compile static methods which in turn will return a pattern object. The matcher class is a matcher object that interprets the pattern and performs match operations against an input string, you obtain a matcher object by invoking matcher() method. PatternSyntaxException object is an unchecked exception that indicates a syntax error in a regular expression pattern.
JavaScript also uses regular expressions, it has methods test() and exec() these are direct regex methods. The string class then has methods that have regex’s methods inside of them for example match(), replace(), search() and split these all perform regex searches on strings. If you want to know if there is a pattern found in a string, you would use the test() or search() methods but for more information you would use the exec() or match() methods but is slower in execution. Is you are to use the exec() or match() and if the match succeeds, these methods return an array and update the properties of the associated regular expression object.  
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions.

## Can all formal languages be encoded as regular expressions?

Many formal languages can be encoded as a regular expressions, but there are some that are difficult and sometimes really hard to recognize. Also there are formal languages that cannot be recognized by a computer https://dzone.com/articles/back-basics-regular.
Most languages have simple ways of being identified in their formal languages, so in turn this makes it easy for them to be formed into regular expressions, as regular expressions such for patterns some languages have no pattern to follow. http://blog.kenficara.com/2013/06/30/irregular-language-and-regular-expressions/


