# GetTextFormat Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat`

Gets the text format for the specified text in this annotation.
Gets the text format for the specified text in this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextFormat( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetTextFormat(Index)
```

```

System.object GetTextFormat( 
   System.int Index
)
```

```

System.Object^ GetTextFormat( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Number indicating which text within this annotation to check

#### Return Value

[ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md)

Remarks

The behavior of this method differs depending on the type of annotation.

- [Datum target](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md) and [Datum feature symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)  
    
  These symbols always use the document default setting for dimension text format to  
  display text within the symbol. The index argument is not used and should be set  
  to 0.
- [Geometric Tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md), [display dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md), [simple notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md), [surface finish](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md), and [weld symbols](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
    
  These symbols can either use the document default setting to display text within  
  the symbol (dimension text setting for the geometric tolerance symbols and display  
  dimensions, or note text setting for notes) or they can use a local format. The index  
  argument is not used and should be set to 0.
- [Blocks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) (and compound notes for documents created in SOLIDWORKS 2015 and earlier)  
    
  These symbols might contain several different pieces of text; each piece can use  
  the document default setting for notes or a local format. The index argument identifies  
  the text. The index value is 0-based. If the index value is invalid, then this method  
  returns a Nothing or null pointer. To get the number of text or [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) objects, use [IAnnotation::GetTextFormatCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.md).
- Rich text format  
    
  If a note contains embedded rich text information in the string, then this method returns  
  a text format that does not necessarily reflect what is displayed on the screen for  
  that note. Use [INote::HasMultipleFonts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~HasMultipleFonts.md) to determine if the note contains embedded  
  rich text information.

ITextFormat is returned if it is for a local setting or for the document  
default setting. To determine whether or not this annotation is using the document  
default settings for text format, use [IAnnotation::GetUseDocTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.md). To set the  
text format information, use [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md).

Example

[Change Text Format (VBA)](Change_Text_Format_Example_VB.htm)  
[Get Whether Note Contains Rich Embedded Text (VBA)](Get_Whether_Note_Contains_Rich-embedded_Text_Example_VB.htm)  
[Increase Width of Text (VBA)](Increase_Width_of_Text_Example_VB.htm)  
[Modify and Reload Sheet Format Template (C#)](Modify_and_Reload_Sheet_Format_Template_Example_CSharp.htm)  
[Modify and Reload Sheet Format Template (VB.NET)](Modify_and_Reload_Sheet_Format_Template_Example_VBNET.htm)  
[Modify and Reload Sheet Format Template (VBA)](Modify_and_Reload_Sheet_Format_Template_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md)  
[IAnnotation::GetTextFormatCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.md)  
[IAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md)  
[IAnnotation::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md)
