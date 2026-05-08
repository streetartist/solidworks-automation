# ISetFaces Method (IHealEdgesFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~ISetFaces`

Gets the faces whose edges were healed.
Gets the faces whose edges were healed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetFaces( _
   ByVal Count As System.Integer, _
   ByRef EntIn As Face2 _
) 
```

```

Dim instance As IHealEdgesFeatureData
Dim Count As System.Integer
Dim EntIn As Face2
 
instance.ISetFaces(Count, EntIn)
```

```

void ISetFaces( 
   System.int Count,
   ref Face2 EntIn
)
```

```

void ISetFaces( 
   System.int Count,
   Face2^% EntIn
) 
```

#### Parameters

*Count*
:   Number of faces whose edges were healed

*EntIn*
:   - in-process, unmanaged C++: Pointer to [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) whose edges were healed

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHealEdgesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData.md)  
[IHealEdgesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.md)  
[IHealEdgesFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~IGetFaces.md)  
[IHealEdgesFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData~Faces.md)
