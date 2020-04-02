package com.test.jmeter;

import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

@RestController
public class HelloController {

    @RequestMapping("/")
    public String index() {
        return "Greetings from Spring Boot!";
    }

    /**
     * 获取用户列表接口 GET请求
     * @return
     */
    @RequestMapping(value = "users", method = RequestMethod.GET)
    public @ResponseBody Object users(){
        List<String> userList = new ArrayList<>();
        userList.add("tom");
        userList.add("may");
        userList.add("jay");
        System.out.println("get request, users api");
        return userList;
    }

    /**
     * 登录接口 POST请求
     * @param name 用户名
     * @param pwd 密码
     * @return
     */
    @RequestMapping(value = "login", method = RequestMethod.POST)
    public @ResponseBody Object login(String name, String pwd){
        HashMap<String, Object> map = new HashMap<>();
        if ("jay".equals(name) && "123".equals(pwd)){
            map.put("status", 0);
        } else {
            map.put("status", -1);
        }
        System.out.println("post request, login api");
        return map;
    }

    /**
     *
     * @param name
     * @return
     */
    @RequestMapping(value = "info", method = RequestMethod.GET)
    public @ResponseBody Object info(String name){
        List<String> userList = new ArrayList<>();
        userList.add(name);
        userList.add(name.length()+"");
        System.out.println("get request, info api");
        return userList;
    }
}

