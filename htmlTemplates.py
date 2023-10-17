css = '''
<style>
.chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
}
.chat-message.user {
    background-color: #2b313e;
}
.chat-message.bot {
    background-color: #475063;
}
.chat-message .avatar {
    width: 20%;
}
.chat-message .avatar-container {
    width: 78px; /* Ancho cuadrado deseado */
    height: 78px; /* Alto cuadrado deseado */
    overflow: hidden; /* Recorta cualquier contenido que se desborde */
}
.chat-message .avatar img {
    width: 100%; /* Asegura que la imagen llene el contenedor cuadrado */
    height: auto;
    border-radius: 50%; /* Hace que la imagen sea redonda */
    object-fit: cover;
}
.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <div class="avatar-container">
            <img src="https://cdn.pixabay.com/photo/2023/02/05/17/33/ai-generated-7770055_1280.jpg">
        </div>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <div class="avatar-container">
            <img src="https://cdn.pixabay.com/photo/2016/11/29/13/14/attractive-1869761_1280.jpg">
        </div>    
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''