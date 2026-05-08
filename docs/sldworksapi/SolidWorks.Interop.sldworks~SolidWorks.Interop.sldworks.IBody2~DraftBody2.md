# DraftBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DraftBody2`

Adds drafts to the specified faces on a temporary body. This method modifies the body.
Adds drafts to the specified faces on a temporary body. This method modifies the body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DraftBody2( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object, _
   ByVal EdgeList As System.Object, _
   ByVal BasePoint As System.Object, _
   ByVal DraftAngle As System.Double, _
   ByVal Dir As System.Object _
) As System.Boolean
```

```

Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim EdgeList As System.Object
Dim BasePoint As System.Object
Dim DraftAngle As System.Double
Dim Dir As System.Object
Dim value As System.Boolean
 
value = instance.DraftBody2(NumOfFaces, FaceList, EdgeList, BasePoint, DraftAngle, Dir)
```

```

System.bool DraftBody2( 
   System.int NumOfFaces,
   System.object FaceList,
   System.object EdgeList,
   System.object BasePoint,
   System.double DraftAngle,
   System.object Dir
)
```

```

System.bool DraftBody2( 
   System.int NumOfFaces,
   System.Object^ FaceList,
   System.Object^ EdgeList,
   System.Object^ BasePoint,
   System.double DraftAngle,
   System.Object^ Dir
) 
```

#### Parameters

*NumOfFaces*
:   Number of faces to draft

*FaceList*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to draft

*EdgeList*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), one for each face, along which to apply the drafts

*BasePoint*
:   Pointer to a [MathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object (x,y,z values of the base point)

*DraftAngle*
:   Draft angle

*Dir*
:   Array of 3 doubles (x, y, z), a vector which specifies the direction of the draft

#### Return Value

True if drafts are applied, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IDraftBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDraftBody2.md)
