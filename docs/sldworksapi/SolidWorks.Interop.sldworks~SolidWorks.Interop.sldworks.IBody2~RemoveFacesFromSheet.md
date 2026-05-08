# RemoveFacesFromSheet Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveFacesFromSheet`

Removes the specified faces from a sheet (surface) body.
Removes the specified faces from a sheet (surface) body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemoveFacesFromSheet( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FacesToRemove As System.Object _
) 
```

```

Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FacesToRemove As System.Object
 
instance.RemoveFacesFromSheet(NumOfFaces, FacesToRemove)
```

```

void RemoveFacesFromSheet( 
   System.int NumOfFaces,
   System.object FacesToRemove
)
```

```

void RemoveFacesFromSheet( 
   System.int NumOfFaces,
   System.Object^ FacesToRemove
) 
```

#### Parameters

*NumOfFaces*
:   Number of faces generated when these two bodies intersect

*FacesToRemove*
:   Array of faces to remove

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IRemoveFacesFromSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveFacesFromSheet.md)
