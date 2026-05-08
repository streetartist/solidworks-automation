# GetSupplementalFaces Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetSupplementalFaces`

Gets the faces in this mate.
Gets the faces in this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSupplementalFaces( _
   ByVal WhichOne As System.Integer _
) As System.Object
```

```

Dim instance As IMate2
Dim WhichOne As System.Integer
Dim value As System.Object
 
value = instance.GetSupplementalFaces(WhichOne)
```

```

System.object GetSupplementalFaces( 
   System.int WhichOne
)
```

```

System.Object^ GetSupplementalFaces( 
   System.int WhichOne
) 
```

#### Parameters

*WhichOne*
:   Number of components in this mate

#### Return Value

Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) in this mate

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::IGetSupplementalFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IGetSupplementalFaces.md)  
[IMate2::HasLoadBearingFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces.md)  
[IMate2::IsLoadBearingFacesBonded Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded.md)
