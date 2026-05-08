# GetTemplateSizes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetTemplateSizes`

Gets the sheet properties from a template document.
Gets the sheet properties from a template document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTemplateSizes( _
   ByVal FileName As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Object
 
value = instance.GetTemplateSizes(FileName)
```

```

System.object GetTemplateSizes( 
   System.string FileName
)
```

```

System.Object^ GetTemplateSizes( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Name of template with full directory path

#### Return Value

Array of 3 doubles containing the paper size, width, and  height

Example

[Get Drawing Template Size (VBA)](Get_Drawing_Template_Size_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IGetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetTemplateSizes.md)  
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.md)  
[ISldWorks::PreSelectDwgTemplateSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreSelectDwgTemplateSize.md)
