import asyncio
from aiosmtpd.controller import Controller

async def data_handle(server, session, envelope):
    print('Message from:', envelope.mail_from)
    print('Message for:', envelope.rcpt_tos)
    print('Message data:\n', envelope.content.decode('utf8', errors='replace'))
    return '250 Message accepted for delivery'

async def main():
    controller = Controller(data_handle, port=1050)
    controller.start()
    print('SMTP server is running on port 1050...')
    try:
        while True:
            await asyncio.sleep(3600)
    except KeyboardInterrupt:
        controller.stop()

if __name__ == "__main__":
    asyncio.run(main())
