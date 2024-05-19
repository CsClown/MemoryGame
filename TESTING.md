# Testing

## Code Validation

The [Towers of Hanoi](https://towers-of-hanoi-game.herokuapp.com/) application was thouroughly tested. Python code was reviewed in the [CI Python Linter](https://pep8ci.herokuapp.com/#). As I was continuously correcting warnings and mistakes using pylint in my GitPod, when I ran the code through the CI Python Linter, there was only one warning about an extra line at the end of the file, which I subsequently deleted. Currently, the [run.py file](/run.py) has no errors.

[CI Python Linter No Errors](/readme-images/python_linter_all_clear.png)

Bugs and warnings encountered during the development process will be described below.

## Browser Compatibility

The website was tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. There were no errors discovered in the functionality of the CLI application.

## Responsiveness Test

I did not perform a responsivness test as this CLI application is intended to be used on desktop only. Just for illustration purposes, I am including [Am I Responsive Image](readme-images/amiresponsive.png).

## Fixed Bugs

| Bug                                                                                | Where            | How                                                                                                     | Commit                                                                                                  |
|------------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| choose_difficulty() was not returning an integer.                                  | run.py           | I used int() around the returned variable.                                                              | [cd66067](https://github.com/lucia2007/towers-of-hanoi/commit/cd6606731d4da21cfd10e20f487fa75aa53be177) |
| The disks were not drawn correctly.                                                | run.py           | I had to adjust the linear function used for visualization of the disks.                                | [21316c1](https://github.com/lucia2007/towers-of-hanoi/commit/21316c136c79213bac4c1eaa683efe5d431ccefc) |
| Missing parameter in move_disk_to().                                               | run.py           | I had to add a parameter to move_disk_to(scr:int).                                                      | [ecba3d0](https://github.com/lucia2007/towers-of-hanoi/commit/ecba3d08f7bf64d73c126f2cd57c2069344818dd) |
| Function validate_number(height) needed improving.                                 | run.py           | I changed the order of the statements and changed the name of the parameter.                            | [7dd2437](https://github.com/lucia2007/towers-of-hanoi/commit/7dd2437edf72fbf63ed66c63d99e9a5e96d121d7) |
| move_disk_from() needed a change in the order of statements.                       | run.py           | I included the first print message in the while loop.                                                   | [80e7d9f](https://github.com/lucia2007/towers-of-hanoi/commit/80e7d9f9a260321e6740e1669d2a5c11c288e954) |
| I was converting a variable to integer in the wrong place.                         | run.py           | I changed the variable to int() when returned.                                                          | [060edc9](https://github.com/lucia2007/towers-of-hanoi/commit/060edc99fa2c11c4017a02b4c50f3971549154d4) |
| Pyramids were not being printed in the middle of the base.                         | run.py           | I had to add a space in the print().                                                                    | [5edcbba](https://github.com/lucia2007/towers-of-hanoi/commit/5edcbba42d3390ef376543dc5d6bdeb955ddff5b) |
| I forgot to include COLORAMA in requirements.                                      | requirements.txt | I added "colorama==0.4.6" to the relevant file.                                                         | [d09f13f](https://github.com/lucia2007/towers-of-hanoi/commit/d09f13f18c9ea833ce1bbe40564f3a672d4c183a) |
| There were warnings regarding the ASCII form of You Won! Some lines were too long. | run.py           | I added "r" to the print statement of the ASCII Art to create raw string and improved print statements. | [36ec779](https://github.com/lucia2007/towers-of-hanoi/commit/36ec7799be58bb8fff5454b2786768de2db2b56a) |
| I was overwriting variable names in a few places.                                  | run.py           | I had to choose unique names of variables (paramater vs argument).                                      | [13bb8bd](https://github.com/lucia2007/towers-of-hanoi/commit/13bb8bdd1bc33277d3d95764a78eca8bfacdab94) |
| Moves variable was not being printed out.                                          | run.py           | I had to add "f" to the print statement.                                                                | [706a380](https://github.com/lucia2007/towers-of-hanoi/commit/706a380ca7599e539b98303078503b24c25f2d9e) |
| The pyramids were not being printed correctly.                                     | run.py           | I had to take out empty space from the print out statements.                                            | [488a982](https://github.com/lucia2007/towers-of-hanoi/commit/488a9824f6ae13dd873640a80503bd1aa8b6583c) |
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