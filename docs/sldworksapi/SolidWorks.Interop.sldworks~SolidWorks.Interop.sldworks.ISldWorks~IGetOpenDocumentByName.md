# IGetOpenDocumentByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName`

Obsolete. Superseded ISldWorks::IGetOpenDocumentByName2.
Obsolete. Superseded [ISldWorks::IGetOpenDocumentByName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetOpenDocumentByName2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetOpenDocumentByName( _
   ByVal DocumentName As System.String _
) As ModelDoc
```

```

Dim instance As ISldWorks
Dim DocumentName As System.String
Dim value As ModelDoc
 
value = instance.IGetOpenDocumentByName(DocumentName)
```

```

ModelDoc IGetOpenDocumentByName( 
   System.string DocumentName
)
```

```

ModelDoc^ IGetOpenDocumentByName( 
   System.String^ DocumentName
) 
```

#### Parameters

*DocumentName*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
