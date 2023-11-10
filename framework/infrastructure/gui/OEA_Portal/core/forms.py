from django import forms
from django.forms import formset_factory

CHOICES =(
    ("hash","hash"),
    ("hash-no-lookup","hash-no-lookup"),
    ("no-op","no-op"),
    ("partition-by","partition-by"),
    ("mask","mask"),
)

TYPES = (
    ("string", "string"),
    ("integer", "integer"),
    ("float", "float"),
    ("long", "long"),
    ("object", "object"),
    ("array", "array"),
)

CONSTRAINTS = (
    ("None", "None"),
    ("primary key", "primary key"),
    ("foreign key", "foreign key")
)

class InstallationForm(forms.Form):
    def __init__(self, version_choices, *args, **kwargs):
        super(InstallationForm, self).__init__(*args, **kwargs)
        self.fields['oea_version'].choices = version_choices
    oea_suffix = forms.CharField(max_length=10)
    oea_version = forms.ChoiceField()
    location = forms.CharField(max_length=15)
    include_groups = forms.BooleanField(required=False, label='Include Groups')

class AssetInstallationForm(forms.Form):
    asset_name = forms.CharField(max_length=50)
    asset_type = forms.ChoiceField(choices=(
        ("module", "module"),
        ("package", "package"),
        ("schema", "schema")
    ), required=True)
    asset_version = forms.CharField(max_length=5)

class AssetUninstallationForm(forms.Form):
    asset_name = forms.CharField(max_length=50)
    asset_type = forms.ChoiceField(choices=(
        ("module", "module"),
        ("package", "package"),
        ("schema", "schema")
    ), required=True)
    asset_version = forms.CharField(max_length=5)

class ColumnMetadata(forms.Form):
    column_name = forms.CharField(max_length=100)
    column_type = forms.ChoiceField(choices=TYPES)
    pseuodynimization = forms.ChoiceField(choices=CHOICES)
    constraint = forms.ChoiceField(choices=CONSTRAINTS)

class BaseMetadataFormset(forms.BaseFormSet):
    def add_fields(self, form, index):
        """ hide ordering and deletion fields """
        super().add_fields(form, index)
        if 'ORDER' in form.fields:
            form.fields['ORDER'].widget = forms.HiddenInput()
        if 'DELETE' in form.fields:
            form.fields['DELETE'].widget = forms.HiddenInput()

MetadataFormSet = formset_factory(ColumnMetadata, formset=BaseMetadataFormset, extra=1, can_delete=True)