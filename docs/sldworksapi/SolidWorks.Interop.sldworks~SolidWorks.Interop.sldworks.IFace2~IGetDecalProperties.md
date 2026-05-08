# IGetDecalProperties Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties`

Gets the properties of the specified decal on this face.
Gets the properties of the specified decal on this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetDecalProperties( _
   ByVal PDecal As Decal, _
   ByRef pFaceDecalProperties As FaceDecalProperties _
) 
```

```

Dim instance As IFace2
Dim PDecal As Decal
Dim pFaceDecalProperties As FaceDecalProperties
 
instance.IGetDecalProperties(PDecal, pFaceDecalProperties)
```

```

void IGetDecalProperties( 
   Decal PDecal,
   ref FaceDecalProperties pFaceDecalProperties
)
```

```

void IGetDecalProperties( 
   Decal^ PDecal,
   FaceDecalProperties^% pFaceDecalProperties
) 
```

#### Parameters

*PDecal*
:   [Decal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.md) whose properties to get

*pFaceDecalProperties*
:   - in-process, unmanaged C++: Pointer to an array of [decal properties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetAllDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.md)  
[IFace2::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetDecalsCount.md)  
[IFace2::IGetAllDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetAllDecalProperties.md)
