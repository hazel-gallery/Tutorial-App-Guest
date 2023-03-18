import streamlit as st
from PIL import Image

st.title('Connecting AWS')

st.markdown('''
    When you create a Hazel account, you'll go through a 
    standard sign-up process. After signing up, you'll be asked to 
    connect your AWS account in order to set up a role 
    that will enable Hazel to provide you with service.
    At Hazel, we take the security and reliability of 
    our service seriously, and we follow the best practices 
    recommended by AWS for setting up cross-account service. 
    To learn more about these practices, please visit 
    this [AWS documentation page.]({})

'''.format('https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html'))

st.markdown('''
    To get started with setting up the cross-account 
    service, please follow these steps:
''')

st.markdown('''
    :zero: This tutorial assumes you already have an AWS account.
    If you don't, please use [this link]({}). In the event that the 
    link does not work, you can search for "AWS Sign Up" to find 
    the appropriate page.
'''.format('https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=header_signup&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email')
)

st.text('')

st.markdown('''
    :one: Once you have logged into your AWS account, navigate 
    to the top search bar and type in :orange[**IAM**]. This will 
    allow you to easily locate and access the :orange[**IAM**] service.
''')
iam_service_img = Image.open('images/iam_service.png')
st.image(iam_service_img)

st.text('')
st.text('')

st.markdown('''
    :two: Under :orange[**Access management**], select :orange[**Roles**],
    then click the :orange[**Create role**] button. 
''')
iam_create_role_img = Image.open('images/iam_create_role.jpg')
st.image(iam_create_role_img)

st.text('')
st.text('')

st.markdown('''
    :three: In the :orange[**Select trusted entity**] step, choose 
    :orange[**AWS account**]. Check the radio button for :orange[**Another AWS account**]
    and type in the Account ID: :blue[**419331123186**]. This is the
    Hazel AWS account from which you will receive the service. \n
    Select the :orange[**Require external ID (Best practice when a third party will 
    assume this role)**] option. You may use any phase for the External ID as 
    you like. External ID serves as an extra layer of security 
    to help prevent any malicious cross-account manipulation 
    of resources. Click :orange[**Next**]
    to proceed.
''')

trusted_entity_img = Image.open('images/iam_trusted_entity.jpg') 
st.image(trusted_entity_img)

st.text('')
st.text('')

st.markdown('''
    :four: In the :orange[**Add permissions**] step, you will add 3 policies
    to the role: :orange[AmazonEC2FullAccess], :orange[AmazonSSMFullAccess],
    and :orange[IAMFullAccess]. Search for each term in the search bar, select 
    its corresponding checkbox, and click :orange[**Next**] to proceed.
''')
policy_img = Image.open('images/iam_policy.jpg') 
st.image(policy_img)

st.text('')
st.text('')

st.markdown('''

    :five: In the final step, enter the :orange[**Role name**] as 
    :blue[**HazelService**]. We recommend using this default name 
    if it is not already taken. However, if the name is already in use, 
    you can choose another name that best fits your naming convention. 

    Next, carefully review the trusted entities and ensure that all three permissions
    have been added. Once you have confirmed this, click on the 
    :orange[**Create role**] to complete the process.

''')
role_review_img = Image.open('images/iam_role_review.jpg') 
st.image(role_review_img)

st.text('')
st.text('')

st.markdown('''
    :six: Once the role has been created, you will be able to 
    see it displayed in the dashboard. Look for the name you chose, 
    such as :orange[**HazelService**] or another name, and verify that it 
    appears as expected.
''')
after_role_created_img = Image.open('images/iam_after_role_created.jpg') 
st.image(after_role_created_img)

st.text('')
st.text('')

st.markdown('''
    :seven: If you ever need to review the information for a specific 
    role, simply click on the role name, and you will be able to view 
    a summary of its permissions and trusted relationships. This feature 
    can be helpful if you forget your External ID or need to add additional 
    permissions to the role at a later time.
''')
role_summary_img = Image.open('images/iam_role_summary.jpg') 
st.image(role_summary_img)       

st.text('')
st.text('')

st.markdown('''
    :eight: Your AWS account ID can be found in the dropdown menu located
    in the upper right corner of the AWS console. Please copy that and 
    proceed to the final step.
''')
account_id_img = Image.open('images/iam_account_id.jpg') 
st.image(account_id_img)     

st.text('')
st.text('')


st.markdown('''
    :nine: Return to our app, under :orange[**Account**], select
    :orange[**Connect Clouds**]. Please follow the prompt to enter your 
    :orange[**AWS Account ID**], the :orange[**Role name**], and 
    the :orange[**External ID**] that you created above.

''')
connect_clouds_img = Image.open('images/connect_clouds.jpg') 
st.image(connect_clouds_img)         



