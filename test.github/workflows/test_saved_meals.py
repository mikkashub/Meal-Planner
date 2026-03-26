import pytest
from playwright.sync_api import Page, expect

# This looks for the meal plan and deletes it
def test_delete_saved_meal(page: Page):
    # 0. Pre-condition: Ensure we are logged in (usually handled in a global setup)
    # page.goto("/login") ...
    
    # 1. Open Saved Meals
    page.goto("/saved-meals")

    # 2. Select a plan and click delete
    # Added a 'wait' to ensure the list is loaded before looking for text
    meal_plan = page.locator("text=Weekly High Protein Plan")
    
    # We check if it exists first so the test doesn't crash cryptically
    expect(meal_plan).to_be_visible() 
    
    meal_plan.click()
    page.locator("button#delete").click()
    
    # Click the confirmation (using a 'role' is often more reliable than IDs)
    page.get_by_role("button", name="Confirm").click()

    # 3. Verify it is gone (Expected Result)
    # Playwright will wait up to 5 seconds for it to disappear
    expect(meal_plan).to_be_hidden()

# testing to make sure code gets uploaded