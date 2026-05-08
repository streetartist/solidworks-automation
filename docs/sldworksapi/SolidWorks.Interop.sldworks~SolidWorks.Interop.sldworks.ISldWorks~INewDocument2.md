# INewDocument2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument2`

Creates a new document based on the specified template.
Creates a new document based on the specified template.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function INewDocument2( _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As ModelDoc2
```

```

Dim instance As ISldWorks
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As ModelDoc2
 
value = instance.INewDocument2(TemplateName, PaperSize, Width, Height)
```

```

ModelDoc2 INewDocument2( 
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

```

ModelDoc2^ INewDocument2( 
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
) 
```

#### Parameters

*TemplateName*
:   Name of the template to use for creating the new document

*PaperSize*
:   Size of paper as defined in [swDwgPaperSizes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)

*Width*
:   Width of paper; used only when PaperSize is swDwgPapersUserDefined

*Height*
:   Height of paper; used only when PaperSize is swDwgPapersUserDefined

#### Return Value

Newly created [document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) or NULL if the operation fails

Remarks

To get the default template filename, use [ISldWorks::GetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.md):

- for parts: swDefaultTemplatePart
- for assemblies: swDefaultTemplateAssembly
- for drawings: swDefaultTemplateDrawing

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.md)  
[ISldWorks::NewDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDocument.md)
