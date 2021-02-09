import argparse
from countdownday import count_down_day
def parse_arguments():
    '''
    cmd line argparse for daycountdown
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('date',help='input a sting of yyyy,mm,dd')
    args = parser.parse_args()
    return args

def run_prog():
    "run the cmd line prog"
    args = parse_arguments()
    count_down_day(args.date)