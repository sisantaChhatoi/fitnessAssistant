from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer
from plans.serializers import PlanSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id']

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    plans = PlanSerializer(many=True, read_only=True)
    badge_id = serializers.IntegerField(write_only=True, required=False)
    achievement_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Customer
        fields = ['id', 'age', 'height', 'weight', 'gender', 'points', 
                  'achievements', 'kind', 'badges', 'user', 'plans',
                  'badge_id', 'achievement_id']
        read_only_fields = ['id', 'points']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        # Create the User instance
        user = User.objects.create_user(
            username=user_data.get('username'),
            email=user_data.get('email', ''),
            first_name=user_data.get('first_name', ''),
            last_name=user_data.get('last_name', '')
        )
        # Create the Customer instance
        customer = Customer.objects.create(user=user, **validated_data)
        return customer

    def update(self, instance, validated_data):
        # Handle nested user data if provided
        if 'user' in validated_data:
            user_data = validated_data.pop('user')
            user = instance.user

            # Update user fields
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()

        # Handle badge_id if provided (add a single badge to the customer)
        badge_id = validated_data.pop('badge_id', None)
        if badge_id is not None:
            instance.badges.add(badge_id)

        # Handle achievement_id if provided (add a single achievement to the customer)
        achievement_id = validated_data.pop('achievement_id', None)
        if achievement_id is not None:
            instance.achievements.add(achievement_id)

        # Update customer fields
        for attr, value in validated_data.items():
            if attr in ['badges', 'achievements']:
                # Handle many-to-many relationships
                if attr == 'badges':
                    instance.badges.set(value)
                elif attr == 'achievements':
                    instance.achievements.set(value)
            else:
                setattr(instance, attr, value)

        instance.save()
        return instance
