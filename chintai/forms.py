from django import forms


class InquiryForm(forms.Form):
    name = forms.CharField(label="お名前", max_length=30)
    email = forms.CharField(label="メールアドレス")
    title = forms.CharField(label="タイトル", max_length=30)
    message = forms.CharField(label="メッセージ", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control col-9"
        self.fields["name"].widget.attrs["placeholder"] = "お名前を入力してください。"

        self.fields["email"].widget.attrs["class"] = "form-control col-11"
        self.fields["email"].widget.attrs["placeholder"] = "メールアドレスを入力してください。"

        self.fields["title"].widget.attrs["class"] = "form-control col-9"
        self.fields["title"].widget.attrs["placeholder"] = "タイトルを入力してください。"

        self.fields["message"].widget.attrs["class"] = "form-control col-9"
        self.fields["message"].widget.attrs["placeholder"] = "メッセージを入力してください。"
