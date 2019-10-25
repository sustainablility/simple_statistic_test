from numpy import *
import numpy as np
import pandas as pd

path='./'
filename = 'test.json'
predefinedHeaders = ['tweetid','userid','postdate','latitude','longitude','message','statusescount','friendscount','followerscount']

def read_json_spit_statistic_data(path, filename, predefinedHeaders):

	# read data from 'path+filename'
	data=pd.read_json(path+filename)
	# group data by 'user_id'
	user_info=data.groupby('userid',as_index=False).first()
	# extract data by 'predefinedHeaders'
	user_info=user_info[predefinedHeaders]

	# define an empty dataframe
	static_frame = pd.DataFrame()

	# get raw numbers from data
	tweetid_array = user_info['tweetid'].values
	userid_array = user_info['userid'].values
	postdate_array = user_info['postdate'].values
	latitude_array = user_info['latitude'].values
	longitude_array = user_info['longitude'].values
	message_array = user_info['message'].values
	statusescount_array = user_info['statusescount'].values
	friendscount_array = user_info['friendscount'].values
	followerscount_array = user_info['followerscount'].values

	# get max number of followerscount
	max_followerscount = np.max(followerscount_array)
	
	# get mean number of friendscount
	mean_friendscount = np.mean(friendscount_array)

	# get std of friendscount
	std_friendscount = np.std(friendscount_array)

	# get min numbers of posts
	meadian_statusescount = np.min(statusescount_array)


	# put them into dataframe
	static_frame['max_followerscount'] = [max_followerscount]
	static_frame['mean_friendscount'] = [mean_friendscount]
	static_frame['std_friendscount'] = [std_friendscount]
	static_frame['meadian_statusescount'] = [meadian_statusescount]
	
	return static_frame.to_json(orient='records')

#print(read_json_spit_statistic_data(path, filename, predefinedHeaders))
