from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
methodProsal = ['Name','Abstract','Kind of Used Data','A/B Testing','Association Rules','Bayesian Techniques','CNNs','Collaborative Filtering','Cross-Validation','Data Visualization','Decision Trees',
                'Ensemble Methods','Evolutionary Approaches','GANs','Gradient Boosted Machines','HMMs','kNN and Other Clustering','Lift Analysis',
                'Logistic Regression','Markov Logic Networks','Naive Bayes','Natural Language Processing','Neural Networks','PCA and Dimensionality Reduction',
                'Prescriptive Modeling','Random Forests','Recommender Systems','RNNs','Segmentation','Simulation','SVMs','Text Analytics','Time Series Analysis','LinkPdf']
keywordOfMethod = ['A/B Testing','Association Rules','Bayesian Techniques','CNNs','Collaborative Filtering','Cross-Validation','Data Visualization','Decision Trees',
                'Ensemble Methods','Evolutionary Approaches','GANs','Gradient Boosted Machines','HMMs','kNN and Other Clustering','Lift Analysis',
                'Logistic Regression','Markov Logic Networks','Naive Bayes','Natural Language Processing','Neural Networks','PCA and Dimensionality Reduction',
                'Prescriptive Modeling','Random Forests','Recommender Systems','RNNs','Segmentation','Simulation','SVMs','Text Analytics','Time Series Analysis']
# 30 topics
# methodProsal = ['Name','Abstract','LinkPdf']
df = pd.DataFrame(columns=methodProsal)
df_statistical = pd.DataFrame(columns=keywordOfMethod)

# driver = webdriver.PhantomJS()
driver = webdriver.Chrome(executable_path='D:/chromedriver_win32/chromedriver.exe')
url =['http://papers.nips.cc/book/advances-in-neural-information-processing-systems-28-2015', 'http://papers.nips.cc/book/advances-in-neural-information-processing-systems-29-2016']
fileName = ['pfiev2015.csv','pfiev2016.csv']
def crawlPaperFromNIPS(url):
    driver.get(url)
    eleList = driver.find_elements_by_tag_name("li")
    listOfPaper = []
   
    index = 0
    i=1
    try:
    #     for i in range(1,len(ele)):
        while eleList:
            ele = eleList.pop()
    #         name = ele.text
            urlPdf = "/html/body/div[2]/div/ul/li[" + str(i) +"]/a[1]"
    #         driverAbstract = webdriver.PhantomJS() # webdriver.Chrome()
            urlAbstract = ele.find_element(By.XPATH,urlPdf).get_attribute('href')
            print(i,'. ',urlAbstract)
            listOfPaper.append(urlAbstract)
            i = i+1
            if(i>10):
                break;
    except:
        pass
    # finally:
    #     df.to_csv("ListOfPaper.csv")
    
    #     driver.close()
    #     driver.quit()
    
    while listOfPaper:
        ele = listOfPaper.pop()
        driver.get(ele)
        abstract = driver.find_element(By.CLASS_NAME, "abstract").text
        name = driver.find_element(By.CLASS_NAME,"subtitle").text
        linkpdf = ele + ".pdf"
        df.at[index,"Name"] = name
        df.at[index,"LinkPdf"] = linkpdf
        df.at[index,"Abstract"] = abstract
        #find research method of the paper
        abstract = str(abstract).lower()
        for item in keywordOfMethod:
            if item.lower() in abstract:
                df.at[index,item] = 'X'
                df_statistical.at[index,item] = 'X'
                break
            else:
                df.at[index,item] = "O"
                df_statistical.at[index,item] = 'O'
        #====end find===================== 
        index=index+1 
        if(index>10):
            break;
    return df
for i in range(0,len(url)):
    crawlPaperFromNIPS(url[i]).to_csv(fileName[i])
    df_statistical.apply(pd.value_counts).to_csv("statistical_"+fileName[i])
    df_statistical.drop(df_statistical.index, inplace=True)
driver.close()
driver.quit()


