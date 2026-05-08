# GetDependencies Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDependencies`

Obsolete. Superseded by IModelDoc2::GetDependencies2.
Obsolete. Superseded by [IModelDoc2::GetDependencies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetDependencies2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDependencies( _
   ByVal Traverseflag As System.Integer, _
   ByVal Searchflag As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim Traverseflag As System.Integer
Dim Searchflag As System.Integer
Dim value As System.Object
 
value = instance.GetDependencies(Traverseflag, Searchflag)
```

```

System.object GetDependencies( 
   System.int Traverseflag,
   System.int Searchflag
)
```

```

System.Object^ GetDependencies( 
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

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
