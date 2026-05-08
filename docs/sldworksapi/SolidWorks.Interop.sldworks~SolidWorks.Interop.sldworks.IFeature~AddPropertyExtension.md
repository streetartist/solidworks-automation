# AddPropertyExtension Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddPropertyExtension`

Adds a property extension to this feature.
Adds a property extension to this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

```

Dim instance As IFeature
Dim PropertyExtension As System.Object
Dim value As System.Integer
 
value = instance.AddPropertyExtension(PropertyExtension)
```

```

System.int AddPropertyExtension( 
   System.object PropertyExtension
)
```

```

System.int AddPropertyExtension( 
   System.Object^ PropertyExtension
) 
```

#### Parameters

*PropertyExtension*
:   Value of the property extension to add to this feature

#### Return Value

1 if the property extension is added to the feature, -1 if not

Remarks

This method does not support adding multiple property extensions to the same feature.

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the feature.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), or [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) interfaces instead of this method. These interfaces provide more flexibility.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetPropertyExtension.md)  
[IFeature::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ResetPropertyExtension.md)
