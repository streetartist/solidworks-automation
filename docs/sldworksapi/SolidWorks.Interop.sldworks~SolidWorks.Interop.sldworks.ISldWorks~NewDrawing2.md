# NewDrawing2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDrawing2`

Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2.
Obsolete. Superseded by [ISldWorks::NewDocument](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDocument.md) and [ISldWorks::INewDocument2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function NewDrawing2( _
   ByVal TemplateToUse As System.Integer, _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.Object
```

```

Dim instance As ISldWorks
Dim TemplateToUse As System.Integer
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Object
 
value = instance.NewDrawing2(TemplateToUse, TemplateName, PaperSize, Width, Height)
```

```

System.object NewDrawing2( 
   System.int TemplateToUse,
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

```

System.Object^ NewDrawing2( 
   System.int TemplateToUse,
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
) 
```

#### Parameters

*TemplateToUse*

*TemplateName*

*PaperSize*

*Width*

*Height*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
