# InsertCenterMark2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark2`

Obsolete. Superseded by IDrawingDoc::InsertCenterMark3.
Obsolete. Superseded by [IDrawingDoc::InsertCenterMark3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCenterMark2( _
   ByVal Style As System.Integer, _
   ByVal Propagate As System.Boolean _
) As CenterMark
```

```

Dim instance As IDrawingDoc
Dim Style As System.Integer
Dim Propagate As System.Boolean
Dim value As CenterMark
 
value = instance.InsertCenterMark2(Style, Propagate)
```

```

CenterMark InsertCenterMark2( 
   System.int Style,
   System.bool Propagate
)
```

```

CenterMark^ InsertCenterMark2( 
   System.int Style,
   System.bool Propagate
) 
```

#### Parameters

*Style*
:   Style as defined in [swCenterMarkStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkStyle_e.html)

*Propagate*
:   True if the center mark should propagate throughout the pattern, false if not

#### Return Value

Pointer to the [centermark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
