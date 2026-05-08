# DeleteBlends2 Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2`

Obsolete. Superseded by IBody2::DeleteBlends3.
Obsolete. Superseded by [IBody2::DeleteBlends3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteBlends2( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object, _
   ByVal DoLocalCheck As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim DoLocalCheck As System.Boolean
Dim value As System.Boolean
 
value = instance.DeleteBlends2(NumOfFaces, FaceList, DoLocalCheck)
```

```

System.bool DeleteBlends2( 
   System.int NumOfFaces,
   System.object FaceList,
   System.bool DoLocalCheck
)
```

```

System.bool DeleteBlends2( 
   System.int NumOfFaces,
   System.Object^ FaceList,
   System.bool DoLocalCheck
) 
```

#### Parameters

*NumOfFaces*
:   Number of faces to delete

*FaceList*
:   List of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to delete

*DoLocalCheck*
:   True to perform a local check, false to not

#### Return Value

True if the set of fillet faces are removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IDeleteBlends2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.md)
