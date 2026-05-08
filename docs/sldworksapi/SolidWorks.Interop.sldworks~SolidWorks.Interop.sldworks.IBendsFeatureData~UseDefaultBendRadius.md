# UseDefaultBendRadius Property (IBendsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~UseDefaultBendRadius`

Get or sets whether to use the default bend radius for this Flatten-Bends/Process-Bends feature.
Get or sets whether to use the default bend radius for this Flatten-Bends/Process-Bends feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseDefaultBendRadius As System.Boolean
```

```

Dim instance As IBendsFeatureData
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

True to use the default bend radius, false to not

Example

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)  
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)  
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.md)  
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.md)  
[IBendsFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~BendRadius.md)
