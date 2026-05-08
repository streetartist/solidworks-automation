# GetTextSegmentCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentCount`

Gets the number of text segments in the current paragraph.
Gets the number of text segments in the current paragraph.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextSegmentCount() As System.Integer
```

```

Dim instance As IParagraphs
Dim value As System.Integer
 
value = instance.GetTextSegmentCount()
```

```

System.int GetTextSegmentCount()
```

```

System.int GetTextSegmentCount(); 
```

#### Return Value

Number of text segments

Remarks

Paragraphs contain one or more text segments. Each text segment has a different format.

Before calling this method, set the current paragraph using [IParagraphs::CurrentParagraph](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~CurrentParagraph.md).

Example

See the [IParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParagraphs Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs.md)  
[IParagraphs Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.md)  
[IParagraphs::GetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentFormat.md)  
[IParagraphs::GetTextSegmentText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~GetTextSegmentText.md)  
[IParagraphs::SetTextSegmentFormat Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs~SetTextSegmentFormat.md)
