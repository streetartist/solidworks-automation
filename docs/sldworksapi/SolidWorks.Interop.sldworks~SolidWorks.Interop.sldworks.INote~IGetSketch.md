# IGetSketch Method (INote)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetSketch`

Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the sketch for the current compound note.
Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the sketch for the current compound note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSketch() As Sketch
```

```

Dim instance As INote
Dim value As Sketch
 
value = instance.IGetSketch()
```

```

Sketch IGetSketch()
```

```

Sketch^ IGetSketch(); 
```

#### Return Value

[Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) for this compound note

Remarks

If the current note is not a compound note, then a NULL value is returned.

For adding or modifying actual sketch geometry in a compound note, use [INote::BeginSketchEdit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BeginSketchEdit.md), which activates the sketch of the compound note for modification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::AddText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.md)  
[INote::BeginSketchEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BeginSketchEdit.md)  
[INote::EndSketchEdit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~EndSketchEdit.md)  
[INote::GetCompoundTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextAtIndex.md)  
[INote::GetCompoundTextCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetCompoundTextCount.md)  
[INote::GetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtent.md)  
[INote::GetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetExtentAtIndex.md)  
[INote::GetHeightAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex.md)  
[INote::GetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextJustificationAtIndex.md)  
[INote::GetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetTextOffsetAtIndex.md)  
[INote::IGetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtent.md)  
[INote::IGetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtentAtIndex.md)  
[INote::IGetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetTextOffsetAtIndex.md)  
[INote::IsCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsCompoundNote.md)  
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.md)  
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.md)  
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.md)  
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.md)
