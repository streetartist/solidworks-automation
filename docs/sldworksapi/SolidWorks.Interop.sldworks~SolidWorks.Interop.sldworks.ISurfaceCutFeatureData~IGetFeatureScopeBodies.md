# IGetFeatureScopeBodies Method (ISurfaceCutFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies`

Gets the solid bodies that the surface-cut feature affects in a multibody part.
Gets the solid bodies that the surface-cut feature affects in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFeatureScopeBodies( _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As ISurfaceCutFeatureData
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IGetFeatureScopeBodies(Count)
```

```

Body2 IGetFeatureScopeBodies( 
   System.int Count
)
```

```

Body2^ IGetFeatureScopeBodies( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of solid bodies to affect

#### Return Value

- in-process, unmanaged C++: Pointer to an array of solid [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) of size Count
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData.

Before calling this method, call [ISurfaceCutFeatureData::GetFeatureScopeBodiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~IGetFeatureScopeBodies.md) to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.md)  
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.md)  
[ISurfaceCutFeatureData::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~ISetFeatureScopeBodies.md)  
[ISurfaceCutFeatureData::AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~AutoSelect.md)  
[ISurfaceCutFeatureData::FeatureScope Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScope.md)  
[ISurfaceCutFeatureData::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~FeatureScopeBodies.md)
