# ISetEntities Method (ISurfaceKnitFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~ISetEntities`

Sets the faces and surfaces to knit.
Sets the faces and surfaces to knit.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetEntities( _
   ByVal Count As System.Integer, _
   ByRef FaceArr As System.Object _
) 
```

```

Dim instance As ISurfaceKnitFeatureData
Dim Count As System.Integer
Dim FaceArr As System.Object
 
instance.ISetEntities(Count, FaceArr)
```

```

void ISetEntities( 
   System.int Count,
   ref System.object FaceArr
)
```

```

void ISetEntities( 
   System.int Count,
   System.Object^% FaceArr
) 
```

#### Parameters

*Count*
:   Number of faces

*FaceArr*
:   - in-process, unmanaged C++: Pointer to an array of knit entities ([faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) and [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)) of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.md)  
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.md)  
[ISurfaceKnitFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~Entities.md)  
[ISurfaceKnitFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~IGetEntities.md)  
[ISurfaceKnitFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~GetEntitiesCount.md)
