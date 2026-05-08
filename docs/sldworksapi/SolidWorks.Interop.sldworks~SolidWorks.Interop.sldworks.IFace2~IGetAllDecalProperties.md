# IGetAllDecalProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetAllDecalProperties`

Gets the decal properties applied to this face.
Gets the decal properties applied to this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAllDecalProperties( _
   ByVal Count As System.Integer _
) As FaceDecalProperties
```

```

Dim instance As IFace2
Dim Count As System.Integer
Dim value As FaceDecalProperties
 
value = instance.IGetAllDecalProperties(Count)
```

```

FaceDecalProperties IGetAllDecalProperties( 
   System.int Count
)
```

```

FaceDecalProperties^ IGetAllDecalProperties( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of decals applied to this face

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [decal properties applied to this face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IFace2::GetDecalsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetDecalsCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetAllDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.md)  
[IFace2::IGetDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties.md)
