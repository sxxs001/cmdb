# -*-coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models

import uuid


#第三方模块
#from uuidfield import UUIDField
#from djorm_pguuid.fields import UUIDField
from macaddress.fields import MACAddressField
from mptt.models import MPTTModel, TreeForeignKey



# Create your models here.


class CommInfo(models.Model):
    '''
    '''
    _hostuse_status = (
        ('1', '在途'),#下单生产还未到机房里
        ('2', '已分配'),
        ('3', '预留'),#为某项目保留的资源，核算部门字段需填写预留部门。计算对应部门的使用成本
        ('4', '回收中'),#进入回收阶段
        ('5', '重装中'),#用于服务器重装流程，变化途径：在用，重装中，在用。
        ('6', '在用'),#在使用中，在线上
        ('7', '未用'),#资源未分配的状态
        ('8', '维护中'),#对应正在维修的场景
        ('9', '报废'),#服务器退出使用生命周期 对虚拟机就是销毁状态
        ('10', '下线')
    )
    hostuse_status = models.CharField('主机使用状态', choices=_hostuse_status, max_length=255, help_text='',
                                   default='6')
    _port_function = (
        ('1', '接入'),
        ('2', '上联'),
        ('3', '下联'),
        ('4', '对联'),
    )
    port_function = models.CharField('物理端口用途分类', choices=_port_function, max_length=255, help_text='',
                                   default='1')
    _domainname_function = (
        ('1.1', '公网域名'),
        ('2.1', '内部域名'),
    )
    _domainname_function = models.CharField('域名分类', choices=_domainname_function, max_length=255, help_text='',
                                     default='1')

    _ip_function = (
        ('1', '公网'),
        ('2', '内网/专线'),
        ('3', 'VIP'),
        ('4', 'DHCP'),
        ('5', 'F5'),
        ('6', 'NORMAL'),
    )
    ip_function = models.CharField('IP段用途分类', choices=_ip_function, max_length=255, help_text='',
                                     default='1')
    _host_function = (
        ('1.1', '数据库:MySQL'),
        ('1.2', '数据库:Influxdb'),
        ('1.3', '数据库:PostgreSQL'),
        ('1.4', '数据库:Oracle'),
        ('1.5', '数据库:Cassandra'),
        ('1.6', '数据库:MongoDB'),
        ('2.1', '基础组件:DNS'),
        ('3.1', '监控:Smokeping'),
        ('3.2', '监控:Bpm_url'),
        ('3.3', '监控:F5'),
        ('4.1', '数据分析:Greenplum'),
        ('5.1', '大数据:Hadoop'),
        ('6.1', '中间件:Corvus Proxy'),
        ('6.2', '中间件:Redis Node'),
        ('6.3', '中间件:Ceph'),
        ('6.4', '中间件:Etcd'),
        ('7.1', '搜索:Elasticsearch'),
        ('8.1', '虚拟化:Citrix'),
        ('10.1', '其他'),
    )
    host_function = models.CharField('主机用途', choices=_host_function, max_length=255, help_text='',
                                     default='1')
    _env = (
        ('1.1', 'alpha'),
        ('6.1', 'other/asd/dmz/zoo/nocTest'),
        ('3.1', 'pre'),
        ('2.1', 'beta'),
        ('4.1', 'ppe'),
        ('5.1', 'ops/prod/pro'),
    )
    env = models.CharField('环境', choices=_env, max_length=255, help_text='',
                                     default='1')

    # netaddr0 = MACAddressField(blank=True, integer=False)
    # netaddr1 = MACAddressField(blank=True, integer=False)
    # netaddr2 = MACAddressField(blank=True, integer=False)
    # netaddr3 = MACAddressField(blank=True, integer=False)
    # netaddr4 = MACAddressField(blank=True, integer=False)
    # netaddr5 = MACAddressField(blank=True, integer=False)


    class Meta:
        abstract = True




class Dept(models.Model):
    class Meta:
        verbose_name = '/Meta/部门'
        verbose_name_plural = '/Meta/部门'
    name = models.CharField('部门名称', max_length=255, unique=True, help_text='必须唯一&不能为空')
    ownername = models.CharField('部门负责人姓名', max_length=255, help_text='',
                                      null=True, blank=True)
    ownerid = models.CharField('部门负责人工号', max_length=255,  unique=True, help_text='必须唯一',
                                    null=True, blank=True)
    ownermail = models.EmailField('部门负责人邮箱地址',  unique=True, help_text='必须唯一',
                                        null=True, blank=True)
    _status = (
        ('T','正常'),
        ('F','异常')
    )
    status = models.CharField('部门状态',  choices=_status, max_length=255, help_text='',
                                   default='T')
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            null=True, blank=True)
    def __unicode__(self):
        return self.name
        #return ",".join([str(i.brand) for i in ModelConf.objects.get(brand_model=obj.brand_model)])


class OperatingSystem(models.Model):
    '''
    支持自动或者后台配置操作系统相关字段&内容
    '''
    '''
    除id外，不建议 对字段设置主键 primary_key=True, 设置则不会自建 自增id字段
    '''
    os_name = models.CharField('操作系统发行版',  max_length=255, unique=True,
                               help_text='必须唯一&不能为空')
    #operating_type =
    #memo = models.CharField('备注', max_length=300, help_text='备注', blank=True)
    '''
        这里不能使用ModelChoiceField 字段，允许用户后台添加，而非下拉框
    '''
    #class Meta:
    #    abstract = True

    def __unicode__(self):
        return self.os_name


class OperatingSystemVersion(models.Model):
    class Meta:
        verbose_name = '/Meta/操作系统'
        verbose_name_plural = '/Meta/操作系统'
    os_name = models.ForeignKey(OperatingSystem, related_name='OperatingSystem_Version',
                                verbose_name='操作系统发行版')
    os_version = models.CharField('版本号', max_length=255, unique=True,
                                  help_text='必须唯一&不能为空')
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            null=True, blank=True)
    def __unicode__(self):
        return self.os_version


class Provider(models.Model):
    class Meta:
        verbose_name = '/Meta/供应商'
        verbose_name_plural = '/Meta/供应商'

    #ptype = models.CharField('供应商类别', max_length=300, help_text='必须唯一&不能为空')

    _ptype = (
        ('1','公有云'),
        ('2','负载均衡'),
        ('3','带宽&专线'),
        ('4','服务器&主机'),
        ('5','交换机'),
        ('6','IDC'),
        ('7','存储'),
        ('8','安全&防火墙&证书'),
        ('9','系统集成&OA'),
    )
    type = models.CharField('供应商类别',  choices=_ptype, max_length=255, help_text='',
                             default='9')
    name = models.CharField('供应商公司', max_length=255,help_text='必须唯一&不能为空',
                              unique=True)
    owner = models.CharField('供应商负责人', max_length=255,help_text='必须唯一&不能为空',
                              unique=True)
    mb_num = models.CharField('供应商手机',max_length=255,help_text='必须唯一&不能为空',
                              unique=True)
    tel_num = models.CharField('供应商座机', max_length=255, help_text='选填',
                               blank=True, null=True)
    cooperate = models.CharField('供应商紧密度', max_length=255, help_text='选填',
                                  blank=True, null=True)
    memo = models.CharField('备注', max_length=255, help_text='选填',
                             blank=True, null=True)

    def __unicode__(self):
        return self.name


class ProviderIssue(models.Model):
    import django.utils.timezone as timezone
    #from cmdbv1.widgets import RichTextEditorWidget

    class Meta:
        verbose_name = '/Meta/供应商问题'
        verbose_name_plural = '/Meta/供应商问题'

    _stype = (
        ('1','NOC平台'),
        ('2','监控告警平台'),
        ('3','脚本&自动发现'),
        ('4','人工发现'),
        ('5','其他上报渠道'),
    )
    stype = models.CharField('问题来源渠道', choices=_stype,max_length=255, default='5')
    start_date = models.DateTimeField('问题发生时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择',default = timezone.now)
    _type = (
        ('1','硬件故障'),
        ('2','软件故障'),
        ('3','服务故障'),
        ('4','其他故障'),
    )
    type = models.CharField('故障分类',  choices=_type, max_length=255,default='1')
    #formfield_overrides = {
    #    models.TextField: {'widget': RichTextEditorWidget},
    #}
    name = models.ForeignKey(Provider, related_name='Provider_Name', verbose_name='供应商')
    remark = models.TextField('问题描述', max_length=1000,help_text='')

    solution = models.TextField('解决方案', max_length=1000,blank=True, null=True)
    progress = models.CharField('解决进度', max_length=255, help_text='',
                                blank=True, null=True)
    end_date = models.DateTimeField('问题解决时间', max_length=255,help_text='',
                                    blank=True, null=True)
    #pifaultduration = models.CharField('影响时长', max_length=300, help_text='可选',blank=True, null=True)
    memo = models.CharField('备注', max_length=255, help_text='选填',
                              blank=True, null=True)

    def __unicode__(self):
        return self.remark


class PrartType(models.Model):
    class Meta:
        verbose_name = '/Meta/配件类别'
        verbose_name_plural = '/Meta/配件类别'
    type = models.CharField('配件类别', max_length=255, help_text='必须唯一&不能为空',
                            unique=True)
    provider = models.ManyToManyField(Provider, related_name='provider', verbose_name='供应商')
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)
    def __unicode__(self):
        return self.type





class BrandModel(models.Model):
    class Meta:
        verbose_name = '/Meta/品牌型号'
        verbose_name_plural = '/Meta/品牌型号'
    brand = models.CharField('品牌', max_length=255, help_text='必须唯一&不能为空',)
                              #unique=True)'对于同品牌的不同机型来说，品牌字段肯定不能唯一'
    brand_model = models.CharField('型号', max_length=255, help_text='必须唯一&不能为空',
                                   unique=True)
    support_url = models.URLField('技术支持地址', max_length=255,default='' )
    memo = models.CharField('备注', max_length=255, help_text='选填',
                              blank=True, null=True)
    def __unicode__(self):
        return u'%s %s' % (self.brand, self.brand_model)
        #_a = self.brand + '  /  ' +self.brand_model
        #return _a



class ModelConf(models.Model):
    class Meta:
        verbose_name = '/Meta/机型配置'
        verbose_name_plural = '/Meta/机型配置'
    #brand_model = models.ForeignKey(BrandModel, related_name='model',verbose_name='品牌/型号')
    brand_model = models.ManyToManyField(BrandModel, related_name='model', verbose_name='品牌/型号')
    _type = (
        ('1','标配'),
        ('2','非标'),
    )
    type = models.CharField('是否标准化配置',  choices=_type, max_length=255,
                            help_text='',default='1')#

    _conf_sn = (
       ('1','py9'),
       ('2','py5'),
       ('3','py0_2'),
       ('4','py2'),
       ('5','vm1'),
       ('6','py1'),
       ('7','py0'),
       ('8','py0_3'),
       ('9','py3'),
       ('10','py4'),
       ('11','adb2'),
       ('12','tvm0'),
       ('13','avm11'),
       ('14','avm13'),
       ('15','vm3'),
       ('16','avm2'),
       ('17','py11'),
       ('18','adb1'),
    )
    conf_sn = models.CharField('机型编号',  choices=_conf_sn, max_length=300, help_text='必须唯一&不能为空',)#
    memory = models.CharField('内存', max_length=255, help_text='')
    cpu = models.CharField('CPU', max_length=255, help_text='')
    store = models.CharField('存储', max_length=255, help_text='')
    network = models.CharField('网络', max_length=255, help_text='')
    remark = models.CharField('描述', max_length=255, help_text='')

    memory_bench = models.CharField('内存性能', max_length=255, help_text='选填',
                                    blank=True, null=True)
    cpu_bench = models.CharField('CPU性能', max_length=255, help_text='选填',
                                 blank=True, null=True)
    store_bench = models.CharField('存储/IOPS性能', max_length=255, help_text='选填',
                                   blank=True, null=True)
    network_bench = models.CharField('网络/PPS性能', max_length=255, help_text='选填',
                                     blank=True, null=True)
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)
    def __unicode__(self):
        return self.type


class MPTTProduct(MPTTModel):
    class Meta:
        verbose_name = '/Meta/产品线&产品'
        verbose_name_plural = '/Meta/产品线&产品'

    _type = (
        ('1', '正常'),
        ('2', '异常'),
    )
    type = models.CharField('状态', choices=_type, max_length=255,
                            help_text='', default='1')
    name = models.CharField('产品', max_length=255, help_text='',
                            unique=True)
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)

    #title = models.CharField(max_length=50)

    parent = TreeForeignKey("self", blank=True, null=True, related_name="children", db_index=True)

    def __unicode__(self):
        return self.name
    class MPTTMeta:
        order_insertion_by = ['name']

    #def__unicode__(self):
    #returnself.title



class ProductLine(models.Model):
    class Meta:
        verbose_name = '/Meta/产品线'
        verbose_name_plural = '/Meta/产品线'
    _type = (
        ('1','正常'),
        ('2','异常'),
    )
    type = models.CharField('产品线状态',  choices=_type, max_length=255,
                            help_text='',default='1')
    name = models.CharField('产品线', max_length=255, help_text='',
                            unique=True)
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)
    def __unicode__(self):
        return self.name

class Product(models.Model):
    class Meta:
        verbose_name = '/Meta/产品'
        verbose_name_plural = '/Meta/产品'
    _type = (
        ('1','正常'),
        ('2','异常'),
    )
    type = models.CharField('产品状态',  choices=_type, max_length=255,
                            help_text='',default='1')
    name = models.ManyToManyField(ProductLine, related_name='Product_ProductLine', verbose_name='产品线')
    product = models.CharField('产品', max_length=255, help_text='')
                            #unique=True)
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)
    def __unicode__(self):
        return self.product

class Recover(models.Model):
    import django.utils.timezone as timezone

    class Meta:
        verbose_name = '/Meta/主机回收'
        verbose_name_plural = '/Meta/主机回收'

    uuid = models.UUIDField(default=uuid.uuid4, help_text='UUID',)  # (primary_key=True, default=uuid.uuid4, editable=False)
    start_date = models.DateTimeField('发起时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择', default=timezone.now)
    hostname = models.CharField('主机名', max_length=255, help_text='')
                            #unique=True)
    ip = models.GenericIPAddressField('主机IP地址')
    #name = models.ForeignKey(Provider, related_name='Provider_Name', verbose_name='供应商')
    dept = models.ForeignKey(Dept,related_name='dept', verbose_name='核算部门')
    _recover_type = (
        ('1','EWF'),
        ('2','其他'),
    )
    recover_type = models.CharField('回收人', choices=_recover_type, max_length=255,
                            help_text='', default='1')
    _status = (
        ('1', '完成'),
        ('2', '异常'),
    )
    status = models.CharField('回收结果', choices=_status, max_length=255,
                            help_text='', default='1')
    applicant = models.CharField('发起人', max_length=255, help_text='')
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)
    end_date = models.DateTimeField('结束时间', max_length=255, help_text='',
                                    blank=True, null=True)


class PhysicalError(models.Model):
    import django.utils.timezone as timezone

    class Meta:
        verbose_name = '/Meta/硬件故障'
        verbose_name_plural = '/Meta/硬件故障'

    type = models.ForeignKey(PrartType, related_name='PhysicalError_error', verbose_name='故障类别')
    remark = models.TextField('故障信息', max_length=255,help_text='')
    start_date = models.DateTimeField('发生时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择', default=timezone.now)
    _status = (
        ('1', '已修复'),
        ('2', '未修复'),
    )
    status = models.CharField('修复状态', choices=_status, max_length=255, default='2')
    end_date = models.DateTimeField('修复时间', max_length=255,help_text='',
                                    blank=True, null=True)
    open_date = models.DateTimeField('报修时间', max_length=255,
                                     help_text='默认值当前时间,可自行选择', default=timezone.now)

    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)



    hostname = models.CharField('主机名', max_length=255, help_text='')
    # unique=True)
    ip = models.GenericIPAddressField('主机IP地址')
    pebrand_model = models.ForeignKey(BrandModel, related_name='pebrand_model', verbose_name='品牌/型号')
    conf =  models.TextField('配置项', max_length=255, help_text='',
                             default = "网卡bond配置:\n cpu省电硬件配置:\n cpu省电软件配置:\n cpu超线程:\n bios版本:\n 文件系统xfs:\n 虚拟化超分:")


    def __unicode__(self):
        return self.remark


class Project(models.Model):
    import django.utils.timezone as timezone

    class Meta:
        verbose_name = '/Meta/项目'
        verbose_name_plural = '/Meta/项目'

    dept = models.ForeignKey(Dept, related_name='dept_project', verbose_name='部门')

    _status = (
        ('1', '正常'),
        ('2', '下线'),
    )
    status = models.CharField('项目状态', choices=_status, max_length=255, default='1')

    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)

    project = models.CharField('项目', max_length=255, help_text='',unique=True)

    def __unicode__(self):
        return self.project


class Staff(models.Model):
    import django.utils.timezone as timezone

    class Meta:
        verbose_name = '/Meta/人员信息'
        verbose_name_plural = '/Meta/人员信息'

    dept = models.ForeignKey(Dept, related_name='dept_staff', verbose_name='部门')

    _status = (
        ('1', '在职'),
        ('2', '异常'),
    )
    status = models.CharField('在职状态', choices=_status, max_length=255, default='1')
    number = models.CharField('工号', max_length=255, help_text='', unique=True)
    cnname = models.CharField('中文姓名', max_length=255, help_text='')
    name = models.CharField('英文姓名', max_length=255, help_text='')
    mail = models.EmailField('邮箱',  unique=True, help_text='必须唯一',
                                        null=True, blank=True)
    change_date = models.DateTimeField('最后更新时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择', default=timezone.now)
    memo = models.CharField('备注', max_length=255, help_text='选填',
                            blank=True, null=True)


    def __unicode__(self):
        #return self.cnname
        return u'%s %s %s %s %s' %(self.status, self.number, self.cnname, self.name, self.mail )
        #return ",".join( self.number, self.cnname, self.name, self.mail)
        #return u'%s %s' % (self.first_name, self.last_name)




class Idc(models.Model):
    class Meta:
        verbose_name = '/Meta/机房'
        verbose_name_plural = '/Meta/机房'

    name = models.CharField('机房', max_length=255, help_text='')
    remark = models.CharField('描述', max_length=1000, help_text='')
    address = models.CharField('地址', max_length=1000, help_text='')
    contact = models.CharField('联系人', max_length=1000, help_text='')

    mb_num = models.CharField('手机', max_length=255, help_text='必须唯一&不能为空',
                              unique=True)
    tel_num = models.CharField('座机', max_length=255, help_text='选填',
                               blank=True, null=True)
    code = models.CharField('机房编码', max_length=1000, help_text='')
    memo = models.TextField('备注', max_length=255, help_text='',
                             default = "宽带及类型:\n其他:")

    def __unicode__(self):
        return self.name

class Deliver(models.Model):
    import django.utils.timezone as timezone

    class Meta:
        verbose_name = '/Meta/主机交付'
        verbose_name_plural = '/Meta/主机交付'

    apply_date = models.DateTimeField('申请时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择', default=timezone.now)
    uuid = models.UUIDField(default=uuid.uuid4, help_text='UUID', )
    applicant_dept = models.ForeignKey(Dept, related_name='applicant_dept', verbose_name='申请部门')
    applicant_cname = models.ForeignKey(Staff, related_name='applicant_staff_cname', verbose_name='申请人')
    applicant_no = models.ForeignKey(Staff, related_name='applicant_staff_no', verbose_name='申请人工号')

    use_dept = models.ForeignKey(Dept, related_name='use_dept', verbose_name='使用部门')
    use_deptowner = models.ForeignKey(Dept, related_name='applicant_dept_owner', verbose_name='使用部门负责人')
    use_names = models.ForeignKey(Staff, related_name='applicant_staff_cnames', verbose_name='使用人')

    _apply_type = (
        ('1', '新增'),
        ('2', '扩容'),
    )
    type = models.CharField('需求类型', choices=_apply_type, max_length=255, default='1')
    modelconf = models.ForeignKey(ModelConf, related_name='modelconf_deliver', verbose_name='配置编号')
    count = models.IntegerField('申请数量',  help_text='')
    _status = (
        ('1', '交付完成'),
        ('2', '扩容'),
        ('3','待采购'),
        ('4','采购中'),
        ('5','待交付'),
        ('6', '交付中'),
    )
    status = models.CharField('状态', choices=_status, max_length=255, default='3')
    idc = models.ForeignKey(Idc, related_name='idc', verbose_name='机房')
    expect_date = models.DateTimeField('期待交付时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择', default=timezone.now)
    actual_date = models.DateTimeField('实际交付时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择',blank=True, null=True)

    memo = models.TextField('备注', max_length=255, help_text='',
                            default="评审单号:\n申请单号:\n主机名:\n其他:")


    def __unicode__(self):
        return self.type


class ContractConfig(models.Model):
    class Meta:
        verbose_name = '/Meta/合同详情[配置|钱款]'
        verbose_name_plural = '/Meta/合同详情[配置|钱款]'
    import django.utils.timezone as timezone
    prartyype = models.ForeignKey(PrartType, related_name='prartyype', verbose_name='配置类别')

    _conf = (
        ('1.1', "服务器类项目:\n类别:\n配置详情:\n数量:\n品牌/规格:\n单价:\n总价:\n"),
        ('2.1', "通信/通话类项目:\n类别:\n配置详情:\n数量:\n品牌/规格:\n单价:\n总价:\n"),
        ('3.1', "网络/带宽:\n类别:\n配置详情:\n数量:\n品牌/规格:\n单价:\n总价:\n"),
    )
    conf = models.TextField('配置', choices=_conf, max_length=255)

    _cost = (
        ('1.1', "服务器类项目:\n类别:\n配置详情:\n数量:\n品牌/规格:\n单价:\n总价:\n"),
        ('2.1', "通信/通话类项目:\n初装费:\n月固定费用:\n长途费用:\n国际费用:\n市话费用/分钟:\n长途费用/分钟:\n总价:\n优惠价/优惠方式:"),
        ('3.1', "网络/带宽:\n初装费:\n每月固定费用:\n优惠价/优惠方式:"),
    )
    cost = models.TextField('报价', choices=_cost, max_length=255)

    _status = (
        ('1.1', '询价'),
        ('2.1', '比价'),
    )
    status = models.CharField('状态', choices=_status, max_length=255)
    _stage = (
        ('1.1', '首次'),
        ('2.1', '调整'),
    )
    stage = models.CharField('阶段', choices=_stage, max_length=255)

    op_date = models.DateTimeField('变更时间', max_length=255,
                                   help_text='默认值当前时间,可自行选择', default=timezone.now)
    upload = models.ImageField('上传附件[账单/合同/发票/邮件],可图片外格式')

    def __unicode__(self):
        return self.conf


class Contract(models.Model):
    import django.utils.timezone as timezone

    class Meta:
        verbose_name = '/Meta/合同'
        verbose_name_plural = '/Meta/合同'

    _status = (
        ('1', '等待供应商发送合同电子版'),
        ('2', '法务审批中'),
        ('3', '快递盖章纸质合同制供应商'),
        ('4', '供应商录入'),
        ('5', '供应商入库'),
        ('6', '供应商下单'),
    )
    status = models.CharField('状态', choices=_status, max_length=255, default='6')
    sn = models.IntegerField('财务编号', help_text='财务编号')
    aparty = models.CharField('甲方', max_length=255, )
    bparty = models.ForeignKey(Provider,related_name='bparty', verbose_name='乙方' )
    project = models.CharField('项目', max_length=255, )
    contract_amount = models.TextField('合同金额', max_length=255, help_text='',
                            default="合同金额:\n服务器金额:\n其他金额:\n其他:")
    delivery_time = models.DateTimeField('到货时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择', default=timezone.now)
    receipt_place = models.CharField('收货地点', max_length=255, help_text='')
    advance_payment = models.TextField('预付款', max_length=255, help_text='',
                            default="预付款:\n付款日期:\n比例:\n其他:")
    final_payment = models.TextField('尾款', max_length=255, help_text='',
                                       default="尾款:\n付款日期:\n比例:\n其他:")
    signing_date = models.DateTimeField('签订时间', max_length=255,
                                      help_text='默认值当前时间,可自行选择', default=timezone.now)
    conf_details = models.ManyToManyField(ContractConfig, related_name='contractconfig', verbose_name='配置详情')
    memo = models.TextField('备注', max_length=255, help_text='',
                            default="比价时间:\n比价过程:\n决策时间:\n安装调试时间:\n首次付款时间:\n其他:[如包括赠送多少IP]")


    def __unicode__(self):
        return self.project





