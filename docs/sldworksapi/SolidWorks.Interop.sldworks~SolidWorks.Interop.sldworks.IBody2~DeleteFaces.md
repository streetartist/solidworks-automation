# DeleteFaces Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces`

Obsolete. Superseded by IBody2::DeleteFaces3.
Obsolete. Superseded by [IBody2::DeleteFaces3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteFaces( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object _
) As System.Boolean
```

```

Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim value As System.Boolean
 
value = instance.DeleteFaces(NumOfFaces, FaceList)
```

```

System.bool DeleteFaces( 
   System.int NumOfFaces,
   System.object FaceList
)
```

```

System.bool DeleteFaces( 
   System.int NumOfFaces,
   System.Object^ FaceList
) 
```

#### Parameters

*NumOfFaces*

*FaceList*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
