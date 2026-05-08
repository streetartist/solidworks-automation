# AddPropertyExtension2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddPropertyExtension2`

Adds a property extension to this body.
Adds a property extension to this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPropertyExtension2( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

```

Dim instance As IBody2
Dim PropertyExtension As System.Object
Dim value As System.Integer
 
value = instance.AddPropertyExtension2(PropertyExtension)
```

```

System.int AddPropertyExtension2( 
   System.object PropertyExtension
)
```

```

System.int AddPropertyExtension2( 
   System.Object^ PropertyExtension
) 
```

#### Parameters

*PropertyExtension*
:   Value of the property extension to add to this body (see **Remarks**)

#### Return Value

Size of the array to which the property extension value is added

Remarks

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the body.

The 1-based array is a first-in-last-out structured list, whose size is used by [IBody2::GetPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetPropertyExtension2.md) to access the property extension.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), and [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) interfaces instead of this method. These interfaces provide more flexibility.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ResetPropertyExtension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetPropertyExtension2.md)
