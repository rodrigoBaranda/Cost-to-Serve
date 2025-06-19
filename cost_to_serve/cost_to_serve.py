"""Simple Reflex demo with a basic dashboard."""

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

# brand color inspired by Accenture's purple
ACCENT_COLOR = "#A100FF"


class State(rx.State):
    """Application state."""
    pass


def navbar() -> rx.Component:
    """Simple purple navigation bar with links."""
    return rx.hstack(
        rx.heading("Cost to Serve", size="4", margin_left="2"),
        rx.spacer(),
        rx.link("Home", href="/"),
        rx.link("KPIs", href="/kpis"),
        rx.link("Charts", href="/charts"),
        width="100%",
        padding_x="4",
        padding_y="2",
        background_color=ACCENT_COLOR,
        color="white",
        position="sticky",
        top="0",
        z_index="10",
    )


def layout(*children: rx.Component) -> rx.Component:
    """Wrap pages with a nav bar."""
    return rx.vstack(navbar(), *children, spacing="6")


def index() -> rx.Component:
    """The home page of the app."""
    body = rx.center(
        rx.vstack(
            rx.heading("Cost to Serve POC"),
            rx.text("Explore KPIs and charts using the navigation above."),
            spacing="4",
        ),
        min_height="80vh",
    )
    return layout(body)


app = rx.App()
app.add_page(index)


def kpi_page() -> rx.Component:
    """Display mock KPIs."""
    content = rx.vstack(
        rx.heading("Mock KPIs"),
        rx.hstack(
            rx.box(
                rx.text("Total Orders"),
                rx.text("1,250"),
                padding="1em",
                border=f"1px solid {ACCENT_COLOR}",
                border_radius="md",
            ),
            rx.box(
                rx.text("Avg Cost per Order"),
                rx.text("$35"),
                padding="1em",
                border=f"1px solid {ACCENT_COLOR}",
                border_radius="md",
            ),
            rx.box(
                rx.text("On-time Delivery"),
                rx.text("95%"),
                padding="1em",
                border=f"1px solid {ACCENT_COLOR}",
                border_radius="md",
            ),
            spacing="6",
        ),
        padding="4",
        spacing="6",
    )
    return layout(content)


def charts_page() -> rx.Component:
    """Display mock charts using Recharts."""
    content = rx.vstack(
        rx.heading("Mock Charts"),
        rx.recharts.line_chart(
            rx.recharts.line(data_key="cost", stroke=ACCENT_COLOR),
            rx.recharts.x_axis(data_key="month"),
            rx.recharts.y_axis(),
            rx.recharts.tooltip(),
            rx.recharts.legend(),
            data=mock_line_data,
            height=300,
        ),
        rx.recharts.bar_chart(
            rx.recharts.bar(data_key="orders", fill=ACCENT_COLOR),
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
    return layout(content)


app.add_page(kpi_page, route="/kpis", title="KPIs")
app.add_page(charts_page, route="/charts", title="Charts")

