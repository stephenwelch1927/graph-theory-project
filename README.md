# graph-theory-project

What Is A Regular Expression

A regular expression which is also known as regex or regexp is a sequence of characters that specifies a particular search pattern. Usually these patterns are used by string-searching-algorithms for find or find and replace operations on a strings, or for input validation. It is a theoretical computer and formal language theory.
Regular expressions are used in search engines, search and replace dialogs of word processors and text editors. Many programming languages provide Regex capabilities wither built-in or via libraries.
Regex’s is often used to mean the specific, standard textual syntax for representing patterns for matching text. Each character in a regular expression (that is describing its pattern) is either a  metacharacter which has a special meaning or a regular character that has a literal meaning. For an example of this is the letter s. ‘s’ is a literal character and ‘.’ Is a metacharacter that matches every character except a newline. For example this b. regex could match for an example ‘b%’, ‘b6’ or ‘ba’, a simple case of a regular expression is to locate a word that is spelt two different ways like the regular expression seriali[sz]e will match both “serialize” and “serialise”. Wildcard characters also achieve this but are more limited in what they can pattern, as they have fewer metacharacters and a simple language base.
The usual context of wildcard characters is in gobbing similar names in a list of files, where as regexes are usually employed in applications that pattern-match text strings in general.
Some examples of a regular expressions and their form:

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

References
https://en.wikipedia.org/wiki/Regular_expression