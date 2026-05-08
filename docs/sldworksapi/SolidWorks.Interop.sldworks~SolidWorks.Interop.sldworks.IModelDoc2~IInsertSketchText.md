# IInsertSketchText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertSketchText`

Obsolete. Superseded by IModelDoc2::InsertSketchText.
Obsolete. Superseded by [IModelDoc2::InsertSketchText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchText.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertSketchText( _
   ByVal Ptx As System.Double, _
   ByVal Pty As System.Double, _
   ByVal Ptz As System.Double, _
   ByVal Text As System.String, _
   ByVal Alignment As System.Integer, _
   ByVal FlipDirection As System.Integer, _
   ByVal HorizontalMirror As System.Integer, _
   ByVal WidthFactor As System.Integer, _
   ByVal SpaceBetweenChars As System.Integer _
) As SketchText
```

```

Dim instance As IModelDoc2
Dim Ptx As System.Double
Dim Pty As System.Double
Dim Ptz As System.Double
Dim Text As System.String
Dim Alignment As System.Integer
Dim FlipDirection As System.Integer
Dim HorizontalMirror As System.Integer
Dim WidthFactor As System.Integer
Dim SpaceBetweenChars As System.Integer
Dim value As SketchText
 
value = instance.IInsertSketchText(Ptx, Pty, Ptz, Text, Alignment, FlipDirection, HorizontalMirror, WidthFactor, SpaceBetweenChars)
```

```

SketchText IInsertSketchText( 
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.string Text,
   System.int Alignment,
   System.int FlipDirection,
   System.int HorizontalMirror,
   System.int WidthFactor,
   System.int SpaceBetweenChars
)
```

```

SketchText^ IInsertSketchText( 
   System.double Ptx,
   System.double Pty,
   System.double Ptz,
   System.String^ Text,
   System.int Alignment,
   System.int FlipDirection,
   System.int HorizontalMirror,
   System.int WidthFactor,
   System.int SpaceBetweenChars
) 
```

#### Parameters

*Ptx*
:   X coordinate of text

*Pty*
:   Y coordinate of text

*Ptz*
:   Z coordinate of text

*Text*
:   Text to insert (see **Remarks**)

*Alignment*
:   Alignment:

    - 0 = Left
    - 1 = Center
    - 2 = Right
    - 3 = Fully justified

    (see **Remarks**)

*FlipDirection*
:   1 to flip text vertically about the selected entity, 0 to not (see **Remarks**)

*HorizontalMirror*
:   1 to flip text horizontally, 0 to not

*WidthFactor*
:   6 <= Percentage by which to evenly widen each character in the text block < = 1667

*SpaceBetweenChars*
:   1 <= Percentage of space between each character in the text block <= 10000; valid only if Alignment != 3

#### Return Value

[Sketch text](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)

Remarks

Alignment and FlipDirection are valid only when a curve, edge, or sketch segment is selected. Text appears along the selected entity. If an entity is not selected, Text appears horizontally starting at the origin. [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) the curve, edge, or sketch segment with Mark = 1.

See the SOL**IDWORKS user-interface help > Sketching > Sketch Entities > Sketch Text > SketchText PropertyManager** topic for more information about this functionality.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::DissolveSketchText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DissolveSketchText.md)
