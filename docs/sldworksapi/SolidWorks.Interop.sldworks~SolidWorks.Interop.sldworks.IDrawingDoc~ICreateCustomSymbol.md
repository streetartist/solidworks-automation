# ICreateCustomSymbol Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCustomSymbol`

Obsolete. Superseded by ISkethcManager::MakeSketchBlockFromFile, ISketchManager::MakeSketchBlockSelected, and ISketchManager::MakeSketchBlockFromSketch.
Obsolete. Superseded by [ISkethcManager::MakeSketchBlockFromFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md), [ISketchManager::MakeSketchBlockSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md), and [ISketchManager::MakeSketchBlockFromSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateCustomSymbol( _
   ByVal SegmentCount As System.Integer, _
   ByRef Segments As SketchSegment, _
   ByVal PointCount As System.Integer, _
   ByRef Points As SketchPoint, _
   ByVal NoteCount As System.Integer, _
   ByRef Notes As Note _
) As CustomSymbol
```

```

Dim instance As IDrawingDoc
Dim SegmentCount As System.Integer
Dim Segments As SketchSegment
Dim PointCount As System.Integer
Dim Points As SketchPoint
Dim NoteCount As System.Integer
Dim Notes As Note
Dim value As CustomSymbol
 
value = instance.ICreateCustomSymbol(SegmentCount, Segments, PointCount, Points, NoteCount, Notes)
```

```

CustomSymbol ICreateCustomSymbol( 
   System.int SegmentCount,
   ref SketchSegment Segments,
   System.int PointCount,
   ref SketchPoint Points,
   System.int NoteCount,
   ref Note Notes
)
```

```

CustomSymbol^ ICreateCustomSymbol( 
   System.int SegmentCount,
   SketchSegment^% Segments,
   System.int PointCount,
   SketchPoint^% Points,
   System.int NoteCount,
   Note^% Notes
) 
```

#### Parameters

*SegmentCount*

*Segments*

*PointCount*

*Points*

*NoteCount*

*Notes*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
