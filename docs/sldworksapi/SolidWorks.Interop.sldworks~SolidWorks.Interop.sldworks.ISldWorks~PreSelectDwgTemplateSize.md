# PreSelectDwgTemplateSize Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreSelectDwgTemplateSize`

Establishes which template to use when creating a drawing.
Establishes which template to use when creating a drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub PreSelectDwgTemplateSize( _
   ByVal TemplateToUse As System.Integer, _
   ByVal TemplateName As System.String _
) 
```

```

Dim instance As ISldWorks
Dim TemplateToUse As System.Integer
Dim TemplateName As System.String
 
instance.PreSelectDwgTemplateSize(TemplateToUse, TemplateName)
```

```

void PreSelectDwgTemplateSize( 
   System.int TemplateToUse,
   System.string TemplateName
)
```

```

void PreSelectDwgTemplateSize( 
   System.int TemplateToUse,
   System.String^ TemplateName
) 
```

#### Parameters

*TemplateToUse*
:   Type of template to use as defined in [swDwgTemplates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)

*TemplateName*
:   Reserved for future use; use NULL

Remarks

By calling this method and specifying a template size, no dialog appears when the end-user interactively selects File, New, Drawing.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.md)  
[ISldWorks::GetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetTemplateSizes.md)  
[ISldWorks::IGetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetTemplateSizes.md)
