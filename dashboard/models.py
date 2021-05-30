from django.db import models
from accounts.models import CustomUser


class RentalProperty(models.Model):
    """賃貸物件モデル"""

    user = models.ForeignKey(
        CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    prooerty_name = models.CharField(verbose_name='物件名', max_length=40)
    rent = models.IntegerField(verbose_name='賃料')
    address1 = models.CharField(
        verbose_name='住所１', max_length=10,
        choices=[
            ("東京都", "東京都"),
        ])
    address2 = models.CharField(
        verbose_name='住所２', max_length=10,
        choices=[
            ("新宿区", "新宿区"),
            ("渋谷区", "渋谷区"),
            ("目黒区", "目黒区"),
        ])
    address3 = models.CharField(verbose_name="住所３", max_length=20)
    nearest_sta1 = models.CharField(
        verbose_name='最寄り駅１', max_length=6,
        choices=[
            ("新宿", "新宿"),
            ("代々木", "代々木"),
            ("原宿", "原宿"),
            ("渋谷", "渋谷"),
            ("恵比寿", "恵比寿"),
        ])
    min_walk_from_sta1 = models.IntegerField(verbose_name='駅１徒歩')
    area = models.FloatField(verbose_name="面積", max_length=10)
    layout = models.CharField(
        verbose_name="間取り", max_length=10,
        choices=[
            ("1R", "1R"),
            ("1K", "1K"),
            ("1LDK", "1LDK"),
            ("2LDK", "2LDK"),
            ("3LDK", "3LDK"),
        ])
    # バストイレ別の場合、True
    is_separated = models.BooleanField(
        verbose_name="バストイレ",
        choices=[
            (True, "バストイレ別"),
            (False, "ユニットバス"),
        ])
    # 室内洗濯機置場がある場合、True
    has_indoor_laundry_space = models.BooleanField(
        verbose_name="室内洗濯機置場",
        choices=[
            (True, "室内洗濯機置場あり"),
            (False, "室内洗濯機置場なし"),
        ])
    # 掲載写真
    photo1 = models.ImageField(verbose_name="写真１", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        verbose_name_plural = "RentalProperty"

    def __str__(self):
        return f'{self.prooerty_name}({self.nearest_sta1}駅徒歩{self.min_walk_from_sta1})'
