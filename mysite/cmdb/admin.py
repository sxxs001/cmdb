# -*-coding:utf-8 -*-

from django.contrib import admin

# Register your models here.
from .models import OperatingSystem, Dept, OperatingSystemVersion,\
    Provider, ProviderIssue,PrartType,BrandModel,Product,ProductLine,\
    Recover,PhysicalError,Project,Staff,Idc,ModelConf,Deliver,ContractConfig,Contract,MPTTProduct

from django_extensions.admin import ForeignKeyAutocompleteAdmin


from mptt.admin import MPTTModelAdmin



class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('get_os_info', 'os_version', 'get_memo_info')
    def get_os_info(self,obj):
        return u'%s'% OperatingSystemVersion.objects.get(os_version=obj.os_version).os_name
    def get_memo_info(self,obj):
        return u'%s'% OperatingSystemVersion.objects.get(os_version=obj.os_version).memo
    get_os_info.short_description = u'操作系统发行版'
    get_memo_info.short_description = u'备注'
    search_fields = ('os_version', 'memo', 'os_name__os_name')


class OperatingSystemVersionInline(admin.TabularInline):
    model = OperatingSystemVersion


class OperatingSystemVersionAdmin(admin.ModelAdmin):
    inlines = [OperatingSystemVersionInline]
    list_display = ('os_name', 'get_os_info')
    def get_os_info(self,obj):
    #def _get_os_info():
        #return u'%s'%obj.os_version
        #Sales.objects.filter(user=obj)
        _os_version = ''
        for _p in OperatingSystem.objects.values():
            for _t in OperatingSystemVersion.objects.filter(os_name_id=_p['id']):
                _os_version += str( _t )
                #pass
        return _os_version
    get_os_info.short_description = u'小版本'



class DeptAdmin(admin.ModelAdmin):
    list_display = ('name', 'ownername','ownerid','ownermail','status','memo')
    fieldsets = (
        ['主要信息',{
            'fields':('name','ownername','ownerid','ownermail'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('status','memo'),
        }]
    )
    search_fields = ('name', 'ownername','ownerid',
                     'ownermail','status','memo')

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('type', 'name','owner','mb_num','tel_num','cooperate','memo')
    fieldsets = (
        ['主要信息',{
            'fields':('type','name','owner','mb_num'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('tel_num','cooperate','memo'),
        }]
    )
    search_fields = ('type', 'name','owner','mb_num','tel_num','cooperate','memo')


#class OperatingSystemVersionInline(admin.TabularInline):
#    model = OperatingSystemVersion

#class ProviderIssueAdmin(ForeignKeyAutocompleteAdmin):
class ProviderIssueAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('stype','start_date', 'get_name','type','remark',
                    'progress','end_date','solution','memo')



    def get_name(self,obj):
        return u'%s'% ProviderIssue.objects.get(remark=obj.remark).name
        get_name.short_description = u'供应商'

    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('stype','start_date','name','type','remark'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('solution','progress','end_date','memo'),
        }]
    )
    search_fields = ('stype','type','remark',
                     'progress','solution','memo','name__name')
    #不能搜索 start_date end_date 对象

class PrartTypeAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('type','memo')
    filter_horizontal = ('provider',)
    fieldsets = (
        ['主要信息', {
            # 'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields': ('type', 'provider',),
        }],
        ['其他信息', {
            # 'classes': ('collapse',), # CSS
            'fields': ('memo',),
        }]
    )
    search_fields = ('type','memo')


'''
仅限于外键模式
#class PhysicalConfInline(admin.StackedInline):
#    model = PhysicalConf

#class PhysicalConfAdmin(admin.ModelAdmin):
#    inlines = [PhysicalConfInline]
'''


class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('brand','brand_model', 'support_url','memo')
    search_fields = ('brand','brand_model', 'support_url','memo')

#class ModelConfInline(admin.StackedInline):
#    model = ModelConf


class ModelConfAdmin(admin.ModelAdmin):
    #inlines = [ModelConfInline]

    def get_brandmodel_info(self,obj):
    #     #return u'%s'% OperatingSystemVersion.objects.get(os_version=obj.os_version).memo
    #     #return u'%s %s'% str  ( ModelConf.objects.get(brand_model=obj.brand_model).brand_model, ModelConf.objects.get(brand_model=obj.brand_model).brand_model )
    #
        #return u'%s' % ModelConf.objects.get(memory='2')
        #return u'%s' % str(ModelConf.objects.get(brand_model=obj.brand_model).brand_model)
        #_t = ''
        #for i in ModelConf.objects.get(memory=obj.memory).brand_model.all():
        #for i in ModelConf.objects.get(brand_model=obj.brand_model).brand_model.all():
        #    _t += str( i )
        #return u'%s' % _t

        return ",".join([ str(i.brand)  for i in ModelConf.objects.get(brand_model=obj.brand_model) ])
    #BrandModel.objects.get(brand_model=obj.brand_model).brand

    get_brandmodel_info.short_description = u'品牌/型号'

    #def get_brand_model_info(self,obj):
    #    return u'%s'% OperatingSystemVersion.objects.get(os_version=obj.os_version).memo
    #get_os_info.short_description = u'操作系统发行版'
    filter_horizontal = ('brand_model',)


    list_display = ('type', 'conf_sn','memory','cpu','store','network','remark','memory_bench','cpu_bench','store_bench','network_bench','memo')
    #list_display = (
    #'brand_model', 'type', 'memory', 'cpu', 'store', 'network', 'remark', 'memory_bench', 'cpu_bench',
    #'store_bench', 'network_bench', 'memo')
    fieldsets = (
        ['主要信息',{
            'fields':('brand_model','conf_sn','type','memory','cpu','store','network','remark'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('memory_bench','cpu_bench','store_bench','network_bench','memo'),
        }]
    )
#     search_fields = ('pctype', 'pcdesc','pcmemory','pccpu','pcstore','pcnt','pcmemo')
#


class MPTTProductAdmin(admin.ModelAdmin):

    list_display = ('type', 'name','memo')
    # fieldsets = (
    #     ['主要信息',{
    #         'fields':('type','name',),
    #     }],
    #     ['其他信息',{
    #         #'classes': ('collapse',), # CSS
    #         'fields': ('memo',),
    #     }]
    # )


class ProductLineAdmin(admin.ModelAdmin):

    list_display = ('type', 'name','memo')
    fieldsets = (
        ['主要信息',{
            'fields':('type','name',),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('memo',),
        }]
    )


class ProductAdmin(admin.ModelAdmin):

    list_display = ('type','product','memo')
    filter_horizontal = ('name',)

    fieldsets = (
        ['主要信息',{
            'fields':('type','name','product'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('memo',),
        }]
    )


class RecoverAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('dept','uuid','recover_type','start_date','hostname', 'ip',
                    'status','applicant','end_date','memo')

    def get_name(self,obj):
        return u'%s'% ProviderIssue.objects.get(remark=obj.remark).name
        get_name.short_description = u'供应商'

    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('dept','uuid','start_date','hostname','ip','applicant'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('recover_type','status','end_date','memo'),
        }]
    )
    search_fields = ('dept','recover_type','hostname', 'ip',
                    'status','applicant','memo')
    #不能搜索 start_date end_date 对象




class PhysicalErrorAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('type','remark','start_date','status', 'end_date',
                    'open_date','hostname','ip','pebrand_model','conf','memo')

    def get_name(self,obj):
        return u'%s'% ProviderIssue.objects.get(remark=obj.remark).name
        get_name.short_description = u'供应商'

    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('type','remark','start_date','open_date','hostname','ip','pebrand_model'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('status','end_date','conf','memo'),
        }]
    )
    #search_fields = ('dept','recover_type','hostname', 'ip',
    #                'status','applicant','memo')
    #不能搜索 start_date end_date 对象



class ProjectAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('status','dept','project','memo')

    def get_name(self,obj):
        return u'%s'% ProviderIssue.objects.get(remark=obj.remark).name
        get_name.short_description = u'供应商'

    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('status','dept','project',),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('memo',),
        }]
    )
    #search_fields = ('dept','recover_type','hostname', 'ip',
    #                'status','applicant','memo')
    #不能搜索 start_date end_date 对象



class StaffAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('dept','status','number','cnname','name','mail','change_date','memo')

    def get_name(self,obj):
        return u'%s'% ProviderIssue.objects.get(remark=obj.remark).name
        get_name.short_description = u'供应商'

    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('dept','status','number','cnname','name','mail'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('change_date','memo',),
        }]
    )
    #search_fields = ('dept','recover_type','hostname', 'ip',
    #                'status','applicant','memo')
    #不能搜索 start_date end_date 对象



class IdcAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('name','remark','address','contact','mb_num','tel_num','code','memo')

    def get_name(self,obj):
        return u'%s'% ProviderIssue.objects.get(remark=obj.remark).name
        get_name.short_description = u'供应商'

    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('name','remark','address','contact','mb_num','tel_num','code'),
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('memo',),
        }]
    )
    #search_fields = ('dept','recover_type','hostname', 'ip',
    #                'status','applicant','memo')
    #不能搜索 start_date end_date 对象



class DeliverAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('apply_date','uuid','applicant_dept','applicant_cname','applicant_no',
                    'use_dept','use_deptowner','use_names',
                    'type','modelconf','count','status','idc','expect_date','actual_date','memo')

    def get_name(self,obj):
        return u'%s'% ProviderIssue.objects.get(remark=obj.remark).name
        get_name.short_description = u'供应商'

    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('apply_date','uuid','applicant_dept','applicant_cname','applicant_no',
                      'use_dept','use_deptowner','use_names',
                      'type', 'modelconf', 'count', 'status', 'idc', 'expect_date', )
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('actual_date','memo',),
        }]
    )
    #search_fields = ('dept','recover_type','hostname', 'ip',
    #                'status','applicant','memo')
    #不能搜索 start_date end_date 对象




class ContractConfigAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    list_display = ('prartyype','conf','cost','status',
                    'stage','op_date','upload')

    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('prartyype','conf','cost','status',
                      'stage','op_date', 'upload')
        }],
        #['其他信息',{
        #    #'classes': ('collapse',), # CSS
        #    'fields': ('',),
        #}]
    )
    #search_fields = ('dept','recover_type','hostname', 'ip',
    #                'status','applicant','memo')
    #不能搜索 start_date end_date 对象




class ContractAdmin(admin.ModelAdmin):
    #inlines = [OperatingSystemVersionInline]

    #raw_id_fields = ("piname",)
    #list_display_links = ("get_pcname",)
    filter_horizontal = ('conf_details',)
    list_display = ('status','sn','aparty','bparty','project','contract_amount',
                    'delivery_time','receipt_place','advance_payment',
                    'final_payment','signing_date','memo')



    #filter_horizontal = ('piname',)
    fieldsets = (
        ['主要信息',{
            #'fields':('pistype','piname','pitype','piremark',('sdfsdfsdf',{'fields':['pistartdate']})),
            'fields':('status','sn','aparty','bparty','project','contract_amount',
                      'delivery_time','receipt_place','advance_payment',
                      'final_payment', 'signing_date', 'conf_details', )
        }],
        ['其他信息',{
            #'classes': ('collapse',), # CSS
            'fields': ('memo',),
        }]
    )
    #search_fields = ('dept','recover_type','hostname', 'ip',
    #                'status','applicant','memo')
    #不能搜索 start_date end_date 对象




admin.site.register(OperatingSystem,OperatingSystemVersionAdmin)
admin.site.register(Dept, DeptAdmin)
admin.site.register(OperatingSystemVersion,OperatingSystemAdmin)
admin.site.register(Provider,ProviderAdmin)
admin.site.register(ProviderIssue,ProviderIssueAdmin)
admin.site.register(PrartType,PrartTypeAdmin)
admin.site.register(BrandModel,BrandModelAdmin)
admin.site.register(ModelConf,ModelConfAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductLine,ProductLineAdmin)
admin.site.register(Recover,RecoverAdmin)
admin.site.register(PhysicalError,PhysicalErrorAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Idc,IdcAdmin)
admin.site.register(Deliver,DeliverAdmin)

admin.site.register(ContractConfig,ContractConfigAdmin)
admin.site.register(Contract,ContractAdmin)

admin.site.register(MPTTProduct,MPTTProductAdmin)
#admin.site.register(Suppliers, SuppliersAdmin)
#admin.site.register()