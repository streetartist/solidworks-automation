# RemoveModelColorizer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveModelColorizer`

Removes your installed implemented interface of the ISwColorContour interface.
Removes your installed implemented interface of the [ISwColorContour](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour.md) interface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemoveModelColorizer( _
   ByVal PInterface As System.Object _
) 
```

```

Dim instance As IModelDocExtension
Dim PInterface As System.Object
 
instance.RemoveModelColorizer(PInterface)
```

```

void RemoveModelColorizer( 
   System.object PInterface
)
```

```

void RemoveModelColorizer( 
   System.Object^ PInterface
) 
```

#### Parameters

*PInterface*
:   Pointer to your installed implemented interface

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::InstallModelColorizer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InstallModelColorizer.md)
