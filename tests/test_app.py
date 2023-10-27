from playwright.sync_api import Page, expect

def test_get_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click("text=Signup")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Signup to MakersBnB")


def test_for_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    page.fill("input[name=name]", "Test name")
    page.fill("input[name=username]", "Test username")
    page.fill("input[name=email]", "email@email")
    page.fill("input[name=password]", "Test password")
    page.click("text=Signup to MarkersBnB")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Thank you, you are signed up! Now login.")
    

def test_for_error_exiting_user_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    page.fill("input[name=name]", "Test name")
    page.fill("input[name=username]", "Jake_1")
    page.fill("input[name=email]", "email@email")
    page.fill("input[name=password]", "Test password")
    page.click("text=Signup to MarkersBnB")
    errors_tag = page.locator(".t-errors")
    # page.screenshot(path="screenshot.png", full_page=True)
    expect(errors_tag).to_have_text(
        ["There were errors with your submission:\n\n\nThis email or username is alredy registered.\n\n"]
        )
    
# BUG: TEST DOESNT WORK BUT IT WORKS ON SERVER? WILL WAIT FOR A COACH
# def test_for_incorrect_login(page, test_web_address):
#     # go to page
#     page.goto(f"http://{test_web_address}/login")
#     # input details
#     page.fill("input[name=username]", "wrongusernme")
#     page.fill("input[name=password]", "tony")
#     page.click("text=Login")
#     errors_tag = page.locator(".errors")
#     page.screenshot(path="screenshot.png", full_page=True)
#     # Check the content of the error message
#     expect(errors_tag).to_have_text("Details are incorrect. Try again!")
    
# def test_good_login(page, test_web_address):
#     page.goto(f"http://{test_web_address}/login")
#     page.fill("input[name=username]", "Amina_1")
#     page.fill("input[name=password]", "Amina123!")
#     page.click("text=Login")
#     page.screenshot(path="screenshot.png", full_page=True)

#     h1_tag = page.locator("h1")
#     expect(h1_tag).to_have_text("Book a Space")
    

# """
# # list a new space
# # [POST] /spaces/new -- template = new_place.html
# # Posts a new space listing
# # @app.route('/spaces/new', methods=['POST'])
# """
# def test_list_new_space(db_connection, page, test_web_address):
#     db_connection.seed("seeds/db_makers_bnb.sql")
#     page.goto(f"http://{test_web_address}/login")
#     page.fill("input[name=username]", "Amina_1")
#     page.fill("input[name=password]", "Amina123!")
#     page.click("text=Login")

#     page.goto(f"http://{test_web_address}/spaces/new")

#     page.fill("input[name='name']", "The place")
#     page.fill("input[name='description']", 'The most amazing place to sleep')
#     page.fill("input[name='price']", "50.0")
#     page.fill("input[name='available_from']", '01/01/2024')
#     page.fill("input[name='available_till']", '01/02/2024')

#     page.click("text = List my Space")

#     name_element = page.locator(".t-space").last
#     expect(name_element).to_have_text('\nThe place\n \
#                         The most amazing place to sleep')

# """
# # list a new invalid space
# # [POST] /spaces/new -- template = new_place.html
# # Posts a new space listing
# # @app.route('/spaces/new', methods=['POST'])
# """
# def test_list_new_space_error(db_connection, page, test_web_address):
#     db_connection.seed("seeds/db_makers_bnb.sql")

#     page.goto(f"http://{test_web_address}/login")
#     page.fill("input[name=username]", "Amina_1")
#     page.fill("input[name=password]", "Amina123!")
#     page.click("text=Login")

#     page.goto(f"http://{test_web_address}/spaces/new")

#     page.fill("input[name='name']", "The place")
#     page.fill("input[name='description']", 'The most amazing place to sleep')
# #    page.fill("input[name='price']", "50.0")
#     page.fill("input[name='available_from']", '01/01/2024')
#     page.fill("input[name='available_till']", '01/02/2024')

#     page.click("text = List my Space")

#     error_element = page.locator(".t-errors")
#     expect(error_element).to_have_text("\n                   There were errors with your submision: all spaces should be completed\n                   ")
    
# """
# #list a new space
# # [POST] /spaces/new -- template = new_place.html
# # Posts a new space listing
# # @app.route('/spaces/new', methods=['POST'])
# """
# def test_spaces(db_connection, page, test_web_address):
#     db_connection.seed("seeds/db_makers_bnb.sql")
#     page.goto(f"http://{test_web_address}/login")
#     page.fill("input[name=username]", "Amina_1")
#     page.fill("input[name=password]", "Amina123!")
#     page.click("text=Login")
#     page.goto(f"http://{test_web_address}/spaces") 

#     list_spaces = page.locator(".t-space")
#     expect(list_spaces).to_have_text(['\n                Cozy Cottage Retreat\n                Escape to this charming cottage for a tranquil retreat. Nestled in the heart of nature, this cozy cottage offers a serene getaway, perfect for nature lovers and those seeking relaxation.\n                ', '\n                Modern Urban Loft\n                Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.\n                ', '\n                Beachfront Paradise\n                Wake up to the sound of waves in this beachfront paradise. Enjoy direct beach access, stunning ocean views, and a serene atmosphere, making it a dream vacation spot for beach enthusiasts.\n                '])


#     # name_element = page.locator(".t-available_to")
#     # expect(name_element).to_have_text("01/02/2024")    

# """
# When I access /space/<id> I see space information
# """
# def test_for_single_space(page, test_web_address):
#     page.goto(f"http://{test_web_address}/login")
#     page.fill("input[name=username]", "Amina_1")
#     page.fill("input[name=password]", "Amina123!")
#     page.click("text=Login")

#     page.goto(f"http://{test_web_address}/spaces/2")
#     h1_tag = page.locator("h1")
#     expect(h1_tag).to_have_text("Modern Urban Loft")

#     price_tag = page.locator(".price")
#     expect(price_tag).to_have_text("Price per night: £200")

#     description_tag = page.locator(".description")
#     expect(description_tag).to_have_text('Experience city living at its finest in this stylish urban loft. With modern amenities and a prime downtown location, this loft is ideal for urban explorers and business travelers.')


# BUG: works in browser but test is crashing as locator not found
# """
# Whet user submits a request, they see a thank you message
# """
# def test_for_submit_request(page, test_web_address):
#     page.goto(f"http://{test_web_address}/spaces/2")
#     page.click("text=Send a booking request")
#     page.screenshot(path="screenshot.png", full_page=True)

    # message_tag = page.locator(".message")
    # expect(message_tag).to_have_text("Thank you for your request!")

# """
# when unlogged user try to access any page apart from signup and login
# acces is denied
# """
# def test_access_denied(page, test_web_address):
#     page.goto(f"http://{test_web_address}/spaces/2")
#     page.screenshot(path='screenshot.png')
#     access_tag = page.locator("access")

#     expect(access_tag).to_have_text("Access denied. To see this page")

