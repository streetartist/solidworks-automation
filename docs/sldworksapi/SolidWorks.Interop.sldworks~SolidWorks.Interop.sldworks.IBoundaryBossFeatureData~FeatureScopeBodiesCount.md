# FeatureScopeBodiesCount Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodiesCount`

Gets the number of bodies that this boundary feature affects in a multibody part.
Gets the number of bodies that this boundary feature affects in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FeatureScopeBodiesCount As System.Integer
```

```

Dim instance As IBoundaryBossFeatureData
Dim value As System.Integer
 
value = instance.FeatureScopeBodiesCount
```

```

System.int FeatureScopeBodiesCount {get;}
```

```

property System.int FeatureScopeBodiesCount {
   System.int get();
}
```

#### Property Value

Number of bodies

Remarks

This property is only available when [IBoundaryBossFeatureData::FeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScope.md) is true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBoundaryBossFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData.md)  
[IBoundaryBossFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.md)  
[IBoundaryBossFeatureData::FeatureScopeBodies Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~FeatureScopeBodies.md)  
[IBoundaryBossFeatureData::AutoSelect Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData~AutoSelect.md)
