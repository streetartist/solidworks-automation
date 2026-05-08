# GetDocumentDependenciesCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependenciesCount`

Obsolete. Superseded by ISldWorks::IGetDocumentDependenciesCount2.
Obsolete. Superseded by [ISldWorks::IGetDocumentDependenciesCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependenciesCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDocumentDependenciesCount( _
   ByVal Document As System.String, _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Document As System.String
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.Integer
 
value = instance.GetDocumentDependenciesCount(Document, Traverseflag, Searchflag)
```

```

System.int GetDocumentDependenciesCount( 
   System.string Document,
   System.int Traverseflag,
   System.int Searchflag
)
```

```

System.int GetDocumentDependenciesCount( 
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
