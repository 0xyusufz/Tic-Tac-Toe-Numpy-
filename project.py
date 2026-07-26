# import numpy as np

# board = np.zeros([3,3],dtype=int)

# def print_board(b):
#     symbols = {0: " ",1:"X",-1:"O"}
#     for r in range(3):
#         row= " | ".join([symbols[val] for val in b[r]])
#         print(" "+row)
#         if r < 2:
#             print("---+---+---")
#     print()

# def check_winner(b):
#     if 3 in np.sum(b,axis= 1) or 3 in np.sum(b,axis = 0) or 3 == np.trace(b) or 3 == np.trace(np.fliplr(b)):
#         return "X"
#     if -3 in np.sum(b,axis= 1) or -3 in np.sum(b,axis = 0) or -3 == np.trace(b) or -3 == np.trace(np.fliplr(b)):
#         return "O"
#     if not 0 in b:
#         return "DRAW"
#     return None

# current = 1
# print("Welcome to Tic-Tac-Toe")
# print_board(board)

# while True:
#     if current == 1:
#         player = "X"
#     else:
#         player = "O"
#     print(f"current chance : {player}")
#     try:
#         row = int(input(f"{player}: enter the row b/w 0 to 2: "))
#         if row >2 or row < 0:
#             raise Exception("please enter b/w 0 to 2: ")
#         col = int(input(f"{player}: enter the column b/w 0 to 2: "))
#         if col >2 or row < 0:
#             raise Exception("please enter b/w 0 to 2: ")
#     except ValueError:
#         print("please enter th number only \n")
#         continue
#     except Exception as e:
#         print(f"something went wrong \n{e} \n")
#         continue
    
#     if board[row,col] != 0:
#         print("cell already taken")
#         print_board(board)
#         continue
#     board[row,col] = current
#     print_board(board)
    
#     result = check_winner(board)
#     if result is not None:
#         if result == "DRAW":
#             print("Match Draw")
#         else:
#             print(f"{result}: wins")
#         break
#     if current == 1:
#         current = -1
#         print(f"{current} from if")
#     else:
#         current = 1





import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#111827,#1e293b);
}

.title{
text-align:center;
font-size:48px;
font-weight:700;
color:white;
margin-bottom:5px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#94a3b8;
margin-bottom:30px;
}

.turn{
padding:15px;
border-radius:12px;
background:rgba(255,255,255,.08);
backdrop-filter:blur(12px);
color:white;
font-size:20px;
text-align:center;
margin-bottom:25px;
border:1px solid rgba(255,255,255,.1);
}

.stButton>button{
height:90px;
width:90px;
font-size:42px;
font-weight:bold;
border-radius:18px;
border:none;
background:#1e293b;
color:white;
transition:.25s;
}

.stButton>button:hover{
background:#2563eb;
transform:scale(1.08);
box-shadow:0px 0px 18px #2563eb;
}

.reset button{
background:#16a34a;
color:white;
font-size:18px;
height:50px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Initialize
# -----------------------------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3,3),dtype=int)

if "current" not in st.session_state:
    st.session_state.current = 1

if "winner" not in st.session_state:
    st.session_state.winner = None

# -----------------------------
# Winner Check
# -----------------------------
def check_winner(board):

    if (
        3 in np.sum(board,axis=1)
        or 3 in np.sum(board,axis=0)
        or np.trace(board)==3
        or np.trace(np.fliplr(board))==3
    ):
        return "X"

    if (
        -3 in np.sum(board,axis=1)
        or -3 in np.sum(board,axis=0)
        or np.trace(board)==-3
        or np.trace(np.fliplr(board))==-3
    ):
        return "O"

    if not 0 in board:
        return "DRAW"

    return None

# -----------------------------
# Move
# -----------------------------
def play(row,col):

    if st.session_state.winner:
        return

    board=st.session_state.board

    if board[row,col]!=0:
        return

    board[row,col]=st.session_state.current

    result=check_winner(board)

    if result:
        st.session_state.winner=result
    else:
        st.session_state.current*=-1

# -----------------------------
# UI
# -----------------------------
st.markdown("<div class='title'>🎮 Tic Tac Toe</div>",unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Premium Streamlit Edition</div>",unsafe_allow_html=True)

if st.session_state.winner is None:
    turn="❌ X" if st.session_state.current==1 else "⭕ O"
    st.markdown(
        f"<div class='turn'>Current Turn : {turn}</div>",
        unsafe_allow_html=True
    )

symbols={
0:"",
1:"❌",
-1:"⭕"
}

board=st.session_state.board

for r in range(3):

    cols=st.columns(3)

    for c in range(3):

        with cols[c]:

            st.button(
                symbols[board[r,c]],
                key=f"{r}{c}",
                on_click=play,
                args=(r,c)
            )

st.write("")

if st.session_state.winner=="X":
    st.success("🏆 Player X Wins!")

elif st.session_state.winner=="O":
    st.success("🏆 Player O Wins!")

elif st.session_state.winner=="DRAW":
    st.warning("🤝 Match Draw!")

st.write("")

if st.button("🔄 New Game"):

    st.session_state.board=np.zeros((3,3),dtype=int)
    st.session_state.current=1
    st.session_state.winner=None
    st.rerun()