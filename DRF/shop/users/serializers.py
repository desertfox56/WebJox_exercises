from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions
import re

class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    password2 = serializers.CharField()
    
    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = ['email', 'username', 'password', 'password2']
 
    # Метод для сохранения нового пользователя
    def save(self,role, *args, **kwargs):
        # Создаём объект класса User
        user = User.objects.create_user(
            email=self.validated_data['email'], # Назначаем Email
            username=self.validated_data['username'], # Назначаем Логин
            password=self.validated_data['password']  # Назначаем пароль
        )
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Проверяем на валидность повторный пароль
        password2 = self.validated_data['password2']
        # Проверяем совпадают ли пароли
        if password != password2:
            # Если нет, то выводим ошибку
            raise serializers.ValidationError({"password": "Пароль не совпадает"})
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        #Случай если роль клиента
        if role == "client":
            client = Client(user_ptr_id=user.id)
            client.save()
        #Случай если роль менеджера
        elif role == "shop_manager":
            shop_manager = ShopManager(user_ptr_id=user.id)
            shop_manager.save()
        # Возвращаем нового пользователя 
        return user
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['email','password', 'username', 'FIO', 'address', 'phone_number']

class ShopManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopManager
        fields = ['email','password', 'username', 'FIO', 'phone_number', 'industry', 'work_address']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    username_field = get_user_model().USERNAME_FIELD

    def validate(self, attrs):
        username = attrs.get(self.username_field)
        credentials = {
            'email': '',
            'username': '',
            'password': attrs.get('password')
        }

        # Проверяем, является ли введенное значение адресом электронной почты
        if '@' in username and '.' in username:
            credentials['email'] = username
        elif re.match(r"^\+?1?\d{9,15}$", username):
            credentials['phone_number'] = username
        else:
            credentials['username'] = username

        return super().validate(credentials)
