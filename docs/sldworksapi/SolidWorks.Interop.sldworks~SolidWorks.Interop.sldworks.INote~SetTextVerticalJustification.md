# SetTextVerticalJustification Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextVerticalJustification`

Sets the vertical justification of a standard note.
Sets the vertical justification of a standard note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetTextVerticalJustification( _
   ByVal Justification As System.Integer _
) 
```

```

Dim instance As INote
Dim Justification As System.Integer
 
instance.SetTextVerticalJustification(Justification)
```

```

void SetTextVerticalJustification( 
   System.int Justification
)
```

```

void SetTextVerticalJustification( 
   System.int Justification
) 
```

#### Parameters

*Justification*
:   Vertical justification as defined in [swTextAlignmentVertical\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTextAlignmentVertical_e.html)

Example

[Anchor a Note (C#)](Anchor_a_Note_Example_CSharp.htm)  
[Anchor a Note (VB.NET)](Anchor_a_Note_Example_VBNET.htm)  
[Anchor a Note (VBA)](Anchor_a_Note_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::GetTextVerticalJustification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextVerticalJustification.md)  
[INote::GetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetText.md)  
[INote::GetTextAngleAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextAngleAtIndex.md)  
[INote::GetTextCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextCount.md)  
[INote::GetTextFontAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextFontAtIndex.md)  
[INote::GetTextHeightAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextHeightAtIndex.md)  
[INote::GetTextInvertAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextInvertAtIndex.md)  
[INote::GetTextJustification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustification.md)  
[INote::GetTextLineSpacingAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextLineSpacingAtIndex.md)  
[INote::GetTextPoint2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPoint2.md)  
[INote::GetTextPositionAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextPositionAtIndex.md)  
[INote::GetTextRefPositionAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextRefPositionAtIndex.md)  
[INote::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetText.md)  
[INote::SetTextJustification Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustification.md)  
[INote::SetTextPoint Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.md)  
[INote::PropertyLinkedText Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.md)  
[INote::TextRightToLeft Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~TextRightToLeft.md)
