package com.hunk.springbootdemo.Controller;

import com.hunk.springbootdemo.Dao.Product;
import com.hunk.springbootdemo.Service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@Controller
@RequestMapping("/product")
public class ProductController {
    @Autowired
    private ProductService productService;

    @GetMapping("")
    public String getProductList(Model model) {

        //customerMapper.insert("hunkguo", "1367435987346");


        List<Product> list=productService.getList();
        model.addAttribute("products",list);
        model.addAttribute("isProductManage", true);
        return "product/index";
    }

    @GetMapping("/create")
    public String getCreate(@ModelAttribute("productsInfo")  Product productsInfo){
        return "product/create";
    }

    @PostMapping("/create")
    public String postCreate(@ModelAttribute(value = "productsInfo") Product productsInfo){

        int result = productService.addProduct(productsInfo);

        if(result>0) {
            return "redirect:/product";
        }
        else
        {
            return "redirect:/product";
        }
    }



    @GetMapping("/intoUpdate")
    public String intoUpdate(@RequestParam("id") int id, Model model){
        Product productInfo = productService.findProductById(id);
        model.addAttribute("productInfo", productInfo);
        return "product/update";
    }

    @PostMapping("/saveupdate")
    public String saveUpdate(@ModelAttribute(value = "productInfo") Product productInfo){
        int result = productService.updateProduct(productInfo);
        if(result>0) {
            return "redirect:/product";
        }
        else
        {
            return "redirect:/product";
        }
    }
}
