# GetTextSegmentFormat Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentFormat`

Gets the text format for the specified text segment in the current paragraph.
Gets the text format for the specified text segment in the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextSegmentFormat( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IParagraphs
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetTextSegmentFormat(Index)
```

```

System.object GetTextSegmentFormat( 
   System.int Index
)
```

```

System.Object^ GetTextSegmentFormat( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based index of text segment whose text format to get

#### Return Value

[ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md)

Remarks

Paragraphs contain one or more text segments. Each text segment has a different format.

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.md).

To populate Index, call [IParagraphs::GetTextSegmentCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentCount.md).

Example

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)  
[IParagraphs::GetTextSegmentText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentText.md)  
[IParagraphis::SetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetTextSegmentFormat.md)
