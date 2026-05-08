# IGetConfigurationNames Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetConfigurationNames`

Obsolete. Superseded by IModelDoc2::IGetConfigurationNames.
Obsolete. Superseded by [IModelDoc2::IGetConfigurationNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationNames.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConfigurationNames( _
   ByRef Count As System.Integer _
) As System.String
```

```

Dim instance As IModelDoc
Dim Count As System.Integer
Dim value As System.String
 
value = instance.IGetConfigurationNames(Count)
```

```

System.string IGetConfigurationNames( 
   out System.int Count
)
```

```

System.String^ IGetConfigurationNames( 
   [Out] System.int Count
) 
```

#### Parameters

*Count*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
