# TrimByD1 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~TrimByD1`

Gets whether to trim surfaces in Direction 1 when curves do not form a closed boundary feature.
Gets whether to trim surfaces in Direction 1 when curves do not form a closed boundary feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TrimByD1 As System.Boolean
```

```

Dim instance As IBoundaryBossFeatureData
Dim value As System.Boolean
 
instance.TrimByD1 = value
 
value = instance.TrimByD1
```

```

System.bool TrimByD1 {get; set;}
```

```

property System.bool TrimByD1 {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to trim surfaces in Direction 1 when curves do not form a closed boundary feature, false to not

Remarks

This property is only available when curves exist in both Direction 1 and Direction 2.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::D1Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D1Curves.md)  
[IBoundaryBossFeatureData::D2Curves Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~D2Curves.md)
