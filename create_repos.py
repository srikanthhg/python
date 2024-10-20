import gitlab

URL='https://gitlab.com'
GITLAB_TOKEN='' #enter gitlab token here

try:
    gl = gitlab.Gitlab(url=URL, private_token=GITLAB_TOKEN)
    print("connected to gitlab...")

except gitlab.exceptions.GitlabConnectionError as e:
    print(f"Failed to cnnect to gitlab: {e.error_message}")
    exit(1)

project_names=[]
n=int(input("Enter no of projects you want ot create: "))
for i in range(n):
    ele=input("Enter the name of the project and press enter: ")
    project_names.append(ele)

print()
print("Below are the existing group names & group ids:")
print("-----------------------------------------------")

existing_groups = gl.groups.list(get_all=True)

for existing_group in existing_groups:
    print("Group Name:",existing_group.name, "-", existing_group.id)

namespace_id=input(f"Enter the existing namespace id where you want to create the new project {project_names}: ")
namespace_id=int(namespace_id)
print()

for existing_group in existing_groups:
    if existing_group.id == namespace_id:
        existing_projects = existing_group.projects.list(get_all=True)
        existing_project_names={existing_project.name for existing_project in existing_projects}
        for p_names in range(len(project_names)):

            if project_names[p_names] in existing_project_names:
                print(project_names[p_names], "has already been taken")

            else:
                try:
                    print(f"Creating Project.....{project_names[p_names]}")
                    project = gl.projects.create({
                        'name': project_names[p_names],
                        'description': 'This is project three.',
                        'visibility': 'private',
                        'namespace_id': namespace_id
                    })
                    print(f"Project '{project_names[p_names]}' created successfully in {existing_group.name}")
                except gitlab.exceptions.GitlabCreateError as e:
                    print(f"Failed to create project: {e.error_message}")
                    print(f"Response code: {e.response_code}")
                    print(f"Response body: {e.response_body}")



print("If you want to delete repositories press 1 or press 0")
if bool(input()):
    print("press 1 for delete all repositories in a specific group")
    if bool(input()):
    
        print("List of existing namespaces")
        existing_groups = gl.groups.list(get_all=True)
        for existing_group in existing_groups:
            print("Group Name:",existing_group.name, "-", existing_group.id)
            namespace_id=input(f"Enter the existing namespace id where you want to delete all projects: ")
            namespace_id=int(namespace_id)
    
            existing_groups = gl.groups.list(get_all=True)
            for existing_group in existing_groups:
                if existing_group.name == namespace_id:
                    existing_projects = existing_group.projects.list(get_all=True)
                    for existing_project in existing_projects:
                        print(f"Deleting project: {existing_group.name}: {existing_project.name} : {existing_project.id}" )
                        project.delete()
    else:
        existing_projects = existing_group.projects.list(get_all=True)
        for existing_project in existing_projects:
            print(f"List of projects: {existing_group.name}: {existing_project.name} : {existing_project.id}" )
            a= input("enter project id to delete:")
            gl.projects.delete(a)
            print(f"{a} project deleted successfully")
            print()




   
    