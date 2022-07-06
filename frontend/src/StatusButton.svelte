<script>
	export let status;
    
    let opTexts = ["비 가 동", "가 동 중"]
    let opText;
    let btnClass;
    $: if(status == 1){
        btnClass = 'button button2'
        opText = opTexts[status];
    }else {
        btnClass = 'button button1'
        opText = opTexts[status];
    }
</script>
<style>
        .button {
        background-color: green;
        border: none;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 36px;
        margin: 4px 2px;
        width: 90%;
        height: 90%;
        border-radius: 4px;
    }
    .button1 {
        background-color: red;
    }
    .button2 {
        background-color: green;
    }
</style>
<button class={btnClass}>{opText}</button>