# ISetCavitySurfaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetCavitySurfaces`

Sets the cavity surface bodies for this tooling split feature.
Sets the cavity surface bodies for this tooling split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetCavitySurfaces( _
   ByVal Count As System.Integer, _
   ByRef BodyArr As Body2 _
) 
```

```

Dim instance As IToolingSplitFeatureData
Dim Count As System.Integer
Dim BodyArr As Body2
 
instance.ISetCavitySurfaces(Count, BodyArr)
```

```

void ISetCavitySurfaces( 
   System.int Count,
   ref Body2 BodyArr
)
```

```

void ISetCavitySurfaces( 
   System.int Count,
   Body2^% BodyArr
) 
```

#### Parameters

*Count*
:   Number of cavity surface bodies

*BodyArr*
:   - in-process, unmanaged C++: Pointer to an array of cavity surface [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.md)  
[IToolingSplitFeatureData::GetCavitySurfacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetCavitySurfacesCount.md)  
[IToolingSplitFeatureData::IGetCavitySurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetCavitySurfaces.md)  
[IToolingSplitFeatureData::CavitySurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~CavitySurfaces.md)
