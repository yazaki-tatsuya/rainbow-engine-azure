import flet as ft
def main(page: ft.Page):
    # タイトルを設定
    page.title = "Simple Registration Form"

    # ユーザー名の入力フィールド
    username = ft.TextField(label="Username", autofocus=True)
    page.add(username)

    # パスワードの入力フィールド
    password = ft.TextField(label="Password", password=True)
    page.add(password)

    # 登録ボタン押下時の処理
    def register_click(e):
        # ここで登録処理を行う（今は単に入力されたユーザー名を表示するだけ）
        page.add(ft.Text(value=f"Registered user: {username.value}"))

    # 登録ボタン
    register_btn = ft.ElevatedButton(text="Register", on_click=register_click)
    page.add(register_btn)

ft.app(target=main)
