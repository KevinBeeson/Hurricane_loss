# Hurricane Loss Simulation

This Python program simulates the economic loss from hurricanes in Florida and the Gulf States over a number of years. The simulation uses Poisson and lognormal distributions to model the frequency and economic impact of hurricanes.

## Requirements

- Python 3.x
- NumPy
- tqdm

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/KevinBeeson/Oasis_Technical_test
    cd Oasis_Technical_test
    ```

2. Create a virtual environment (recommended):
    ```bash
    python -m venv Oasis
    ```

3. Activate the virtual environment:
    - On Linux:
        ```bash
        source Oasis/bin/activate
        ```
    - On Windows:
        ```bash
        ./Oasis/scripts/activate
        ```

4. Install the required packages:
    ```bash
    pip install numpy tqdm
    ```

## Usage

Run the simulation with the following command:
```bash
 python gethurricaneloss.py -n <number_of_simulations> -ncpu <number of cpu used> <florida_landfall_rate> <florida_mean> <florida_stddev> <gulf_landfall_rate> <gulf_mean> <gulf_stddev>
```
 ### Arguments

- `-n` or `--simulations`: Number of years to simulate (int)(default: 1000)
- `--ncpu`: Number of CPUs to use for multiprocessing (int)(default: 1)
- `florida_landfall_rate`: Lambda parameter for the Poisson distribution for Florida (float)
- `florida_mean`: Mean of the lognormal distribution for economic loss in Florida (float)
- `florida_stddev`: Standard deviation of the lognormal distribution for economic loss in Florida (float)
- `gulf_landfall_rate`: Lambda parameter for the Poisson distribution for Gulf States (float)
- `gulf_mean`: Mean of the lognormal distribution for economic loss in Gulf States (float)
- `gulf_stddev`: Standard deviation of the lognormal distribution for economic loss in Gulf States (float)

### Return

```
Average yearly economic loss from hurricanes in Florida and the Gulf States: <number> Billion US dollars


Theoretical average yearly economic loss from hurricanes in Florida and the Gulf States: <number> Billion US dollars
```

## Test

Unit tests for this program are provided in the `test.py` file. The tests cover if the hurricane_rate_florida, economic_loss_florida, hurricane_rate_gulf_states, economic_loss_gulf_states create normal outputs 

## Performance

Running profilers on the code shows that most of the time is spent on the numpy poisson and lognormal function. I've compared it to Scipy's poisson and lognormal functions, and Numpy is much faster. I've added multiprocessing so the user can utilise multiple cores, thus increasing the processing speed. They will also have an estimate of the required time for the program to complete.


## Ideas on future features

- Have a way to test convergence to see if increasing the number of samples is necessary.
- Every 10% of the samples, give the user a current mean and standard deviations of the samples.
- Output all the samples to a file so more analysis can be done on the samples. Save every x% so incase the program crashes while running all progress is not lost.
- Plot these samples on a histogram.