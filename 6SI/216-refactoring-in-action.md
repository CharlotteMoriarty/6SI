# Refactoring in action

The previous SI week contains a page about clean code, now let's see the usage of those clean code principles through a real-life example of refactoring.

_"The @author field of a Javadoc tells us who we are. We are authors. And one thing about authors is that they have readers. Indeed, authors are responsible for communicating well with their readers. The next time you write a line of code, remember you are an author, writing for readers who will judge your effort."
_ _(from 'Clean code' by Robert C. Martin)_

Uncle Bob (alias Robert C. Martin) states in his famous book _Clean code_ that spending time and energy for writing self-explaining and readable code pays off as we _read_ code way more than _write_.

You might experience in the last few weeks that it could be challenging to overlook and understand the code of even a 2-week-long project. So imagine the code of a 1-, 2- or even 10-year-long project. Scary, isn't it?

Good news is that there are practices both for keep the code quality and to refactor to clean code.

## Steps of refactoring code

Here are some steps that can help you to make the code clean.

  1. Read through the whole code
  2. Summarize what is the purpose of the script in one sentence.
  3. Run the code to see what is the end result
  4. The code should keep runnable and show the same content when you finish the refactor
  5. Do not forget to run the code frequently to check you are on the right track
  6. How to refactor it?
    * Remove clutter: Clutter is anything in your code that does not add value
      * Format your code
      * Delete comments
    * Remove complexity:
      * bad names
      * long methods
      * deep conditionals
      * improper variable scopes (global, local)
    * Remove cleverness: If it's simple and elegant you wouldn't refer to it as 'clever'
    * Remove the 3 D's:
      * duplication
      * duplication
      * duplication
      * This can be applied by extracting the duplicated code parts into functions



### Practical refactoring

To see the whole process with an explanation in action watch the video above.

The video is quite long, almost 2 hours but mentors of former classes reported that the ones who watched it has significantly deeper understanding about refactoring and clean code.

The video touches advanced topics (tests, classes, coupling, etc.). Just ignore them and concentrate on the main principals, aspects and the process of refactoring.

[![Play on YouTube](https://img.youtube.com/vi/aWiwDdx_rdo/0.jpg):arrow_forward:](https://www.youtube.com/watch?v=aWiwDdx_rdo "Play on YouTube")
