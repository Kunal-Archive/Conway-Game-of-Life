# the main() function

def main():
    # parse argument
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")

    # add arguments
    parser.add_arguments('--grid-size', dest='N', required=False)  
    parser.add_arguments('--mov-file', dest='movfile', required=False)
    parser.add_arguments('--interval', dest='interval', required=False)
    parser.add_arguments('--glider', action='store_true', required=False)
    
    args = parser.parse_args()

