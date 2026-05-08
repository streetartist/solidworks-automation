# GetAttributes Method (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributes`

Gets the attributes for this block instance.
Gets the attributes for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttributes() As System.Object
```

```

Dim instance As ISketchBlockInstance
Dim value As System.Object
 
value = instance.GetAttributes()
```

```

System.object GetAttributes()
```

```

System.Object^ GetAttributes(); 
```

#### Return Value

Array of attributes (see **Remarks**)

Remarks

Attributes are string notes that have tag names and are not read-only.

Use [ISketchBlockInstance::GetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeValue.md) to get attribute's value, or use [ISketchBlockInstance::SetAttributeValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~SetAttributeValue.md) to set an attribute's value.

Example

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)  
[ISketchBlockInstance::GetAttributeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~GetAttributeCount.md)  
[ISketchBlockInstance::IGetAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~IGetAttributes.md)
