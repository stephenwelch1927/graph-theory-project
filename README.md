# graph-theory-project

What Is A Regular Expression

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

How do regular expressions differ across implementations

Regular expressions have many different implementations depending on what language you use, there are various different libraries that you will have available to you.
For example in python you will have the re library that will enable you to use all the regular expressions within that library once you import it, the re library has many different expressions that the user can use. For example in the re library we can use the re.match() function this allows the user to return a matched object on success will return none on failure. The re.search will allow the user to search with three different parameters re.search(pattern, string, flags), the pattern is the regular expression to be matched, the string field is the string that will be matched to the pattern in the string. Flags you can specify using operators like && ||. Taken from https://www.tutorialspoint.com/python/python_reg_expressions.htm.
As above in the python language Java does also have a library called  java.util.regex, Java regular expressions are very similar to the Perl programming language and are very easy to learn. The java.util.regex class primarily consists of three different classes Pattern class, Matcher class and a PatternSyntaxException class https://www.tutorialspoint.com/java/java_regular_expressions.htm The Pattern class is a pattern object that is a compiled representation of a regular expression, to create a pattern you must first invoke one of its compile static methods which in turn will return a pattern object. The matcher class is a matcher object that interprets the pattern and performs match operations against an input string, you obtain a matcher object by invoking matcher() method. PatternSyntaxException object is an unchecked exception that indicates a syntax error in a regular expression pattern.
JavaScript also uses regular expressions, it has methods test() and exec() these are direct regex methods. The string class then has methods that have regex’s methods inside of them for example match(), replace(), search() and split these all perform regex searches on strings. If you want to know if there is a pattern found in a string, you would use the test() or search() methods but for more information you would use the exec() or match() methods but is slower in execution. Is you are to use the exec() or match() and if the match succeeds, these methods return an array and update the properties of the associated regular expression object.  
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions.

Can all formal languages be encoded as regular expressions?

Many formal languages can be encoded as a regular expressions, but there are some that are difficult and sometimes really hard to recognize. Also there are formal languages that cannot be recognized by a computer https://dzone.com/articles/back-basics-regular.
Most languages have simple ways of being identified in their formal languages, so in turn this makes it easy for them to be formed into regular expressions, as regular expressions such for patterns some languages have no pattern to follow. http://blog.kenficara.com/2013/06/30/irregular-language-and-regular-expressions/


