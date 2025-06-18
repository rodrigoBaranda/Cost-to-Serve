"""Hello World Reflex app for the Cost to Serve POC."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """Application state."""
    pass


def index() -> rx.Component:
    """The home page of the app."""
    return rx.center(
        rx.heading("Hello, World!"),
        min_height="100vh",
    )


app = rx.App()
app.add_page(index)

