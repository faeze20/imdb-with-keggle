import pandas as pd
data=pd.read_csv("imdb_clean.csv")
print(data)
print(data.info())
print("mean -relase_year",data["release_year"].mean())
print(data['release_year'].count())
print(data[data["release_year"]==1997].count())
print(data[data["release_year"]==1994 ].count())
maxi=((data.groupby('release_year').count()).max())
print(maxi)
print((data.groupby('release_year').count()))
# print(data[data["release_year"][]]) 
# ham ba grouh bandi ham ba idmax hardo yekkar mikonan

# number year for maximom films
print((data.groupby('release_year').count()).max())
print(data["release_year"].value_counts().idxmax())

max_count = data.groupby('release_year').count()['title'].idxmax()
print("Max count:", max_count)


print("run_time",data.groupby("runtime").max())
print("max_time",data.groupby("runtime").min())
print("min film",data.groupby("title").min())
min_time=(data["runtime"].min())#کوتاهترین فیلم
title=data[data["runtime"]==min_time]["title"]
year=data[data["runtime"]==min_time]["release_year"]
print("min show time is: ","film:",title, year, min_time)
print(year)

#بهترین انیمیشن
rating=data["rating"].max()

#تعداد فیلم های اکشن و دزام
print("best animation is :",rating ,"  ",data[data["rating"]==rating]["title"])
print("dram is :",data[data["genre"]=="Drama"].count())
print("action is :",data[data["genre"]=="Action"].count())
# فیلم ها بدترین 
min_imdb=data["rating"].min()
print("min -imdb", data[data["rating"]==min_imdb]["title"])


print("imdb>8",data[data["rating"]>8].count())
print("imdb>9",data[data["rating"]>9].count())

#بهترین فیلم ها
max_imdb=data["rating"].max()
print("best_film", data[data["rating"]==max_imdb]["title"])


#کدوم فیلم بیشتر از یک نسخه تولید شده؟
print(data.groupby("title").value_counts().min())
s=(data["release_year"].max())
print(s)
print(data[data["release_year"]==s]["title"])

# شمارش تعداد تکرار هر فیلم بر اساس عنوان
film_counts = data['title'].value_counts()

# فیلم‌هایی که بیشتر از یک نسخه تولید شده‌اند
multi_version_films = film_counts[film_counts > 1]

print("فیلم‌هایی که بیشتر از یک نسخه تولید شده‌اند:")
print(multi_version_films)