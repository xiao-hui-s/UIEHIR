from time import time
def get_relational_data(user_id, item_id, data):  # given a user-item pair, return the relational data
    # user, positive, negative, alpha = [], [], [], []
    r0, r1, r2, r3 = [], [], [], []                                     #the item set in ru+ which has relationship r0,r1,r2,r3 with i
    # cnt0, cnt1, cnt2, cnt3 = [], [], [], []                           # the number of corresponding r, for masking
    e1, e2, e3 = [], [], []                                             # the set of specific attribute value for correspoding r except r0
    all_items = data.items.values()
    # get sample
    t1 = time()
    pos = data.user_positive_list[user_id]
    id1 = data.items_traverse[item_id]
    movie1 = data.movie_dict[id1]
    ru_list = list(pos)
    if item_id in ru_list:
        ru_list.remove(item_id)

    for another_item in ru_list:
        id2 = data.items_traverse[another_item]
        movie2 = data.movie_dict[id2]
        shared_genre, shared_director, shared_actor = get_share_attributes(movie1, movie2)
        if len(list(shared_genre)) + len(list(shared_director)) + len(list(shared_actor)) == 0:
            r0.append(another_item)
        if len(list(shared_genre)) != 0:
            for value in shared_genre:
                r1.append(another_item)
                e1.append(value)
        if len(list(shared_director)) != 0:
            for value in shared_director:
                r2.append(another_item)
                e2.append(value)
        if len(list(shared_actor)) != 0:
            for value in shared_actor:
                r3.append(another_item)
                e3.append(value)

    ru1, ru2, ru3 = [], [], []
    pos_item = data.item_positive_list[item_id]
    user1id = data.users_traverse[user_id]
    user1 = data.user_dict[user1id]
    pos_item_list = list(pos_item)
    share_gender_num, share_age_num, share_occupation_num = 0, 0, 0
    if user_id in pos_item_list:
        pos_item_list.remove(user_id)

    for another_user in pos_item_list:
        user2id = data.users_traverse[another_user]
        user2 = data.user_dict[user2id]
        share_gender, share_age, share_occupation = get_share_user_attribute(user1,user2)
        if share_gender == 1:
            ru1.append(another_user)
            share_gender_num = share_gender_num + share_gender
        if share_age == 1:
            ru2.append(another_user)
            share_age_num = share_age_num + share_age
        if share_occupation == 1:
            ru3.append(another_user)
            share_occupation_num = share_occupation_num + share_occupation



    t2 = time()
    #print ('the time of generating batch:%f' % (t2 - t1))
    cnt0=len(r0)
    cnt1=len(r1)
    cnt2=len(r2)
    cnt3=len(r3)
    return r0, r1, r2, r3, e1, e2, e3, cnt0, cnt1, cnt2, cnt3, ru1, ru2, ru3, share_gender_num, share_age_num, share_occupation_num


def get_share_attributes(movie1, movie2):
    genre_list1 = movie1.genre
    genre_list2 = movie2.genre
    len1,len2=len(genre_list1), len(genre_list2)
    if len1==1 and len2==1:
        if genre_list1[0]==genre_list2[0]:
            shared_genre=genre_list1
        else:
            shared_genre=[]
    if len1==1 and len2!=1:
        if genre_list1[0] in genre_list2:
            shared_genre=genre_list1
        else:
            shared_genre=[]
    if len1!=1 and len2==1:
        if genre_list2[0] in genre_list1:
            shared_genre=genre_list2
        else:
            shared_genre=[]
    if len1!=1 and len2!=1:
        shared_genre = filter(set(genre_list1).__contains__, genre_list2)
    #shared_genre = list(set(genre_list1) & set(genre_list2))
    director_list1 = movie1.director
    director_list2 = movie2.director
    len1,len2=len(director_list1), len(director_list2)
    if len1==1 and len2==1:
        if director_list1[0]==director_list2[0]:
            shared_director=director_list1
        else:
            shared_director=[]
    if len1==1 and len2!=1:
        if director_list1[0] in director_list2:
            shared_director=director_list1
        else:
            shared_director=[]
    if len1!=1 and len2==1:
        if director_list2[0] in director_list1:
            shared_director=director_list2
        else:
            shared_director=[]
    if len1!=1 and len2!=1:
        shared_director = filter(set(director_list1).__contains__, director_list2)

    #shared_director = list(set(director_list1) & set(director_list2))
    actor_list1 = movie1.actor
    actor_list2 = movie2.actor
    len1,len2=len(actor_list1), len(actor_list2)
    if len1==1 and len2==1:
        if actor_list1[0]==actor_list2[0]:
            shared_actor=actor_list1
        else:
            shared_actor=[]
    if len1==1 and len2!=1:
        if actor_list1[0] in actor_list2:
            shared_actor=actor_list1
        else:
            shared_actor=[]
    if len1!=1 and len2==1:
        if actor_list2[0] in actor_list1:
            shared_actor=actor_list2
        else:
            shared_actor=[]
    if len1!=1 and len2!=1:
        shared_actor = filter(set(actor_list1).__contains__, actor_list2)
    #shared_actor = list(set(actor_list1) & set(actor_list2))
    return shared_genre, shared_director, shared_actor



def get_share_user_attribute(user1,user2):
    share_gender, share_age, share_occupation = 0, 0, 0
    user1_gender, user1_age, user1_occupation = user1.gender, user1.age, user1.occupation
    user2_gender, user2_age, user2_occupation = user2.gender, user2.age, user2.occupation

    if user1_gender[0] == user2_gender[0]:
        share_gender = 1
    if user1_age[0] == user2_age[0]:
        share_age = 1
    if user1_occupation[0] == user2_occupation[0]:
        share_occupation = 1

    return share_gender, share_age, share_occupation
