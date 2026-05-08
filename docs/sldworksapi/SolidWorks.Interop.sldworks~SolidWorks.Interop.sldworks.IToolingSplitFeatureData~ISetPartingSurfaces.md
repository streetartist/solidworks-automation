# ISetPartingSurfaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetPartingSurfaces`

Sets the parting surface bodies for this tooling split feature.
Sets the parting surface bodies for this tooling split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetPartingSurfaces( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
) 
```

```

Dim instance As IToolingSplitFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2
 
instance.ISetPartingSurfaces(Count, BodyArr)
```

```

void ISetPartingSurfaces( 
   System.int Count,
   ref Body2 BodyArr
)
```

```

void ISetPartingSurfaces( 
   System.int Count,
   Body2^% BodyArr
) 
```

#### Parameters

*Count*
:   Number of parting surface bodies

*BodyArr*
:   - in-process, unmanaged C++: Pointer to an array of parting surface [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.md)  
[IToolingSplitFeatureData::GetPartingSurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetPartingSurfacesCount.md)  
[IToolingSplitFeatureData::IGetPartingSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetPartingSurfaces.md)  
[IToolingSplitFeatureData::PartingSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~PartingSurfaces.md)
