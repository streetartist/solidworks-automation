# GetTextSegmentText Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentText`

Gets the text of the specified text segment in the current paragraph.
Gets the text of the specified text segment in the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextSegmentText( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As IParagraphs
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetTextSegmentText(Index)
```

```

System.string GetTextSegmentText( 
   System.int Index
)
```

```

System.String^ GetTextSegmentText( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based index of text segment whose text to get

#### Return Value

Text of text segment

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
[IParagraphs::GetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentFormat.md)
