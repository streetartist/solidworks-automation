# IGetTemplateSizes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetTemplateSizes`

Gets the sheet properties from a template document.
Gets the sheet properties from a template document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTemplateSizes( _
   ByVal FileName As System.String, _
   ByRef PaperSize As System.Integer, _
   ByRef Width As System.Double, _
   ByRef Height As System.Double _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Boolean
 
value = instance.IGetTemplateSizes(FileName, PaperSize, Width, Height)
```

```

System.bool IGetTemplateSizes( 
   System.string FileName,
   out System.int PaperSize,
   out System.double Width,
   out System.double Height
)
```

```

System.bool IGetTemplateSizes( 
   System.String^ FileName,
   [Out] System.int PaperSize,
   [Out] System.double Width,
   [Out] System.double Height
) 
```

#### Parameters

*FileName*
:   Name of template with full directory path

*PaperSize*
:   Paper size as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*Width*
:   Custom paper width if PaperSize is set to swDwgPapersUserDefined

*Height*
:   Custom paper height if PaperSize is set to swDwgPapersUserDefined

#### Return Value

True if the operation is successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetTemplateSizes.md)  
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.md)  
[ISldWorks::PreSelectDwgTemplateSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreSelectDwgTemplateSize.md)
