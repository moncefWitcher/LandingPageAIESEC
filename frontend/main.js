



console.log('hello word')

const DataForm= new FormData();
DataForm.append('username' , 'anotherUser')
DataForm.append('email' , 'user@gmail.com')
DataForm.append('password' , 'chamali123@')

const submiting = async ()=> {
await axios ({
    method : 'post' ,
    url : 'https://aieseclandingpage.herokuapp.com/log/singin/' ,
    data : DataForm
})
.then((response)=>{
    console.log(response.data) ;

}) .catch(function (error) {
    console.log(error)
  });


}

const login = async ()=> {
    await axios ({
        method : 'post' ,
        url : 'http://127.0.0.1:8000/log/in/' ,
        data : DataForm
    })
    .then((response)=>{
        console.log(response.data) ;
    
    }) .catch(function (error) {
        console.log(error)
      });
    
    
    }


    const changePassword = async ()=> {
        
        await axios ({
            method : 'post' ,
            url : 'http://127.0.0.1:8000/log/changepassword/' ,
            data : DataForm
        })
        .then((response)=>{
            console.log(response.data) ;
        
        }) .catch(function (error) {
            console.log(error)
          });
        
        
        }

        const testConnection = async ()=> {
            console.log('pushing')
            
            await axios ({
                method : 'post' ,
                url : 'https://aieseclandingpage.herokuapp.com/' ,
                data : DataForm
            })
            .then((response)=>{
                console.log(response.data) ;
            
            }) .catch(function (error) {
                console.log(error)
              });
            }
        // https://aieseclandingpage.herokuapp.com/mc_info/team_members/create/