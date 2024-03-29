import { useEffect, useState} from 'react';
import axios from 'axios';

export const useGarfield = () => {
    interface DataType {
        data: string
    }
  const [data, setData] = useState<DataType>({data: ''});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data: response } = await axios.get('http://hey.now:8000/garfield');
        setData(response);
      } catch (error) {
        console.error(error)
      }
      setLoading(false);
    };

    fetchData();
  }, []);

  return {
    data,
    loading,
  };
};