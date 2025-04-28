class Shipment {
    private String destination;
    private int weight;

    public Shipment (String destination, int weight){
        this.destination = destination;
        this.weight = weight;
    }
    public String getDestination(){
        return destination;
    }
    public int getWeight{
        return weight;
    }
}
List<String> destination = shipments.stream().filter(s -> "New York".equals(s.getDestination())).collect(Collectors.toList())
List<String> destination = shipments.stream().map(Shipment::getDestination()).collect(Collectors.toList())
int totalWeight = shipment.stream().map(Shipment::getWeight).reduce(0,Integer::sum);


import { useState } from "react";

interface CounterProps{
    title: string 
}

function Counter ({ title }: CounterProps){
    const [count, setCount] = useState<number>(0);

    return(
        <button onClick = {() => setCount(count+1)}>Increment</button>
        <button onClick = {()=> setCount(count-1)}Decrement </button>
    );

}

import { useState, useEffect} from "react"

function DataFetcher(){
    useEffect(()=> {
        fetch(api url)
        .then((res) => res.json())
        .then((data)=> setData(data))
        .catch((err)=> console.log(err));
    },[]);
    return (
        <data ? <pre>{JSON.stringify(data)}</pre>: <p> loading... </p>
    )
}

class Elevator{
    
}