# GetNumDependencies Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetNumDependencies`

Gets the number of strings returned by IModelDoc2::GetDependencies2.
Gets the number of strings returned by [IModelDoc2::GetDependencies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDependencies2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNumDependencies( _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.Integer
 
value = instance.GetNumDependencies(Traverseflag, Searchflag)
```

```

System.int GetNumDependencies( 
   System.int Traverseflag,
   System.int Searchflag
)
```

```

System.int GetNumDependencies( 
   System.int Traverseflag,
   System.int Searchflag
) 
```

#### Parameters

*Traverseflag*
:   True to traverse down into all dependent files, false for only the highest level within the dependencies

*Searchflag*
:   True to apply the current search criteria, false to return the dependent file information as it was stored

#### Return Value

Number of strings returned by [IModelDoc2::GetDependencies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDependencies2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IGetNumDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetNumDependencies2.md)  
[IModelDoc2::IGetDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetDependencies2.md)  
[ISldWorks::GetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.md)  
[ISldWorks::GetDocumentDependenciesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependenciesCount.md)  
[ISldWorks::IGetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.md)  
[ISldWorks::IGetDocumentDependenciesCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependenciesCount2.md)
