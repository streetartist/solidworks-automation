# NewDrawing Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDrawing`

Obsolete. Superseded by ISldWorks::NewDocument and ISldWorks::INewDocument2.
Obsolete. Superseded by [ISldWorks::NewDocument](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDocument.md) and [ISldWorks::INewDocument2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function NewDrawing( _
   ByVal TemplateToUse As System.Integer _
) As System.Object
```

```

Dim instance As ISldWorks
Dim TemplateToUse As System.Integer
Dim value As System.Object
 
value = instance.NewDrawing(TemplateToUse)
```

```

System.object NewDrawing( 
   System.int TemplateToUse
)
```

```

System.Object^ NewDrawing( 
   System.int TemplateToUse
) 
```

#### Parameters

*TemplateToUse*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
