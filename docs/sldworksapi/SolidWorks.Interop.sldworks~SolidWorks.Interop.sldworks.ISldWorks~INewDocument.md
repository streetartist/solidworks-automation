# INewDocument Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument`

Obsolete. Superseded by ISldWorks::INewDocument2.
Obsolete. Superseded by [ISldWorks::INewDocument2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function INewDocument( _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As ModelDoc
```

```

Dim instance As ISldWorks
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As ModelDoc
 
value = instance.INewDocument(TemplateName, PaperSize, Width, Height)
```

```

ModelDoc INewDocument( 
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

```

ModelDoc^ INewDocument( 
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
) 
```

#### Parameters

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
