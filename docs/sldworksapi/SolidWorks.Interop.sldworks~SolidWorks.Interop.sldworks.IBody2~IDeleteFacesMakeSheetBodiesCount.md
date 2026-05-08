# IDeleteFacesMakeSheetBodiesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount`

Gets the number of sheet bodies to create from the deleted faces.
Gets the number of sheet bodies to create from the deleted faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDeleteFacesMakeSheetBodiesCount( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceList As Face2 _
) As System.Integer
```

```

Dim instance As IBody2
Dim FaceCount As System.Integer
Dim FaceList As Face2
Dim value As System.Integer
 
value = instance.IDeleteFacesMakeSheetBodiesCount(FaceCount, FaceList)
```

```

System.int IDeleteFacesMakeSheetBodiesCount( 
   System.int FaceCount,
   ref Face2 FaceList
)
```

```

System.int IDeleteFacesMakeSheetBodiesCount( 
   System.int FaceCount,
   Face2^% FaceList
) 
```

#### Parameters

*FaceCount*
:   Number of faces to delete from the body

*FaceList*
:   - in-process, unmanaged C++: Pointer to an array of the [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

Number of sheet bodies to create from the deleted faces

Remarks

To create sheet bodies from deleted faces, call [IBody2::IDeleteFacesMakeSheetBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
