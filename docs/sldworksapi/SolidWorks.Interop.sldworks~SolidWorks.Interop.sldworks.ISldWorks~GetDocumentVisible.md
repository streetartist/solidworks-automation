# GetDocumentVisible Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentVisible`

Gets the visibility of the document to open.
Gets the visibility of the document to open.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDocumentVisible( _
   ByVal Type As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Type As System.Integer
Dim value As System.Boolean
 
value = instance.GetDocumentVisible(Type)
```

```

System.bool GetDocumentVisible( 
   System.int Type
)
```

```

System.bool GetDocumentVisible( 
   System.int Type
) 
```

#### Parameters

*Type*
:   Document type as defined by [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

#### Return Value

True if the document will be visible when opened, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
