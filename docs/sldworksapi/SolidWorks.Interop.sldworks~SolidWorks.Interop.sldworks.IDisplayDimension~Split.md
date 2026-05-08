# Split Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Split`

Gets or sets whether to split a dual dimension above and below an unbroken dimension line (also called a leader).
Gets or sets whether to split a dual dimension above and below an unbroken dimension line (also called a leader).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Split As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.Split = value
 
value = instance.Split
```

```

System.bool Split {get; set;}
```

```

property System.bool Split {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to split a dual dimension above and below an unbroken dimension line, false to not

Example

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)  
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)  
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

Requirements

Setting this method to true only affects the following types of dual dimensions when the **Split when text position is "Solid Leader, Aligned Text"** option is selected in their **Tools > Options > Dimensions** dialog boxes:

- Arc Length
- Chamfer
- Diameter
- Linear
- Radius

To open the Help topic containing instructions on how to get and set the **Split when text position is "Solid Leader, Aligned Text"** option programmatically:

1. Click **Help** > **Use SOLIDWORKS Web Help**, if this menu item is checked.
2. Click **Help > API** **Help**.
3. Type **Document**.
4. Scroll down to the **properties** index subentry.
5. Scroll down to the **dimensions** index sub**-**subentry**.**
6. Double-click the type of dimension listed below **dimensions** whose dual dimension's **Split when text position is "Solid Leader, Aligned Text"** option you want to get or set.

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetUseDocDual Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocDual.md)  
[IDisplayDimension::SetDual Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetDual.md)
