# IGetNumDependencies Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetNumDependencies`

Obsolete. Superseded by IModelDoc2::IGetNumDependencies.
Obsolete. Superseded by [IModelDoc2::IGetNumDependencies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetNumDependencies.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNumDependencies( _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.Integer
```

```

Dim instance As IModelDoc
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.Integer
 
value = instance.IGetNumDependencies(Traverseflag, Searchflag)
```

```

System.int IGetNumDependencies( 
   System.int Traverseflag,
   System.int Searchflag
)
```

```

System.int IGetNumDependencies( 
   System.int Traverseflag,
   System.int Searchflag
) 
```

#### Parameters

*Traverseflag*

*Searchflag*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
