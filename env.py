import os

os.environ["DEVELOPMENT_MODE"] = "True"
os.environ["SECRET_KEY"] = "x*t_odo8_fu+0puvyyc)j85)ourviscr&&^=1t3=($hc2wm8s&"
os.environ["DEBUG"] = "True"
# os.environ["DATABASE_URL"] = "postgres://vyuuvsaj:Rh1ND7t1Z08kMdgtuhkkIm_nzSnZGk4W@kandula.db.elephantsql.com/vyuuvsaj"

# os.environ["STRIPE_PUBLIC_KEY"] = "pk_test_51MmNj9KSG7N8mbvfp0osX4bA8yfYs6bzt5kAm4A9QQS4nAq5LDtJHTZVHE8WnR3dThzbO4z4Na7N5iKJNyM0woUc00AUrnLYJ1"
# os.environ["STRIPE_SECRET_KEY"] = "sk_test_51MmNj9KSG7N8mbvfr0NpjOfFgmaWCyxGHiYY4BPlVKqLn8nhlZa7eUTfPSIbohASdeglRxg8KLs6xWgRULhMdnPC003TeLFERl"
# os.environ["STRIPE_WH_SECRET"] = "whsec_7IB090ZcIU9jkk7hhguEQxIKmyfeLVsB"

# os.environ["MAILCHIMP_API_KEY"] = "507d1d66e61f3d016ad1efa535e8facd-us18"
# os.environ["MAILCHIMP_REGION"] = "us18"
# os.environ["MAILCHIMP_MARKETING_AUDIENCE_ID"] = "44e6262f06"

os.environ["AWS_SES_ACCESS_KEY_ID"] = "AKIAXHWBKM3FZVM3QWWM"
os.environ["AWS_SES_SECRET_ACCESS_KEY"] = "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"

os.environ["AWS_SES_REGION_NAME"] = "eu-west-1"
os.environ["AWS_SES_FROM_EMAIL"] = "johndoe240566@gmail.com"
os.environ["DOMAIN"] = "localhost:3000"
os.environ["AUTH_COOKIE_SECURE"] = "False"
os.environ["REDIRECT_URLS"] = (
    "http://localhost:3000/auth/google,http://localhost:3000/auth/facebook"
)
os.environ["GOOGLE_AUTH_KEY"] = (
    "394248809141-3dsetbn7orr0ggqv3nkunehdpneuc60a.apps.googleusercontent.com"
)

os.environ["GOOGLE_AUTH_SECRET"] = "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"
os.environ["FACEBOOK_AUTH_KEY"] = "296570616786082"
os.environ["FACEBOOK_AUTH_SECRET"] = "a4541b529de9d811c9f9b004886b220c"
