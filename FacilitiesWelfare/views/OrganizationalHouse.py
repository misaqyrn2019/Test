from datetime import datetime
from django.shortcuts import render,redirect
from django.urls import reverse
from account.mixins import (
	FieldsMixin,
	FormValidMixin,
	AuthorAccessMixin,
	AuthorsAccessMixin,
	SuperUserAccessMixin,
    FacilitiesWelfareAccessMixin,
)
from django.views.generic import (
	ListView,
	CreateView,
	UpdateView,
	DeleteView,
    DetailView
)
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from FacilitiesWelfare.models import *
from FacilitiesWelfare.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

class OrganizationalHouseList(FacilitiesWelfareAccessMixin,ListView):
    login_url = '/login/'
    model = OrganizationalHouse
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse_list.html"

    def get_queryset(self):
        return OrganizationalHouse.objects.all()

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(OrganizationalHouse, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class OrganizationalHouseCreate(FacilitiesWelfareAccessMixin,DefineOrganizationalHouse,CreateView):
    model = OrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeOH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse-create-update.html"

class OrganizationalHouseUpdate(FacilitiesWelfareAccessMixin,DefineOrganizationalHouse,UpdateView):
    model = OrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeOH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse-create-update.html"

class OrganizationalHouseDelete(FacilitiesWelfareAccessMixin,DeleteView):
    model = OrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:homeOH')
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse_confirm_delete.html"

class UserOrganizationalHouseListAll(LoginRequiredMixin,ListView):
    model = OrganizationalHouse
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouse_ListAll.html"

class OrganizationalHouseRegUser2(LoginRequiredMixin,DefineRegisterOrganizationalHouse,CreateView):
    model = RegisterOrganizationalHouse
    success_url = reverse_lazy('FacilitiesWelfare:OrganizationalHouse-LST-User')

    def form_valid(self, form):
        form = form.save(commit=False)
        IdOrganizationHouse = self.request.POST.get('IdOrganizationHouse')
        IdUser = self.request.POST.get('IdUser')
        
        #?????? ???????? ???? ???????? ?????????????? ???? ?????????????? ???????? ?????? ???????? ?????????? ?????????? ?????????? ?????? ??????
        CountIDOH = RegisterOrganizationalHouse.objects.filter(
                Q(IdOrganizationHouse = IdOrganizationHouse) & Q(IsVerify = 'Y')
        ).count()
        
        #?????? ?????????? ???????? ?????????????? ???????? ?????????????? ???????? ?? ???????? ???????? ?????????? ?????????? ????????
        CountIDOHUser = RegisterOrganizationalHouse.objects.filter(
            Q(IdUser = IdUser) & Q(IsVerify = 'N')
        ).count()
        
        #?????? ???????? ???? ???? ???????? ?????????????? ?????????? ?????????? ?? ???? ?????? ???????????? ?????? ???????? ???????? ?????????? ????????
        CountOH_Verify_Y = RegisterOrganizationalHouse.objects.filter(
            Q(IdUser = IdUser) & Q(IsVerify = 'Y') & Q(DateExpire__gte = datetime.today())
        ).count()

        #???????? ???? ?????????? ?????????????? ?????? ?????????? ???? ???????? ?????? ?????? ??????????
        if CountIDOH == 0 and CountIDOHUser == 0 and CountOH_Verify_Y == 0:
            form.IsVerify = 'N'
            form.save()
            return redirect(reverse('FacilitiesWelfare:OrganizationalHouse-LST-User'))
        return redirect(reverse('FacilitiesWelfare:OrganizationalHouse-LST-User'))

class OrganizationalHouseListUser(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = RegisterOrganizationalHouse
    template_name = "FacilitiesWelfare/OrganizationalHouse/OrganizationalHouseUser.html"

    def get_queryset(self):
        return RegisterOrganizationalHouse.objects.filter(
            Q(IdUser=self.request.user.pk)
            )

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(RegisterOrganizationalHouse, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs