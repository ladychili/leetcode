# encoding=utf-8
import json 
import pandas as pd

df = pd.read_json('/Users/cathy/GitProject/leetcode/problemset/prob0907_db.json')
all = df[['frontendQuestionId','title', 'titleCn', 'titleSlug', 'difficulty', 'paidOnly']]
all.loc[:,'difficulty'] = all.difficulty.str.capitalize()
all.to_csv('/Users/cathy/GitProject/leetcode/problemset/db0907.csv',index=False)


#### all prob
# all = db_df.merge(df, how='right', left_on='question_id', right_on='questionId')\
#            .astype({'frontend_question_id':str})\
#             .sort_values(['frontend_question_id'])\
#             .reset_index(drop=True)

# all['level'] = all.level.map({1:'Easy',2:'Medium',3:'Hard'})
# col = ['frontend_question_id', 'questionId','title', 'question__title', 'question__title_slug', 'level', 'paid_only']
# all[col].to_csv('/Users/cathy/GitProject/leetcode/problemset/all0415.csv',index=False)


today = all.loc[166:170]

#summary
for idx,row in today.iterrows():
    num = str(row['frontendQuestionId'])
    lvl = row['difficulty']
    ttl = row['title']
    url = row['titleSlug']
    toc_str = '  * [{num}.\({lvl}\){ttl}](sql/{num}.{url}.md)'.format(num=num,lvl=lvl,ttl=ttl,url=url) 
    print(toc_str)


#readme
for idx,row in today.iterrows():
    num = str(row['frontendQuestionId'])
    lvl = row['difficulty']
    ttl = row['title']
    url = row['titleSlug']
    toc_str = '* [{num}.\({lvl}\){ttl}]({num}.{url}.md)'.format(num=num,lvl=lvl,ttl=ttl,url=url) #readme
    print(toc_str)
    
#title and url
for idx,row in today.iterrows():
    num = str(row['frontendQuestionId'])
    lvl = row['difficulty']
    ttl = row['title']
    url = row['titleSlug']
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
    # print(toc_str)
    # print(copy)
    fname = '/Users/cathy/GitProject/leetcode/sql/{num}.{url}.md'.format(num=num,url=url)
    f = open(fname,'w')
    f.write(toc_str)
    f.write(copy)
    f.close()



