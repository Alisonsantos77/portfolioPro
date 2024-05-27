import flet as ft
from components.skills import SkillRing, SkillProgressbar


class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='images/profile_resize.png',
                            border_radius=ft.border_radius.all(100),
                            width=100,
                        ),
                        alignment=ft.alignment.bottom_right,
                        bgcolor=ft.colors.PRIMARY,
                        small_size=20,
                    ),
                    ft.Text(value='Alison Santos', theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='Desenvolvedor Backend', theme_style=ft.TextThemeStyle.BODY_MEDIUM)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=ft.padding.symmetric(vertical=20, horizontal=40),
            alignment=ft.alignment.center
        )


class SidebarContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self):
        location = ft.Container(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(value='Residência:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                            ft.Text(value='Brasil', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(value='Cidade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                            ft.Text(value='Bastos/SP', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(value='Idade:', theme_style=ft.TextThemeStyle.BODY_LARGE),
                            ft.Text(value='23', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                ]
            )
        )
        languages = ft.Row(
            controls=[
                SkillRing(title='Português', value=1),
                SkillRing(title='Inglês', value=0.6),
                SkillRing(title='Espanhol', value=0.4),
            ]
        )

        skills = ft.Column(
            controls=[
                SkillProgressbar(title='Python', value=0.7),
                SkillProgressbar(title='Django', value=0.6),
                SkillProgressbar(title='Django Rest', value=0.4),
                SkillProgressbar(title='Tkinter', value=0.6),

            ]
        )

        technologies = ft.Column(
            controls=[
                ft.ListTile(leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                            title=ft.Text(value='Flet', theme_style=ft.TextThemeStyle.BODY_MEDIUM)),
                ft.ListTile(leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                            title=ft.Text(value='Versionamento com GIT', theme_style=ft.TextThemeStyle.BODY_MEDIUM)),
                ft.ListTile(leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                            title=ft.Text(value='Tailwindcss', theme_style=ft.TextThemeStyle.BODY_MEDIUM)),
                ft.ListTile(leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                            title=ft.Text(value='Django', theme_style=ft.TextThemeStyle.BODY_MEDIUM)),
                ft.ListTile(leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                            title=ft.Text(value='Tkinter', theme_style=ft.TextThemeStyle.BODY_MEDIUM)),
                ft.ListTile(leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                            title=ft.Text(value='Django Rest', theme_style=ft.TextThemeStyle.BODY_MEDIUM)),
                ft.ListTile(leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                            title=ft.Text(value='SQLite3', theme_style=ft.TextThemeStyle.BODY_MEDIUM)),
                ft.ListTile(leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                            title=ft.Text(value='PostgreSQL', theme_style=ft.TextThemeStyle.BODY_MEDIUM)),
            ]
        )
        cv = ft.TextButton(
            text='Download CV', style=ft.ButtonStyle(color=ft.colors.GREY), icon=ft.icons.DOWNLOAD,
            icon_color=ft.colors.GREY,
            url='https://drive.google.com/uc?export=download&id=19UKY95n4gwQgweM5b6yiTt5N7B_u03Fj')

        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=ft.padding.all(20),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    location,
                    ft.Divider(height=30),
                    languages,
                    ft.Divider(height=30),
                    skills,
                    ft.Divider(height=30),
                    technologies,
                    ft.Divider(height=30),
                    cv,
                ]
            )
        )


class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(src='icons/001-instagram.png', height=15, color='white'),
                        url='https://www.instagram.com/alisonsantos.eu/'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/002-linkedin.png', height=15, color='white'),
                        url='www.linkedin.com/in/alisonsantosdev'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/003-github.png', height=15, color='white'),
                        url='https://github.com/Alisonsantos77'
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )


class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter(),
                ]
            ),
            bgcolor=ft.colors.BACKGROUND
        )
