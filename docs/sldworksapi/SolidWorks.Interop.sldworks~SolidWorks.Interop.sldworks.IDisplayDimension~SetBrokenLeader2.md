# SetBrokenLeader2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBrokenLeader2`

Sets the broken leader display characteristic of this display dimension.
Sets the broken leader display characteristic of this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBrokenLeader2( _
   ByVal UseDoc As System.Boolean, _
   ByVal Broken As System.Integer _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim Broken As System.Integer
Dim value As System.Integer
 
value = instance.SetBrokenLeader2(UseDoc, Broken)
```

```

System.int SetBrokenLeader2( 
   System.bool UseDoc,
   System.int Broken
)
```

```

System.int SetBrokenLeader2( 
   System.bool UseDoc,
   System.int Broken
) 
```

#### Parameters

*UseDoc*
:   True uses the document default setting, false uses the setting specified in the Broken argument

*Broken*
:   Broken leader value as defined in [swDisplayDimensionLeaderText\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayDimensionLeaderText_e.html) if UseDoc is false

#### Return Value

Return status:

|  |  |
| --- | --- |
| -1 | Command failed, no broken leader values were set |
| 0 | Command was successful, all precision values were set |
| 1 | Specified broken value is invalid, the display dimension was set to use the document default |

Remarks

Dimension text can be displayed above a solid, unbroken leader line, or broken with the text displayed horizontally or aligned with the leader line. This method allows you to determine if this [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) uses the default document setting for this value or if the user has applied a specific setting.

If UseDoc is True, then SOLIDWORKS ignores the broken value.

The return value indicates the success or failure of this method. In general, a value less than 0 indicates that the command failed, and no broken leader values were set. A value of 0 indicates success.

Use [IDisplayDimension::GetUseDocBrokenLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBrokenLeader.md) and [IDisplayDimension::GetBrokenLeader2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBrokenLeader2.md) to get these values.

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.md)  
[IDisplayDimension::GetUseDocBrokenLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBrokenLeader.md)  
[IDisplayDimension::SolidLeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SolidLeader.md)
