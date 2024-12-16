import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class Menu:
    def __init__(self):
        self.df=pickle.load(open('./artifacts/restaurant-data.pkl','rb'))
        self.vector=pickle.load(open('./artifacts/vector.pkl','rb'))
        self.model=pickle.load(open('./artifacts/model.pkl','rb'))
        self.similar_results=cosine_similarity(self.vector)

    def get_menu_items(self):
        self.menu_array=pickle.load(open('./artifacts/Village-menu.pkl','rb'))
        self.menu_array=self.menu_array.fillna("Not Specified")
        self.item_category=self.menu_array['Item-type'].unique()
        return self.item_category, self.menu_array[['Item-Name', 'Description']]

    def get_similar_results(self, index):
        self.index=int(index)
        self.similar_item_index=[]
        if self.df.loc[self.index,'Restaurant-Name']=='Village - The Soul of India':
            self.similar_val=sorted(list(enumerate(self.similar_results[self.index])), key=lambda x: x[1] ,reverse=True)[:15]
            self.count=1
            self.similar_item_index.append(int(index))
            for val in self.similar_val:
                if self.count<7:
                    if self.df.loc[val[0],'Restaurant-Name']!='Village - The Soul of India':
                        self.similar_item_index.append(val[0])
                        self.count+=1
                else:
                    break

        self.predicted_price=self.model.predict(self.vector[self.similar_item_index])
        # print(self.similar_item_index)
        # self.predicted_price=np.round(self.predicted_price, 2)
        return self.similar_item_index[1:], self.df, self.predicted_price
            

