#include <iostream>
#include <algorithm>
#include <vector>
#include <thread>

int main(void){
    std::vector<std::thread> workers;
    for (int i =0; i<10;i++){
        workers.push_back(std::thread([i](){
           std::cout<<"thread "<<i<<std::endl; 
        }));
    }
    std::cout<<"Main"<<std::endl;
    std::for_each(workers.begin(),workers.end(),[](std::thread & th){
        th.join();
    });
    return 0;
}
        
