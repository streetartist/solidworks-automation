# SetAttributeValue Method (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue`

Sets the }}-->value of the specified attribute for this block instance.
Sets the value of the specified attribute for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetAttributeValue( _
   ByVal TagName As System.String, _
   ByVal Value As System.String _
) As System.Boolean
```

```

Dim instance As ISketchBlockInstance
Dim TagName As System.String
Dim Value As System.String
Dim value As System.Boolean
 
value = instance.SetAttributeValue(TagName, Value)
```

```

System.bool SetAttributeValue( 
   System.string TagName,
   System.string Value
)
```

```

System.bool SetAttributeValue( 
   System.String^ TagName,
   System.String^ Value
) 
```

#### Parameters

*TagName*
:   Tag name of this attribute

*Value*
:   Value for this attribute

#### Return Value

True if the attribute's value is set, false if not

Remarks

Attributes are string notes that have tag names and are not read-only.

Use [ISketchBlockInstance::GetAttributes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes.md) or [ISketchBlockInstance::IGetAttributes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes.md) to the get attributes for this block instance. Use [ISketchBlockInstance::GetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.md) to get an attribute's value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)
