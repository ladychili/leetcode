# encoding=utf-8
import json 
import pandas as pd

df = pd.read_json('/Users/cathy/GitProject/leetcode/problemset/prob0415_all.json')

db_js = json.load(open('/Users/cathy/GitProject/leetcode/problemset/prob0415_db.json','r'))


prob_set = []
for i in db_js:
    # tuple(i['stat']) + 
    meta = tuple(i['stat'].values()) + tuple(i['difficulty'].values()) + tuple([i["paid_only"]])
    prob_set.append(meta)
keys = tuple(i['stat'].keys()) + tuple(i['difficulty'].keys()) + tuple(["paid_only"])

db_df = pd.DataFrame(prob_set,columns=keys)

all = db_df.merge(df, how='left', left_on='question_id', right_on='questionId')\
           .astype({'frontend_question_id':int})\
            .sort_values(['frontend_question_id'])\
            .reset_index(drop=True)

all['level'] = all.level.map({1:'Easy',2:'Medium',3:'Hard'})
col = ['frontend_question_id', 'question_id','title', 'question__title', 'question__title_slug', 'level', 'paid_only']
all[col].to_csv('/Users/cathy/GitProject/leetcode/problemset/db0415.csv',index=False)



#### all prob
# all = db_df.merge(df, how='right', left_on='question_id', right_on='questionId')\
#            .astype({'frontend_question_id':str})\
#             .sort_values(['frontend_question_id'])\
#             .reset_index(drop=True)

# all['level'] = all.level.map({1:'Easy',2:'Medium',3:'Hard'})
# col = ['frontend_question_id', 'questionId','title', 'question__title', 'question__title_slug', 'level', 'paid_only']
# all[col].to_csv('/Users/cathy/GitProject/leetcode/problemset/all0415.csv',index=False)


today = all[col].loc[71:78]

#summary
for idx,row in today.iterrows():
    num = str(row['frontend_question_id'])
    lvl = row['level']
    ttl = row['title']
    url = row['question__title_slug']
    toc_str = '  * [{num}.\({lvl}\){ttl}](sql/{num}.{url}.md)'.format(num=num,lvl=lvl,ttl=ttl,url=url) 
    print(toc_str)


#readme
for idx,row in today.iterrows():
    num = str(row['frontend_question_id'])
    lvl = row['level']
    ttl = row['title']
    url = row['question__title_slug']
    toc_str = '* [{num}.\({lvl}\){ttl}]({num}.{url}.md)'.format(num=num,lvl=lvl,ttl=ttl,url=url) #readme
    print(toc_str)
    
#title and url
for idx,row in today.iterrows():
    num = str(row['frontend_question_id'])
    lvl = row['level']
    ttl = row['title']
    url = row['question__title_slug']
    copy = """\n\n\n
来源：力扣（LeetCode）\n
链接：https://leetcode-cn.com/problems/{url} \n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
\n\n
## Solution \n
```sql
\n\n
```
    """.format(url=url)
    toc_str = '# {num}.({lvl}) {ttl}'.format(num=num,lvl=lvl,ttl=ttl) #readme
    print(toc_str)
    print(copy)
    fname = '/Users/cathy/GitProject/leetcode/sql/{num}.{url}.md'.format(num=num,url=url)
    f = open(fname,'w')
    f.write(toc_str)
    f.write(copy)
    f.close()



