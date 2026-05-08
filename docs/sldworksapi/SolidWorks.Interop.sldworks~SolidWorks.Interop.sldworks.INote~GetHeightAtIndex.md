# GetHeightAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightAtIndex`

Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the specified text item's height in a compound note.
Obsolete for documents created in SOLIDWORKS 2016 and later. Gets the specified text item's height in a compound note.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHeightAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

```

Dim instance As INote
Dim Index As System.Integer
Dim value As System.Double
 
value = instance.GetHeightAtIndex(Index)
```

```

System.double GetHeightAtIndex( 
   System.int Index
)
```

```

System.double GetHeightAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index position of the text

#### Return Value

Text height

Remarks

Because a compound note can have multiple pieces of text, many of the compound note methods require you to specify the index value of the desired text. For example, the first piece of text added to the compound note using [INote::AddText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~AddText.md) has an index number of 1, the second text added has index number of 2, and so on.

If you use this method on a standard note (not a compound note), then the index value must be set to 1.

To set the specified text's height, use [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) or [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md).

Example

[Create Compound Note (VBA)](Create_Compound_Note_Example_VB.htm)

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
[INote::GetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetSketch.md)  
[INote::IGetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtent.md)  
[INote::IGetExtentAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetExtentAtIndex.md)  
[INote::IGetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetSketch.md)  
[INote::IsCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsCompoundNote.md)  
[INote::SetTextAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextAtIndex.md)  
[INote::SetTextJustificationAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextJustificationAtIndex.md)  
[INote::SetTextOffsetAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextOffsetAtIndex.md)  
[INote::SetTextPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetTextPoint.md)  
[INote::SetZeroLengthLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetZeroLengthLeader.md)  
[INote::SetHeightInPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeightInPoints.md)  
[INote::SetHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetHeight.md)  
[INote::GetHeightInPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeightInPoints.md)  
[INote::GetHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetHeight.md)
