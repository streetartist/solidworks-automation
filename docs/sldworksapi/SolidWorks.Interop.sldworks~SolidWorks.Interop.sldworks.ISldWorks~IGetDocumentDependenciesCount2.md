# IGetDocumentDependenciesCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependenciesCount2`

Gets the size of the array needed for a call to ISldWorks::IGetDocumetnDependencies2.
Gets the size of the array needed for a call to [ISldWorks::IGetDocumetnDependencies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDocumentDependenciesCount2( _
   ByVal Document As System.String, _
   ByVal Traverseflag As System.Boolean, _
   ByVal Searchflag As System.Boolean, _
   ByVal AddReadOnlyInfo As System.Boolean _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Document As System.String
Dim Traverseflag As System.Boolean
Dim Searchflag As System.Boolean
Dim AddReadOnlyInfo As System.Boolean
Dim value As System.Integer
 
value = instance.IGetDocumentDependenciesCount2(Document, Traverseflag, Searchflag, AddReadOnlyInfo)
```

```

System.int IGetDocumentDependenciesCount2( 
   System.string Document,
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

```

System.int IGetDocumentDependenciesCount2( 
   System.String^ Document,
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
) 
```

#### Parameters

*Document*
:   Name of the document

*Traverseflag*
:   True if you want to traverse down into all dependent files, false if you want only the highest level within the dependencies

*Searchflag*
:   Set this argument to True if you want to use the search rules to find dependencies, false looks where the documents were last saved

*AddReadOnlyInfo*
:   True if you want to have read-only information with the filenames, false if not

#### Return Value

Number of strings returned by [ISldWorks::IGetDocumetnDependencies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetDocumentDependencies2.md)

Remarks

If SearchFlag is set to True, then the current directory is set to the directory of the document file. This is the same as interactively clikcing the References button in the File Open dialog.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::GetDocumentDependencies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentDependencies2.md)
