"""VK channel manifest."""

from nanobot.channels.plugin import ChannelPlugin

PLUGIN = ChannelPlugin(
    name="vk",
    display_name="VKontakte",
    runtime=f"{__package__}.runtime:VKChannel",
    dependencies=(
        "vkbottle>=4.5,<5",
        "aiohttp>=3.8,<4",
    ),
)
