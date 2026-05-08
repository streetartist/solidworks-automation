# IGetFaces Method (IHealEdgesFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~IGetFaces`

Gets the faces whose edges to heal.
Gets the faces whose edges to heal.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaces( _
   ByVal Count As System.Integer _
) As Face2
```

```

Dim instance As IHealEdgesFeatureData
Dim Count As System.Integer
Dim value As Face2
 
value = instance.IGetFaces(Count)
```

```

Face2 IGetFaces( 
   System.int Count
)
```

```

Face2^ IGetFaces( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of faces whose edges to heal

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) whose edges to heal
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IHealEdgesFeatureData::GetFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~GetFacesCount.md) before using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.md)  
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.md)  
[IHealEdgesFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~ISetFaces.md)  
[IHealEdgesFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~Faces.md)
