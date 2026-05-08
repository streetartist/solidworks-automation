# DraftBody Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~DraftBody`

Obsolete. Superseded by IBody2::DraftBody2.
Obsolete. Superseded by [IBody2::DraftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DraftBody2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DraftBody( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object, _
   ByVal EdgeList As System.Object, _
   ByVal DraftAngle As System.Double, _
   ByVal Dir As System.Object _
) As System.Boolean
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim EdgeList As System.Object
Dim DraftAngle As System.Double
Dim Dir As System.Object
Dim value As System.Boolean
 
value = instance.DraftBody(NumOfFaces, FaceList, EdgeList, DraftAngle, Dir)
```

```

System.bool DraftBody( 
   System.int NumOfFaces,
   System.object FaceList,
   System.object EdgeList,
   System.double DraftAngle,
   System.object Dir
)
```

```

System.bool DraftBody( 
   System.int NumOfFaces,
   System.Object^ FaceList,
   System.Object^ EdgeList,
   System.double DraftAngle,
   System.Object^ Dir
) 
```

#### Parameters

*NumOfFaces*

*FaceList*

*EdgeList*

*DraftAngle*

*Dir*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.md)  
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.md)
