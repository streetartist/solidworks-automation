# ReadOnly Property (IDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReadOnly`

Gets or sets the read-only state of a dimension.
Gets or sets the read-only state of a dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReadOnly As System.Boolean
```

```

Dim instance As IDimension
Dim value As System.Boolean
 
instance.ReadOnly = value
 
value = instance.ReadOnly
```

```

System.bool ReadOnly {get; set;}
```

```

property System.bool ReadOnly {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the dimension is read-only, false if it is writable

Example

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)  
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)  
[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)  
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)
