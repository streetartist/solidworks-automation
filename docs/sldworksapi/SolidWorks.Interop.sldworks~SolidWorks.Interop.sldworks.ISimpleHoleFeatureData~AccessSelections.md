# AccessSelections Method (ISimpleHoleFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData~AccessSelections`

Obsolete. Superseded by ISimpleHoleFeatureData2::AccessSelections.
Obsolete. Superseded by [ISimpleHoleFeatureData2::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~AccessSelections.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AccessSelections( _
   ByVal TopDoc As System.Object, _
   ByVal Component As System.Object _
) As System.Boolean
```

```

Dim instance As ISimpleHoleFeatureData
Dim TopDoc As System.Object
Dim Component As System.Object
Dim value As System.Boolean
 
value = instance.AccessSelections(TopDoc, Component)
```

```

System.bool AccessSelections( 
   System.object TopDoc,
   System.object Component
)
```

```

System.bool AccessSelections( 
   System.Object^ TopDoc,
   System.Object^ Component
) 
```

#### Parameters

*TopDoc*

*Component*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData.md)  
[ISimpleHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData_members.md)
