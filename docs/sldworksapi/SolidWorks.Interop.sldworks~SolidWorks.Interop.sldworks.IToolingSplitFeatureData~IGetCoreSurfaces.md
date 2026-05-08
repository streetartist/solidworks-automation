# IGetCoreSurfaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~IGetCoreSurfaces`

Gets the core surface bodies in this tooling split feature.
Gets the core surface bodies in this tooling split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCoreSurfaces( _
   ByVal Count As System.Integer _
) As Body2
```

```

Dim instance As IToolingSplitFeatureData
Dim Count As System.Integer
Dim value As Body2
 
value = instance.IGetCoreSurfaces(Count)
```

```

Body2 IGetCoreSurfaces( 
   System.int Count
)
```

```

Body2^ IGetCoreSurfaces( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of core surface bodies

#### Return Value

- in-process, unmanaged C++: Pointer to an array of core surface [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IToolingSplitFeatureData::GetCoreSurfacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~GetCoreSurfacesCount.md) before calling this method to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.md)  
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.md)  
[IToolingSplitFeatureData::CoreSurfaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~CoreSurfaces.md)  
[IToolingSplitFeatureData::ISetCoreSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~ISetCoreSurfaces.md)
