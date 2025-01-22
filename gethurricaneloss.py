import numpy as np
import argparse
import logging
from tqdm import tqdm
from multiprocessing import Pool
logging.getLogger().setLevel(logging.INFO)


def hurricane_rate_florida(florida_landfall_rate=1.0):
    """Returns the number of hurricanes that make landfall in Florida in a given year modeled as a Poisson distribution.
    Parameters
    ----------
    florida_landfall_rate : float
    Lambda parameter for the Poisson distribution

    Returns:
    number of hurricanes per year: int
    
    """
    return np.random.poisson(florida_landfall_rate,1)[0]
def economic_loss_florida(florida_mean=10.0,florida_stddev=1.0):
    """Returns the economic loss from a hurricane in Florida modeled as a lognormal distribution.
    Parameters
    ----------
    florida_mean : float
    Mean parameter of the lognormal distribution
    florida_stddev : float
    Standard deviation parameter of the lognormal distribution

    Returns:
    economic loss from a hurricane in dollars: float
    
    """

    return np.random.lognormal(florida_mean,florida_stddev,1)[0]
def hurricane_rate_gulf_states(gulf_landfall_rate=1.0):
    """Returns the number of hurricanes that make landfall in the Gulf States in a given year modeled as a Poisson distribution.
    Parameters
    ----------
    gulf_landfall_rate : float
    Lambda parameter for the Poisson distribution
    
    Returns:
    number of hurricanes per year: int
    """
    return np.random.poisson(gulf_landfall_rate,1)[0]
def economic_loss_gulf_states(gulf_mean=10.0,gulf_stddev=1.0):
    """Returns the economic loss from a hurricane in the Gulf States modeled as a lognormal distribution.
    Parameters
    ----------
    gulf_mean : float
    Mean parameter of the lognormal distribution
    gulf_stddev : float
    Standard deviation parameter of the lognormal distribution
    
    Returns:
    economic loss from a hurricane in dollars: float
    """
    return np.random.lognormal(gulf_mean,gulf_stddev,1)[0]

def multiprocessing_year_loop(year):
        """Returns the total economic loss from hurricanes in Florida and the Gulf States in a given year. used for multiprocessing."""
        yearly_simulation_loss=0
        number_of_hurricanes_florida=hurricane_rate_florida(florida_landfall_rate)
        for i in range(number_of_hurricanes_florida):
            yearly_simulation_loss+=economic_loss_florida(florida_mean,florida_stddev)
        number_of_hurricanes_gulf_states=hurricane_rate_gulf_states(gulf_landfall_rate)
        for i in range(number_of_hurricanes_gulf_states):
            yearly_simulation_loss+=economic_loss_gulf_states(gulf_mean,gulf_stddev)
        return yearly_simulation_loss

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(prog='gethurricaneloss',
                        description='Calculate the average economic loss from hurricanes in Florida and the Gulf States',
                        epilog="""The program uses Monte Carlo simulation to estimate the average economic loss from hurricanes in Florida and the Gulf States.
                        The yearly rate of hurricanes is modelled by a poisson distribution and the economic loss from a hurricane is modelled by a lognormal distribution.
                

                        Example:
                        python gethurricaneloss.py -n 100000 -ncpu 2 1 2.3 1 1 1 1 

                        runs the simulation with 100,000 samples and the following parameters:
                        Florida landfall rate: 1
                        Florida lognormal variable for mean economic loss: 2.3
                        Florida lognormal variable for standard deviation: 1
                        Gulf States landfall rate: 1
                        Gulf States lognormal variable for mean economic loss: 1
                        Gulf States lognormal variable for standard deviation: 1
                        Number of CPUs to use for multiprocessing: 2

                        returns:
                        Average yearly economic loss from hurricanes in Florida and the Gulf States: 21.015434 Billion US dollars
                        Theoretical average yearly economic loss from hurricanes in Florida and the Gulf States: 20.926336 Billion US dollars

                        """,
                        formatter_class=argparse.RawDescriptionHelpFormatter
                        
    )
    parser.add_argument('-n', '--num_monte_carlo_samples', type=int, default=1000,help='Number of Monte Carlo samples to run (int), default=1000') 
    parser.add_argument('florida_landfall_rate', type=float,help='Average yearly rate of hurricanes making landfall in Florida (float)') 
    parser.add_argument('florida_mean', type=float,help='Mean lognormal variable for economic loss from a hurricane in Florida (float)')
    parser.add_argument('florida_stddev', type=float,help='Standard deviation  lognormal variable for for the economic loss from a hurricane in Florida (float)')
    parser.add_argument('gulf_landfall_rate', type=float,help='Average yearly rate of hurricanes making landfall in the Gulf States (float)')
    parser.add_argument('gulf_mean', type=float,help='Mean lognormal variable for economic loss from a hurricane in the Gulf States (float)')
    parser.add_argument('gulf_stddev', type=float,help='Standard deviation lognormal variable for the economic loss from a hurricane in the Gulf States (float)')
    parser.add_argument('-ncpu', type=int,default=1,help='Number of CPUs to use for multiprocessing (int), default=1')
    try:
        args = parser.parse_args()

    except SystemExit:
        logging.error('Please enter a valid type and value for all the arguments')
        exit(1)
    florida_landfall_rate = args.florida_landfall_rate
    florida_mean = args.florida_mean
    florida_stddev = args.florida_stddev
    gulf_landfall_rate = args.gulf_landfall_rate
    gulf_mean = args.gulf_mean
    gulf_stddev = args.gulf_stddev
    simulations = args.num_monte_carlo_samples
    ncpu = args.ncpu

    # do some sanity checks on the input values
    values_above_zero = [florida_landfall_rate, florida_stddev, gulf_landfall_rate, gulf_stddev, simulations,ncpu]
    names = ['florida_landfall_rate', 'florida_stddev', 'gulf_landfall_rate', 'gulf_stddev', 'simulations','ncpu']
    if np.any(np.array(values_above_zero) < 0):
        wrong_values = [names[i] for i in range(len(values_above_zero)) if values_above_zero[i] < 0]
        logging.error('The following values are below zero: ' + ', '.join(wrong_values)+'. Please enter a possitive value')
        exit(1)
    values_above_zero=[florida_mean,gulf_mean] 
    names=['florida_mean','gulf_mean']
    if np.any(np.array(values_above_zero) <= 0):
        wrong_values=[names[i] for i in range(len(values_above_zero)) if values_above_zero[i] <= 0]
        logging.warning('The following values are zero or below: ' + ', '.join(wrong_values)+'. This will be quite unrealistic')

    # Run the Monte Carlo simulation
    logging.info('Running Monte Carlo simulation with the following parameters:')
    logging.info('Number of Monte Carlo samples: %d', simulations)
    logging.info('Florida average landfall rate: %f', florida_landfall_rate)
    logging.info('Florida mean lognormal variable for economic loss: %f', florida_mean)
    logging.info('Florida standard lognormal variable for deviation: %f', florida_stddev)
    logging.info('Gulf States average landfall rate: %f', gulf_landfall_rate)
    logging.info('Gulf States lognormal variable  mean economic loss: %f', gulf_mean)
    logging.info('Gulf States lognormal variable  standard deviation: %f', gulf_stddev)
    logging.info('Number of CPUs to use for multiprocessing: %d', ncpu)

    total_loss=0
    estimated_total = simulations
    with Pool(ncpu) as p:
        total_loss=sum(tqdm(p.imap(multiprocessing_year_loop, range(estimated_total)), total=estimated_total))
    mean_loss=total_loss/simulations

    logging.info('Average yearly economic loss from hurricanes in Florida and the Gulf States: %f Billion US dollars', mean_loss)

    """ 
    If I wasnt using the algorithm specified in the assignment I would have used the following code as it runs much faster:
    total_loss=0
    yearly_number_of_huricanes_florida=np.random.poisson(florida_landfall_rate,simulations)
    total_florida=sum(yearly_number_of_huricanes_florida)
    total_loss_florida=sum(np.random.lognormal(florida_mean,florida_stddev,total_florida))
    yearly_number_of_huricanes_gulf_states=np.random.poisson(gulf_landfall_rate,simulations)
    total_gulf=sum(yearly_number_of_huricanes_gulf_states)
    total_loss_gulf=sum(np.random.lognormal(gulf_mean,gulf_stddev,total_gulf))
    total_loss=total_loss_florida+total_loss_gulf
    mean_loss=total_loss/simulations
    """
    theoretical_mean=np.exp(florida_mean+florida_stddev**2/2)*florida_landfall_rate+np.exp(gulf_mean+gulf_stddev**2/2)*gulf_landfall_rate
    logging.info('Theoretical average yearly economic loss from hurricanes in Florida and the Gulf States: %f Billion US dollars', theoretical_mean)




