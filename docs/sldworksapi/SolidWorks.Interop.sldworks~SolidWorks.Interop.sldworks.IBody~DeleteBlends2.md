# DeleteBlends2 Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~DeleteBlends2`

Obsolete. Superseded by IBody2::CreateBlends2.
Obsolete. Superseded by [IBody2::CreateBlends2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.md).

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

Dim instance As IBody
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

*FaceList*

*DoLocalCheck*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
