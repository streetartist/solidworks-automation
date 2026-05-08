# AddPropertyExtension Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddPropertyExtension`

Adds a property extension to this model.
Adds a property extension to this model.

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

Dim instance As IModelDoc2
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
:   Value of the property extension to add to the model (see **Remarks**)

#### Return Value

Size of the array to which the property extension value is added

Remarks

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the model.

The 1-based array is a first-in-last-out structured list, whose size is used by [IModelDoc2::GetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPropertyExtension.md) to access the property extension..

**NOTE**: SOLIDWORKS recommends that you use [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), and [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) instead of this method. These interfaces provide more flexibility.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetPropertyExtension.md)
