## Final Project Network Programming 2019

### Member
- Faizal Khilmi Muzakki 05111640000120
- Marde Fasma Ul'Aza 05111640000046
- M Hazdi Kurniawan 05111640000072

### Assignment Description
- Implementasikan code bapaknya
- Tambah fitur:
    - Logout
    - Group chat
    - Send file/image
- Implementasikan juga GUI
- Nggak harus sampai selesai, yang penting progress, hehe (( diusahakan ))

### Protocol
#### User => user
- `auth [username] [password]`

- `send [username_to] [message]`

- `inbox`

- `show_file`

- `send_file [username_to] [filename]`

- `download_file [filename]`

- `logout`

#### User => group
- `create_group [group_name]`

![create_group](img/fpprogjar-create_group.png)

- `join_group [group_token]`

![join_group](img/fpprogjar-join_group.png)

- `send_group [group_token] [message]`

![send_group](img/fpprogjar-send_group.png)

- `inbox_group [group_token]`

![inbox_group](img/fpprogjar-inbox_group.png)

- `leave_group [group_token]`

![inbox_group](img/fpprogjar-leave_group.png)
