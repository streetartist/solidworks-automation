# LinkProperty Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkProperty`

Sets whether to link or unlink the specified custom property to or from its parent part.
Sets whether to link or unlink the specified custom property to or from its parent part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LinkProperty( _
   ByVal FieldName As System.String, _
   ByVal FieldLink As System.Boolean _
) As System.Integer
```

```

Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim FieldLink As System.Boolean
Dim value As System.Integer
 
value = instance.LinkProperty(FieldName, FieldLink)
```

```

System.int LinkProperty( 
   System.string FieldName,
   System.bool FieldLink
)
```

```

System.int LinkProperty( 
   System.String^ FieldName,
   System.bool FieldLink
) 
```

#### Parameters

*FieldName*
:   Name of the custom property to link or unlink

*FieldLink*
:   True to link the custom property, false to unlink it

#### Return Value

Result code as defined in [swCustomLinkSetResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCustomLinkSetResult_e.html)

Remarks

This method is valid for cut-list, feature, model, and configuration custom properties.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::LinkAll Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkAll.md)
