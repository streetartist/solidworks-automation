# IDeleteBlends2 Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2`

Obsolete. Superseded by IBody2::DeleteBlends3.
Obsolete. Superseded by [IBody2::DeleteBlends3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeleteBlends2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2, _
   ByVal DoLocalCheck As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As Face2
Dim DoLocalCheck As System.Boolean
Dim value As System.Boolean
 
value = instance.IDeleteBlends2(NumOfFaces, FaceList, DoLocalCheck)
```

```

System.bool IDeleteBlends2( 
   System.int NumOfFaces,
   ref Face2 FaceList,
   System.bool DoLocalCheck
)
```

```

System.bool IDeleteBlends2( 
   System.int NumOfFaces,
   Face2^% FaceList,
   System.bool DoLocalCheck
) 
```

#### Parameters

*NumOfFaces*
:   Number of faces to delete

*FaceList*
:   - in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of size NumOfFaces to delete
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*DoLocalCheck*
:   True to perform a local check, false if not

#### Return Value

True if a set of fillet faces are removed, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::DeleteBlends2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.md)  
[IBody2::DeleteFaces5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces5.md)
