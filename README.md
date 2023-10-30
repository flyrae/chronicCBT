    - `register.html`: 这个文件是应用程序注册页面的HTML模板。它扩展了`base.html`模板，并包括特定于注册页面的内容。
    - `profile.html`: 这个文件是应用程序用户个人资料页面的HTML模板。它扩展了`base.html`模板，并包括特定于用户个人资料页面的内容。
- `tests/`: 这个目录包含应用程序的单元测试。
  - `__init__.py`: 这个文件是单元测试的入口点。它设置测试环境并导入必要的模块。
  - `test_routes.py`: 这个文件包含应用程序路由的单元测试。它导入必要的模块并为每个路由定义测试用例。
- `requirements.txt`: 这个文件列出了项目所需的Python软件包。
- `run.py`: 这个文件是运行应用程序的入口点。它导入`app`模块并启动Flask应用程序。
- `README.md`: 这个文件包含项目的文档。

## 入门

要运行应用程序，请按照以下步骤操作：

1. 运行`pip install -r requirements.txt`安装所需的Python软件包。
2. 运行`python run.py`启动应用程序。
3. 打开Web浏览器并导航到`http://localhost:5000`以查看主页。

## 测试

要运行单元测试，请按照以下步骤操作：

1. 运行`pip install -r requirements.txt`安装所需的Python软件包。
2. 运行`python -m unittest discover -s tests`运行测试。

## 许可证
