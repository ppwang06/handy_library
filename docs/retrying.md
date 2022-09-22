###### retrying使用   

[参考文章](https://www.cnblogs.com/tulintao/p/11604808.html)  

[简单样例](../tests/tests_retrying.py)

`stop_max_attempt_number`： 在停止之前尝试的最大次数，最后一次如果还是有异常就会抛出异常，停止运行，默认是五次（强调总次数）   
   
`stop_max_delay`: 最大延迟时间，大概的意思就是：如果调用的函数抛出异常了，那么就会重复调用这个函数，最大调用时间，默认100毫秒   

`wait_random_min`: 在两次调用方法停留时长，停留最短的时间，默认是0   

`wait_random_max`: 在两次调用方法停留时长，停留最长时间，默认是1000毫秒  

`wait_incrementing_increment`: 每调用一次就会增加的时长，默认是100毫秒   

`retry_on_exception`: 指定一个函数，如果这个函数返回指定异常，就会重试，如果不是指定的异常就会推出

`retry_on_result`: 指定一个函数，如果指定的函数返回True，就重试，否则抛出异常退出

`wrap_exception`:  参数设置为True/False，如果指定的异常类型，包裹在retryError中，就会看到RetryError和程序抛出的Exception error

`stop_func`: 每次抛出异常的时候都会执行的函数，如果stop_max_delay、stop_max_attmpt_number配合使用，则后两个就会失效，指定的stop_func会有两个参数：attempt、delay

`wait_func`: 和stop_func的用法差不多，就不过多的描述了  


