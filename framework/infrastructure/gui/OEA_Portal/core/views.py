from .forms import *
from OEA_Portal.core.services.AssetManagementService.asset import BaseOEAAsset
from OEA_Portal.core.services.AssetManagementService.operations import *
from OEA_Portal.auth.AzureClient import AzureClient
from OEA_Portal.core.services.utils import *
from django.views.generic import TemplateView
from django.shortcuts import redirect
from OEA_Portal.core.OEAInstaller import OEAInstaller

class HomeView(TemplateView):
    template_name = 'core/homepage.html'

    def get(self, *args, **kwargs):
        config = get_config_data()
        if self.request.environ.get('HTTP_REFERER', None) is None:
            base_url = self.request.environ.get('HTTP_HOST', None)
        else:
            base_url = self.request.environ.get('HTTP_REFERER', None)
        if base_url.split(':')[0] not in ['http', 'https']:
            base_url = 'http://' + base_url
        config['BaseURL'] = base_url.replace('/home','')
        update_config_database(config)
        subscriptions, workspaces = get_subscriptions_and_workspaces_in_tenant()
        return self.render_to_response({'base_url':config['BaseURL'],
        'subscriptions':subscriptions,
        'workspaces':workspaces
        })
    def post(self, *args, **kwargs):
        config = get_config_data()
        config["SubscriptionId"] = self.request.POST.get('SubscriptionSelect')
        config["WorkspaceName"] = self.request.POST.get('WorkspaceSelect')
        update_config_database(config)
        return redirect('dashboard')

class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get(self, *args, **kwargs):
        config = get_config_data()
        azure_client = AzureClient(config['SubscriptionId'])
        workspace = get_workspace_object(azure_client, config['WorkspaceName'])
        modules, packages, schemas, version = get_installed_assets_in_workspace(config['WorkspaceName'], azure_client)
        return self.render_to_response({'base_url':config['BaseURL'],
            'workspace':config['WorkspaceName'],
            'modules': json.dumps([module.__dict__ for module in modules]),
            'packages':json.dumps([package.__dict__ for package in packages]),
            'schemas':json.dumps([schema.__dict__ for schema in schemas]),
            'oea_version': version,
            'storage_account': workspace.storage_account
        })

class InstallationFormView(TemplateView):
    template_name = 'core/installation_form.html'
    config = get_config_data()

    def get_context_data(self, **kwargs):
        context = super(InstallationFormView, self).get_context_data(**kwargs)
        context['base_url'] = self.config['BaseURL']
        return context

    def get(self, *args, **kwargs):
        version_choices = [('0.7', '0.7')]
        form = InstallationForm(version_choices)
        return self.render_to_response({'form':form})

    def post(self, *args, **kwargs):
        subscription_id = self.config['SubscriptionId']
        include_groups = self.request.POST.get('include_groups')
        oea_version = self.request.POST.get('oea_version')
        oea_suffix = self.request.POST.get('oea_suffix')
        location = self.request.POST.get('location')
        oea_installer = OEAInstaller(subscription_id, oea_suffix,oea_version, location, include_groups)
        oea_installer.install()
        return redirect('home')

class AssetInstallationView(TemplateView):
    template_name = 'core/asset_installation.html'

    def get(self, *args, **kwargs):
        config = get_config_data()
        form = AssetInstallationForm()
        return self.render_to_response({'form':form, 'base_url':config['BaseURL']})

    def post(self, *args, **kwargs):
        config = get_config_data()
        asset_name = self.request.POST.get('asset_name')
        asset_type = self.request.POST.get('asset_type')
        asset_version = self.request.POST.get('asset_version')
        azure_client = AzureClient(config['SubscriptionId'])
        asset = BaseOEAAsset(asset_name, asset_version, asset_type)
        # todo: Figure out how to get the OEA instance.
        asset.install(azure_client, OEAInstance('syn-oea-abhinav4', 'rg-oea-abhinav4', 'kv-oea-abhinav4', 'stoeaabhinav4'))
        return redirect('dashboard')

class AssetUninstallationView(TemplateView):
    template_name = 'core/asset_uninstallation.html'
    config = get_config_data()
    def get_context_data(self, **kwargs):
        context = super(AssetUninstallationView, self).get_context_data(**kwargs)
        context['base_url'] = self.config['BaseURL']
        return context

    def get(self, *args, **kwargs):
        form = AssetUninstallationForm()
        return self.render_to_response({'form':form, 'base_url':self.config['BaseURL']})

    def post(self, *args, **kwargs):
        asset_name = self.request.POST.get('asset_name')
        asset_type = self.request.POST.get('asset_type')
        asset_version = self.request.POST.get('asset_version')
        azure_client = AzureClient(self.config['SubscriptionId'])
        asset = BaseOEAAsset(asset_name, asset_version, asset_type)
        asset.uninstall(azure_client, OEAInstance('syn-oea-abhinav4', 'rg-oea-abhinav4', 'kv-oea-abhinav4', 'stoeaabhinav4'))
        return redirect('dashboard')


