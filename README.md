# SCM接口自动化测试代码开发进度
- 物料
  - 物料通用数据- 物料分类
  - 物料分类
  - 物料信息  
  - 物料单位  
  - 物料单位换算  
- 业务伙伴
  - 业务伙伴信息
- 基本信息
  - 币种
  - 税率
  - 原因  


# 运行说明
-  在根目录下的 run.sh文件可以直接运行自动化代码
```shell
pytest testcase/ --alluredir=./result
# 需更换至运行环境的allure路径
/opt/homebrew/bin/allure generate ./result -c -o ./result/report/

/opt/homebrew/bin/allure serve ./result/ -p 8080
```

# 代码调试说明
- 调试单个测试用例时，在utils/env.yml文件中将debug改为True即可。
- run.py 运行时改为False
