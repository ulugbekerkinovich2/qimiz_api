import requests
from rest_framework import serializers

from basic_app.models import QimizOlishZonaDachalari, DachaKategory, DachaVideo, MijozlarFikrlariAudio, \
    MijozlarFikrlariImage, Comments, Form, About
from qimiz.settings import BOT_TOKEN, GROUP_CHAT_ID


def telebot(mess):
    requests.get(
        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&parse_mode=HTML&text={mess}")


class DachaKategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaKategory
        fields = ['id', 'name_uz', 'name_ru']


class QimizOlishZonaDachalariSerializer(serializers.ModelSerializer):
    category = DachaKategorySerializer(read_only=True)

    class Meta:
        model = QimizOlishZonaDachalari
        fields = [
            'id', 'category', 'title_uz', 'title_ru', 'cost', 'text_uz', 'text_ru', 'image'
        ]


class DachaVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DachaVideo
        fields = '__all__'


class MijozlarFikrlariAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MijozlarFikrlariAudio
        fields = '__all__'


class MijozlarFikrlariImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MijozlarFikrlariImage
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'name', 'phone']

    def create(self, validated_data):
        print('keldi')
        # Create the object using the validated data
        my_object = Form.objects.create(**validated_data)
        print(validated_data)
        print(my_object)
        # Send a message to the Telegram group
        message = f"New User : \nismi: {validated_data['name']}\ntelefon raqami: {validated_data['phone']} "
        telebot(message)
        return my_object


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
