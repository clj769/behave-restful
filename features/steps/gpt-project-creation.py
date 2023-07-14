# import filecmp
# import os
# from behave import given, when, then
# from assertpy import assert_that, fail
# import behave_restful.app as app
#
# @given('br-init is run with {location}')
# def setup_br_init_with_location(context, location):
#     context.location_param = None if location == 'no parameters' else location
#     context.project_created_dir = os.path.join(os.getcwd(), context.location_param or 'features')
#
# @when('the application executes')
# def execute_br_init(context):
#     try:
#         app.BrInitApp().init_project(context.location_param)
#     except Exception as exc:
#         context.caught_exception = exc
#
# @then('the project is created at {folder} folder')
# def verify_project_creation(context, folder):
#     comparison_result = filecmp.dircmp(context.project_src_dir, context.project_created_dir)
#     assert_that(comparison_result.diff_files).is_empty()
#
# @then('an exception is raised')
# def verify_exception_raised(context):
#     assert_that('caught_exception', 'Exception not raised').is_in(context)
