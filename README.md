# huntington-pyladiescon23
This repository includes the slides of the public presentation 'Curando enfermedades genéticas con Python' of the PyLadiesCon23 and both the code and files used for the practical case (slide 25 onwards).

## Installation
You simply have to download the .py and fasta files (or get your own fasta files from a database as [NCBI](https://www.ncbi.nlm.nih.gov/)).

## Usage
First you'll have to select the file of your diseased gene of interest. Then you'll have to introduce the position of the mutation (as a positive integer) and the letters that are repeated. Finally, you'll have to specify which is the number of healthy repetitions (also as a positive integer). When finished, you'll have three .txt files saved in the same folder of the .py file with the RNA guide, the DNA mold and the mutated sequence.
If you want to recreate the example of the slides just use the provided fasta file diseased_HTT with the Huntington disease's mutation:
- Mutation position: 5197
- Repeated letters: CAG
- Healthy number of repetitions: 21

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
