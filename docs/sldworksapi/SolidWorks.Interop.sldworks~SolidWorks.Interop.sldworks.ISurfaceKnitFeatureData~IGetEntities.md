# IGetEntities Method (ISurfaceKnitFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~IGetEntities`

Gets the knitted faces and surfaces for this Surface-Knit feature.
Gets the knitted faces and surfaces for this Surface-Knit feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

```

Dim instance As ISurfaceKnitFeatureData
Dim Count As System.Integer
Dim value As System.Object
 
value = instance.IGetEntities(Count)
```

```

System.object IGetEntities( 
   System.int Count
)
```

```

System.Object^ IGetEntities( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of knit entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of knit entities ([faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) and [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISurfaceKnitFeatureData::GetEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~GetEntitiesCount.md) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.md)  
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.md)  
[ISurfaceKnitFeatureData::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~ISetEntities.md)  
[ISurfaceKnitFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~Entities.md)
