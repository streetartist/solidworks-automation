# IInsertMultiJogLeader2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertMultiJogLeader2`

Obsolete. Superseded by IDrawingDoc::InsertMultiJogLeader3.
Obsolete. Superseded by [IDrawingDoc::InsertMultiJogLeader3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertMultiJogLeader3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertMultiJogLeader2( _
   ByVal PointsCount As System.Integer, _
   ByRef Points As MathPoint _
) As MultiJogLeader
```

```

Dim instance As IDrawingDoc
Dim PointsCount As System.Integer
Dim Points As MathPoint
Dim value As MultiJogLeader
 
value = instance.IInsertMultiJogLeader2(PointsCount, Points)
```

```

MultiJogLeader IInsertMultiJogLeader2( 
   System.int PointsCount,
   ref MathPoint Points
)
```

```

MultiJogLeader^ IInsertMultiJogLeader2( 
   System.int PointsCount,
   MathPoint^% Points
) 
```

#### Parameters

*PointsCount*

*Points*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
