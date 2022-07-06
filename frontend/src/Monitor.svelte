<script>
    import json from './wserver.json';
    import StatusButton from './StatusButton.svelte';

    const w_server = 'ws://' + json.websocket_server + ':8000/ws';
    console.log(w_server)
    
    const socket = new WebSocket(w_server);
    
    let recv = {};
    
    socket.addEventListener('open', function(event) {
        console.log("It's Open");
    });
    
    socket.addEventListener('message', function(event) {
        recv = JSON.parse(event.data);
    });
    
</script>

<br>
<table>
    <th>번 호</th>
    <th>장 비 명</th>
    <th>상 태</th>
    <th>I P</th>
    {#each Object.entries(recv) as [ID, paragraph]}
    <tr>
            <td>{ID}</td>
            <td>{paragraph['name']}</td>
            <td><StatusButton status={paragraph['status']}/></td>
            <td>{paragraph['IP']}</td>
    </tr>
    {/each}
</table>

<style>
    td {
        border-bottom: 1px solid #ddd;
        height: 40px;
        font-size: 36px;
    }
    tr:hover {
        background-color: coral;
    }
    tr {
        height: 40px;
        vertical-align: center;
        text-align: center;
    }
    th {
        background-color: #04AA6D;
        color: white;
        vertical-align: center;
        height: 30px;
        border-bottom: 1px solid #ddd;
        font-size: 36px;
    }
    table {
        width: 98%;
    }
</style>