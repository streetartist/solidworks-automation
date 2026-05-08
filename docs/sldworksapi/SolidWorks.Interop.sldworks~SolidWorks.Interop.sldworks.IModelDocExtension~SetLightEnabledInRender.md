# SetLightEnabledInRender Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetLightEnabledInRender`

Sets whether a light is on in this model.
Sets whether a light is on in this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetLightEnabledInRender( _
   ByVal ID As System.Integer, _
   ByVal Val As System.Boolean _
) 
```

```

Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim Val As System.Boolean
 
instance.SetLightEnabledInRender(ID, Val)
```

```

void SetLightEnabledInRender( 
   System.int ID,
   System.bool Val
)
```

```

void SetLightEnabledInRender( 
   System.int ID,
   System.bool Val
) 
```

#### Parameters

*ID*
:   Light ID

*Val*
:   True to enable the light, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetLightEnabledInRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLightEnabledInRender.md)
