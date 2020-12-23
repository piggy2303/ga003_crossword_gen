# Install

Cairo, Pango

## For ubuntu

    sudo apt-get install libcairo2-dev
    sudo apt-get install libpango1.0-dev
    sudo apt-get install python3-gi-cairo

## For mac

    brew install pango

# Setup

    cd genxword
    python3 setup.py install

# Useage

Demo

    python3 orai_crossword_generator.py

list argument, default value and help

    parser.add_argument('--word_list',
                        type=str,
                        default='word_list.txt',
                        help='path to word list txt file')

    parser.add_argument('--owner',
                        type=str,
                        default='Orai',
                        help='to set the name of owner')

    parser.add_argument('--grid_size',
                        type=int,
                        default="17",
                        help='grid_size of crossword.')

    parser.add_argument('--number',
                        type=int,
                        default="20",
                        help='Number of words to be used.')
