package com.hunk.supplychainmanagement.Controller;

import com.hunk.supplychainmanagement.Entity.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@Controller
@RequestMapping("/returns")
public class ReturnsController {
    @Autowired
    private ProductRepository productRepository;
    @Autowired
    private OrderRepository orderRepository;
    @Autowired
    private ReturnsRepository returnsRepository;
    @GetMapping("")
    public String getReturnsList(Model model) {

        List<Returns> list=returnsRepository.findAll();
        model.addAttribute("returns",list);
        model.addAttribute("isReturnsManage", true);
        return "returns/index";
    }
    @GetMapping("/create")
    public String getCreate(@ModelAttribute("returnsInfo") Returns returnsInfo, Model model){
        List<Product> product_list=productRepository.findAll();
        List<Order> order_list=orderRepository.findAll();
        model.addAttribute("product_list",product_list);
        model.addAttribute("order_list",order_list);
        return "returns/create";
    }
    @PostMapping("/save")
    public String postSave(@ModelAttribute(value = "returnsInfo") @Valid Returns returnsInfo){
        returnsRepository.save(returnsInfo);
        return "redirect:/returns";

    }
    @GetMapping("/edit/{id}")
    public String getEdit(@PathVariable("id") int id, Model model){
        Returns returnsInfo = returnsRepository.getOne(id);
        List<Product> product_list=productRepository.findAll();
        List<Order> order_list=orderRepository.findAll();
        model.addAttribute("product_list",product_list);
        model.addAttribute("order_list",order_list);
        model.addAttribute("returnsInfo", returnsInfo);
        return "returns/edit";
    }

    @PostMapping("/update")
    public String postUpdate(@ModelAttribute(value = "returnsInfo") @Valid Returns returnsInfo){

        returnsRepository.save(returnsInfo);
        return "redirect:/returns";
    }

    @GetMapping("/delete/{id}")
    public String getDelete(@PathVariable("id") int id, Model model){
        Returns returnsInfo = returnsRepository.getOne(id);
        returnsRepository.delete(returnsInfo);
        return "redirect:/returns";
    }
}
