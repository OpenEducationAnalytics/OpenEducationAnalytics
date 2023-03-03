import uuid
from .forms import *
from OEA_Portal.core.services.AssetManagementService.asset import BaseOEAAsset
from OEA_Portal.core.services.AssetManagementService.operations import *
from OEA_Portal.auth.AzureClient import AzureClient
from django.http.response import HttpResponse
from OEA_Portal.core.services.utils import *
from OEA_Portal.core.services.SynapseManagementService import SynapseManagementService
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.shortcuts import redirect
from OEA_Portal.core.OEAInstaller import OEAInstaller

base_url = 'temp'

class HomeView(TemplateView):
    template_name = 'core/homepage.html'
    config = get_config_data()

    def get(self, *args, **kwargs):
        global base_url
        if('base_url' in self.request.GET):
            base_url = self.request.GET['base_url']
        subscriptions = get_all_subscriptions_in_tenant()
        workspaces = get_all_workspaces_in_subscription(AzureClient(self.config['SubscriptionId'], self.config['SubscriptionId']))
        return self.render_to_response({'base_url':self.config['BaseURL'],
        'tenants':['123', '456'],
        'subscriptions':subscriptions,
        'workspaces':workspaces
        })

class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'
    config = get_config_data()

    def get(self, *args, **kwargs):
        azure_client = AzureClient(self.config['SubscriptionId'], self.config['SubscriptionId'])
        workspace = get_workspace_object(azure_client, self.config['WorkspaceName'])
        modules, packages, schemas, version = get_installed_assets_in_workspace(self.config['WorkspaceName'], azure_client)
        return self.render_to_response({'base_url':self.config['BaseURL'],
            'modules':modules,
            'packages':packages,
            'schemas':schemas,
            'oea_version': version,
            'storage_account': workspace.storage_account
        })

class InstallationFormView(TemplateView):
    template_name = 'core/installation_form.html'
    config = get_config_data()

    def get_context_data(self, **kwargs):
        context = super(InstallationFormView, self).get_context_data(**kwargs)
        context['base_url'] = base_url
        return context

    def get(self, *args, **kwargs):
        version_choices = [(x,x) for x in self.config['OEA_Versions']]
        form = InstallationForm(version_choices)
        return self.render_to_response({'form':form})

    def post(self, *args, **kwargs):
        tenant_id = self.config['TenantId']
        subscription_id = self.config['SubscriptionId']
        include_groups = self.request.POST.get('include_groups')
        oea_version = self.request.POST.get('oea_version')
        oea_suffix = self.request.POST.get('oea_suffix')
        location = self.request.POST.get('location')

        request_id = uuid.uuid4()
        oea_installer = OEAInstaller(tenant_id, subscription_id, oea_suffix,oea_version, location, include_groups)
        oea_installer.install(request_id)
        return redirect('home')

class AssetInstallationView(TemplateView):
    template_name = 'core/asset_installation.html'
    config = get_config_data()
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['base_url'] = base_url
        return context

    def get(self, *args, **kwargs):
        form = AssetInstallationForm()
        return self.render_to_response({'form':form, 'base_url':base_url})

    def post(self, *args, **kwargs):
        asset_name = self.request.POST.get('asset_name')
        asset_type = self.request.POST.get('asset_type')
        asset_version = self.request.POST.get('asset_version')
        azure_client = AzureClient(self.config['SubscriptionId'], self.config['SubscriptionId'])
        asset = BaseOEAAsset(asset_name, asset_version, asset_type)
        asset.install(azure_client, OEAInstance('syn-oea-abhinav4', 'rg-oea-abhinav4', 'kv-oea-abhinav4', 'stoeaabhinav4'))
        return redirect('home')

class AssetUninstallationView(TemplateView):
    template_name = 'core/asset_uninstallation.html'
    config = get_config_data()
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['base_url'] = base_url
        return context

    def get(self, *args, **kwargs):
        form = AssetUninstallationForm()
        return self.render_to_response({'form':form, 'base_url':base_url})

    def post(self, *args, **kwargs):
        asset_name = self.request.POST.get('asset_name')
        asset_type = self.request.POST.get('asset_type')
        asset_version = self.request.POST.get('asset_version')
        azure_client = AzureClient(self.config['SubscriptionId'], self.config['SubscriptionId'])
        asset = BaseOEAAsset(asset_name, asset_version, asset_type)
        asset.uninstall(azure_client, OEAInstance('syn-oea-abhinav4', 'rg-oea-abhinav4', 'kv-oea-abhinav4', 'stoeaabhinav4'))

        return redirect('home')

class InstalledModulesView(TemplateView):
    template_name = "core/installed_modules.html"

    def get_context_data(self, **kwargs):
        context = super(InstalledModulesView, self).get_context_data(**kwargs)
        context['base_url'] = base_url
        return context

    def get(self, *args, **kwargs):
        data = get_installed_assets_in_workspace()
        return self.render_to_response({'data':data})


