# GetBendNoteAttributeString Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteAttributeString`

Gets the internal string that is used to format the text of the specified bend note attribute in this drawing view of a sheet metal part.
Gets the internal string that is used to format the text of the specified bend note attribute in this drawing view of a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBendNoteAttributeString( _
   ByVal Attribute As System.Integer _
) As System.String
```

```

Dim instance As IView
Dim Attribute As System.Integer
Dim value As System.String
 
value = instance.GetBendNoteAttributeString(Attribute)
```

```

System.string GetBendNoteAttributeString( 
   System.int Attribute
)
```

```

System.String^ GetBendNoteAttributeString( 
   System.int Attribute
) 
```

#### Parameters

*Attribute*
:   Bend note attribute as defined in [swBendNoteAttribute\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendNoteAttribute_e.html)

#### Return Value

String that is used to format the bend note attribute

Remarks

Call this method to specify the Format parameter of [IView::SetBendNoteTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetBendNoteTextFormat.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetBendNoteTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendNoteTextFormat.md)  
[IView::ShowSheetMetalBendNotes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowSheetMetalBendNotes.md)
