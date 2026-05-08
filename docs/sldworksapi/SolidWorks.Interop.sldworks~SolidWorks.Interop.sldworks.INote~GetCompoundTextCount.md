# GetCompoundTextCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextCount`

Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the number of text items in a compound note.
Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the number of text items in a compound note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCompoundTextCount() As System.Integer
```

```

Dim instance As INote
Dim value As System.Integer
 
value = instance.GetCompoundTextCount()
```

```

System.int GetCompoundTextCount()
```

```

System.int GetCompoundTextCount(); 
```

#### Return Value

Number of text items in a compound note

Remarks

Use this method before using any of the following methods:

- [INote::GetCompoundTextAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextAtIndex.md)
- [INote::GetTextOffsetAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextOffsetAtIndex.md) and [INote::IGetTextOffsetAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextOffsetAtIndex.md)
- [INote::GetTextJustificationAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustificationAtIndex.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::AddText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.md)  
[INote::BeginSketchEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BeginSketchEdit.md)  
[INote::EndSketchEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~EndSketchEdit.md)  
[INote::GetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtent.md)  
[INote::GetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtentAtIndex.md)  
[INote::GetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetSketch.md)  
[INote::GetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustificationAtIndex.md)  
[INote::GetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextOffsetAtIndex.md)  
[INote::IGetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtent.md)  
[INote::IGetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtentAtIndex.md)  
[INote::IGetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetSketch.md)  
[INote::IsCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsCompoundNote.md)  
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.md)  
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.md)  
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.md)  
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.md)  
[INote::GetHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex.md)
