# IAccessSelections Method (IVariableFilletFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData~IAccessSelections`

Obsolete. Superseded by IVariableFilletFeatureData2::IAccessSelections.
Obsolete. Superseded by [IVariableFilletFeatureData2::IAccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~IAccessSelections.md).

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

Dim instance As IVariableFilletFeatureData
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

[IVariableFilletFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData.md)  
[IVariableFilletFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData_members.md)
