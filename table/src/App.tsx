import React, { useState, useEffect} from "react";

const url = "http://localhost:8000/visitors";

interface Table {
  id: number,
  ip_address: string,
  request_url: string,
  request_path: string,
  request_method: string,
  request_time: string,
}

const Table: React.FC = () => {
    const [data, setData] = useState<Table[]>([]);


    useEffect(() => {
      fetch(url)  
        .then(res => res.json())
        .then(data => setData(data));
        console.log(data);
    }, []);


    return (
        <div>
          <h1>Logs</h1>
          <table>
            <thead>
                <tr>
                  <th>Id</th>
                  <th>IP Address</th>
                  <th>Request URL</th>
                  <th>Request Path</th>
                  <th>Request Method</th>
                  <th>Request Time</th>
                </tr>
              </thead>  


            <tbody>
            {data.map((item, index) => (
              <tr key={index}> 
                <td>{item.id}</td>  
                <td>{item.ip_address}</td>     
                <td>{item.request_url}</td>        
                <td>{item.request_path}</td>
                <td>{item.request_method}</td>
                <td>{item.request_time}</td>  
              </tr>
            ))}
          </tbody>  

          </table>

        </div>

      );

};

export default Table;