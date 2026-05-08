# GetAttributeValue Method (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue`

Gets the value of the specified attribute for this block instance.
Gets the value of the specified attribute for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttributeValue( _
   ByVal TagName As System.String _
) As System.String
```

```

Dim instance As ISketchBlockInstance
Dim TagName As System.String
Dim value As System.String
 
value = instance.GetAttributeValue(TagName)
```

```

System.string GetAttributeValue( 
   System.string TagName
)
```

```

System.String^ GetAttributeValue( 
   System.String^ TagName
) 
```

#### Parameters

*TagName*
:   Tag name of this attribute

#### Return Value

Value of this attribute

Remarks

Attributes are notes that have tag names and are not read-only.

Use [ISketchBlockInstance::SetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.md) to set an attribute.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockInstance::GetAttributeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeCount.md)  
[ISketchBlockInstance::GetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes.md)  
[ISketchBlockInstance::IGetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes.md)
