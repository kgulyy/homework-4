# -*- coding: utf-8 -*-
from Components.component import Component


class TopMenuOnShopPage(Component):
    FEED_PAGE_LINK = '//a[contains(@data-l,"NavMenu_AltGroup_Main")]'
    FORUM_PAGE_LINK = '//a[contains(@href,"topics")]'
    MARKET_PAGE_LINK = '//a[contains(@href,"market")]'

    def open_feed_page(self):
        super(TopMenuOnShopPage, self).click_element(self.FEED_PAGE_LINK)

    def open_forum_page(self):
        super(TopMenuOnShopPage, self).click_element(self.FORUM_PAGE_LINK)

    def open_market_page(self):
        super(TopMenuOnShopPage, self).click_element(self.MARKET_PAGE_LINK)


class LeftMenuOnShopFeedPage(Component):
    OTHER_ACTIONS_BUTTON = '//em[@class="tico_simb_txt"]'
    REMOVE_SHOP_BUTTON = '//a[contains(@hrefattrs,"RemoveAltGroup")]'
    SUBMIT_REMOVE_BUTTON = '//input[@name="button_delete"]'

    def other_actions(self):
        super(LeftMenuOnShopFeedPage, self).click_element(self.OTHER_ACTIONS_BUTTON)

    def remove_shop(self):
        super(LeftMenuOnShopFeedPage, self).click_element(self.REMOVE_SHOP_BUTTON)

    def submit_remove(self):
        super(LeftMenuOnShopFeedPage, self).click_element(self.SUBMIT_REMOVE_BUTTON)


class HeaderOnShopFeedPage(Component):
    SHOP_NAME = '//h1[@class="mctc_name_tx"]'
    SHOP_CATEGORY = '//div[@class="group-info_category"]'

    def get_shop_name(self):
        return super(HeaderOnShopFeedPage, self).get_element_text(self.SHOP_NAME)

    def get_shop_category(self):
        return super(HeaderOnShopFeedPage, self).get_element_text(self.SHOP_CATEGORY)