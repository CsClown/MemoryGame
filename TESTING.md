# Testing

## Code Validation

The [Python CLI Memory Game](https://python-cli-memory-game-ea3c2c01cc65.herokuapp.com/) application was thouroughly tested. Python code was reviewed in the [CI Python Linter](https://pep8ci.herokuapp.com/#). After a couple of hours fixing white spaces and lines that were too long the [run.py file](/run.py) has no errors.

![CI Python Linter No Errors](assets/readme-images/linter.png)

Bugs and warnings encountered during the development process will be described below.

## Browser Compatibility

The website was tested on the following browsers: Google Chrome, Microsoft Edge and Mozilla Firefox. Unfortunately Mozilla Firefox cuts the ASCII symbols at two thirds of their width.

## Responsiveness Test

I did not perform a responsivness test as this CLI application is intended to be used on desktop only. Just for illustration purposes, I am including [Am I Responsive Image](assets/readme-images/responsive.png).

## Fixed Bugs


## Unfixed Bugs

There are no known bugs in the project.
## Input Validation

Each of the inputs has been throroughly tested. The user makes these choices:

1. User chooses the level of difficulty between 3-6.
    - Possible errors:
      - The user does not choose a number.
      - The user chooses a number which is smaller than 3 or bigger than 6.
    - Each time the user makes an error, they are informed of this fact and are prompted to correct their choice.

      <details><summary><b>Input Validation</b></summary>
   
      ![Connect to GitHub](/readme-images/difficulty_level.png)
      </details><br />

2. User chooses from which base he wants to take a disk, possible inputs: 1, 2 or 3.
   - Possible errors:
     - The user does not choose a number. 
     - The user chooses a number wich is smaller than 1 or bigger than 3.
     - The user wants to move a disk from na empty base.

      <details><summary><b>Input Validation</b></summary>
   
      ![Connect to GitHub](/readme-images/from_base.png)
      </details><br /> 

3. User chooses on which base he wants to place the disk, possible inputs: 1, 2 or 3.
   - Possible errors:
     - The user does not choose a number. 
     - The user chooses a number wich is smaller than 1 or bigger than 3.
     - The user wants to place a bigger disk on a smaller one.

      <details><summary><b>Input Validation</b></summary>
   
      ![Connect to GitHub](/readme-images/to_base.png)
      </details><br /> 

4. User decides if they want to play again ("Y") or if they want to quite ("N").
    - Possible errors:
      - The user does not choose a letter.
      - The user does not choose "Y" or "N". (The input does not have to be capitalized.)

      <details><summary><b>Input Validation</b></summary>
   
      ![Connect to GitHub](/readme-images/play_again.png)
      </details><br /> 
      
## Additional Testing
### Lighthouse

The application was also tested using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Developer Tools. The following aspects were tested:

- Performance - reveals how the site performs during loading
- Accessibility - shows if the site if accessible for all users and suggests ways to improve it
- Best Practices - indicates if the site conforms to industry best practices
- SEO - Search Engine Optimisation - shows if the site is optimised for search engine result rankings

### Results from Lighthouse

[Lighthouse test result](/readme-images/lighthouse_score.png)