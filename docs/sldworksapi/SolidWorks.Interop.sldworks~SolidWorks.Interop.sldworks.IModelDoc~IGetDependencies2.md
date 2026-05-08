# IGetDependencies2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetDependencies2`

Obsolete. Superseded by IModelDoc2::IGetDependencies2.
Obsolete. Superseded by [IModelDoc2::IGetDependencies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetDependencies2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDependencies2( _
   ByVal Traverseflag As System.Boolean, _
   ByVal Searchflag As System.Boolean, _
   ByVal AddReadOnlyInfo As System.Boolean _
) As System.String
```

```

Dim instance As IModelDoc
Dim Traverseflag As System.Boolean
Dim Searchflag As System.Boolean
Dim AddReadOnlyInfo As System.Boolean
Dim value As System.String
 
value = instance.IGetDependencies2(Traverseflag, Searchflag, AddReadOnlyInfo)
```

```

System.string IGetDependencies2( 
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
)
```

```

System.String^ IGetDependencies2( 
   System.bool Traverseflag,
   System.bool Searchflag,
   System.bool AddReadOnlyInfo
) 
```

#### Parameters

*Traverseflag*

*Searchflag*

*AddReadOnlyInfo*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
