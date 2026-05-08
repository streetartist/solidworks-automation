# IGetSupplementalFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IGetSupplementalFaces`

Gets the faces in this mate.
Gets the faces in this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSupplementalFaces( _
   ByVal WhichOne As System.Integer, _
   ByVal FaceCount As System.Integer _
) As Face2
```

```

Dim instance As IMate2
Dim WhichOne As System.Integer
Dim FaceCount As System.Integer
Dim value As Face2
 
value = instance.IGetSupplementalFaces(WhichOne, FaceCount)
```

```

Face2 IGetSupplementalFaces( 
   System.int WhichOne,
   System.int FaceCount
)
```

```

Face2^ IGetSupplementalFaces( 
   System.int WhichOne,
   System.int FaceCount
) 
```

#### Parameters

*WhichOne*
:   Number of components in this mate

*FaceCount*
:   Number of faces in this mate

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) in this mate

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::GetSupplementalFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetSupplementalFaces.md)  
[IMate2::HasLoadBearingFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces.md)  
[IMate2::IsLoadBearingFacesBonded Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded.md)
