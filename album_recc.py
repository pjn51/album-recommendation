import streamlit as st
import pandas as pd

# function definitions
def find_album(df, adjs):
    result = df

    for adj in adjs:
        adj = adj.lower()

        if adj not in df.columns:
            return 'That adjective or combination of adjectives has not appeared in an album review.'
        
        result = result[result[adj] == 1]

    if result.shape[0] == 0:
    	return 'Sorry! No albums fit that description, according to Pitchfork.'

    for album in result['name_x']:
        st.text(album)

df = pd.read_pickle('/Users/patricknorman/Documents/Python/Data/albums.pkl')

st.title('Adjective-Assisted Album Aggregator')

'''
This tool uses text data from thousands of *Pitchfork* album reviews
to give album recommendations based on user-specified adjectives. 

Try it out for yourself by putting an adjective or two in the search bar.
Note that entering multiple adjectives will return fewer results.
'''

user_input = st.text_input('', '')

adjectives = user_input.split(' ')

adjectives = [adj.strip() for adj in adjectives]

#st.text(adjectives)

st.text(find_album(df, adjectives))