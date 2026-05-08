# SetTextSegmentFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetTextSegmentFormat`

Sets the text format for the specified text segment in the current paragraph.
Sets the text format for the specified text segment in the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetTextSegmentFormat( _
   ByVal Segment As System.Integer, _
   ByVal Format As System.Object _
) As System.Boolean
```

```

Dim instance As IParagraphs
Dim Segment As System.Integer
Dim Format As System.Object
Dim value As System.Boolean
 
value = instance.SetTextSegmentFormat(Segment, Format)
```

```

System.bool SetTextSegmentFormat( 
   System.int Segment,
   System.object Format
)
```

```

System.bool SetTextSegmentFormat( 
   System.int Segment,
   System.Object^ Format
) 
```

#### Parameters

*Segment*
:   0-based index of the text segment whose format to set

*Format*
:   [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md)

#### Return Value

True if successful, false if not

Remarks

Paragraphs contain one or more text segments. Each text segment has a different format.

Before calling this method:

- set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.md).
- call [IParagraphs::GetTextSegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentCount.md) to get the total number of text segments and a valid value for Segment.

After calling this method, call [IParagraphs::UpdateParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~UpdateParagraph.md) to update the model.

Example

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)  
[IParagraphics::GetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentFormat.md)
