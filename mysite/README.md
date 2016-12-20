
Installation
        hosts配置 127.0.0.1 cmdb.ops.com
        克隆至家目录

        [启动]
                sudo nginx
                cd ~/PycharmProjects/myvirtual_env/bin
                source activate

                mysite uwsgi --ini /Users/kk/PycharmProjects/mysite/mysite_uwsgi.ini

                cd ../../mysite
                tail -f cmdb.ops.com_* mysite_uwsgi.log

        [静态文件修改后同步]
                python manage.py collectstatic ; touch /Users/kk/PycharmProjects/mysite/mysite_uwsgi.pid; sudo nginx -t ;sudo nginx -s reload



Documentation
	[接口]
		http://cmdb.ops.com/api/
	
	
			
Building the Docs

	
Contributing
	Pillow
	django-macaddress
	django-mptt


Change Log
	v20161214
		改造产品线/产品 数据形态为 树状数据结构【django-mptt】
	v20161213
		创建REST API（django-rest-framework）
	






