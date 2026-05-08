# Name Property (IDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Name`

Gets or sets the name of a dimension.
Gets or sets the name of a dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Name As System.String
```

```

Dim instance As IDimension
Dim value As System.String
 
instance.Name = value
 
value = instance.Name
```

```

System.string Name {get; set;}
```

```

property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the dimension

Remarks

If setting the name of a dimension, do not include any of the special characters reserved by SOLIDWORKS.

Example

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)  
[Get Component Via Display Dimension (VBA)](Get_Component_Via_Display_Dimension_Example_VB.htm)  
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)  
[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::FullName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~FullName.md)
