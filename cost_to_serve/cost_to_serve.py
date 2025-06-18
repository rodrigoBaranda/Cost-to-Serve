"""Hello World Reflex app for the Cost to Serve POC."""

import reflex as rx

from rxconfig import config

mock_line_data = [
    {"month": "Jan", "cost": 3200},
    {"month": "Feb", "cost": 3400},
    {"month": "Mar", "cost": 3000},
    {"month": "Apr", "cost": 3600},
]

mock_bar_data = [
    {"warehouse": "A", "orders": 400},
    {"warehouse": "B", "orders": 300},
    {"warehouse": "C", "orders": 500},
]


class State(rx.State):
    """Application state."""
    pass


def index() -> rx.Component:
    """The home page of the app."""
    return rx.center(
        rx.vstack(
            rx.heading("Cost to Serve POC"),
            rx.link("View KPIs", href="/kpis"),
            rx.link("View Charts", href="/charts"),
            spacing="4",
        ),
        min_height="100vh",
    )


app = rx.App()
app.add_page(index)


def kpi_page() -> rx.Component:
    """Display mock KPIs."""
    return rx.vstack(
        rx.heading("Mock KPIs"),
        rx.hstack(
            rx.box(
                rx.text("Total Orders"),
                rx.text("1,250"),
                padding="1em",
                border="1px solid #ccc",
                border_radius="md",
            ),
            rx.box(
                rx.text("Avg Cost per Order"),
                rx.text("$35"),
                padding="1em",
                border="1px solid #ccc",
                border_radius="md",
            ),
            rx.box(
                rx.text("On-time Delivery"),
                rx.text("95%"),
                padding="1em",
                border="1px solid #ccc",
                border_radius="md",
            ),
            spacing="6",
        ),
        padding="4",
        spacing="6",
    )


def charts_page() -> rx.Component:
    """Display mock charts using Recharts."""
    return rx.vstack(
        rx.heading("Mock Charts"),
        rx.recharts.line_chart(
            rx.recharts.line(data_key="cost", stroke="#8884d8"),
            rx.recharts.x_axis(data_key="month"),
            rx.recharts.y_axis(),
            rx.recharts.tooltip(),
            rx.recharts.legend(),
            data=mock_line_data,
            height=300,
        ),
        rx.recharts.bar_chart(
            rx.recharts.bar(data_key="orders", fill="#82ca9d"),
            rx.recharts.x_axis(data_key="warehouse"),
            rx.recharts.y_axis(),
            rx.recharts.tooltip(),
            rx.recharts.legend(),
            data=mock_bar_data,
            height=300,
        ),
        padding="4",
        spacing="6",
    )


app.add_page(kpi_page, route="/kpis", title="KPIs")
app.add_page(charts_page, route="/charts", title="Charts")

