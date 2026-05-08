# GetUseDocTextFormat Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat`

Gets whether SOLIDWORKS is currently using the document default text format setting for this annotation.
Gets whether SOLIDWORKS is currently using the document default text format setting for this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUseDocTextFormat( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.GetUseDocTextFormat(Index)
```

```

System.bool GetUseDocTextFormat( 
   System.int Index
)
```

```

System.bool GetUseDocTextFormat( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Number indicating which text within this annotation to check (see **Remarks**)

#### Return Value

True if the setting is a document default setting, false if not

Remarks

The behavior of this method differs slightly depending on the type of annotation.

- [Weld](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md), [Datum Target](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md), [Datum Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.md), and [Surface Finish](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md) Symbols  
    
  These symbols always use the document default setting for dimension text format of the text objects within the symbol. Therefore, this method always returns True for these annotation types. The index argument is not used and should be set to 0.
- [Geometric Tolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md) Symbols, [Display Dimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md), and [Simple Notes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
    
  These symbols can use the document default setting to display all of the text objects within the symbol (dimension text setting for the geometric tolerance symbols and display dimensions, or note text setting for notes), in which case this method returns True. They can also use a local format, in which case this method returns false. The index argument is not used and should be set to 0.
- [Blocks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md) (and compound notes created in SOLIDWORKS 2015 and earlier)  
    
  These symbols can contain several different pieces of text, each individually using the document default setting for notes or a local format. The index argument identifies the text. The index value is 0-based. If the index value is invalid, this method returns True. To get the number of text or text format objects, use [IAnnotation::GetTextFormatCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.md).

To get the text format object for this annotation, use [IAnnotation::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md), [IAnnotation::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md), [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md), or [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)
