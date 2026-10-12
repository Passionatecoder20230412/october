import time

from playwright.sync_api import sync_playwright


def test_alerts():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://automatewithbipin.com/")
        page.locator('[data-view="alerts"]').click()


        page.on('dialog',lambda dialog : dialog.accept(prompt_text="Vijay Anegondi"))
        page.locator('[id="promptBtn"]').click()

        #dbclick
        page.locator('[data-view="mouse"]').click()
        page.locator('[id="doubleClickZone"]').dblclick()
        page.locator('[id="rightClickZone"]').click(button='right')
        page.locator('[id="hoverBtn"]').hover()

        #actions advanced

        page.locator('[data-view="advanced"]').click()
        page.locator('[class="dragitem"]').drag_to(page.locator('[class="dropzone"]'))
        page.locator('[id="budgetSlider"]').press('ArrowRight')
        page.locator('[id="budgetSlider"]').press('ArrowRight')
        page.locator('[id="budgetSlider"]').press('ArrowRight')
        page.locator('[data-view="shadow"]').click()
        page.locator('[id="shadowInput"]').fill("Vijay Anegondi")
        # page.locator('[placeholder="Two boundaries deep"]').fill("Vijay Anegondi")
        l=['[class="host-box"]','[id="shadowOuter"]','[id="innerHost"]','[id="nestedShadowInput"]']
        # st=""
        # for i )in range(len(l)):
        #     if i==0:
        #         st=f"locator({l[i]})."
        #     else:
        #         st=f".locator({l[i]})."
        #
        # st1=st[:-1]
        # page.st1.fill("vijay Anegondi"



        # page.goto("https://demo.automationtesting.in/Alerts.html")
        # page.goto("https://demo.automationtesting.in/Frames.html")
        # frame = page.frame_locator('[src="SingleFrame.html"]')
        # cnt = frame.locator('//h5').all_inner_texts()
        # print(cnt[0])
        # frame.locator('[type="text"]').first.fill('Vijay Anegondi')
        # time.sleep(5)
        # page.locator('[href="#Multiple"]').click()
        # frame2=page.frame_locator('[src="MultipleFrames.html"]')
        # in_frame=frame2.frame_locator('[src="SingleFrame.html"]')
        # in_frame.locator('[type="text"]').nth(0).fill('Vijay Anegondi')
        # time.sleep(5)


        # time.sleep(3)
        # page2=context.new_page()
        # page2.goto("https://demo.automationtesting.in/Alerts.html")
        # time.sleep(3)
        # page3=context.new_page()
        # page3.goto("https://demo.automationtesting.in/Alerts.html")
        # time.sleep(3)
        # context.pages[0].bring_to_front()
        # time.sleep(3)
        # context.pages[0].goto("https://automationexercise.com")
        # time.sleep(3)
        # print("vijay")
        # page.close()
        # page2.close()
        # time.sleep(3)
        # page3.close()
        # time.sleep(3)
        # context.close()
        #
        #
        #
        # context2 = browser.new_context()
        # page = context2.new_page()
        # page.goto("https://demo.automationtesting.in/Alerts.html")
        # time.sleep(3)
        # page2 = context2.new_page()
        # page2.goto("https://demo.automationtesting.in/Alerts.html")
        # time.sleep(3)
        # page3 = context2.new_page()
        # page3.goto("https://demo.automationtesting.in/Alerts.html")
        # time.sleep(3)
        # context.pages[0].bring_to_front()
        # time.sleep(3)
        # context2.pages[0].goto("https://automationexercise.com")
        # time.sleep(3)
        # print("vijay")
        # page.close()
        # page2.close()
        # time.sleep(3)
        # page3.close()
        # time.sleep(3)
        # context.close()

        # page.locator('[href="#Textbox"]').click()



        # with page.expect_event("dialog") as d:
        #     page.locator('[onclick="promptbox()"]').click()
        #
        # dialog = d.value

        # 4. Handle the prompt (pass your text inside accept if you need to type)
        # dialog.accept(prompt_text="Hello World")
        # Pass the handler directly inside the expect_event parameter
        # with page.expect_event("dialog", handler=lambda dialog: dialog.accept(prompt_text="Hello World")):
        #     page.locator('[onclick="promptbox()"]').click()
        #
        # # Code continues outside the block
        # print(page.locator("#demo1").text_content())
        #
        # time.sleep(20)
        



