import vk
import getpass


APP_ID = 6029694


def get_user_login():
    return input('Your vk login: ')


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friend_unids = api.friends.getOnline(order='hints')
    return api.users.get(user_ids=','.join(map(str, friend_unids)))


def output_friends_to_console(friends_online):
    print('Your friends online:')
    for friend in friends_online:
        print('{0} {1}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
