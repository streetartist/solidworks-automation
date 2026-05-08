# InsertCenterMark3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark3`

Inserts a center mark in a drawing document.
Inserts a center mark in a drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCenterMark3( _
   ByVal Style As System.Integer, _
   ByVal Propagate As System.Boolean, _
   ByVal Slot As System.Boolean _
) As CenterMark
```

```

Dim instance As IDrawingDoc
Dim Style As System.Integer
Dim Propagate As System.Boolean
Dim Slot As System.Boolean
Dim value As CenterMark
 
value = instance.InsertCenterMark3(Style, Propagate, Slot)
```

```

CenterMark InsertCenterMark3( 
   System.int Style,
   System.bool Propagate,
   System.bool Slot
)
```

```

CenterMark^ InsertCenterMark3( 
   System.int Style,
   System.bool Propagate,
   System.bool Slot
) 
```

#### Parameters

*Style*
:   Style as defined in [swCenterMarkStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkStyle_e.html)

*Propagate*
:   True if the center mark should propagate throughout the pattern, false if not

*Slot*
:   True if this is slot-style center mark, false if not

#### Return Value

[Center mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md)

Remarks

Call [IView::AutoInsertCenterMarks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.md) to automatically insert center marks in multiple drawing views.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
