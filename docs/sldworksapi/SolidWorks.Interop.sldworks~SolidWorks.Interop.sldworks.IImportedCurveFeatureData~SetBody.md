# SetBody Method (IImportedCurveFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData~SetBody`

Modifies the wire body for this imported curve feature.
Modifies the wire body for this imported curve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetBody( _
   ByVal DispBody As Body2 _
) 
```

```

Dim instance As IImportedCurveFeatureData
Dim DispBody As Body2
 
instance.SetBody(DispBody)
```

```

void SetBody( 
   Body2 DispBody
)
```

```

void SetBody( 
   Body2^ DispBody
) 
```

#### Parameters

*DispBody*
:   Wire [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Wire bodies contain wires, loops, coedges, edges, and vertices. Wires typically represent profiles, construction lines, and center lines of swept shapes. Wires can also represent wire frames that, when surfaced, form shells.

The following methods create wire bodies:

- [IEdge::CreateWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~CreateWireBody.md)
- [ICurve::CreateWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~CreateWireBody.md)
- [IModeler::CreateWireBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.md)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IImportedCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData.md)  
[IImportedCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.md)
