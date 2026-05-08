# GetLightEnabledInRender Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLightEnabledInRender`

Gets whether a light is on in this model.
Gets whether a light is on in this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLightEnabledInRender( _
   ByVal ID As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim value As System.Boolean
 
value = instance.GetLightEnabledInRender(ID)
```

```

System.bool GetLightEnabledInRender( 
   System.int ID
)
```

```

System.bool GetLightEnabledInRender( 
   System.int ID
) 
```

#### Parameters

*ID*
:   Light ID

#### Return Value

True of the light is on, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::SetLightEnabledInRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetLightEnabledInRender.md)
