# IGetDocumentDependencies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies`

Obsolete. Superseded by ISldWorks::IGetDocumentDependencies2.
Obsolete. Superseded by [ISldWorks::IGetDocumentDependencies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDocumentDependencies( _
   ByVal Document As System.String, _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.String
```

```

Dim instance As ISldWorks
Dim Document As System.String
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.String
 
value = instance.IGetDocumentDependencies(Document, Traverseflag, Searchflag)
```

```

System.string IGetDocumentDependencies( 
   System.string Document,
   System.int Traverseflag,
   System.int Searchflag
)
```

```

System.String^ IGetDocumentDependencies( 
   System.String^ Document,
   System.int Traverseflag,
   System.int Searchflag
) 
```

#### Parameters

*Document*

*Traverseflag*

*Searchflag*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
