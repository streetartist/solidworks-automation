# IInsertMultiJogLeader3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertMultiJogLeader3`

Inserts a multi-jog leader.
Inserts a multi-jog leader.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertMultiJogLeader3( _
   ByVal PointsCount As System.Integer, _
   ByRef Points As MathPoint, _
   ByVal StartPointArrowStyle As System.Integer, _
   ByVal EndPointArrowStyle As System.Integer _
) As MultiJogLeader
```

```

Dim instance As IDrawingDoc
Dim PointsCount As System.Integer
Dim Points As MathPoint
Dim StartPointArrowStyle As System.Integer
Dim EndPointArrowStyle As System.Integer
Dim value As MultiJogLeader
 
value = instance.IInsertMultiJogLeader3(PointsCount, Points, StartPointArrowStyle, EndPointArrowStyle)
```

```

MultiJogLeader IInsertMultiJogLeader3( 
   System.int PointsCount,
   ref MathPoint Points,
   System.int StartPointArrowStyle,
   System.int EndPointArrowStyle
)
```

```

MultiJogLeader^ IInsertMultiJogLeader3( 
   System.int PointsCount,
   MathPoint^% Points,
   System.int StartPointArrowStyle,
   System.int EndPointArrowStyle
) 
```

#### Parameters

*PointsCount*
:   Number of points

*Points*
:   Array of [points](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) of size PointsCount

*StartPointArrowStyle*
:   Starting point's arrowhead style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

*EndPointArrowStyle*
:   Ending point's arrowhead style as defined in  [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

#### Return Value

Pointer to the newly created [multi-jog leader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::InsertMultiJogLeader3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertMultiJogLeader3.md)
