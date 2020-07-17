# coding=utf8
import re

text = '''
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <meta name="renderer" content="webkit">
    <meta name="SiteName" content="网站名称">
    <meta name="SiteDomain" content="网站域名">
    <meta name="SiteIDCode" content="政府网站标识码">
    <meta name="Description" content="描述">
    <meta name="Keywords" content="关键词">
    <title>【湖北省中心】（武西高铁云梦东站联络线）孝感市孝云大道长兴三路延伸工程与京广铁路交叉工程XYSG标段施工总价承包招标资格预审公告(代招标公告)<font color='#2ac36e'>[文件获取中]</font></title>
    <link rel="stylesheet" href="/shengbenji/js/lib/chosen/chosen.css">
    <link rel="stylesheet" href="/shengbenji/css/common.css">
    <link rel="stylesheet" href="/shengbenji/css/article.css">
	<link rel="stylesheet" href="/shengbenji/css/detail.css">
    <script src="/shengbenji/js/lib/jquery.min.js"></script>
    <!--[if lt IE 9]>  
         <script src="/shengbenjijs/respond.min.js"></script>
    <![endif]-->

   <link rel="stylesheet" href="/shengbenji/css/webBuilderCommonGray.css"></head>

<body>
    <!-- header -->
    <div id="header"></div>
    <!-- 正文 -->
    <div class="ewb-container">
        <!-- 位置 -->
        <div class="ewb-location">
            当前的位置：
            <a href="/shengbenji/">首页 </a>&gt; <span><a href="/shengbenji/jyxx/about.html">交易信息</a> </span>&gt; <span><a href="/shengbenji/jyxx/004002/about.html">招标公告</a> </span>&gt; <span><a href="/shengbenji/jyxx/004002/004002004/about.html" id="viewGuid" value="cms_63f44e47-030e-4892-99f9-d0a65c278332" style="color:orange;">铁路工程</a> </span><span style="display: none;">
				<div id="cate">004002004</div></span>
        </div>
        <!-- article -->
        <!-- <div class="ewb-article-font">
									【字体：
									<a class="changeSize" href="javascript:void(0);">大</a>
									<a class="changeSize" href="javascript:void(0);">中</a>
									<a class="changeSize" href="javascript:void(0);">小</a>】
								</div> -->
        <div class="ewb-article">
			 
						<div class="news-article">
							<span style="display: none;" id="infoid">63f44e47-030e-4892-99f9-d0a65c278332</span>
							<h3>【湖北省中心】（武西高铁云梦东站联络线）孝感市孝云大道长兴三路延伸工程与京广铁路交叉工程XYSG标段施工总价承包招标资格预审公告(代招标公告)<font color='#2ac36e'>[文件获取中]</font></h3>
							<div class="ewb-article-sources clearfix">
								<span></span>发布时间：2020-07-16 18:25<span></span>浏览：<span id="infoViewCount"></span>次
							</div>
							<div class="ewb-article-info">
								<div class="ewb-article-p"  id="infoContentM">
									<!DOCTYPE html>
<html xmlns='http://www.w3.org/1999/xhtml'>
<head>
<meta charset='UTF-8' />
<meta http-equiv='X-UA-Compatible' content='IE=edge' />
<style type="text/css">
.table-c {
	border-right: 1px solid;
	border-bottom: 1px solid
}

.table-c td {
	border-left: 1px solid;
	border-top: 1px solid
}
body {
	background: url(http://www.hbbidcloud.cn:8080/TPBidder/jsgcztbmis2/images/hbpztbmark.jpg) repeat;
	word-wrap:break-word;
	word-break:break-all;
}
</style>
<title>资格预审公告</title>
</head>
<body>
	<table width="100%" border="0" style="font-size: 22px; font-family: '宋体'; line-height: 2.5">
		<tr><td><div align="center">（武西高铁云梦东站联络线）孝感市孝云大道长兴三路延伸工程与京广铁路交叉工程XYSG标段施工总价承包招标资格预审公告(代招标公告)</div></td></tr>
		<tr>
			<td><div align="center">
					招标编号：HBSJ-202007TL-027001001
				</div></td>
		</tr>
		<tr>
			<td colspan="2">1.招标条件</td>
		</tr>
		<tr>
			 <td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;本招标项目（武西高铁云梦东站联络线）孝感市孝云大道长兴三路延伸工程与京广铁路交叉工程（项目名称）已由孝感市发展和改革委员会以《市发展改革委关于（武西高铁孝感西站联络线）孝感市孝云大道长兴三路延伸工程可行性研究报告的批复》（孝发改审批〔2018〕147号）批准建设，项目业主为孝感市公路管理局，建设资金来自自筹和银行贷款，项目出资比例为自筹25%和银行贷款75%，招标人为武汉武铁工程项目管理有限公司,招标代理机构为湖北华科工程咨询有限公司。项目已具备招标条件，现进行公开招标，特邀请有兴趣的潜在投标人（以下简称申请人）提出资格预审申请。</td>
		</tr>
		<tr>
			<td colspan="2">2.项目概况与招标范围</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;2.1项目概况</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;建设地点：湖北省孝感市 <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;建设规模：孝感市孝云大道长兴三路延伸工程起于国道G107，延现状长兴三路向西下穿武西客专、上跨孝花线、京广铁路。本工程于京广铁路上行线K1120+144.942处拆除既有1×20m简支T梁立交桥，分幅新建2×60m预应力砼T构箱梁上跨京广铁路，与铁路交叉角度为88.7°，采用挂篮悬浇+转体法施工；桥梁下部采用板式空心桥墩；桩基采用钻孔灌注桩。主要技术标准：城市主干道；双向六车道；计算行车速度60km/h；汽车荷载等级为城-A级，跨铁部分考虑1.3倍的增大系数；桥下铁路净空不小于8.2m；设计安全等级一级；主体结构使用年限100年。<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其他：/<br>
			</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;2.2招标范围</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;招标范围：（武西高铁云梦东站联络线）孝感市孝云大道长兴三路延伸工程与京广铁路交叉工程的建筑工程；招标主要内容为桥涵、大临设施及过渡工程等。<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;标段划分：划分为1个施工标段（XYSG标段），标段内容为中铁武汉勘察设计研究院有限公司2020年4月设计的《（武西高铁云梦东站联络线）孝感市孝云大道长兴三路延伸工程与京广铁路交叉工程施工图设计（全一册）》所涉及的桥涵、大临设施及过渡工程（汽车运输便道、临水、临电、材料场、电力过渡）等工程（不含沥青砼铺装、伸缩缝安装，临建设施砼硬面凿除及工程建设引起的铁路设施的防护和迁改等）。<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;计划工期：660日历天，计划开工日期2020年8月30日<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;合同估算价：6400.0万元<br>
			</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;2.3其他：/<br>
			</td>
		</tr>
		<tr>
			<td colspan="2">3.申请人资格要求</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;3.1本次资格预审要求申请人具备 ：在中华人民共和国境内合法注册的独立法人，具备市政公用工程施工总承包一级及以上或桥梁工程专业承包二级及以上资质，同时具备铁路工程施工总承包二级及以上资质，2015年7月28日至2020年7月27日（递交资格预审文件之日起前5年内）具有上跨铁路营业线转体施工的桥梁工程施工业绩，并在人员、设备、资金等方面具有相应的施工能力。其中，申请人拟派项目经理须具备市政公用工程专业（或铁路工程专业）一级注册建造师执业资格和有效的安全生产考核合格证书，且未在其他在建工程项目任职。（具体要求详见资格预审文件）<br> &nbsp;&nbsp;&nbsp;&nbsp;3.2本次资格预审接受联合体资格预审申请。联合体申请资格预审的，应满足下列要求：联合体牵头人须具备市政公用工程施工总承包一级及以上或桥梁工程专业承包二级及以上资质，联合体成员（含联合体牵头人）数量不超过两家。组成联合体的各方不得再单独或与其他单位组成联合体参与本项目投标<br>
				&nbsp;&nbsp;&nbsp;&nbsp;3.3各申请人可就本项目上述标段中的/(具体数量）个标段提出资格预审申请，通过资格审查后参加相应标段的投标，但最多允许中标/(具体数量）个标段(适用于分标段的招标项目)。<br>
				&nbsp;&nbsp;&nbsp;&nbsp;3.4其它：/
			</td>
		</tr>
		<tr>
			<td colspan="2">4.资格预审方法</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;本次资格预审采用合格制。			</td>
		</tr>
		<tr>
			<td colspan="2">5.资格预审文件的获取</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;5.1
				凡有意申请资格预审者（若为联合体申请，指联合体所有成员），应当在湖北省电子招投标交易平台（以下简称“电子交易平台”，下同）（网址：www.hbbidcloud.cn）进行注册登记，并办理CA数字证书（具体操作参见“电子交易平台”—办事指南—交易主体注册登记指南）。<br>
				&nbsp;&nbsp;&nbsp;&nbsp;5.2
				完成注册登记后，请于2020年07月17日至2020年07月21日24：00时止（北京时间、下同），通过互联网使用CA数字证书登录“电子交易平台”，在所申请标段免费下载资格预审文件。联合体申请的，由联合体牵头人下载资格预审文件（具体操作参见“电子交易平台”—办事指南—招标（资审）文件下载指南）。未按规定从“电子交易平台”下载资格预审文件的，招标人
				（“电子交易平台”）拒收其申请文件。<br>
			</td>
		</tr>
		<tr>
			<td colspan="2">6.资格预审申请文件的递交</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;6.1 资格预审申请文件递交截止时间为：2020年07月28日 14时30分<br>
				&nbsp;&nbsp;&nbsp;&nbsp;6.2 申请人应当在资格预审申请截止时间前，通过互联网使用CA数字证书登录“电子交易平台”，将<b>加密的电子资格预审申请文件</b>上传，申请人完成资格预审申请文件上传后，“电子交易平台”即时向申请人发出电子签收凭证，递交时间以电子签收凭证载明的传输完成时间为准。逾期未完成上传或未加密的电子资格预审申请文件，招标人（“电子交易平台”）将拒收。<br>
			</td>
		</tr>
		<tr>
			<td colspan="2">7.发布公告的媒介</td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;本次资格预审公告同时在湖北省公共资源交易电子服务系统（网址：www.hbggzyfwpt.cn）、中国招标投标公共服务平台（http://www.cebpubservice.com）上发布</td>
		</tr>
		<tr>
			<td colspan="2">8.联系方式</td>
		</tr>
		<tr>
			<td width="1000" colspan="2"><table width="1000" border="0" style="font-size: 19px; font-family: '宋体'">
					<tr>
						<td width="170px"><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;招标人:</div></td>
						<td ><div align="left">武汉武铁工程项目管理有限公司</div></td>
						<td width="170px"><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;代理机构:</div></td>
						<td ><div align="left">湖北华科工程咨询有限公司</div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;地址:</div></td>
						<td><div align="left">武汉市武昌区八一路2号</div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;地址:</div></td>
						<td><div align="left">武汉市洪山区徐东大街团结名居桔园</div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;邮编:</div></td>
						<td><div align="left"></div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;邮编:</div></td>
						<td><div align="left"></div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;联系人:</div></td>
						<td><div align="left">郑亮华，余工</div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;联系人:</div></td>
						<td><div align="left">吴昱</div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;电话:</div></td>
						<td><div align="left">027-51121283</div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;电话:</div></td>
						<td><div align="left">15071455612</div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;传真:</div></td>
						<td><div align="left"></div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;传真:</div></td>
						<td><div align="left"></div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;电子邮件:</div></td>
						<td><div align="left"></div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;电子邮件:</div></td>
						<td><div align="left"></div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;网 址:</div></td>
						<td><div align="left"></div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;网 址:</div></td>
						<td><div align="left"></div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;开户银行:</div></td>
						<td><div align="left"></div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;开户银行:</div></td>
						<td><div align="left"></div></td>
					</tr>
					<tr>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;账 号:</div></td>
						<td><div align="left"></div></td>
						<td><div align="left">&nbsp;&nbsp;&nbsp;&nbsp;账 号:</div></td>
						<td><div align="left"></div></td>
					</tr>
				</table></td>
		</tr>
		<tr>
			<td><div align="right">2020年07月16日</div></td>
		</tr>

		<tr>
			<td colspan="2">备注:“在所申请标段免费下载资格预审文件”是指申请人拟申请某标段资格预审的，应按规定下载该标段的资格预审文件。申请人的下载活动“电子交易平台”将予以记录，并可在“下载情况查询”中查看，该记录作为申请人是否下载该标段资格预审文件的依据。</td>
		</tr>
	</table>
</body>
</html></div>
							</div>
						</div><input type="hidden" id="souceinfoid" value="63f44e47-030e-4892-99f9-d0a65c278332"/>
					<!-- <script type="text/javascript">
				$("#infoContentM").find("span").attr("style", "font-size: 18px;line-height: 24px;text-indent: 2em;");
				$(".changeSize").on('click', function(){
					var judge = $(this).html().trim();
					var size;
					if(judge == "大"){
						size = 22;
					}else if(judge == "中"){
						size = 20;
					}else if(judge == "小"){
						size = 16;
					}else{
						size = 18;
					}
					$("#infoContentM").attr("style", "font-size: "+ size + "px;");
					$("#infoContentM").find("span").attr("style", "font-size: "+ size + "px;");
				})
			</script> -->
            <p class="ewb-article-add clearfix">
				
            </p>
        </div>
    </div>
    <!-- footer -->
    <div id="footer"></div>
    <!-- 页面脚本 -->
	<script src="/shengbenji/js/webBuilderCommon.js"></script>
    <script src="/shengbenji/js/lib/chosen/chosen.jquery.js"></script>
    <script src="/shengbenji/js/lib/respond.min.js"></script>
    <script src="/shengbenji/js/common.js"></script>
	<script src="/shengbenji/js/lib/tabview.js"></script>
	<script src="/shengbenji/js/pageView.js"></script>
	
</body>

</html>
'''
text2 = '''

<!DOCTYPE html>
<html>

<head>
    <!-- 必须，不要动 -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="renderer" content="webkit" />
    <!-- 移动端必须、PC端非响应式可以去掉 -->
    <meta name="viewport" content="initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no">
    <!-- SEO用 -->
    <meta name="SiteName" content="湖北省公共资源交易中心（湖北省政府采购中心）">
<meta name="SiteDomain" content="http://jycg.hubei.gov.cn/">
<meta name="SiteIDCode" content="4200000016">
<meta name="ColumnName" content="政府采购" />
<meta name="ColumnDescription" content="政府采购,主要用于湖北省公共资源交易中心（湖北省政府采购中心）政府采购，需求公告，采购公告，变更公告，结果公告，其他公告，采购合同，办事指南等信息的发布" />
<meta name="ColumnKeywords" content="湖北省公共资源交易中心（湖北省政府采购中心）,湖北省交易采购中心,湖北交易采购中心,省交易采购中心,湖北省公共资源交易中心,湖北公共资源交易中心,公共资源交易中心,湖北政府采购中心,省公共资源交易中心,省政府采购中心湖北省政府采购中心,政府采购中心,湖北省交易（采购）中心,省交易（采购）中心政府采购,需求公告采购公告变更公告结果公告其他公告采购合同办事指南" />
<meta name="ColumnType" content="政府采购" />
    <title>政府采购 - 湖北省公共资源交易中心（湖北省政府采购中心）
    </title>
    <link rel="shortcut icon" href="http://jycg.hubei.gov.cn/material/images/ico.png" />
    <link rel="stylesheet" type="text/css" href="http://jycg.hubei.gov.cn/material/css/bootstrap.css" />
    <link rel="stylesheet" type="text/css" href="http://jycg.hubei.gov.cn/material/css/common.css" />
    <link rel="stylesheet" type="text/css" href="http://jycg.hubei.gov.cn/material/css/ui03.css" />
    <!-- 兼容低版本IE -->
    <!--[if lt IE 9]>
    <script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/html5shiv.js"></script>
    <script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/respond.js"></script>
    <![endif]-->
    <meta content="{qt1074790464hB79EjVUoj_eY_NFv9JlnXANxV2Ba5vMb8J1594950597190Vmv3vAnekh00bscekh0gBqr0l3650IVRr55PONtM0.eshuIB3C4PbyEBq2ek0IJkeRU9q2U1VxQqwTqoq1EYVnY1yAwAVqlccGvUamLWoLiSzIrhv2lziova1A;qm45414D3e2af6qqqqqqqqqqqqqqqqk674l4096qhuQ_UJp5BP9Qr0qqr0iK0R7wbenFUf.QAqqK_N7YKaN24QD9GGKrXUguZqQo27LMcfjhCGLMcR.tTGXVnNUx2V7|[mU27svQLwn7Xr1EIpSS2posihhxQTn4i8WmPnmDew.R8BKo8xI0OTc4BxW3G5btd3jRtj2u6RBeZ.6uaRBNZ.mDfpQef6YbGAH7GyTObhBS7ST5FU5y7_ldEA7xWuDUuIX2b4DDsKQYV2648wWpunbhIIJwdCChKhBxDy2I0UJ794UhkwdAPe1_EpJekn2s4w_yR2TnfhLNA76bCIt2PdoMbV4mI7mh5x3L4dvkZwt9OgsX4RX2SdYi7U_e1gnKpi5za_61ZE5L4zbMbIg9byvcFw4Rm9c4UR_ysGciWK_7GCbU1ANxqOccK3F2gfng}9EtE1br1sDzRmTmUHV7Ein0ot1WeqbpjYlywinT8H3wJVCmMU8HSc69UKYxgoylOUAexUCTM8Rzrru9PAQewHL0XCAMpmfVn2V_0o4a_qpMSCjmtOAF2WjAOjrhfmBYiys4Zo5a_GVhfxLAOSqHqxGSDlAiGF4SIb3MyVzTF_8tecP0KrYWTr2mcxKAc80qqqqqqqq!x7z,aac,amr,asm,avi,bak,bat,bmp,bin,c,cab,css,csv,com,cpp,dat,dll,doc,dot,docx,exe,eot,fla,flc,fon,fot,font,gdb,gif,gz,gho,hlp,hpp,htc,ico,ini,inf,ins,iso,js,jar,jpg,jpeg,json,java,lib,log,mid,mp4,mpa,m4a,mp3,mpg,mkv,mod,mov,mim,mpp,msi,mpeg,obj,ocx,ogg,olb,ole,otf,py,pyc,pas,pgm,ppm,pps,ppt,pdf,pptx,png,pic,pli,psd,qif,qtx,ra,rm,ram,rmvb,reg,res,rtf,rar,so,sbl,sfx,swa,swf,svg,sys,tar,taz,tif,tiff,torrent,txt,ttf,vsd,vss,vsw,vxd,woff,woff2,wmv,wma,wav,wps,xbm,xpm,xls,xlsx,xsl,xml,z,zip,apk,plist,ipaqqqqqqq"><!--[if lt IE 9]><script r='m'>document.createElement("section")</script><![endif]--><script type="text/javascript" charset="iso-8859-1" src="/4QbVtADbnLVIc/d.FxJzG50F.3e2af61.js" r='m'></script><script type="text/javascript" r="m">(function(){var _$ll=0,_$lQ=[[7,3,2,4,1,0,6,5],[49,44,46,44,92,70,84,47,93,74,45,74,22,41,79,74,10,63,77,8,30,50,83,64,12,85,90,97,74,25,57,82,32,26,52,28,18,73,43,59,28,67,40,9,69,71,28,65,76,4,76,72,70,35,28,78,56,81,21,94,5,13,53,28,31,58,28,20,54,19,1,74,38,91,86,19,3,37,74,23,19,74,98,70,66,48,75,62,39,74,87,34,51,80,61,11,33,7,17,88,96,16,89,27,29,95,55,0,15,42,24,68,6,14,2,60,36,74],[5,3,12,33,12,19,17,32,28,10,31,9,14,20,7,31,6,4,26,1,25,13,23,13,24,15,0,30,0,29,0,2,0,21,16,0,8,0,22,11,27,18,31],[23,45,31,42,5,28,10,13,21,26,24,36,16,27,39,43,20,38,22,47,34,36,12,5,4,11,6,15,3,32,3,45,8,29,37,18,8,30,7,25,7,35,9,35,17,36,7,46,17,43,19,2,1,44,40,0,25,17,46,19,32,14,33,41,10],[30,24,2,22,35,4,26,21,16,3,7,13,24,15,10,28,24,33,18,28,5,31,9,1,32,29,27,19,5,0,20,11,17,12,32,8,19,34,0,24,25,36,6,23,21,14,24]];function _$o8(_$oT,_$gR){return _$FD.Math.abs(_$oT)%_$gR;}function _$LM(_$A3){var _$Mx=_$5u();if(_$5u()){_$A3[_$o8(_$yi()+_$Bt(),16)]=_$_W(_$A3);}_$A3[2]=_$zr()-_$A3[_$o8(_$ir(),16)];var _$oe=_$cU(_$A3);var _$3J=_$ld(_$A3);return _$hL(_$A3);}function _$5u(){return 1}function _$yi(){return 13}function _$Bt(){return 3}function _$_W(_$A3){_$A3[_$o8(_$n2(),16)]=_$I6();var _$Mx=_$NL();var _$oe=_$fS();_$A3[0]=_$OX();return _$ir();}function _$n2(){return 5}function _$I6(){return 11}function _$NL(){return 4}function _$fS(){return 2}function _$OX(){return 14}function _$ir(){return 12}function _$zr(){return 9}function _$cU(_$A3){_$A3[4]=_$fS();_$A3[_$o8(_$zr(),16)]=_$$o();var _$Mx=_$lV();var _$3J=_$9T();return _$NL();}function _$$o(){return 15}function _$lV(){return 8}function _$9T(){return 6}function _$ld(_$A3){_$A3[0]=_$OX();_$fK(_$A3);_$A3[_$o8(_$lV(),16)]=_$9T();return _$yi()+_$Bt();}function _$fK(_$A3){_$A3[10]=_$lV();var _$3J=_$yi();var _$oe=_$Bt();_$A3[9]=_$$o();return _$n2();}function _$hL(_$A3){if(_$n2()){_$A3[11]=_$5u();}_$ES(_$A3);if(_$n2()+_$I6()){if(_$93()){_$A3[13]=_$Bt();}}_$A3[_$o8(_$A3[_$o8(_$NL(),16)],16)]=_$5W(_$A3);var _$Mx=_$$o();var _$3J=_$n2();return _$A3[_$o8(_$5u()+_$93(),16)];}function _$ES(_$A3){var _$Mx=_$lV();if(_$$o()){var _$3J=_$9T();}_$AL(_$A3);_$A3[_$o8(_$yi(),16)]=_$Bt();return _$zr();}function _$AL(_$A3){var _$3J=_$LR();var _$Mx=_$lV();_$A3[6]=_$NL();var _$Mx=_$zr();var _$3J=_$$o();_$A3[_$o8(_$LR(),16)]=_$lV();return _$9T();}function _$LR(){return 10}function _$93(){return 7}function _$5W(_$A3){_$A3[_$o8(_$zr(),16)]=_$$o();_$A3[5]=_$I6();_$A3[_$o8(_$9T(),16)]=_$NL();return _$fS();}var _$cy,_$9r,_$FD,_$Kz,_$V8,_$LM,_$G6;var _$wj,_$Gj,_$Pb=_$ll,_$Ix=_$lQ[0];while(1){_$Gj=_$Ix[_$Pb++];if(_$Gj<4){if(_$Gj<1){_$V8=_$FD['$_ts']={};}else if(_$Gj<2){if( !_$wj)_$Pb+=1;}else if(_$Gj<3){_$V8=_$FD['$_ts'];}else{_$FD=window,_$G6=String,_$Kz=Array;}}else{if(_$Gj<5){_$wj= !_$V8;}else if(_$Gj<6){return;}else if(_$Gj<7){_$7V(0);}else{_$cy=[4,16,64,256,1024,4096,16384,65536];}}}function _$7V(_$oe,_$oT){function _$iP(){var _$G6=_$4Y.charCodeAt(_$gf++ ),_$o8;if(_$G6<128){return _$G6;}else if(_$G6<251){return _$G6-32;}else if(_$G6===251){return 0;}else if(_$G6===254){_$G6=_$4Y.charCodeAt(_$gf++ );if(_$G6>=128)_$G6-=32;_$o8=_$4Y.charCodeAt(_$gf++ );if(_$o8>=128)_$o8-=32;return _$G6*219+_$o8;}else if(_$G6===255){_$G6=_$4Y.charCodeAt(_$gf++ );if(_$G6>=128)_$G6-=32;_$o8=_$4Y.charCodeAt(_$gf++ );if(_$o8>=128)_$o8-=32;_$G6=_$G6*219*219+_$o8*219;_$o8=_$4Y.charCodeAt(_$gf++ );if(_$o8>=128)_$o8-=32;return _$G6+_$o8;}else if(_$G6===252){_$o8=_$4Y.charCodeAt(_$gf++ );if(_$o8>=128)_$o8-=32;return -_$o8;}else if(_$G6===253){_$G6=_$4Y.charCodeAt(_$gf++ );if(_$G6>=128)_$G6-=32;_$o8=_$4Y.charCodeAt(_$gf++ );if(_$o8>=128)_$o8-=32;return _$G6* -219-_$o8;}else{}}var _$gf,_$4Y,_$E8,_$Pa,_$G6,_$o8,_$ll,_$Pb,_$wj,_$0M,_$Gj,_$Ix,_$A3,_$$Z,_$QL,_$3J,_$Mx,_$v9,_$_5,_$mk;var _$yi,_$_W,_$5u=_$oe,_$n2=_$lQ[1];while(1){_$_W=_$n2[_$5u++];if(_$_W<64){if(_$_W<16){if(_$_W<4){if(_$_W<1){_$oT._$Kz=_$LM;}else if(_$_W<2){_$V8._$t3=1;}else if(_$_W<3){_$oT._$Pb="_$VX";}else{return 1;}}else if(_$_W<8){if(_$_W<5){_$7V(90,_$V8);}else if(_$_W<6){_$A3.push(")();");}else if(_$_W<7){_$oT._$Ix="_$Ts";}else{_$oT._$GC="_$NL";}}else if(_$_W<12){if(_$_W<9){_$G6+="kOpNzFkqxIUEPNF9EHp5ecX1gaKWW5VafnP6J38BNovigc9FKDrotVEcL6yL6cHAklRgLVfvGC1p4AIQiBHUSyudc5e3XmTsTiVX5U";}else if(_$_W<10){var _$_5=_$iP();}else if(_$_W<11){var _$G6='';}else{_$oT._$fv="_$n2";}}else{if(_$_W<13){_$G6+="cVHJwaf9bTdwhoNF2q1hSJTgciE7KFz$0CM9IjBHx07wwMP2HzqbWGQrmyPzzzDjxQLkTvJUojc0xEZlgu14PiXXIYiH7Ba4M$rcaL";}else if(_$_W<14){var _$3J=_$A3.join('');}else if(_$_W<15){_$oT._$hl="_$D1";}else{_$oT._$0M="tRUcvtq14dQuHbHjyu9H7a";}}}else if(_$_W<32){if(_$_W<20){if(_$_W<17){_$oT._$5u="_$zr";}else if(_$_W<18){_$oT._$1p="_$fS";}else if(_$_W<19){var _$Pa=_$V8.aebi=[];}else{if( !_$yi)_$5u+=1;}}else if(_$_W<24){if(_$_W<21){var _$Mx=_$7V(10);}else if(_$_W<22){for(_$QL=0;_$QL<_$mk;_$QL++ ){_$1B(16,_$QL,_$A3);}}else if(_$_W<23){var _$G6,_$o8,_$ll=_$oT.length,_$Pb=new _$Kz(_$ll/2),_$wj='_$';}else{_$yi=_$oT===undefined||_$oT==="";}}else if(_$_W<28){if(_$_W<25){_$oT._$Gj="_$95";}else if(_$_W<26){_$V8._$G6=new Date().getTime();}else if(_$_W<27){var _$G6=_$7V(10);}else{_$oT._$V8="Wt._XTzz3cA";}}else{if(_$_W<29){}else if(_$_W<30){_$oT._$BP="lARAYy0bkkA";}else if(_$_W<31){_$G6+="9hOHJmbaCxK8iRoE957ynIkKXO$tEzVlq7TbcZQukimbzi$jhcLcsuRoqt531qbc8uXznMwKMAvW41BjuYIIiQlKbdpxoqU8cvOYgD";}else{_$o8=_$7V(10);}}}else if(_$_W<48){if(_$_W<36){if(_$_W<33){var _$E8=_$V8._$Tb;}else if(_$_W<34){_$oT._$iB="_$I6";}else if(_$_W<35){_$oT._$FD=44;}else{_$v9=_$4Y.substr(_$gf,_$Ix).split(String.fromCharCode(255));}}else if(_$_W<40){if(_$_W<37){_$oT._$A3="_$ud";}else if(_$_W<38){return 0;}else if(_$_W<39){var _$G6=_$FD.eval.toString();}else{return ret;}}else if(_$_W<44){if(_$_W<41){var _$0M=_$iP();}else if(_$_W<42){for(_$G6=0,_$o8=0;_$o8<_$ll;_$o8+=2){_$Pb[_$G6++ ]=_$wj+_$oT.substr(_$o8,2);}}else if(_$_W<43){_$oT._$CL="_$Fl";}else{var _$Pb=_$4Y.length;}}else{if(_$_W<45){_$5u+=47;}else if(_$_W<46){return new Date().getTime();}else if(_$_W<47){var _$Ix=_$iP();}else{_$5u+=1;}}}else{if(_$_W<52){if(_$_W<49){_$5u+=2;}else if(_$_W<50){_$V8._$Tb=_$7V(16);}else if(_$_W<51){_$G6+="03Q_t3CLZwhlBYWfh$6KfRj5pqOycu19IuFGnkQpRuLut_xw4K7ScIiwKrdLnmsE$q$5i1lhhFw9grxL9PzsCmUG0aBpFKemDONUhB";}else{_$oT._$St=1;}}else if(_$_W<56){if(_$_W<53){var _$o8=_$7V(10);}else if(_$_W<54){_$V8._$G6-=_$7V(10);}else if(_$_W<55){_$yi=_$Mx-_$G6>12000;}else{_$oT._$Vl="";}}else if(_$_W<60){if(_$_W<57){var _$A3=[];}else if(_$_W<58){var _$4Y=_$V8["3e2af61"];}else if(_$_W<59){_$7V(79,_$3J);}else{var _$gf=0;}}else{if(_$_W<61){_$oT._$BY="_$1g";}else if(_$_W<62){_$oT._$LV="_$_W";}else if(_$_W<63){ret=_$G6.call(_$FD,_$oT);}else{_$G6+="cy9rFDKzV8LMoTgRiP4YE8Pagf_5$Zv9m6jw0mqaknv8_zfihNgN49_jyQ99mF5ruhStBPCnDRqXlQkj7V1Bgx6iG6o8llPbwj0MGj";}}}}else{if(_$_W<80){if(_$_W<68){if(_$_W<65){_$G6+="1is1ii05R8sb7k7JHEGketlFpsBC_RcxW82bZE844v7deYDhsnnGEp7$NvpmQvPj2S0tAiLOGL6C$zuvBQ2D1jAU0x7ujgeWGmVytn";}else if(_$_W<66){_$mk=_$iP();}else if(_$_W<67){ret=_$FD.execScript(_$oT);}else{var _$wj=_$iP();}}else if(_$_W<72){if(_$_W<69){_$oT._$Zw="_$21";}else if(_$_W<70){var _$$Z=_$iP();}else if(_$_W<71){if( !_$yi)_$5u+=2;}else{var _$Gj=_$iP();}}else if(_$_W<76){if(_$_W<73){_$yi=_$mk>0;}else if(_$_W<74){var _$ll=_$7V(72);}else if(_$_W<75){return;}else{_$G6=_$FD.eval;}}else{if(_$_W<77){_$5u+=-47;}else if(_$_W<78){_$G6+="IxA3mkQL3JMxoe5uyiBt_Wn2I6NLfSOXirzrcU$olV9TldfKhLESALLR935WyzPCsSd0y8iYk5LnuOTNXlTMCpWbhys4clFeujFCiS";}else if(_$_W<79){_$gf+=_$Ix;}else{return _$Pb;}}}else if(_$_W<96){if(_$_W<84){if(_$_W<81){_$oT._$IQ="_$ir";}else if(_$_W<82){var _$mk=_$iP();}else if(_$_W<83){_$V8["3e2af61"]=_$9r;}else{_$G6+="7DN5XhFRDZg69ZxJ9sY5yHMQtcaDV6lNn8dXuSh1yNsNxymAT7kVJQw0uP3sE6I$Di5aKN2T6bUFHdo9TOZej3fgQkkdi4K9nOlCiO";}}else if(_$_W<88){if(_$_W<85){_$7V(29);}else if(_$_W<86){_$G6+="uii$BMIdwvO3PyA25FEQunjnlx2I_6O9B2q$ZxqDm$wIq51LtJfwfyAdJbkgb8OiI_CBN6cG6twOh01v8DjuSMso_xrf3B_KrxTAVJ";}else if(_$_W<87){_$yi=_$G6!=="functioneval(){[nativecode]}";}else{_$oT._$uh=40;}}else if(_$_W<92){if(_$_W<89){_$oT._$4A="_$OX";}else if(_$_W<90){_$oT._$oe="_$wj";}else if(_$_W<91){_$G6+="jfk2GF3oXp2FjO3AqdBe9OhMGVL3AW4R0qm_BfRDMFcaXJxS4Xq6otBS3SA9A7K$jAgJD_DehVSSCUkDe8QPeaKwkwh4BD$aKT01wHd5";}else{_$G6=_$G6.replace(/[\r\n\s]/g,"");}}else{if(_$_W<93){_$yi=_$V8["3e2af61"];}else if(_$_W<94){_$1B(0);}else if(_$_W<95){for(_$QL=0;_$QL<_$mk;_$QL++ ){_$A3.push("}");}}else{_$oT._$oT="oA9YEb1JuNsCWfVoLGU7QA";}}}else{if(_$_W<97){_$oT._$HU="_$cU";}else if(_$_W<98){return _$7V(12,_$G6);}else{_$yi=_$FD.execScript;}}}}function _$1B(_$Pb,_$m6,_$jw){function _$0m(){var _$Gj=[0];Array.prototype.push.apply(_$Gj,arguments);return _$gx.apply(this,_$Gj);}var _$G6,_$o8,_$ll,_$qa,_$kn,_$v8,_$_z,_$fi,_$hN,_$gN,_$49,_$_j,_$yQ,_$99,_$mF,_$5r;var _$0M,_$Ix,_$wj=_$Pb,_$A3=_$lQ[2];while(1){_$Ix=_$A3[_$wj++];if(_$Ix<16){if(_$Ix<4){if(_$Ix<1){}else if(_$Ix<2){var _$_z=_$iP();}else if(_$Ix<3){var _$99=_$1B(11);}else{var _$o8=_$G6>1?document.scripts[_$G6-2].src:_$9r;}}else if(_$Ix<8){if(_$Ix<5){var _$kn=_$iP();}else if(_$Ix<6){var _$G6=document.scripts.length;}else if(_$Ix<7){var _$qa=_$iP();}else{return _$o8;}}else if(_$Ix<12){if(_$Ix<9){var _$mF=_$1B(11);}else if(_$Ix<10){var _$G6=_$iP();}else if(_$Ix<11){_$qa.send();}else{var _$5r=[];}}else{if(_$Ix<13){_$wj+=19;}else if(_$Ix<14){_$wj+=-19;}else if(_$Ix<15){var _$o8=new Array(_$G6);}else{var _$49=_$iP();}}}else if(_$Ix<32){if(_$Ix<20){if(_$Ix<17){_$Pa[_$m6]=_$G6;}else if(_$Ix<18){_$qa=_$FD.ActiveXObject?new _$FD.ActiveXObject('Microsoft.XMLHTTP'):new _$FD.XMLHttpRequest();}else if(_$Ix<19){_$gx(7,_$jw);}else{if( !_$0M)_$wj+=4;}}else if(_$Ix<24){if(_$Ix<21){for(_$ll=0;_$ll<_$G6;_$ll++ ){_$o8[_$ll]=_$iP();}}else if(_$Ix<22){var _$G6=_$1B(11);}else if(_$Ix<23){var _$o8=_$iP();}else{_$0M=_$o8;}}else if(_$Ix<28){if(_$Ix<25){var _$gN=_$iP();}else if(_$Ix<26){var _$fi=_$iP();}else if(_$Ix<27){var _$v8=_$iP();}else{for(_$ll=0;_$ll<_$o8;_$ll++ ){_$5r[_$ll]=_$1B(11);}}}else{if(_$Ix<29){_$qa.onreadystatechange=_$0m;}else if(_$Ix<30){var _$yQ=_$1B(11);}else if(_$Ix<31){var _$_j=_$1B(11);}else{return;}}}else{if(_$Ix<33){_$qa.open('GET',_$o8,false);}else{var _$hN=_$iP();}}}function _$gx(_$o8,_$uh){var _$St,_$G6;var _$Pb,_$0M,_$ll=_$o8,_$Gj=_$lQ[3];while(1){_$0M=_$Gj[_$ll++];if(_$0M<16){if(_$0M<4){if(_$0M<1){_$uh.push("while(1){");}else if(_$0M<2){_$uh.push("];");}else if(_$0M<3){_$uh.push(_$m6);}else{_$ll+=13;}}else if(_$0M<8){if(_$0M<5){for(_$G6=0;_$G6<_$_j.length;_$G6++ ){_$uh.push(",");_$uh.push(_$E8[_$_j[_$G6]]);}}else if(_$0M<6){if( !_$Pb)_$ll+=1;}else if(_$0M<7){for(_$G6=0;_$G6<_$99.length;_$G6+=2){_$6i(0,_$99[_$G6],_$99[_$G6+1],_$uh);}}else{_$uh.push(",");}}else if(_$0M<12){if(_$0M<9){_$uh.push("var ");}else if(_$0M<10){_$Pb=_$yQ.length;}else if(_$0M<11){return;}else{_$uh.push("){");}}else{if(_$0M<13){_$Pb=_$_j.length;}else if(_$0M<14){var _$G6,_$St=4;}else if(_$0M<15){_$uh.push("++];");}else{_$6i(40);}}}else if(_$0M<32){if(_$0M<20){if(_$0M<17){_$uh.push("=0,");}else if(_$0M<18){_$uh.push("=");}else if(_$0M<19){_$uh.push(";");}else{_$uh.push("[");}}else if(_$0M<24){if(_$0M<21){_$uh.push("=$_ts.aebi;");}else if(_$0M<22){_$Pb=_$m6==0;}else if(_$0M<23){_$uh.push("function ");}else{_$Pb=_$qa.readyState==4;}}else if(_$0M<28){if(_$0M<25){_$uh.push("(function(){var ");}else if(_$0M<26){_$uh.push(_$E8[_$gN]);}else if(_$0M<27){if( !_$Pb)_$ll+=8;}else{_$uh.push(_$E8[_$_5]);}}else{if(_$0M<29){_$7V(29);}else if(_$0M<30){_$uh.push(_$E8[_$yQ[0]]);}else if(_$0M<31){_$uh.push(_$E8[_$v8]);}else{_$7V(79,_$qa.responseText);}}}else{if(_$0M<36){if(_$0M<33){_$uh.push(_$E8[_$qa]);}else if(_$0M<34){_$6i(13,0,_$5r.length);}else if(_$0M<35){_$uh.push("(");}else{_$ll+=-13;}}else if(_$0M<40){if(_$0M<37){_$uh.push(_$E8[_$kn]);}else if(_$0M<38){for(_$G6=1;_$G6<_$yQ.length;_$G6++ ){_$uh.push(",");_$uh.push(_$E8[_$yQ[_$G6]]);}}else if(_$0M<39){_$ll+=8;}else{_$uh.push("=$_ts.scj,");}}else if(_$0M<44){if(_$0M<41){if( !_$Pb)_$ll+=9;}else if(_$0M<42){_$uh.push("}");}else if(_$0M<43){_$Pb=_$V8["3e2af61"];}else{_$uh.push(_$E8[_$$Z]);}}else{if(_$0M<45){_$Pb=_$5r.length;}else if(_$0M<46){if( !_$Pb)_$ll+=4;}else if(_$0M<47){_$uh.push(_$E8[_$49]);}else{_$uh.push(_$E8[_$fi]);}}}}function _$6i(_$wj,_$BP,_$Cn,_$DR){var _$G6,_$o8,_$ll,_$Pb;var _$Gj,_$A3,_$0M=_$wj,_$mk=_$lQ[4];while(1){_$A3=_$mk[_$0M++];if(_$A3<16){if(_$A3<4){if(_$A3<1){_$uh.push("}");}else if(_$A3<2){if( !_$Gj)_$0M+=7;}else if(_$A3<3){var _$G6=_$5r[_$BP];}else{_$0M+=2;}}else if(_$A3<8){if(_$A3<5){for(k=0;k<_$o8;k+=2){_$uh.push(_$v9[_$G6[k]]);_$uh.push(_$E8[_$G6[k+1]]);}}else if(_$A3<6){_$6i(2,_$BP);}else if(_$A3<7){for(_$o8=0;_$o8<_$G6;_$o8+=2){_$uh.push(_$v9[_$mF[_$o8]]);_$uh.push(_$E8[_$mF[_$o8+1]]);}}else{_$Gj=_$G6.length!=_$o8;}}else if(_$A3<12){if(_$A3<9){for(;_$BP+_$ll<_$Cn;_$BP+=_$ll){_$uh.push(_$o8);_$uh.push(_$E8[_$gN]);_$uh.push('<');_$uh.push(_$BP+_$ll);_$uh.push("){");_$6i(13,_$BP,_$BP+_$ll);_$o8="}else if(";}}else if(_$A3<10){_$Gj=_$Pb<=_$St;}else if(_$A3<11){_$Gj=_$Pb==0;}else{_$ll=0;}}else{if(_$A3<13){}else if(_$A3<14){_$0M+=-5;}else if(_$A3<15){_$uh.push(_$v9[_$mF[_$G6]]);}else{var _$G6,_$o8,_$ll,_$Pb=_$Cn-_$BP;}}}else if(_$A3<32){if(_$A3<20){if(_$A3<17){_$uh.push(_$v9[_$G6[_$o8]]);}else if(_$A3<18){for(_$G6=1;_$G6<7;_$G6++ ){if(_$Pb<=_$cy[_$G6]){_$ll=_$cy[_$G6-1];break;}}}else if(_$A3<19){_$Gj=_$Pb==1;}else{_$uh.push("}else{");}}else if(_$A3<24){if(_$A3<21){_$0M+=8;}else if(_$A3<22){if( !_$Gj)_$0M+=1;}else if(_$A3<23){var _$o8=_$G6.length;}else{_$Gj=_$mF.length!=_$G6;}}else if(_$A3<28){if(_$A3<25){return;}else if(_$A3<26){var _$G6=_$mF.length;}else if(_$A3<27){_$0M+=3;}else{for(;_$BP<_$Cn;_$BP++ ){_$uh.push(_$o8);_$uh.push(_$E8[_$gN]);_$uh.push('<');_$uh.push(_$BP+1);_$uh.push("){");_$6i(2,_$BP);_$o8="}else if(";}}}else{if(_$A3<29){if( !_$Gj)_$0M+=2;}else if(_$A3<30){_$Cn-- ;}else if(_$A3<31){_$DR.push(["function ",_$E8[_$BP],"(){var ",_$E8[_$_z],"=[",_$Cn,"];Array.prototype.push.apply(",_$E8[_$_z],",arguments);return ",_$E8[_$hN],".apply(this,",_$E8[_$_z],");}"].join(''));}else{_$0M+=17;}}}else{if(_$A3<36){if(_$A3<33){_$o8="if(";}else if(_$A3<34){_$0M+=21;}else if(_$A3<35){_$6i(13,_$BP,_$Cn);}else{_$o8-=_$o8%2;}}else{_$G6-=_$G6%2;}}}}}}}})()</script><script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/jquery_1_12_4.js"></script>
    <script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/common.js"></script>
    <!-- 二维码 -->
    <script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/jquery_qrcode_min.js"></script>
    <!-- 打印 -->
    <script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/Print.js"></script>
<style>
body .wrap a {
    color: #252525;
}
.header .nav li a {
    color: #fff;
}
.wrap a:link {
    text-decoration: none;
}
.footer .copyright p a{
    color: #fff;
}
.footer .copyright p {
    font-size: 14px;
}


</style>
</head>

<body>
    <!-- dom -->
    <div class="wrap">
        <!-- header 开始 -->
        <div class="header">
            <div class="ht">
                <div class="inner clearfix">
                    <p class="fl">
                       <script type="text/javaScript">
                            var sysdate = new Date(); 
                            var year = sysdate.getFullYear(); 
                             var month = sysdate.getMonth(); 
                              var date = sysdate.getDate(); 
                            var day = sysdate.getDay(); 
                              var week = ['日', '一', '二', '三', '四', '五', '六']; 
                             document.write("今天是: "+year + "年" + (month + 1) + "月" + date + "日 星期" + week[day]);
                        </script>
                    </p>
                    <p class="fr"><a href="http://www.gov.cn/" target="_blank">中国政府网</a>|<a href="http://www.hubei.gov.cn/" target="_blank">湖北政府网</a>|<a id="StranLink"  href="#" name="StranLink">繁体</a>|<!--<a href="https://mail.163.com/" target="_blank">邮箱登录</a><span class="hidden-xs">|</span>--><a href="http://wza.hubei.gov.cn/.m/jycg_wza/index.html
">无障碍阅读</a><span class="hidden-xs">|</span><a href="#" class="hidden-xs"><img src="http://jycg.hubei.gov.cn/material/images/sjb.png" />手机版<img src="http://jycg.hubei.gov.cn/material/images/a1.jpg" alt="" class="sj-ewm" /></a><span class="hidden-xs">|</span><a href="#" class="hidden-xs"><img src="http://jycg.hubei.gov.cn/material/images/ggzyjy-wxdl.png" />微信<img src="http://jycg.hubei.gov.cn/material/images/wx_ewm.jpg" alt="" class="sj-ewm" /></a><span class="hidden-xs">|</span><a id="login" style="cursor: pointer;" class="hidden-xs">登录</a><span class="hidden-xs">|</span><a id="zhuce" href="https://oauth.hubei.gov.cn:8443/hbyzw/zwfw/personInfo/personInfoReg.jsp?appCode=hbzfjyhpt" style="cursor: pointer;" class="hidden-xs">注册</a>
                    </p>
                </div>
            </div>
            <div class="inner clearfix">
                <h1><a href="http://jycg.hubei.gov.cn/" target="_blank" class="nt">湖北省人民政府</a></h1>
                <div class="search" id="search">
                    <div class="search-btn"></div>
                    <div class="search-box">
                        <input type="text" maxlength="20" value="" onclick="if(this.value=='请输入关键字'){this.value='';}" placeholder="请输入关键字" id="textfield" />
                        <button  onclick="chkSearch();"><span class="iconfont icon-jyh-search"></span>搜 索</button>
                        <!-- <a href="javascript:" class="go"><span class="iconfont icon-jyh-ai robot fl"></span><div class="hidden-xs fl"><span>智能助手</span></div></a> </div> -->
                    </div>
                </div>

            </div>
            <div class="nav">
                <ul>
                    <li><a href="http://jycg.hubei.gov.cn/"><i class="s1"></i><b>首页</b></a></li>
                    <li><a href="http://jycg.hubei.gov.cn/fbjd/"><i class="s2"></i><b>发布解读</b></a></li>
                    <li><a href="http://jycg.hubei.gov.cn/hdjl/"><i class="s3"></i><b>互动交流</b></a></li>
                    <li><a href="http://zwfw.hubei.gov.cn/s/index.html" target="_blank"><i class="s4"></i><b>办事服务</b></a></li>
                    <li><a href="http://jycg.hubei.gov.cn/jyxx/"><i class="s6"></i><b>交易信息</b></a></li>
                    <li><a href="http://jycg.hubei.gov.cn/bmdt/"><i class="s5"></i><b>部门动态</b></a></li>
                </ul>
            </div>
        </div>
<script>
function chkSearch(){
	if($('#textfield').val() == '' || $('#textfield').val().length == 0){
		layer.alert('请输入关键字');
		return false;
	}
var keywords = encodeURI($('#textfield').val());
$url = '/site/jycg/search.html?searchWord='+keywords +'&siteId=84&pageSize=10';
	window.open($url,'_blank'); 
}	
    $('#textfield').on('keypress',function (event) {
        if (event.keyCode === 13){
            chkSearch();
        }
    });
</script>
        <!-- header 结束 -->
        <!-- content 开始 -->
        <div class="content mt20 fdzdgk-xl">
            <!-- part1 开始 -->
            <div class="grid p1">
                <div class="where mb20">
                    <a href="../../" title="首页" class="CurrChnlCls">首页</a>><a href="../" title="交易信息" class="CurrChnlCls">交易信息</a>><a href="./" title="政府采购" class="CurrChnlCls">政府采购</a>
                </div>
                <div class="row">
                    <div class="main">
                        <div class="article">
                            <div class="article-box"></div>
                            <div class="apendix"></div>
                            <div class="article-code tc">
                                <a href="javascript:" class="mt20" onclick="print();"><img src="http://jycg.hubei.gov.cn/material/images/fdxl1.jpg" />打印 </a>
                                <a href="javascript:" onclick="window.close();"><img src="http://jycg.hubei.gov.cn/material/images/fdxl2.jpg" />关闭</a>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <!-- part1 结束 -->
        </div>
        <!-- content 结束 -->

        <!-- footer 开始 -->
        <div class="footer">
            <div class="links">
                <ul class="row">
                    <li class="col-md-4"><a href="javascript:">省直部门</a>
                        <ul>
                             
<li><a href="http://fgw.hubei.gov.cn" target="_blank" title="湖北省发展和改革委员会">湖北省发展和改革委员会</a></li>
                            
<li><a href="http://jyt.hubei.gov.cn" target="_blank" title="湖北省教育厅">湖北省教育厅</a></li>
                            
<li><a href="http://kjt.hubei.gov.cn/" target="_blank" title="湖北省科学技术厅">湖北省科学技术厅</a></li>
                            
<li><a href="http://jxt.hubei.gov.cn/" target="_blank" title="湖北省经济和信息化厅">湖北省经济和信息化厅</a></li>
                            
<li><a href="http://mzw.hubei.gov.cn/" target="_blank" title="湖北省民族宗教事务委员会">湖北省民族宗教事务委员会</a></li>
                            
<li><a href="http://gat.hubei.gov.cn" target="_blank" title="湖北省公安厅">湖北省公安厅</a></li>
                            
<li><a href="http://mzt.hubei.gov.cn/" target="_blank" title="湖北省民政厅">湖北省民政厅</a></li>
                            
<li><a href="http://sft.hubei.gov.cn/" target="_blank" title="湖北省司法厅">湖北省司法厅</a></li>
                            
<li><a href="http://czt.hubei.gov.cn/" target="_blank" title="湖北省财政厅">湖北省财政厅</a></li>
                            
<li><a href="http://rst.hubei.gov.cn" target="_blank" title="湖北省人力资源和社会保障厅">湖北省人力资源和社会保障厅</a></li>
                            
<li><a href="http://zrzyt.hubei.gov.cn/" target="_blank" title="湖北省自然资源厅">湖北省自然资源厅</a></li>
                            
<li><a href="http://sthjt.hubei.gov.cn/xwzx/" target="_blank" title="湖北省生态环境厅">湖北省生态环境厅</a></li>
                            
<li><a href="http://zscqj.hubei.gov.cn/" target="_blank" title="湖北省知识产权局">湖北省知识产权局</a></li>
                            
<li><a href="http://fda.hubei.gov.cn/" target="_blank" title="湖北省药品监督管理局">湖北省药品监督管理局</a></li>
                            
<li><a href="http://lyj.hubei.gov.cn/" target="_blank" title="湖北省林业局">湖北省林业局</a></li>
                            
<li><a href="http://jyj.hubei.gov.cn/" target="_blank" title="湖北省监狱管理局">湖北省监狱管理局</a></li>
                            
<li><a href="http://lsj.hubei.gov.cn/" target="_blank" title="湖北省粮食局">湖北省粮食局</a></li>
                            
<li><a href="http://ztb.hubei.gov.cn/" target="_blank" title="湖北省公共资源交易监督管理局">湖北省公共资源交易监督管理局</a></li>
                            
<li><a href="http://jgswj.hubei.gov.cn/" target="_blank" title="湖北省机关事务管理局">湖北省机关事务管理局</a></li>
                            
<li><a href="http://dfjrjgj.hubei.gov.cn/" target="_blank" title="湖北省地方金融监督管理局">湖北省地方金融监督管理局</a></li>
                            
<li><a href="http://fpb.hubei.gov.cn/" target="_blank" title="湖北省扶贫开发办公室">湖北省扶贫开发办公室</a></li>
                            
<li><a href="http://zys.hubei.gov.cn/" target="_blank" title="湖北省政府研究室">湖北省政府研究室</a></li>
                            
<li><a href="http://rfb.hubei.gov.cn/" target="_blank" title="湖北省人民防空办公室">湖北省人民防空办公室</a></li>
                            
<li><a href="http://ybj.hubei.gov.cn/" target="_blank" title="湖北省医疗保障局">湖北省医疗保障局</a></li>
                            
<li><a href="http://tjj.hubei.gov.cn/" target="_blank" title="湖北省统计局">湖北省统计局</a></li>
                            
<li><a href="http://tyj.hubei.gov.cn/" target="_blank" title="湖北省体育局">湖北省体育局</a></li>
                            
<li><a href="http://gdj.hubei.gov.cn/" target="_blank" title="湖北省广播电视局">湖北省广播电视局</a></li>
                            
<li><a href="http://scjg.hubei.gov.cn/" target="_blank" title="湖北省市场监督管理局">湖北省市场监督管理局</a></li>
                            
<li><a href="http://gzw.hubei.gov.cn/" target="_blank" title="湖北省国有资产监督管理委员会">湖北省国有资产监督管理委员会</a></li>
                            
<li><a href="http://sjt.hubei.gov.cn/" target="_blank" title="湖北省审计厅">湖北省审计厅</a></li>
                            
<li><a href="http://yjt.hubei.gov.cn/" target="_blank" title="湖北省应急管理厅">湖北省应急管理厅</a></li>
                            
<li><a href="http://va.hubei.gov.cn/" target="_blank" title="湖北省退役军人事务厅">湖北省退役军人事务厅</a></li>
                            
<li><a href="http://wjw.hubei.gov.cn/" target="_blank" title="湖北省卫生健康委员会">湖北省卫生健康委员会</a></li>
                            
<li><a href="http://dzj.hubei.gov.cn" target="_blank" title="湖北省地质局">湖北省地质局</a></li>
                            
<li><a href="http://jycg.hubei.gov.cn/" target="_blank" title="湖北省公共资源交易中心（湖北省政府采购中心）">湖北省公共资源交易中心（湖北省政府采购中心）</a></li>
                            
<li><a href="http://hb.cma.gov.cn/" target="_blank" title="湖北省气象局">湖北省气象局</a></li>
                            
<li><a href="http://gxs.hubei.gov.cn" target="_blank" title="湖北省供销社">湖北省供销社</a></li>
                            
<li><a href="http://wlt.hubei.gov.cn/" target="_blank" title="湖北省文化和旅游厅">湖北省文化和旅游厅</a></li>
                            
<li><a href="http://swt.hubei.gov.cn/" target="_blank" title="湖北省商务厅">湖北省商务厅</a></li>
                            
<li><a href="http://nyt.hubei.gov.cn/" target="_blank" title="湖北省农业农村厅">湖北省农业农村厅</a></li>
                            
<li><a href="http://slt.hubei.gov.cn/" target="_blank" title="湖北省水利厅">湖北省水利厅</a></li>
                            
<li><a href="http://jtt.hubei.gov.cn/" target="_blank" title="湖北省交通运输厅">湖北省交通运输厅</a></li>
                            
<li><a href="http://zjt.hubei.gov.cn/" target="_blank" title="湖北省住房和城乡建设厅">湖北省住房和城乡建设厅</a></li>
                            

                        </ul>
                    </li>
                    <li class="col-md-4"><a href="javascript:">各省交易采购中心</a>
                        <ul>
                             
<li><a href="http://www.zycg.gov.cn/" target="_blank" title="中央国家机关政府采购中心">中央国家机关政府采购中心</a></li>
                            
<li><a href="http://zzcg.ccgp.gov.cn/" target="_blank" title="中共中央直属机关采购中心">中共中央直属机关采购中心</a></li>
                            
<li><a href="http://www.bcactc.com/default.aspx" target="_blank" title="北京市建设工程发包承包交易中心">北京市建设工程发包承包交易中心</a></li>
                            
<li><a href="http://bgpc.beijing.gov.cn/" target="_blank" title="北京市政府采购中心">北京市政府采购中心</a></li>
                            
<li><a href="http://www.shcpe.cn/jyfw/index.html" target="_blank" title="上海市建设工程交易服务中心">上海市建设工程交易服务中心</a></li>
                            
<li><a href="http://www.shanghai.gov.cn/nw2/nw2314/nw2319/nw32905/nw32914/nw32994/nw33029/nw40238/index.html" target="_blank" title="上海市政府采购中心">上海市政府采购中心</a></li>
                            
<li><a href="http://ggzy.gd.gov.cn/" target="_blank" title="广东省公共资源交易中心">广东省公共资源交易中心</a></li>
                            
<li><a href="http://ggzy.gz.gov.cn/html/index.html" target="_blank" title="广州公共资源交易中心">广州公共资源交易中心</a></li>
                            
<li><a href="http://gpcgd.gd.gov.cn/" target="_blank" title="广东省政府采购中心">广东省政府采购中心</a></li>
                            
<li><a href="http://prec.sxzwfw.gov.cn/cmsController.do?goPage&page=index" target="_blank" title="山西省公共资源交易中心（山西省省级政府采购中心）">山西省公共资源交易中心（山西省省级政府采购中心）</a></li>
                            
<li><a href="http://www.ggzyzx.jl.gov.cn/" target="_blank" title="吉林省公共资源交易中心（吉林省政府采购中心）">吉林省公共资源交易中心（吉林省政府采购中心）</a></li>
                            
<li><a href="http://www.spprec.com/sczwweb/" target="_blank" title="四川省政府政务服务和公共资源交易服务中心">四川省政府政务服务和公共资源交易服务中心</a></li>
                            
<li><a href="http://www.hljggzyjyw.gov.cn/" target="_blank" title="黑龙江省公共资源交易中心">黑龙江省公共资源交易中心</a></li>
                            
<li><a href="http://www.hnggzy.com/hnsggzy/" target="_blank" title="河南省公共资源交易中心">河南省公共资源交易中心</a></li>
                            
<li><a href="http://ggzyjyzx.shandong.gov.cn/" target="_blank" title="山东省公共资源交易中心（山东省政府采购中心）">山东省公共资源交易中心（山东省政府采购中心）</a></li>
                            
<li><a href="https://ggzy.hunan.gov.cn/" target="_blank" title="湖南省公共资源交易中心">湖南省公共资源交易中心</a></li>
                            
<li><a href="http://60.28.163.169/" target="_blank" title="天津市公共资源交易中心（天津市政府采购中心）">天津市公共资源交易中心（天津市政府采购中心）</a></li>
                            
<li><a href="http://tjgpc.cz.tj.gov.cn/" target="_blank" title="天津市政府采购中心">天津市政府采购中心</a></li>
                            
<li><a href="http://new.zmctc.com/zjgcjy/" target="_blank" title="浙江省公共资源交易中心">浙江省公共资源交易中心</a></li>
                            
<li><a href="http://www.zjzfcg.gov.cn/" target="_blank" title="浙江省政府采购中心">浙江省政府采购中心</a></li>
                            
<li><a href="http://jsggzy.jszwfw.gov.cn/" target="_blank" title="江苏省公共资源交易中心">江苏省公共资源交易中心</a></li>
                            
<li><a href="http://www.bidchance.com/company-194538.html" target="_blank" title="江苏省省级行政机关政府采购中心">江苏省省级行政机关政府采购中心</a></li>
                            
<li><a href="http://ggzy.hefei.gov.cn/" target="_blank" title="安徽合肥公共资源交易中心">安徽合肥公共资源交易中心</a></li>
                            
<li><a href="http://ggzy.gz.gov.cn/html/index.html" target="_blank" title="河北省公共资源交易中心">河北省公共资源交易中心</a></li>
                            
<li><a href="http://www.ccgp-hebei.gov.cn/province/" target="_blank" title="河北省政府采购中心">河北省政府采购中心</a></li>
                            
<li><a href="http://zfcg.ggzyjy.nmg.gov.cn/" target="_blank" title="内蒙古政府采购中心">内蒙古政府采购中心</a></li>
                            
<li><a href="http://www.sxzfcg.cn/" target="_blank" title="山西省政府采购中心">山西省政府采购中心</a></li>
                            
<li><a href="http://www.ccgp-jilin.gov.cn/" target="_blank" title="吉林省政府采购中心">吉林省政府采购中心</a></li>
                            
<li><a href="http://www.fjggzyjy.cn/" target="_blank" title="福建省公共资源交易中心">福建省公共资源交易中心</a></li>
                            
<li><a href="http://gxggzy.gxzf.gov.cn/gxzbw/" target="_blank" title="广西壮族自治区公共资源交易中心">广西壮族自治区公共资源交易中心</a></li>
                            
<li><a href="http://gxzfcg.gxzf.gov.cn/" target="_blank" title="广西壮族自治区政府采购中心">广西壮族自治区政府采购中心</a></li>
                            
<li><a href="http://zw.hainan.gov.cn/ggzy/" target="_blank" title="海南省公共资源交易服务中心">海南省公共资源交易服务中心</a></li>
                            
                        </ul>
                    </li>
                    <li class="col-md-4"><a href="javascript:">各市州交易采购中心 </a>
                        <ul>
                             
<li><a href="http://www.jy.whzbtb.com/V2PRTS/" target="_blank" title="武汉市">武汉市</a></li>
                            
<li><a href="http://jyzx.xiangyang.gov.cn/" target="_blank" title="襄阳市">襄阳市</a></li>
                            
<li><a href="http://ggzyjyzx.yichang.gov.cn/" target="_blank" title="宜昌市">宜昌市</a></li>
                            
<li><a href="http://www.hsztbzx.com/" target="_blank" title="黄石市">黄石市</a></li>
                            
<li><a href="http://ggzyjy.shiyan.gov.cn/" target="_blank" title="十堰市">十堰市</a></li>
                            
<li><a href="http://www.jzggzy.com/" target="_blank" title="荆州市">荆州市</a></li>
                            
<li><a href="http://zyjy.jingmen.gov.cn/Front/" target="_blank" title="荆门市">荆门市</a></li>
                            
<li><a href="http://www.ezggzy.cn/" target="_blank" title="鄂州市">鄂州市</a></li>
                            
<li><a href="http://xg.xgsggzy.com/website/" target="_blank" title="孝感市">孝感市</a></li>
                            
<li><a href="http://ggzy.hg.gov.cn/ceinwz/indexhg.htm" target="_blank" title="黄冈市">黄冈市</a></li>
                            
<li><a href="http://xnztb.xianning.gov.cn/xnweb/jyxx/" target="_blank" title="咸宁市">咸宁市</a></li>
                            
<li><a href="http://www.hbbidcloud.cn/suizhou/" target="_blank" title="随州市">随州市</a></li>
                            
<li><a href="http://ggzy.enshi.gov.cn/TPFront/" target="_blank" title="恩施自治州">恩施自治州</a></li>
                            
<li><a href="http://www.xtggzy.com/" target="_blank" title="仙桃市">仙桃市</a></li>
                            
<li><a href="http://ztb.tianmen.gov.cn/" target="_blank" title="天门市">天门市</a></li>
                            
<li><a href="http://www.qjggzy.cn/qjztb/gy_index.do" target="_blank" title="潜江市">潜江市</a></li>
                            
<li><a href="http://ggzy.zhsnj.cn/" target="_blank" title="神龙架林区">神龙架林区</a></li>
                            
                        </ul>
                    </li>
                    <li class="col-md-4"><a href="javascript:">友情链接</a>
                        <ul>
                             
<li><a href="http://www.wuhan.gov.cn/" target="_blank" title="武汉市">武汉市</a></li>
                            
<li><a href="http://www.xiangyang.gov.cn/wzsy/" target="_blank" title="襄阳市">襄阳市</a></li>
                            
<li><a href="http://www.yichang.gov.cn/" target="_blank" title="宜昌市">宜昌市</a></li>
                            
<li><a href="http://www.huangshi.gov.cn/" target="_blank" title="黄石市">黄石市</a></li>
                            
<li><a href="http://www.shiyan.gov.cn/" target="_blank" title="十堰市">十堰市</a></li>
                            
<li><a href="http://www.jingzhou.gov.cn/" target="_blank" title="荆州市">荆州市</a></li>
                            
<li><a href="http://www.jingmen.gov.cn/" target="_blank" title="荆门市">荆门市</a></li>
                            
<li><a href="http://www.ezhou.gov.cn/" target="_blank" title="鄂州市">鄂州市</a></li>
                            
<li><a href="http://www.xiaogan.gov.cn/" target="_blank" title="孝感市">孝感市</a></li>
                            
<li><a href="http://www.hg.gov.cn/" target="_blank" title="黄冈市">黄冈市</a></li>
                            
<li><a href="http://www.xianning.gov.cn/" target="_blank" title="咸宁市">咸宁市</a></li>
                            
<li><a href="http://www.suizhou.gov.cn/" target="_blank" title="随州市">随州市</a></li>
                            
<li><a href="http://www.enshi.gov.cn/" target="_blank" title="恩施州">恩施州</a></li>
                            
<li><a href="http://www.xiantao.gov.cn" target="_blank" title="仙桃市">仙桃市</a></li>
                            
<li><a href="http://www.tianmen.gov.cn" target="_blank" title="天门市">天门市</a></li>
                            
<li><a href="http://www.hbqj.gov.cn" target="_blank" title="潜江市">潜江市</a></li>
                            
<li><a href="http://www.snj.gov.cn/" target="_blank" title="神农架林区">神农架林区</a></li>
                            
                        </ul>
                    </li>
                </ul>
            </div>
            <div class="copyright clearfix">
                <div class="footer-map p20 fl" style="padding: 8px;">
                    <p>版权所有：湖北省公共资源交易中心（湖北省政府采购中心）</p>
                    <p>招投标交易平台及CA：027-86629953</p>
                    <p>地 址：湖北省武汉市武昌区中北路252号（岳家嘴地铁站G出口）</p>
                </div>

                <div class="p20 fl" style="padding: 8px;">
                    <p><img src="http://jycg.hubei.gov.cn/material/images/footer_icp.png" alt="" />&ensp;鄂公网安备 42010602000665号</p>
                    <p>政府采购电子平台及网上商城 ：87835187/87835122</p>
                    <p>网站标识码：4200000101鄂ICP备05011090号-1 </p>
                </div>
                <div class=" p20 fl" style="padding: 8px;">
                    <p><a href="http://jycg.hubei.gov.cn/bsfw/lxdh/" target="_blank" style="margin: 0 0px;">联系电话：86629951（点击查看更多）</a></p>
                    <p>药械采购：86629920 拍卖交易：86629968</p>
                    <p>邮 编：430071 &ensp;&ensp; | &ensp;&ensp; <a href="http://jycg.hubei.gov.cn/fzlm/wzdt/" target="_blank">网站地图</a> </p>
                </div>

                <div class="gov" style="left: -15px;"><a href="http://bszs.conac.cn/sitename?method=show&id=54918B9009DD6A86E053012819AC70B5" target="_blank"><img src="http://jycg.hubei.gov.cn/material/images/gov_img.png" alt="" /></a></div>
                <div class="jc" style="top: 45%;right: -15px;"><a href="http://121.43.68.40/exposure/jiucuo.html?site_code=4200000069" target="_blank"><img src="http://jycg.hubei.gov.cn/material/images/jiucuo.png" alt="" /></a></div>
            </div>
        </div>

<!-- 外链弹框JS、CSS 开始-->
<link type="text/css" rel="stylesheet" href="http://jycg.hubei.gov.cn/material/css/wltz.css" />
<script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/bootstrap.min.js"></script>
<script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/wltz.js"></script>
<script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/ssoAjax.js"></script>
<!-- 外链弹框JS、CSS结束-->
<script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/ztzh.js"></script>

<div id="myModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"  style="height:185px;">
    <div class="modal-header">
        <button type="button" class="bootstrap-close" data-dismiss="modal" aria-hidden="true">×</button>
        <h3 id="myModalLabel">&nbsp;</h3>
    </div>
    <div class="modal-body">
        <p>您访问的链接即将离开“<span id="modalDomainName"></span>”门户网站 是否继续？</p>
        <input id="modalOuterURL" type="hidden" />
    </div>
    <div class="modal-footer">
        <button class="bootstrap-btn bootstrap-btn-default" data-dismiss="modal" aria-hidden="true">放弃</button>
        <button class="bootstrap-btn bootstrap-btn-danger" onClick="toRedirect()">继续访问</button>
    </div>
</div>

<!--百度统计--!>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?197b0a423d2d21ba532734d13a1f861f";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
<!--百度统计--!>
<!--访问统计--!>
<script id="_trs_ta_js" src="//ta.trs.cn/c/js/ta.js?mpid=4085" async="async" defer="defer"></script>
<!--访问统计--!>
<script>
//导航高亮
        var href = window.location.pathname;
        var chnls = ['/fbjd/', '/hdjl/', '/bsfw/', '/jyxx/', '/bmdt/'];
		
        var chnl_index= 0;
        for (var i = 0 ;i < chnls.length; i ++) {
            var index = href.search(chnls[i]);
            if(index == 0) {
                chnl_index = i + 1;
                break;
            }
        }
        var lis = jQuery(".nav ul li");
        lis.eq(chnl_index).addClass("current");
 </script>
        <!-- footer 结束 -->

    </div>
    <!-- dom 结束 -->
    <!-- js -->
    <script type="text/javascript" src="http://jycg.hubei.gov.cn/material/js/query-view.js"></script>
</body>

</html>
'''



clearHtmlTag = re.compile("\<.*?\>" )
newText = clearHtmlTag.sub('',text)
newText2 = clearHtmlTag.sub('',text2)

#print(newText)

reg = r'招标人:\s(.*)'

wordreg = re.compile(reg, re.MULTILINE)
wordreglist = re.findall(wordreg, newText)

reg2 = r'采 购 人：(.*)'
wordreg2 = re.compile(reg2)
wordreglist2 = re.findall(wordreg2, newText2)

print(wordreglist)
print(wordreglist2)

#for word in wordreglist:
#	print(word)