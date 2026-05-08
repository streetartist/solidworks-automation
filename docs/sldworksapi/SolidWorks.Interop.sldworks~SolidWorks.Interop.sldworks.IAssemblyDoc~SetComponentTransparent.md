# SetComponentTransparent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentTransparent`

Enables or disables transparency on the selected components.
Enables or disables transparency on the selected components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetComponentTransparent( _
   ByVal State As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim State As System.Boolean
Dim value As System.Boolean
 
value = instance.SetComponentTransparent(State)
```

```

System.bool SetComponentTransparent( 
   System.bool State
)
```

```

System.bool SetComponentTransparent( 
   System.bool State
) 
```

#### Parameters

*State*
:   True to set the components transparent, false to not

#### Return Value

True if components are transparent, false if not

Remarks

If you set the transparent state to True, then the components are automatically assigned a transparency value of 75%.

If you want transparency (and other optical properties) set to specific values, then use the [IComponent2::GetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.md) and [ISetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2.md)[SetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.md)[IComponent2::SetMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.md).

To set other component transparencies, set these user preferences: [swEdgesInContextEditTransparencyType and swEdgesInContextEditTransparency](ms-help://SolidWorks.Interop.swconst/SolidWorks/SO_Display.htm). You should set these preferences before editing the part to see their effect while editing the part.

Example

[Set Components Transparent (VBA)](Set_Components_Transparent_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
