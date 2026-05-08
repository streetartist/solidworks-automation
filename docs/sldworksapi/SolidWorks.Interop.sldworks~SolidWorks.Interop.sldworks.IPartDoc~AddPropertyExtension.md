# AddPropertyExtension Method (IPartDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~AddPropertyExtension`

Adds a property extension to this part.
Adds a property extension to this part.

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

Dim instance As IPartDoc
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
:   Value of the property extension to add to this part (see **Remarks**)

#### Return Value

Size of the array to which the property extension value is added

Remarks

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the part.

The 1-based array is a first-in-last-out structured list, whose size is used by [IPartDoc::GetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetPropertyExtension.md) to access the property extension. See the examples in **Example**.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md), [IAttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md), and [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) interfaces instead of this method. These interfaces provide more flexibility.

Example

[Add and Get Property Extensions (C#)](Add_and_Get_Property_Extension_Example_CSharp.htm)  
[Add and Get Property Extensions (VB.NET)](Add_and_Get_Property_Extension_Example_VBNET.htm)  
[Add and Get Property Extensions (VBA)](Add_and_Get_Property_Extension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ResetPropertyExtension.md)
