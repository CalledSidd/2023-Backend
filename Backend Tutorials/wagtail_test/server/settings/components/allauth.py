CUSTOM_ALLAUTH_CONFIG_PATH = "server.apps.main.allauth"
ACCOUNT_ADAPTER = CUSTOM_ALLAUTH_CONFIG_PATH + ".adapter.AllAuthAccountAdapter"
ACCOUNT_FORMS = {
    "signup": CUSTOM_ALLAUTH_CONFIG_PATH + ".forms.SignupForm",
    "reset_password": CUSTOM_ALLAUTH_CONFIG_PATH + ".forms.ResetPasswordForm",
}
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
