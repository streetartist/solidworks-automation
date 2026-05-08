# UseDefaultBendRadius Property (IJogFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~UseDefaultBendRadius`

Gets or sets whether to use the default bend radius for this jog feature.
Gets or sets whether to use the default bend radius for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDefaultBendRadius As System.Boolean
```

```

Dim instance As IJogFeatureData
Dim value As System.Boolean
 
instance.UseDefaultBendRadius = value
 
value = instance.UseDefaultBendRadius
```

```

System.bool UseDefaultBendRadius {get; set;}
```

```

property System.bool UseDefaultBendRadius {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True uses the default bend radius, false does not

Example

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)  
[IJogFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~BendRadius.md)
