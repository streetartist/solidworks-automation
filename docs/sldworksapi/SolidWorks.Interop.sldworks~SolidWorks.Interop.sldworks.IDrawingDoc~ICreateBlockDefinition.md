# ICreateBlockDefinition Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateBlockDefinition`

Obsolete. Superseded by ISketchManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.
Obsolete. Superseded by [ISketchManager::MakeSketchBlockFromFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md), [ISketchManager::MakeSketchBlockSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md), and [ISketchManager::MakeSketchBlockFromSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBlockDefinition( _
   ByVal Name As System.String, _
   ByVal XRefFileName As System.String, _
   ByVal Instance As System.Boolean, _
   ByVal SegmentCount As System.Integer, _
   ByRef Segments As SketchSegment, _
   ByVal PointCount As System.Integer, _
   ByRef Points As SketchPoint, _
   ByVal NoteCount As System.Integer, _
   ByRef Notes As Note, _
   ByVal DimensionCount As System.Integer, _
   ByRef Dimensions As DisplayDimension, _
   ByVal BlockCount As System.Integer, _
   ByRef Blocks As BlockInstance _
) As BlockDefinition
```

```

Dim instance As IDrawingDoc
Dim Name As System.String
Dim XRefFileName As System.String
Dim Instance As System.Boolean
Dim SegmentCount As System.Integer
Dim Segments As SketchSegment
Dim PointCount As System.Integer
Dim Points As SketchPoint
Dim NoteCount As System.Integer
Dim Notes As Note
Dim DimensionCount As System.Integer
Dim Dimensions As DisplayDimension
Dim BlockCount As System.Integer
Dim Blocks As BlockInstance
Dim value As BlockDefinition
 
value = instance.ICreateBlockDefinition(Name, XRefFileName, Instance, SegmentCount, Segments, PointCount, Points, NoteCount, Notes, DimensionCount, Dimensions, BlockCount, Blocks)
```

```

BlockDefinition ICreateBlockDefinition( 
   System.string Name,
   System.string XRefFileName,
   System.bool Instance,
   System.int SegmentCount,
   ref SketchSegment Segments,
   System.int PointCount,
   ref SketchPoint Points,
   System.int NoteCount,
   ref Note Notes,
   System.int DimensionCount,
   ref DisplayDimension Dimensions,
   System.int BlockCount,
   ref BlockInstance Blocks
)
```

```

BlockDefinition^ ICreateBlockDefinition( 
   System.String^ Name,
   System.String^ XRefFileName,
   System.bool Instance,
   System.int SegmentCount,
   SketchSegment^% Segments,
   System.int PointCount,
   SketchPoint^% Points,
   System.int NoteCount,
   Note^% Notes,
   System.int DimensionCount,
   DisplayDimension^% Dimensions,
   System.int BlockCount,
   BlockInstance^% Blocks
) 
```

#### Parameters

*Name*

*XRefFileName*

*Instance*

*SegmentCount*

*Segments*

*PointCount*

*Points*

*NoteCount*

*Notes*

*DimensionCount*

*Dimensions*

*BlockCount*

*Blocks*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
