# IAccessSelections Method (IDomeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData~IAccessSelections`

Obsolete. Superseded by IDomeFeatureData2::IAccessSelections.
Obsolete. Superseded by [IDomeFeatureData2::IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IAccessSelections.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAccessSelections( _
   ByVal TopDoc As ModelDoc, _
   ByVal Component As Component _
) As System.Boolean
```

```

Dim instance As IDomeFeatureData
Dim TopDoc As ModelDoc
Dim Component As Component
Dim value As System.Boolean
 
value = instance.IAccessSelections(TopDoc, Component)
```

```

System.bool IAccessSelections( 
   ModelDoc TopDoc,
   Component Component
)
```

```

System.bool IAccessSelections( 
   ModelDoc^ TopDoc,
   Component^ Component
) 
```

#### Parameters

*TopDoc*

*Component*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDomeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData.md)  
[IDomeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData_members.md)
