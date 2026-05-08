# IGetTessellation Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTessellation`

Gets the ITessellation object.
Gets the [ITessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md) object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTessellation( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2 _
) As Tessellation
```

```

Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As Face2
Dim value As Tessellation
 
value = instance.IGetTessellation(NumOfFaces, FaceList)
```

```

Tessellation IGetTessellation( 
   System.int NumOfFaces,
   ref Face2 FaceList
)
```

```

Tessellation^ IGetTessellation( 
   System.int NumOfFaces,
   Face2^% FaceList
) 
```

#### Parameters

*NumOfFaces*
:   Number of faces to tessellate

*FaceList*
:   Array of faces to tessellate; if this is NULL, then SOLIDWORKS will tessellate the body

#### Return Value

Pointer to the [ITessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md) object

Example

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetTessellation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTessellation.md)
