from services.mailer import send_mail


def run(to: str, subject: str, body: str) -> None:
    send_mail(to, subject, body)
