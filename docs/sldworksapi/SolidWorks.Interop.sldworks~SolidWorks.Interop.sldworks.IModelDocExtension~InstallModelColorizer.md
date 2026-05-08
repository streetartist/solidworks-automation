# InstallModelColorizer Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InstallModelColorizer`

Installs your implemented interface of the ISwColorContour interface.
Installs your implemented interface of the [ISwColorContour](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour.md) interface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InstallModelColorizer( _
   ByVal PInterface As System.Object _
) 
```

```

Dim instance As IModelDocExtension
Dim PInterface As System.Object
 
instance.InstallModelColorizer(PInterface)
```

```

void InstallModelColorizer( 
   System.object PInterface
)
```

```

void InstallModelColorizer( 
   System.Object^ PInterface
) 
```

#### Parameters

*PInterface*
:   Pointer to your implemented interface

Remarks

After your implemented interface is installed, the SOLIDWORKS software calls [ISwColorContour::Value](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour~Value.md) on each graphical update. Your implemented interface must provide the corresponding color for each vertex and the value associated with each vertex. This value is displayed when the cursor is over that vertex.

Additionally, when the cursor is over the model, the SOLIDWORKS software calls [ISwColorContour::DisplayString](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwColorContour~DisplayString.md) and passes the value to be formatted by your implemented interface, which the SOLIDWORKS software will then display.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::RemoveModelColorizer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveModelColorizer.md)
