# Title     : TODO
# Objective : TODO
# Created by: lenovo
# Created on: 2020/3/26

#创建一个二维矩阵
x <- matrix(nrow = 2,ncol = 2)

y = matrix(1:4,nrow=2,ncol=2)

#创建三维数组dim = c(3,3,3) 3个 3X3的矩阵
arr <- array(c(1,2),dim = c(3,3,3))

attributes(y)

dimnames(y) = list(c("a","b"),c("c","d"))

#因子 factor
  ##1 分类数据/有序无序

#基线为female
f1 <- factor(c("female","male","female","male",'female'))

# 基线为male
f2 <- factor(c("female","male","female","male","make"),level = c("male","female","make"))

#查看因子
table(f2)
class(unclass(f2))

#缺失值 NA NaN
#NaN属于NA 但是NA不属于NaN

v1 <- c(1,NA,2,NA)

is.na(v1)

##数据框 data frame

df1 = data.frame(id = c(1,2,3,4), name = c("a","b","c","d"),score = c(99,94,96,100))

df2 = data.frame(id = c(1,2,3,4),score = c(99,94,96,100))
#转换为矩阵
m2 <- data.matrix(df2)


#时间和日期
d1 = date()  #字符串
d2 = Sys.Date() #日期
d3 = as.Date("2019-07-31") #日期

weekdays(d3)
months(d3)
julian(d3)
quarters(d3)

as.numeric(d2-d3)
d2-d3


#时间

t1 = Sys.time()

t2 = as.POSIXlt(t1)

t2$sec

##c1
c1 <- c(1,23,4)
c2 <- seq(1,9, by = 0.1)
c3 = c('a','b','c','d')

## 向量切片
t <- c3[c(1,2)] # a b

# 2是否属于该向量
2 %in% c1

## 向量运算  不同长度的向量做运算应该是 整数倍的关系

c5 <- c(1,2,3,4,5,6)
c6 <- c(1,2,3)

c5 - c6

## 对向量进行排序 decreasing = TRUE 为倒序排序

c6 <- sort(c5,decreasing = TRUE)


##列表
list_data <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
                  list("green",12.3))

## 给每个元素命名 通过data$name 的方式进行调用查看
names(list_data) = c('c1','m1','l1')

##添加元素 更新元素

list_data[4] <- "new element"
list_data[4] <- "new element"


# switch
common.compute <- function(x,type){

  switch(
    type,
    sum = sum(x),
    mean = mean(x),
    sqrt = sqrt(x),
    max = max(x)
  )

}

#repeat
cond <- 1
repeat{
  print("loop")

  cond <- cond + 1

  if (cond > 5){
    break()
  }

}

#for letters <- c(a:z)
# next 就是python中的 continue
les = letters[1:26]

for (i in les){

  if (i == 'a'){
    next()
  }
  print(i)
}


library(openxlsx)
data<- read.xlsx("F:\\R-workspace\\data\\nation_code.xlsx", sheet = 1)
View(data)



# 数据组合
city <- c("Tampa","Seattle","Hartford","Denver")
state <- c("FL","WA","CT","CO")
zipcode <- c(33602,98104,06161,80294)

addresses <- cbind(city,state,zipcode)  # 为4行3列的矩阵


new.address <- data.frame(
  city = c("Lowry","Charlotte"),
  state = c("CO","FL"),
  zipcode = c("80230","33949"),
  stringsAsFactors = FALSE
)


library(MASS)
merged.Pima <- merge(x = Pima.te, y = Pima.tr,
                     by.x = c("bp", "bmi"),
                     by.y = c("bp", "bmi")
)
print(merged.Pima)
nrow(merged.Pima)


ship <- ships

##  类似于逆透视操作 对每列的值加上唯一标识码进行标识
molten.ships <- melt(ships, id = c("type","year"))
library(reshape)

## 对type+year 进行分组 对variableb标识的数据进行求和
recasted.ship <- cast(molten.ships, type+year~variable,sum)

##paste(a,b,c, sep = "*") collapse 用于集合类 sep 用于单个对象
a <- "1"
b <- "2"
c <- "3"
paste(a,b,c, sep = "*")

d = c("1","2","3")
paste(d,collapse = "*  ")


##format(x, digits, nsmall, scientific, width, justify = c("left", "right", "centre", "none"))

#x是向量输入。
#digits是显示的总位数。
##科学设置为TRUE以显示科学记数法。
#width指示通过在开始处填充空白来显示的最小宽度。
#justify是字符串向左，右或中心的显示

# 求字符串的长度
str <- 'ab  dc'
nchar(str)

toupper(str)
tolower(str)
substring(str,1,2)

## 列表的合并

list1 = list(1,2,3)
list2 = list('aa','b')


merge_list = c(list1,list2)

