# PullDirectionBase Property (IPartingLineFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionBase`

Gets or sets the direction of pull for the parting line feature.
Gets or sets the direction of pull for the parting line feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PullDirectionBase As System.Object
```

```

Dim instance As IPartingLineFeatureData
Dim value As System.Object
 
instance.PullDirectionBase = value
 
value = instance.PullDirectionBase
```

```

System.object PullDirectionBase {get; set;}
```

```

property System.Object^ PullDirectionBase {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Entity that indicates the direction of pull: [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), or [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)  
[IPartingLineFeatureData::DraftAnalysis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.md)  
[IPartingLineFeatureData::PullDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirection.md)  
[IPartingLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.md)
