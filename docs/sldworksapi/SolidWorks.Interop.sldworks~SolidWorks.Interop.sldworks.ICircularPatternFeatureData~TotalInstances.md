# TotalInstances Property (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances`

Gets or sets the total number of pattern instances in Direction 1 of this circular pattern feature.
Gets or sets the total number of pattern instances in Direction 1 of this circular pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TotalInstances As System.Integer
```

```

Dim instance As ICircularPatternFeatureData
Dim value As System.Integer
 
instance.TotalInstances = value
 
value = instance.TotalInstances
```

```

System.int TotalInstances {get; set;}
```

```

property System.int TotalInstances {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Total number of pattern instances in Direction 1

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Get Transform for Each Circular Pattern Instance (C#)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_CSharp.htm)  
[Get Transform for Each Circular Pattern Instance (VB.NET)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VBNET.htm)  
[Get Transform for Each Circular Pattern Instance (VBA)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)  
[ICircularPatternFeatureData::EqualSpacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing.md)  
[ICircularPatternFeatureData::Spacing Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing.md)  
[ICircularPatternFeatureData::TotalInstances2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances2.md)
