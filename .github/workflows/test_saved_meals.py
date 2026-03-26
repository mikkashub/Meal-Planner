import pytest
import os
from playwright.sync_api import Page, expect


# HELPER: This creates the correct path for local file / github
def get_local_url():
    current_dir = os.path.dirname(os.path.abpath(__file__))

    # Adjust 'saved-meals.html' if file is named differently
    file_path = os.path.join(current_dir, "saved-meals.html")
    return f"file:///{file_path}".replace("\\","/")

# Save a valid meal plan to Saved Meals
def test_save_valid_meal_plan(page: Page):
    # assuming there's a generator.html 
    page.goto(get_url("generator.html"))

    # click save meals & confirm
    page.get_by_role("button", name="Save Meals").click()
    page.get_by_role("button", name="Confirm Save").click()

    # Expected: Saved successfully message
    expect(page.locator("text=Saved successfully")).to_be_visible()

# Open Saved Meals and display exisiting saved plans
def test_display_saved_meals(page: Page):
    page.goto(get_url("saved-meals.html"))

    # Expected: Displays all saved meal plans
    expect(page.locator("text=Weekly High Protein Plan")).to_be_visible()

# Delete an existing saved meal plan
def test_delete_saved_meal(page: Page):
    page.goto(get_url("saved-meals.html"))

    # Select and Click delete
    page.locator("text=Weekly High Protein Plan").click()
    page.locator("button#delete").click()

    # Confirm deletion
    page.get_by_role("button", name="Confirm").click()

    # Expected: Removes from list
    expect(page.locator("text=Weekly High Protein Plan")).to_be_hidden()

# Open Saved Meals when no plans exist
def test_open_empty_saved_meals(page: Page):

    # Point to a version of the page with no data
    page.goto(get_url("saved-meals=empty.html"))

    #Expected: "No saved meals found"
    expect(page.locator("text=No saved meals found")).to_be_visible()

# Attempt to save duplicate meal plan
def test_save_duplicate_meal_plan(page: Page):
    page.goto(get_url("generator.html"))

    # Click Save again (assuming one is already saved)
    page.get_by_role("button", name="Save Meal Plan").click()

    # Expected: Informs user the meal already exists
    expect(page.locator("text=meal already exists")).to_be_visible()