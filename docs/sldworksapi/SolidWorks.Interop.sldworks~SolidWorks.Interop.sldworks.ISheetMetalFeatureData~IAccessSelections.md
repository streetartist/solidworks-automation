# IAccessSelections Method (ISheetMetalFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~IAccessSelections`

Obsolete. Superseded by ISheetMetalFeatureData::IAccessSelections2.
Obsolete. Superseded by [ISheetMetalFeatureData::IAccessSelections2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~IAccessSelections2.md).

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

Dim instance As ISheetMetalFeatureData
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

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.md)
