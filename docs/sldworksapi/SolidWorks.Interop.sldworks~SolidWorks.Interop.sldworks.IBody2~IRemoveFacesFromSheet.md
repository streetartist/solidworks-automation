# IRemoveFacesFromSheet Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveFacesFromSheet`

Removes the specified faces from a sheet (surface) body.
Removes the specified faces from a sheet (surface) body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IRemoveFacesFromSheet( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FacesToRemove As Face2 _
) 
```

```

Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FacesToRemove As Face2
 
instance.IRemoveFacesFromSheet(NumOfFaces, FacesToRemove)
```

```

void IRemoveFacesFromSheet( 
   System.int NumOfFaces,
   ref Face2 FacesToRemove
)
```

```

void IRemoveFacesFromSheet( 
   System.int NumOfFaces,
   Face2^% FacesToRemove
) 
```

#### Parameters

*NumOfFaces*
:   Number of faces generated when these two bodies intersect

*FacesToRemove*
:   Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to remove

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::RemoveFacesFromSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveFacesFromSheet.md)
