# DrivenState Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~DrivenState`

Gets or sets the driven state of a dimension.
Gets or sets the driven state of a dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DrivenState As System.Integer
```

```

Dim instance As IDimension
Dim value As System.Integer
 
instance.DrivenState = value
 
value = instance.DrivenState
```

```

System.int DrivenState {get; set;}
```

```

property System.int DrivenState {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Driven state of the dimension as defined in [swDimensionDrivenState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionDrivenState_e.html)

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
