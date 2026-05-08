# GetTextFormatCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount`

Gets the number of text formats for this annotation.
Gets the number of text formats for this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextFormatCount() As System.Integer
```

```

Dim instance As IAnnotation
Dim value As System.Integer
 
value = instance.GetTextFormatCount()
```

```

System.int GetTextFormatCount()
```

```

System.int GetTextFormatCount(); 
```

#### Return Value

Number of text formats

Remarks

The value returned by this method is intended to be used with [IAnnotation::GetUseDocTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.md), [IAnnotation::GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md), [IAnnotation::IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md), [IAnnotation::SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md), and [IAnnotation::ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md). The index input argument for these methods must be less than the number returned by this method.  

This value is not necessarily the same as the number of text objects within a symbol. For example, there are multiple text objects in a geometric tolerance symbol, but they all share the same text format so SOLIDWORKS returns 1. In fact, for all of the annotations except blocks (and compound notes in documents created in SOLIDWORKS 2015 and earlier), this method should return 1. For blocks and compound notes, each piece of text within the symbol has its own text format, so the return value should match the number of TextFormat objects.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md)  
[IAnnotation::IGetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md)  
[IAnnotation::ISetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md)  
[IAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md)  
[IAnnotation::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.md)
