import pytest


@pytest.mark.manual
@pytest.mark.tier(2)
def test_tagvis_ssui_catalog_items():
    """
    Polarion:
        assignee: anikifor
        casecomponent: ssui
        caseimportance: medium
        caseautomation: notautomated
        initialEstimate: 1/8h
        testSteps:
            1.Create groups with tag
            2. Create user and assign it to group
            3. As admin create service catalog and catalog item
            4. Log in as user to ssui
            5. Check catalog item list -> User should not see any items
            6. As admin set tag to catalog item
            7. As user, check visibility -> User should see tagged catalog item
    """
    pass
