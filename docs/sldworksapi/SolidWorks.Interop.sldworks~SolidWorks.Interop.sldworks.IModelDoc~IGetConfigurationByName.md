# IGetConfigurationByName Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetConfigurationByName`

Obsolete. Superseded by IModelDoc2::IGetConfigurationByName.
Obsolete. Superseded by [IModelDoc2::IGetConfigurationByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetConfigurationByName.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetConfigurationByName( _
   ByVal Name As System.String _
) As Configuration
```

```

Dim instance As IModelDoc
Dim Name As System.String
Dim value As Configuration
 
value = instance.IGetConfigurationByName(Name)
```

```

Configuration IGetConfigurationByName( 
   System.string Name
)
```

```

Configuration^ IGetConfigurationByName( 
   System.String^ Name
) 
```

#### Parameters

*Name*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
