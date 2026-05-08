# FeatureByName Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FeatureByName`

Gets the specified feature for this component.
Gets the specified feature for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureByName( _
   ByVal Name As System.String _
) As Feature
```

```

Dim instance As IComponent2
Dim Name As System.String
Dim value As Feature
 
value = instance.FeatureByName(Name)
```

```

Feature FeatureByName( 
   System.string Name
)
```

```

Feature^ FeatureByName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of the feature to retrieve

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
