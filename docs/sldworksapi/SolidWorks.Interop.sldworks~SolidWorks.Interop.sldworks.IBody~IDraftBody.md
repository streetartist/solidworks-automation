# IDraftBody Method (IBody)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IDraftBody`

Obsolete. Superseded by IBody2::IDraftBody2.
Obsolete. Superseded by [IBody2::IDraftBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDraftBody2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IDraftBody( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face, _
   ByRef EdgeList As Edge, _
   ByVal DraftAngle As System.Double, _
   ByRef Dir As System.Double _
) As System.Boolean
```

```

Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As Face
Dim EdgeList As Edge
Dim DraftAngle As System.Double
Dim Dir As System.Double
Dim value As System.Boolean
 
value = instance.IDraftBody(NumOfFaces, FaceList, EdgeList, DraftAngle, Dir)
```

```

System.bool IDraftBody( 
   System.int NumOfFaces,
   ref Face FaceList,
   ref Edge EdgeList,
   System.double DraftAngle,
   ref System.double Dir
)
```

```

System.bool IDraftBody( 
   System.int NumOfFaces,
   Face^% FaceList,
   Edge^% EdgeList,
   System.double DraftAngle,
   System.double% Dir
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
