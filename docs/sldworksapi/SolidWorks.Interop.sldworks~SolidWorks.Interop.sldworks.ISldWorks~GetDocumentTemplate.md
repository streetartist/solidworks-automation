# GetDocumentTemplate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate`

Gets the name of document template that can be used in ISldWorks::NewDocument or ISldWorks::INewDocument2.
Gets the name of document template that can be used in [ISldWorks::NewDocument](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDocument.md) or [ISldWorks::INewDocument2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDocumentTemplate( _
   ByVal Mode As System.Integer, _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.String
```

```

Dim instance As ISldWorks
Dim Mode As System.Integer
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.String
 
value = instance.GetDocumentTemplate(Mode, TemplateName, PaperSize, Width, Height)
```

```

System.string GetDocumentTemplate( 
   System.int Mode,
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

```

System.String^ GetDocumentTemplate( 
   System.int Mode,
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
) 
```

#### Parameters

*Mode*
:   Document type as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html) (see Remarks)

*TemplateName*
:   Name of custom template including full directory path

*PaperSize*
:   Size of paper as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*Width*
:   Width of paper; used only when paperSize is swDwgPapersUserDefined

*Height*
:   Height of paper; used only when paperSize is swDwgPapersUserDefined

#### Return Value

Name of the selected document template

Remarks

|  |  |
| --- | --- |
| If type is... | Then... |
| swDocPART or swDocASSEMBLY | Remaining arguments are not used. |
| swDocDRAWING | Remaining arguments are used to determine which drawing template to use. |

Example

[Get Locations and Names of Document Templates (VBA)](Get_Locations_and_Names_of_Document_Templates_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetTemplateSizes.md)  
[ISldWorks::IGetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetTemplateSizes.md)  
[ISldWorks::PreSelectDwgTemplateSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreSelectDwgTemplateSize.md)
