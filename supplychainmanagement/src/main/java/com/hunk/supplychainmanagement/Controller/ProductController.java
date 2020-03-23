package com.hunk.supplychainmanagement.Controller;

import com.hunk.supplychainmanagement.Entity.*;
import com.hunk.supplychainmanagement.Entity.ProductRepository;
import com.hunk.supplychainmanagement.QiniuUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.FileInputStream;
import java.util.List;
import java.util.UUID;

@Controller
@RequestMapping("/product")
public class ProductController {
    @Autowired
    private ProductRepository productRepository;

    @GetMapping("")
    public String getCustomerList(Model model) {

        List<Product> list=productRepository.findAll();
        model.addAttribute("products",list);
        model.addAttribute("isProductManage", true);
        return "product/index";
    }

    @GetMapping("/create")
    public String getCreate(@ModelAttribute("productInfo") Product productInfo){
        return "product/create";
    }

    @PostMapping("/save")
    public String postSave(@ModelAttribute(value = "productInfo") Product productInfo){
        productRepository.save(productInfo);
        return "redirect:/product";

    }

    @GetMapping("/edit/{id}")
    public String getEdit(@PathVariable("id") int id, Model model){
        Product productInfo = productRepository.getOne(id);
        model.addAttribute("productInfo", productInfo);
        return "product/edit";
    }

    @PostMapping("/update")
    public String postUpdate(@ModelAttribute(value = "productInfo") Product productInfo){

        productRepository.save(productInfo);
        return "redirect:/product";
    }

    @GetMapping("/delete/{id}")
    public String getDelete(@PathVariable("id") int id, Model model){
        Product productInfo = productRepository.getOne(id);
        productRepository.delete(productInfo);
        return "redirect:/product";
    }


    @GetMapping("/detail/{id}")
    public String getProductDetail(@PathVariable("id") int id, Model model){
        Product productInfo = productRepository.getOne(id);
        model.addAttribute("productInfo", productInfo);

        List <ProductImage> productImageList = productImageRepository.findByProduct(productInfo);
        model.addAttribute("productImageList", productImageList);

        return "product/detail";
    }


    @Autowired
    private QiniuUtil qiniuUtil;

    @Autowired
    private ProductImageRepository productImageRepository;

    @PostMapping("/productimgupload")
    public String productImgUpload(@RequestParam("productinputfile") MultipartFile file,@RequestParam("id") int id,@RequestParam("description") String description,Model model) {

        Product productInfo = productRepository.getOne(id);

        if (file.isEmpty()) {
            return "请选择文件";
        }
        try {
            FileInputStream fileInputStream = (FileInputStream) file.getInputStream();
            String originalFilename = file.getOriginalFilename();
            String fileExtend = originalFilename.substring(originalFilename.lastIndexOf("."));
            //默认不指定key的情况下，以文件内容的hash值作为文件名
            String fileKey = UUID.randomUUID().toString().replace("-", "") + fileExtend;
            String filpath = "http://"+qiniuUtil.upload(fileInputStream,fileKey);
            //q78df05md.bkt.clouddn.com/7a59ac0db37844df8604b849fd8ee277.JPG


            ProductImage pi = new ProductImage();
            pi.setImageFilePath(filpath);
            pi.setProduct(productInfo);
            pi.setDescription(description);
            productImageRepository.save(pi);

            return "redirect:/product/detail/"+id;
        } catch (Exception e) {
            e.printStackTrace();

            model.addAttribute("message", "上传失败");
            return "redirect:/product/detail/"+id;
        }

    }
}
