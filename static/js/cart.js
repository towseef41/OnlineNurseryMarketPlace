document.addEventListener("DOMContentLoaded", function(e) {

var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action

        console.log('productID:',productId,'action:',action)
        console.log('USER:',user)
        if(user === 'AnonymousUser'){
            console.log('Not Logged In')

        }else{
            updateUserOrder(productId, action)
        }
    })
}

});
function updateUserOrder(productId, action){
    console.log("User is logged in, Sending data...")

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type' : 'application/json',
            'X-CSRFToken': csrftoken,
            'Accept': "application/json",
        },
        body:JSON.stringify({'productId': productId,'action': action})
    })

    .then((response)=>{
        response.json()
    })

    .then((responseData) => {
        console.log('data:',responseData)
        location.reload()
        
    })
}

