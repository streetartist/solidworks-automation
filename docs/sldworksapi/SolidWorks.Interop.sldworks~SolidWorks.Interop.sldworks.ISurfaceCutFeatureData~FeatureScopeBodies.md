# FeatureScopeBodies Property (ISurfaceCutFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScopeBodies`

Gets or sets the solid bodies that the surface-cut feature affects in a multibody part.
Gets or sets the solid bodies that the surface-cut feature affects in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FeatureScopeBodies As System.Object
```

```

Dim instance As ISurfaceCutFeatureData
Dim value As System.Object
 
instance.FeatureScopeBodies = value
 
value = instance.FeatureScopeBodies
```

```

System.object FeatureScopeBodies {get; set;}
```

```

property System.Object^ FeatureScopeBodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of solid [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) that the surface-cut feature affects

Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.md)  
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.md)  
[ISurfaceCutFeatureData::GetFeatureScopeBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~GetFeatureScopeBodiesCount.md)  
[ISurfaceCutFeatureData::IGetFeatureScopeBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.md)  
[ISurfaceCutFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~ISetFeatureScopeBodies.md)  
[ISurfaceCutFeatureData::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~AutoSelect.md)  
[ISurfaceCutFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScope.md)
